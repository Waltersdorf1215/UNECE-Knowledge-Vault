---
type: skill
skill_category: Acquire
skill_version: "1.0.0"
status: active
tags: [skill, acquire, confluence, UNECE, GRVA, crawler, seeder]
related: [IMPORT_PIPELINE, CHANGELOG, ROADMAP]
source: "https://wiki.unece.org"
last_updated: 2026-06-27
created: 2026-06-27
script: "unece_space_seeder.py"
output: "output/seed.json"
---

# Skill: UNECE Space Seeder

**Category:** Acquire
**Version:** 1.0.0
**Script:** `unece_space_seeder.py`
**Output:** `output/seed.json`

---

## Purpose

Crawl a UNECE Confluence space starting from a root page, traverse the complete page hierarchy recursively, collect structural metadata and attachment references, and export a single structured JSON file (`seed.json`) for downstream consumption by the Import Pipeline.

**This skill is a pure discovery and indexing tool.** It does not summarize, classify, interpret, or write to the knowledge graph.

---

## Primary Use Case

The GRVA Confluence space at:

```
https://wiki.unece.org/spaces/trans/pages/63310525/Working+Party+on+Automated+Autonomous+and+Connected+Vehicles+GRVA
```

contains the navigation tree for all GRVA working activities: ADS IWG, CS/OTA, DSSAD/EDR, AEBS, ADAS, and their session pages with attached documents. This skill uses that page tree as the source of truth for what documents exist — without interpreting any of them.

---

## Skill Responsibilities

| Responsibility | Included |
|---|---|
| Accept a root Confluence page URL | ✓ |
| Traverse all child pages recursively | ✓ |
| Build the complete page hierarchy | ✓ |
| Extract structural metadata per page | ✓ |
| Collect attachment references | ✓ |
| Produce `seed.json` | ✓ |
| Summarize document content | ✗ Never |
| Classify regulations | ✗ Never |
| Infer relationships | ✗ Never |
| Update vault Markdown files | ✗ Never |
| Write to `12 Attachments/` or knowledge notes | ✗ Never |

---

## Installation

Requires Python 3.9+ and the `requests` library:

```bash
pip install requests
```

---

## Usage

### Basic run — GRVA space

```bash
python3 unece_space_seeder.py \
    --url "https://wiki.unece.org/spaces/trans/pages/63310525/Working+Party+on+Automated+Autonomous+and+Connected+Vehicles+GRVA" \
    --output output/seed.json
```

### Skip attachments (faster — hierarchy only)

```bash
python3 unece_space_seeder.py \
    --url "https://wiki.unece.org/spaces/trans/pages/63310525/..." \
    --output output/seed_hierarchy_only.json \
    --no-attachments
```

### Authenticated run (if the space requires login)

```bash
python3 unece_space_seeder.py \
    --url "https://wiki.unece.org/spaces/trans/pages/63310525/..." \
    --username YOUR_USERNAME \
    --password YOUR_API_TOKEN \
    --output output/seed.json
```

### All options

```
--url URL               Root Confluence page URL (required)
--output PATH           Output JSON file (default: seed.json)
--username USER         Confluence username (optional)
--password PASS         Confluence password or API token (optional)
--no-attachments        Skip attachment collection
--log-level LEVEL       DEBUG | INFO | WARNING | ERROR (default: INFO)
```

---

## Output: seed.json Schema

```json
{
  "seed_metadata": {
    "skill": "UNECE_Space_Seeder",
    "skill_version": "1.0.0",
    "root_url": "https://...",
    "root_page_id": "63310525",
    "space_key": "trans",
    "crawled_at": "2026-06-27T12:00:00+00:00",
    "total_pages": 142,
    "total_attachments": 398,
    "total_sessions": 24,
    "total_meetings": 12,
    "errors": 0
  },
  "hierarchy": {
    "page_id": "63310525",
    "title": "Working Party on Automated/Autonomous and Connected Vehicles (GRVA)",
    "url": "https://wiki.unece.org/spaces/trans/pages/63310525",
    "page_type": "working_party_root",
    "working_group": null,
    "depth": 0,
    "last_updated": "2026-04-15T10:30:00.000Z",
    "parent_id": null,
    "attachment_count": 2,
    "child_count": 8,
    "children": [ ... ]
  },
  "page_index": {
    "63310525": {
      "page_id": "63310525",
      "title": "Working Party on Automated/Autonomous and Connected Vehicles (GRVA)",
      "url": "https://...",
      "page_type": "working_party_root",
      "working_group": null,
      "depth": 0,
      "last_updated": "2026-04-15T10:30:00.000Z",
      "parent_id": null,
      "attachment_count": 2,
      "child_count": 8
    }
  },
  "sessions": [
    {
      "page_id": "...",
      "title": "24th session (January 2026)",
      "url": "https://...",
      "working_group": "ADS",
      "last_updated": "...",
      "depth": 3
    }
  ],
  "meetings": [],
  "attachments": [
    {
      "attachment_id": "...",
      "filename": "ECE-TRANS-WP29-GRVA-2026-2.pdf",
      "media_type": "application/pdf",
      "page_id": "...",
      "page_title": "24th session (January 2026)",
      "working_group": "ADS",
      "last_updated": "...",
      "download_url": "https://wiki.unece.org/download/attachments/...",
      "file_size_bytes": 1245184
    }
  ],
  "document_index": {
    "by_media_type": {
      "application/pdf": ["att_id_1", "att_id_2"],
      "application/vnd.ms-word": ["att_id_3"]
    },
    "by_working_group": {
      "ADS": ["att_id_1"],
      "CS/OTA": ["att_id_2"]
    }
  }
}
```

---

## Page Types (Structural Only)

The seeder assigns a `page_type` to each page based on its title pattern and depth. This is **structural classification only** — it never classifies regulatory content.

| page_type | Detection rule |
|---|---|
| `working_party_root` | Depth 0 (the root page itself) |
| `programme_area` | Depth 1 child of root (e.g., "ADS", "CS/OTA") |
| `informal_working_group` | Title contains "IWG", "Informal Working Group", "Task Force", "TF" |
| `session` | Title matches session pattern ("24th session", "GRVA-24", etc.) |
| `document_list` | Title contains "Documents", "Attachments" |
| `agenda` | Title contains "Agenda" |
| `report` | Title contains "Report" |
| `page` | Default — no pattern matched |

---

## Working Group Detection

The seeder extracts a `working_group` label from page titles and ancestor titles. It matches against a known shortname list: `ADS`, `CS/OTA`, `DSSAD`, `EDR`, `AEBS`, `ADAS`, `VMAD`, `FRAV`.

This is **pattern matching on page titles only** — not regulatory classification. The working group field is set to `null` when no match is found.

---

## Rate Limiting

The seeder waits 0.5 seconds between API calls and retries on HTTP 429/5xx errors (up to 3 retries with exponential backoff). This keeps the crawl safe for the UNECE wiki server.

---

## Integration with Import Pipeline

The `seed.json` produced by this skill feeds directly into `IMPORT_PIPELINE.md` Stage 1 (Batch Discovery):

```
UNECE Confluence Space
        ↓
[UNECE_Space_Seeder.py]     ← this skill
        ↓
output/seed.json            ← page hierarchy + attachment index
        ↓
12 Attachments/Inbox/       ← user selects documents to download
        ↓
IMPORT_PIPELINE.md          ← Stage 2: Document Classification
        ↓
Knowledge Graph
```

The seed does not download files. It produces a reference index so that the user can select which documents to download into `12 Attachments/Inbox/` for processing.

---

## Constraints (Non-Negotiable)

1. **Never summarizes** — reads page metadata only; never reads page body content
2. **Never classifies regulations** — `page_type` is structural; document types are media types only
3. **Never infers relationships** — does not connect pages to vault entities
4. **Never updates the vault** — writes only to `output/`; never touches `.md` notes
5. **Idempotent** — running twice on the same space produces the same output
6. **No knowledge output** — `seed.json` contains structural data, not knowledge claims

---

## Known Limitations

- The UNECE Confluence wiki may restrict access to some pages or attachments without authentication
- Page type detection is heuristic; some pages may receive generic `page` classification
- The `working_group` field relies on title pattern matching and may return `null` for pages with non-standard titles
- Confluence API pagination is handled but very large spaces (1000+ pages) may take several minutes

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-06-27 | Initial implementation |
