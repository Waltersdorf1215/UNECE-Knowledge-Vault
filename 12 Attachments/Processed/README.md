# Processed — Import Manifests and Processing Records

This folder contains Markdown **import manifests** — one per processed document — that record classification, metadata, extraction status, and vault links.

**The original PDF/DOCX files are never moved here.** They remain permanently in `../Inbox/`. This folder contains only Markdown records referencing them.

## Subfolders

| Folder | Contains manifests for |
|---|---|
| `Regulations/` | UN Regulations (Rx), UN GTRs, EU implementing regulations |
| `Working Documents/` | Official formal working documents (ECE/TRANS/WP.29/…) |
| `Informal Documents/` | Informal documents (GRVA-XX-YYY, WP.29-XXX, ADS-XX-YYY) |
| `Reports/` | Session reports, IWG reports, progress reports |
| `Agendas/` | Session agendas and annotated agendas |
| `Presentations/` | Slide decks, briefing documents |

## Manifest File Format

Each manifest is named to match the source document:

```
[DocumentNumber or Filename]-manifest.md
```

Example: `ECE-TRANS-WP29-2026-139-manifest.md`

### Manifest YAML Frontmatter

```yaml
---
type: document_manifest
document_type: Regulation | Working Document | Informal Document | Meeting Report | Agenda | Presentation | Blog | Academic Paper | Other
authority_level: UNECE Official | UNECE Working Document | UNECE Informal Document | OEM Official | Academic | Personal
classification_confidence: high | medium | low | needs_review
meeting: ""                  # e.g., WP.29 199th Session
working_group: ""            # e.g., GRVA, ADS IWG, VMAD
document_number: ""          # e.g., ECE/TRANS/WP.29/2026/139
source_url: ""               # URL where downloaded (if known)
inbox_path: ""               # relative path to original file in Inbox/
status: pending | extracted | partial | needs_review
extraction_date: YYYY-MM-DD
vault_notes_updated: []      # list of vault notes updated from this document
---
```

## How Manifests Are Created

Claude creates a manifest automatically during Stage 2 (Document Classification) of the import pipeline. The manifest is updated as processing advances through the pipeline stages.

When `status: extracted`, the document has been fully processed and all knowledge has been merged into the vault. When `status: needs_review`, the classification confidence was low and the manifest needs human verification before extraction proceeds.
