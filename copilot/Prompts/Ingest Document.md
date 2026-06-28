# Prompt: Ingest Document

**Parameters to fill before use:**
- `{{DOCUMENT_PATH}}` — local file path or attachment reference
- `{{DOCUMENT_TYPE}}` — e.g., UN GTR, UN Regulation, Working Document, Informal Document, Meeting Report
- `{{DOCUMENT_NUMBER}}` — e.g., ECE/TRANS/WP.29/2026/139 (or "unknown")
- `{{SUBMITTING_BODY}}` — e.g., GRVA, WP.29, ADS IWG
- `{{SESSION}}` — e.g., WP.29 199th session (or "unknown")

---

## Prompt Text

```
You are maintaining the UNECE Knowledge OS Obsidian vault.

Before starting, read:
- CLAUDE.md
- IMPORT_PIPELINE.md (all 9 stages including Stage 5.5)
- KNOWLEDGE_RULES.md (especially Rule Zero)

Document to ingest:
- Path: {{DOCUMENT_PATH}}
- Type: {{DOCUMENT_TYPE}}
- Document number: {{DOCUMENT_NUMBER}}
- Submitting body: {{SUBMITTING_BODY}}
- Associated session: {{SESSION}}

Execute the full import pipeline (IMPORT_PIPELINE.md Stages 1–9).

Critical constraint: Before merging any statement, apply Stage 5.5 — 
Knowledge Classification. Every statement must be classified as:
- Official Fact (explicitly stated; cite source inline)
- Structural Relationship (explicit in document; cite source)
- Interpretation (label *Interpretation:*)
- Personal Insight (Research Notes only)

Never merge an inferred relationship as an official fact.

At the end, produce a changelog entry for CHANGELOG.md.
```

---

## Notes

- Replace all `{{PARAMETERS}}` with actual values before using
- If document number is unknown, use "unknown" and add `[VERIFY]` to the note
- If the document is a PDF, use pypdf for extraction: `python3 -c "import pypdf; ..."`
