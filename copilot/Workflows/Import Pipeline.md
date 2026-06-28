# Workflow: Import Pipeline

**Type:** Multi-step SOP
**Vault Reference:** `IMPORT_PIPELINE.md` (authoritative definition)
**Duration:** One session per document (typically)
**Output:** Updated knowledge graph, new/updated notes, CHANGELOG.md entry

---

## Purpose

This workflow guides Claude through the full document import process for the UNECE Knowledge OS. It sequences the 9-stage pipeline from `IMPORT_PIPELINE.md` with explicit checkpoints, decision points, and epistemic safeguards.

Use this workflow whenever a new UNECE document (PDF, DOCX, or text) arrives for ingestion.

---

## Pre-Flight Checks

Before starting, confirm:
- [ ] `CLAUDE.md` read this session
- [ ] `IMPORT_PIPELINE.md` read this session
- [ ] `KNOWLEDGE_RULES.md` read this session (especially Rule Zero)
- [ ] `RELATIONSHIPS.md` Section 0 (Evidential Constraint) read this session
- [ ] Document is accessible (local file path confirmed)

---

## Phase 1 — Document Intake
*Uses: `Tasks/Import Document.md`, `Prompts/Ingest Document.md`*

### 1.1 Classify the Document
Determine: UN Regulation | UN GTR | Working Document | Informal Document | Meeting Report | Presentation | Other

### 1.2 Extract Metadata
| Field | Value |
|---|---|
| Title | |
| Document Number | |
| Date | |
| Submitting Body | |
| Associated Meeting | |
| Status | |

### 1.3 Locate in Vault
Does a note already exist for the primary entity this document describes?
- If YES → prepare to update the existing note
- If NO → prepare to create a new note (use `Tasks/Create Entity.md`)

---

## Phase 2 — Entity Discovery

**Do not touch any vault file yet.**

Read the document and build an entity list:

| Entity | Type | Vault Status |
|---|---|---|
| | | exists / missing |

For each entity: search the vault for an existing note.

---

## Phase 3 — Relationship Mapping

For each pair of entities, identify the relationship and classify its evidence tier:

| Entity A | Relationship | Entity B | Evidence Tier | Source |
|---|---|---|---|---|
| | | | Explicit / Structural / Inferred | |

**Inferred relationships do not enter the graph without a `[VERIFY]` flag or `*Interpretation:*` label.**

---

## Phase 4 — Knowledge Classification Gate
*Uses: `Prompts/Classify Knowledge.md`*

For each statement to be merged:

Run through the four-question Inference Drift Test:
1. Explicitly stated in source? → Official Fact + cite
2. Derived by combining sources? → Interpretation + label
3. Structural process relationship? → Structural Relationship + cite
4. Personal analysis? → Research Note only

Only classified statements proceed to Phase 5.

---

## Phase 5 — Merge
*Uses: `Prompts/Update Entity.md` or `Prompts/Create Regulation Note.md` / `Prompts/Create Concept Note.md`*

For each entity:
1. Update existing note or create new note
2. Apply correct labels (Fact citation / `*Interpretation:*`)
3. Add wiki links for all discovered relationships
4. Set `knowledge_type` and `evidence_level` YAML fields

---

## Phase 6 — Validation

Check:
- [ ] No new orphan notes created
- [ ] No broken wiki links
- [ ] All merged statements classified
- [ ] All facts have inline citations
- [ ] All interpretations labeled
- [ ] No personal insights in authoritative notes

---

## Phase 7 — Research Note (if warranted)

Create a Research Note if the document introduces:
- New regulatory direction
- Key design philosophy
- AI or technology implications
- Strategic open questions

---

## Phase 8 — Timeline Update
*Uses: `Tasks/Update Timeline.md`*

Add any confirmed milestones to the relevant `14 Timeline/` notes.

---

## Phase 9 — Changelog

Add an entry to `CHANGELOG.md` at the top of the file:
```
## Import — YYYY-MM-DD | [Document Title]
**Imported Documents**: ...
**Updated Notes**: ...
**Created Notes**: ...
**New Relationships**: ...
**Open Questions**: ...
**Follow-up Documents**: ...
```

Also update `ROADMAP.md` — move the imported item from its priority queue to Completed.

---

## Exit Criteria

- [ ] All phases completed
- [ ] CHANGELOG.md updated
- [ ] ROADMAP.md updated
- [ ] No unclassified statements remain in notes
