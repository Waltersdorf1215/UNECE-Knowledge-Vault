# Inbox — Raw Meeting Package Drop Zone

This is the entry point for all unprocessed documents.

## How to Use

1. Download the full document package from a UNECE meeting or working group session.
2. Drop the files into the appropriate subfolder without renaming them.
3. Tell Claude: "New documents in Inbox — please process."
4. Claude will scan, classify, and extract knowledge automatically. No manual classification needed.

## Subfolders

| Folder | Drop documents from |
|---|---|
| `GRVA/` | GRVA plenary sessions |
| `WP29/` | WP.29 sessions |
| `VMAD/` | VMAD informal working group sessions |
| `FRAV/` | FRAV informal working group sessions |
| `ADS/` | ADS IWG sessions |
| `Misc/` | Everything else — EU regulations, OEM documents, academic papers |

## Rules

- **Never rename files.** Preserve the original filename exactly as downloaded.
- **Never delete files from Inbox.** Knowledge extraction references originals by path.
- **Nested meeting packages are fine.** If a GRVA session has its own subfolder, keep that structure.
- **All file types are accepted.** PDF, DOCX, XLSX, PPT — Claude will handle each.

## What Happens Next

Claude performs three pre-extraction stages automatically:

1. **Batch Discovery** — scans Inbox for new files, builds a discovery manifest
2. **Document Classification** — identifies each document's type (Regulation, Working Document, Informal Document, Meeting Report, Agenda, Presentation, etc.)
3. **Authority Classification** — assigns each document an authority level (UNECE Official, UNECE Working Document, UNECE Informal, OEM Official, Academic, Personal)

Only after those three stages does knowledge extraction begin.

Processing records are written to `../Processed/` — the original files in Inbox are never modified.
