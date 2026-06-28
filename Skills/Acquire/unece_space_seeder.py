#!/usr/bin/env python3
"""
UNECE Space Seeder
Skill: Acquire/UNECE_Space_Seeder  v1.0.0

Crawl a UNECE Confluence space starting from a root page URL.
Traverse the full page hierarchy, collect structural metadata and
attachment references, and export a single seed.json.

CONSTRAINTS — This script must never:
  - Read or summarize page body content
  - Classify regulatory documents or concepts
  - Infer relationships between UNECE entities
  - Write to any vault Markdown file

Its only output is structured JSON.
"""

import argparse
import json
import logging
import re
import sys
import time
from datetime import datetime, timezone
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("Error: 'requests' is required.  Run:  pip install requests")
    sys.exit(1)


# ── Constants ─────────────────────────────────────────────────────────────────

VERSION         = "1.0.0"
DEFAULT_OUTPUT  = "output/seed.json"
REQUEST_DELAY   = 0.5   # seconds — be considerate to the server
PAGE_SIZE       = 50    # Confluence pagination limit
MAX_RETRIES     = 3


# ── Logging ───────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("seeder")


# ── URL helpers ───────────────────────────────────────────────────────────────

def extract_page_id(url: str) -> str:
    """Extract the numeric page ID from a Confluence page URL.

    Handles the modern format:
        https://wiki.unece.org/spaces/{key}/pages/{id}/...
    """
    m = re.search(r"/pages/(\d+)", url)
    if m:
        return m.group(1)
    raise ValueError(
        f"Cannot extract page ID from URL: {url}\n"
        "Expected format: …/spaces/{key}/pages/{page_id}/…"
    )


def extract_base_url(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"


def page_view_url(base_url: str, space_key: str, page_id: str) -> str:
    return f"{base_url}/spaces/{space_key}/pages/{page_id}"


# ── Confluence REST API client ────────────────────────────────────────────────

class ConfluenceClient:
    """Minimal Confluence REST API v1 client.

    Only fetches page metadata and attachment metadata.
    Never reads page body content.
    """

    def __init__(self, base_url: str, auth: Optional[tuple] = None):
        self.base_url = base_url.rstrip("/")
        self.api_base = f"{self.base_url}/rest/api"
        self.session  = self._build_session(auth)

    # ── Session setup ─────────────────────────────────────────────────────────

    def _build_session(self, auth: Optional[tuple]) -> requests.Session:
        s = requests.Session()
        if auth:
            s.auth = auth
        retry = Retry(
            total            = MAX_RETRIES,
            backoff_factor   = 1.0,
            status_forcelist = [429, 500, 502, 503, 504],
            allowed_methods  = ["GET"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        s.mount("https://", adapter)
        s.mount("http://",  adapter)
        s.headers.update({"Accept": "application/json"})
        return s

    # ── HTTP ──────────────────────────────────────────────────────────────────

    def _get(self, path: str, params: Optional[dict] = None) -> dict:
        url = f"{self.api_base}{path}"
        time.sleep(REQUEST_DELAY)
        resp = self.session.get(url, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    # ── Public methods ────────────────────────────────────────────────────────

    def get_page(self, page_id: str) -> dict:
        """Fetch page metadata (no body content)."""
        return self._get(
            f"/content/{page_id}",
            {"expand": "version,space,ancestors"},
        )

    def get_children(self, page_id: str) -> list:
        """Return all child pages, handling Confluence pagination."""
        results, start = [], 0
        while True:
            data = self._get(
                f"/content/{page_id}/child/page",
                {"limit": PAGE_SIZE, "start": start, "expand": "version"},
            )
            batch = data.get("results", [])
            results.extend(batch)
            if len(batch) < PAGE_SIZE:
                break
            start += PAGE_SIZE
        return results

    def get_attachments(self, page_id: str) -> list:
        """Return all attachment metadata for a page, handling pagination."""
        results, start = [], 0
        while True:
            data = self._get(
                f"/content/{page_id}/child/attachment",
                {
                    "limit":  PAGE_SIZE,
                    "start":  start,
                    "expand": "version,metadata.mediaType",
                },
            )
            batch = data.get("results", [])
            results.extend(batch)
            if len(batch) < PAGE_SIZE:
                break
            start += PAGE_SIZE
        return results


# ── Structural page classification ───────────────────────────────────────────
# This is structural only — it uses title patterns and hierarchy depth.
# It NEVER classifies regulatory content, concepts, or documents.

_SESSION_RE = re.compile(
    r"""
    \b(
        \d{1,3}(?:st|nd|rd|th)?\s*(?:session|meeting)  # "24th session"
      | session\s+\d+                                    # "session 24"
      | GRVA[-\s]\d{2}                                   # "GRVA-24"
      | WP\.?29[-\s]\d+                                  # "WP.29-199"
    )\b
    """,
    re.IGNORECASE | re.VERBOSE,
)

_KNOWN_WG_NAMES = ["ADS", "CS/OTA", "DSSAD", "EDR", "AEBS", "ADAS", "VMAD", "FRAV"]


def classify_page_type(title: str, depth: int) -> str:
    """Return a structural page type label.

    Purely structural — no regulatory interpretation.
    """
    if depth == 0:
        return "working_party_root"

    t = title.lower()

    if _SESSION_RE.search(title):
        return "session"

    if any(k in t for k in ("document", "documents", "attachment", "attachments")):
        return "document_list"

    if "agenda" in t:
        return "agenda"

    if "report" in t:
        return "report"

    if any(k in t for k in ("iwg", "informal working group", "task force", " tf", "tf ")):
        return "informal_working_group"

    if depth == 1:
        return "programme_area"

    return "page"


def extract_working_group(title: str, ancestor_titles: list) -> Optional[str]:
    """Return the closest known working-group shortname from title or ancestors.

    Returns the raw string — no regulatory interpretation.
    """
    for wg in _KNOWN_WG_NAMES:
        if wg.lower() in title.lower():
            return wg
    for ancestor in reversed(ancestor_titles):
        for wg in _KNOWN_WG_NAMES:
            if wg.lower() in ancestor.lower():
                return wg
    return None


# ── Core seeder ───────────────────────────────────────────────────────────────

class UNECESpaceSeeder:
    """Recursively crawl a UNECE Confluence space and produce seed.json."""

    def __init__(
        self,
        client: ConfluenceClient,
        root_url: str,
        include_attachments: bool = True,
    ):
        self.client              = client
        self.root_url            = root_url
        self.include_attachments = include_attachments
        self.base_url            = extract_base_url(root_url)
        self.root_page_id        = extract_page_id(root_url)

        # Accumulated state
        self.page_index:     dict = {}
        self.all_attachments: list = []
        self.sessions:        list = []
        self.meetings:        list = []
        self._stats = {"pages": 0, "attachments": 0, "errors": 0}

    # ── Public entry point ───────────────────────────────────────────────────

    def crawl(self) -> dict:
        log.info("UNECE Space Seeder  v%s", VERSION)
        log.info("Root URL  : %s", self.root_url)
        log.info("Root ID   : %s", self.root_page_id)

        root_raw  = self.client.get_page(self.root_page_id)
        space_key = root_raw.get("space", {}).get("key", "unknown")
        log.info("Space key : %s", space_key)

        log.info("Traversing page hierarchy …")
        hierarchy = self._crawl_page(
            page_raw        = root_raw,
            depth           = 0,
            parent_id       = None,
            ancestor_titles = [],
            space_key       = space_key,
        )

        crawled_at = datetime.now(timezone.utc).isoformat()
        seed = {
            "seed_metadata": {
                "skill":              "UNECE_Space_Seeder",
                "skill_version":      VERSION,
                "root_url":           self.root_url,
                "root_page_id":       self.root_page_id,
                "space_key":          space_key,
                "crawled_at":         crawled_at,
                "total_pages":        self._stats["pages"],
                "total_attachments":  self._stats["attachments"],
                "total_sessions":     len(self.sessions),
                "total_meetings":     len(self.meetings),
                "errors":             self._stats["errors"],
            },
            "hierarchy":      hierarchy,
            "page_index":     self.page_index,
            "sessions":       self.sessions,
            "meetings":       self.meetings,
            "attachments":    self.all_attachments,
            "document_index": self._build_document_index(),
        }

        log.info(
            "Done — %d pages | %d attachments | %d sessions | %d errors",
            self._stats["pages"],
            self._stats["attachments"],
            len(self.sessions),
            self._stats["errors"],
        )
        return seed

    # ── Recursive page crawler ───────────────────────────────────────────────

    def _crawl_page(
        self,
        page_raw: dict,
        depth: int,
        parent_id: Optional[str],
        ancestor_titles: list,
        space_key: str,
    ) -> dict:
        page_id  = str(page_raw["id"])
        title    = page_raw.get("title", "")
        version  = page_raw.get("version", {})

        last_updated  = version.get("when", "")
        page_type     = classify_page_type(title, depth)
        working_group = extract_working_group(title, ancestor_titles)
        url           = page_view_url(self.base_url, space_key, page_id)

        self._stats["pages"] += 1
        if self._stats["pages"] % 20 == 0:
            log.info("  … %d pages crawled", self._stats["pages"])

        # ── Fetch children ────────────────────────────────────────────────────
        try:
            children_raw = self.client.get_children(page_id)
        except Exception as exc:
            log.warning("Could not fetch children of %s (%s): %s", page_id, title, exc)
            children_raw = []
            self._stats["errors"] += 1

        # ── Fetch attachments ─────────────────────────────────────────────────
        page_attachments = []
        if self.include_attachments:
            try:
                page_attachments = self._collect_attachments(
                    page_id, title, working_group
                )
            except Exception as exc:
                log.warning("Could not fetch attachments of %s (%s): %s", page_id, title, exc)
                self._stats["errors"] += 1

        # ── Build hierarchy node ──────────────────────────────────────────────
        node = {
            "page_id":          page_id,
            "title":            title,
            "url":              url,
            "page_type":        page_type,
            "working_group":    working_group,
            "depth":            depth,
            "last_updated":     last_updated,
            "parent_id":        parent_id,
            "attachment_count": len(page_attachments),
            "child_count":      len(children_raw),
            "children":         [],
        }

        # ── Flat index entry ──────────────────────────────────────────────────
        self.page_index[page_id] = {
            "page_id":          page_id,
            "title":            title,
            "url":              url,
            "page_type":        page_type,
            "working_group":    working_group,
            "depth":            depth,
            "last_updated":     last_updated,
            "parent_id":        parent_id,
            "attachment_count": len(page_attachments),
            "child_count":      len(children_raw),
        }

        # ── Classify as session ───────────────────────────────────────────────
        if page_type == "session":
            self.sessions.append({
                "page_id":      page_id,
                "title":        title,
                "url":          url,
                "working_group": working_group,
                "last_updated": last_updated,
                "depth":        depth,
                "parent_id":    parent_id,
            })

        # ── Recurse ───────────────────────────────────────────────────────────
        new_ancestors = ancestor_titles + [title]
        for child_raw in children_raw:
            child_id = str(child_raw.get("id", ""))
            try:
                child_full = self.client.get_page(child_id)
            except Exception as exc:
                log.warning("Could not fetch page %s: %s", child_id, exc)
                self._stats["errors"] += 1
                continue
            child_node = self._crawl_page(
                page_raw        = child_full,
                depth           = depth + 1,
                parent_id       = page_id,
                ancestor_titles = new_ancestors,
                space_key       = space_key,
            )
            node["children"].append(child_node)

        return node

    # ── Attachment collection ─────────────────────────────────────────────────

    def _collect_attachments(
        self,
        page_id: str,
        page_title: str,
        working_group: Optional[str],
    ) -> list:
        raw_list = self.client.get_attachments(page_id)
        result   = []
        for att in raw_list:
            att_id   = str(att.get("id", ""))
            filename = att.get("title", "")
            version  = att.get("version", {})
            metadata = att.get("metadata", {})
            links    = att.get("_links", {})

            # Build download URL (attachment content — not yet downloaded)
            download_url = ""
            if "download" in links:
                download_url = self.base_url + links["download"]

            record = {
                "attachment_id":  att_id,
                "filename":       filename,
                "media_type":     metadata.get("mediaType", ""),
                "file_size_bytes": metadata.get("fileSize", None),
                "page_id":        page_id,
                "page_title":     page_title,
                "working_group":  working_group,
                "last_updated":   version.get("when", ""),
                "download_url":   download_url,
            }
            result.append(record)
            self.all_attachments.append(record)
            self._stats["attachments"] += 1

        return result

    # ── Document index ────────────────────────────────────────────────────────

    def _build_document_index(self) -> dict:
        """Group attachment IDs by media type and working group for lookup."""
        by_media_type:     dict = {}
        by_working_group:  dict = {}

        for att in self.all_attachments:
            mt = att.get("media_type") or "unknown"
            by_media_type.setdefault(mt, []).append(att["attachment_id"])

            wg = att.get("working_group") or "unclassified"
            by_working_group.setdefault(wg, []).append(att["attachment_id"])

        return {
            "by_media_type":    by_media_type,
            "by_working_group": by_working_group,
        }


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog        = "unece_space_seeder.py",
        description = "Crawl a UNECE Confluence space and export seed.json",
        formatter_class = argparse.RawDescriptionHelpFormatter,
        epilog = """
Examples:
  # Full crawl — GRVA space
  python3 unece_space_seeder.py \\
      --url "https://wiki.unece.org/spaces/trans/pages/63310525/Working+Party+on+Automated+Autonomous+and+Connected+Vehicles+GRVA" \\
      --output output/seed.json

  # Hierarchy only (no attachment metadata)
  python3 unece_space_seeder.py \\
      --url "https://wiki.unece.org/spaces/trans/pages/63310525/..." \\
      --no-attachments \\
      --output output/seed_hierarchy.json

  # Authenticated run
  python3 unece_space_seeder.py \\
      --url "https://wiki.unece.org/spaces/trans/pages/63310525/..." \\
      --username YOUR_USERNAME --password YOUR_TOKEN \\
      --output output/seed.json
        """,
    )
    p.add_argument(
        "--url", required=True,
        help="Root Confluence page URL (must contain /pages/{id}/)",
    )
    p.add_argument(
        "--output", default=DEFAULT_OUTPUT,
        help=f"Output path for seed.json (default: {DEFAULT_OUTPUT})",
    )
    p.add_argument(
        "--username", default=None,
        help="Confluence username — only needed for authenticated spaces",
    )
    p.add_argument(
        "--password", default=None,
        help="Confluence password or personal API token",
    )
    p.add_argument(
        "--no-attachments", action="store_true",
        help="Skip attachment collection (faster; produces hierarchy only)",
    )
    p.add_argument(
        "--log-level", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity (default: INFO)",
    )
    return p


def main() -> None:
    args = build_parser().parse_args()
    logging.getLogger().setLevel(getattr(logging, args.log_level))

    auth = (args.username, args.password) if (args.username and args.password) else None
    base_url = extract_base_url(args.url)

    client = ConfluenceClient(base_url=base_url, auth=auth)
    seeder = UNECESpaceSeeder(
        client              = client,
        root_url            = args.url,
        include_attachments = not args.no_attachments,
    )

    try:
        seed = seeder.crawl()
    except KeyboardInterrupt:
        log.warning("Interrupted by user — partial results not written.")
        sys.exit(1)
    except Exception as exc:
        log.error("Seeder failed: %s", exc)
        sys.exit(1)

    # ── Write output ──────────────────────────────────────────────────────────
    import os
    os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else ".", exist_ok=True)

    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(seed, fh, indent=2, ensure_ascii=False)

    log.info("Output written → %s", args.output)
    meta = seed["seed_metadata"]
    log.info(
        "Summary: %d pages | %d attachments | %d sessions | %d errors",
        meta["total_pages"],
        meta["total_attachments"],
        meta["total_sessions"],
        meta["errors"],
    )


if __name__ == "__main__":
    main()
