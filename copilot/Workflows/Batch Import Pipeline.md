# Workflow: Batch Import Pipeline

**Type:** Multi-step SOP
**Vault Reference:** `IMPORT_PIPELINE.md` (Phase 1 Stages 1–3, then Phase 2 Stages 4–11)
**Duration:** One or two sessions depending on package size
**Trigger:** User drops a meeting package into `12 Attachments/Inbox/`
**Output:** Processing manifests in `Processed/`, updated knowledge graph, CHANGELOG.md entry

---

## Purpose

This workflow handles the import of a full UNECE meeting document package — for example, all documents from a GRVA session or WP.29 session downloaded in bulk. The user drops files into `Inbox/` without pre-sorting; Claude does everything else.

---

## Pre-Flight

- [ ] Files are in `12 Attachments/Inbox/[meeting subfolder]/`
- [ ] `IMPORT_PIPELINE.md` read this session (especially Stages 1–3)
- [ ] `CLAUDE.md` Document Classification rule recalled

---

## Phase 1 — Batch Intake (Stages 1–3)

### Stage 1 — Batch Discovery

List all files in `12 Attachments/Inbox/` that lack a manifest in `12 Attachments/Processed/`.

Build and display a discovery table:

```
| # | File | Inbox Subfolder | Extension | Manifest Exists? |
|---|---|---|---|---|
| 1 | ECE-TRANS-WP29-2026-139e.pdf | UNECE/ | PDF | Yes |
| 2 | GRVA-24-0045.pdf | GRVA/ | PDF | No |
...
```

Files with existing manifests are skipped unless the user explicitly asks for reprocessing.

---

### Stage 2 — Document Classification

For each unprocessed file, determine `document_type` and `classification_confidence`.

Classification rules (in priority order):

1. **Document number in filename** — most reliable signal:
   - `ECE-TRANS-WP.*-\d{4}-\d+` → Working Document or Regulation
   - `GRVA-\d{2}-\d+` → Informal Document
   - `WP\.29-\d{3}-\d+` → Informal Document
   - `ADS-\d{2}-\d+` → Informal Document (ADS IWG)
   - `VMAD-\d{2}-\d+` → Informal Document (VMAD)

2. **Filename keywords**:
   - "Agenda" → Agenda
   - "Report" → Meeting Report
   - "Regulation" or "GTR" → Regulation
   - "Presentation" or ".pptx" → Presentation

3. **Cover page** — for low-confidence files, read the first page to confirm

**Display classification table to user before proceeding:**

```
| File | Classified As | Confidence | Action |
|---|---|---|---|
| ECE-TRANS-WP29-2026-139e.pdf | Regulation | high | proceed |
| GRVA-24-0045.pdf | Informal Document | high | proceed |
| unknown-doc.pdf | Other | low | NEEDS REVIEW — stop |
```

**Stop and ask the user** for any file marked `needs_review` before proceeding.

---

### Stage 3 — Authority Classification

For each document with `classification_confidence: high` or `medium`, assign `authority_level`:

| Classification | Authority Level |
|---|---|
| Regulation (ECE/TRANS/WP.29/YYYY/N) | UNECE Official |
| Working Document (ECE/TRANS/WP.29/GR/YYYY/N) | UNECE Working Document |
| Informal Document (GRVA-XX, WP.29-XXX, ADS-XX) | UNECE Informal Document |
| Meeting Report (final session report) | UNECE Working Document |
| Agenda | UNECE Working Document |
| Presentation | UNECE Informal Document |
| OEM-sourced | OEM Official |
| Academic | Academic |
| Personal | Personal |

**Create a processing manifest** in `12 Attachments/Processed/[type subfolder]/` for each document.

Manifest filename: `[DocumentNumber or sanitised filename]-manifest.md`

Manifest YAML (fill Stage 2–3 fields now; leave extraction fields blank):

```yaml
---
type: document_manifest
document_type: [from Stage 2]
authority_level: [from Stage 3]
classification_confidence: [high | medium | low | needs_review]
meeting: ""
working_group: ""
document_number: ""
source_url: ""
inbox_path: "12 Attachments/Inbox/[subfolder]/[filename]"
status: pending
extraction_date: ""
vault_notes_updated: []
---
```

---

## Phase 1 Output Gate

Before proceeding to Phase 2:
- [ ] Every file has been classified
- [ ] All `needs_review` files have been reported to the user and awaiting decision
- [ ] All manifests created in `Processed/`
- [ ] Classification table confirmed with user (or auto-proceed if all high/medium)

**Do not begin knowledge extraction until this gate passes.**

---

## Phase 2 — Knowledge Extraction (per document)

Run `Workflows/Import Pipeline.md` Stages 4–11 for each document in priority order.

**Priority order for extraction:**
1. Formally adopted regulations and GTRs (UNECE Official)
2. Formal working documents (UNECE Working Document)
3. Session reports (confirms decisions)
4. Informal documents (technical proposals)
5. Agendas (context only)
6. Presentations (background)

---

## Batch Session Management

For large packages (>5 documents), process in multiple sessions:

1. Complete Phase 1 (all files classified) in session 1
2. Extract highest-priority documents in session 1
3. Record progress in each manifest (`status: partial`)
4. Continue in subsequent sessions by scanning for `status: pending` or `status: partial` manifests

**State recovery:** At the start of a resumed session, scan `Processed/` for pending/partial manifests and resume from the highest-priority unfinished document.

---

## Exit Criteria

- [ ] All unprocessed files have manifests
- [ ] `needs_review` files reported or resolved
- [ ] All high/medium confidence documents have `status: extracted` or `status: partial`
- [ ] CHANGELOG.md updated with batch summary
- [ ] ROADMAP.md updated (completed items checked off)
