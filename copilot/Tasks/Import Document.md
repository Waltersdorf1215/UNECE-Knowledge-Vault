# Task: Import Document

**Type:** One-off task
**Output:** Updated knowledge graph + CHANGELOG.md entry

---

## Instructions for Claude

You are maintaining the UNECE Knowledge OS. A new document has been provided for ingestion.

Before doing anything else, read the following vault documents in order:
1. `CLAUDE.md` — operating rules
2. `IMPORT_PIPELINE.md` — the 9-stage import process (plus Stage 5.5 Knowledge Classification)
3. `KNOWLEDGE_RULES.md` — especially Rule Zero (never elevate inference to fact)

Then execute the import using the full pipeline:

### Stage 1 — Document Classification
Identify the document type (UN Regulation, GTR, Working Document, Informal Document, Meeting Report, etc.) and extract metadata (title, document number, date, submitting body, meeting, status).

### Stage 2 — Metadata Extraction
Extract all identifiable metadata. Do not duplicate it across multiple notes.

### Stage 3 — Entity Discovery
Read the document. List every entity encountered before touching any vault file.

### Stage 4 — Existing Knowledge Check
For each entity: search the vault. Update if exists. Create only if genuinely new.

### Stage 5 — Relationship Discovery
Identify entity relationships. Add wiki links. Only update RELATIONSHIPS.md if a new relationship *type* is discovered.

### Stage 5.5 — Knowledge Classification ⚠️ MANDATORY
Before merging any statement, classify it as one of:
- **Official Fact** — explicitly stated in the document; cite source inline
- **Structural Relationship** — explicit in document structure; cite source
- **Interpretation** — derived by reasoning; label `*Interpretation:*`
- **Personal Insight** — your analysis; goes in Research Notes only

Do not merge any statement that cannot be classified.

### Stage 6 — Knowledge Merge
Merge classified knowledge into existing notes. Never overwrite. Prefer append.

### Stage 7 — Knowledge Validation
Check: no orphan notes, no broken links, no duplicate entities, metadata consistent.

### Stage 8 — Research Generation
Create a Research Note in `10 Research Notes/` if the document introduces new regulatory direction, key design philosophy, or strategic implications.

### Stage 9 — Changelog
Add an entry to `CHANGELOG.md` at the top of the file.

---

## Definition of Done

- [ ] Document classified and metadata extracted
- [ ] All entities discovered before any vault modification
- [ ] Existing notes updated, new notes created only when necessary
- [ ] Every merged statement has been classified (Stage 5.5)
- [ ] All facts carry inline citations
- [ ] All interpretations labeled `*Interpretation:*`
- [ ] Personal insights in Research Notes only
- [ ] Graph validated
- [ ] CHANGELOG.md updated
