# Prompt: Classify Batch

**Purpose:** Automatically classify all unprocessed files in `12 Attachments/Inbox/` before knowledge extraction begins.

**Parameters to fill before use:**
- `{{INBOX_PATH}}` — subfolder to scan, e.g., `12 Attachments/Inbox/GRVA/` (or `12 Attachments/Inbox/` for all)
- `{{MEETING_HINT}}` — optional: meeting name to aid classification, e.g., "GRVA 24th Session" (or "unknown")

---

## Prompt Text

```
You are maintaining the UNECE Knowledge OS Obsidian vault.

Read CLAUDE.md — specifically the "Document Classification" rule — before starting.

Task: Classify all unprocessed files in {{INBOX_PATH}}.
Meeting context (if known): {{MEETING_HINT}}

Steps:

1. List all files in {{INBOX_PATH}} recursively.
2. Check 12 Attachments/Processed/ for existing manifests. Skip files that already 
   have a manifest with status: extracted.
3. For each unprocessed file, determine:
   a. document_type (Regulation | Working Document | Informal Document | Meeting Report | 
      Agenda | Presentation | Blog | Academic Paper | Other)
   b. authority_level (UNECE Official | UNECE Working Document | UNECE Informal Document | 
      UNECE Meeting Report | OEM Official | Academic | Personal)
   c. classification_confidence (high | medium | low | needs_review)

4. Use the following classification signals in priority order:
   - Filename document number pattern (most reliable)
   - Inbox subfolder name (GRVA/ → likely GRVA session documents)
   - File extension (.pptx → Presentation, .pdf could be anything)
   - First page content (for ambiguous files — read cover page)

5. Build and display a classification table:

| # | File | document_type | authority_level | confidence |
|---|---|---|---|---|
| 1 | [filename] | [type] | [level] | [confidence] |

6. For all files with confidence: high or medium:
   Create a processing manifest in 12 Attachments/Processed/[type subfolder]/.

7. For all files with confidence: low or needs_review:
   List them separately and DO NOT create a manifest.
   Report to the user and wait for instructions.

Constraint: Never guess when confidence is low. Never rename or move the original files.
Constraint: Do not begin knowledge extraction in this step — classification only.

Output:
- Classification table (all files)
- Needs-review list (files requiring user input)
- Count of manifests created
- Ready-to-extract list (high/medium confidence, manifests created)
```

---

## Notes

- Run this before any knowledge extraction session on a new batch
- For the `needs_review` list, ask the user: "Please confirm the document type for these files before I proceed."
- After user confirms `needs_review` items, update those manifests and add them to the ready-to-extract list
