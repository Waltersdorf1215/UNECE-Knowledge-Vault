# Knowledge Merge Skill

## Purpose

Merge structured evidence and analysis outputs into the UNECE Knowledge OS.

This skill updates Markdown notes **only after evidence has already been collected and analyzed**. It is the only skill permitted to write to knowledge notes in the vault. It never generates knowledge from scratch — it merges verified evidence into the existing graph.

---

## When to Use

Use this skill when the user asks to:

- Merge evidence into the vault
- Update notes from an evidence JSON file
- Update regulation notes (`01 Regulations/`)
- Update concept notes (`05 Concepts/`)
- Update working group notes (`04 Working Groups/`)
- Update timeline notes (`14 Timeline/`)
- Update session notes (`02 WP29/`, `03 GRVA/`, `08 Meetings/`)
- Add or update wiki links
- Create missing entity notes from a known entity list
- Route uncertain or unsupported claims to the Review Queue (`11 Review/Pending/`)
- Generate a changelog entry after a merge

---

## When NOT to Use

Do **not** invoke this skill to:

- Browse the web or fetch URLs
- Download PDFs or attachments
- Summarize documents from scratch (no source → no merge)
- Infer relationships that have no explicit evidence
- Overwrite or replace existing sourced knowledge
- Write official claims without a traceable evidence source
- Make regulatory interpretations (those go to Research Notes or Review Queue)
- Run the Acquire or Analyze skill responsibilities

---

## Inputs

This skill expects one or more of the following as input. All inputs must be pre-produced by an Acquire or Analyze skill — this skill does not generate them.

| Input file | Description |
|---|---|
| `evidence.json` | Extracted facts with source citations |
| `entities.json` | Entity list with types and identifiers |
| `relationships.json` | Relationship triples with evidence metadata |
| `timeline.json` | Dated events with source references |
| `source_map.json` | Document → vault note mapping |
| `open_questions.json` | Unresolved items flagged for review |
| Manual user instructions | Direct user request with stated evidence |

If no structured input is present, ask the user to provide evidence before proceeding.

---

## Core Rules

These rules are absolute. They apply to every operation this skill performs.

1. **Update existing notes before creating new ones.** Search the vault before creating any note.
2. **Never overwrite existing knowledge.** Append — do not replace. Existing sourced content is never deleted.
3. **Preserve YAML frontmatter.** Required fields must remain present. `created` is never changed. `last_updated` is set to today's date on every touched note.
4. **Preserve source traceability.** Every fact must carry an inline citation: `**Fact (document, §X.Y):**`
5. **Every official fact must have explicit evidence.** If no source can be named, the claim is not merged.
6. **Every relationship must pass the Evidence Gate.** See Step 4 of the Merge Workflow.
7. **Inferred relationships go to Review Queue.** They are never written into entity notes as official relationships.
8. **Conceptual similarity is not legal dependency.** Two regulations sharing a concept does not mean one requires or references the other.
9. **Low confidence → create review item, do not merge.** When `confidence: low` or `needs_review`, route to `11 Review/Pending/` and do not write to the entity note.
10. **Prefer uncertainty over false certainty.** A `[VERIFY]` flag and an open question are better than a confident wrong fact.

---

## Merge Workflow

### Step 1 — Load Operating System Rules

Before editing any vault file, read the following documents **in this session**:

- `CLAUDE.md` — operating rules and Inference Drift Prevention
- `KNOWLEDGE_RULES.md` — Rule Zero and epistemic labeling
- `SCHEMA.md` — entity types, YAML fields, edge metadata schema
- `RELATIONSHIPS.md` — §0.5 Evidence-backed Relationships and §0.6 Relationship Classes
- `IMPORT_PIPELINE.md` — Stage 7.2 Evidence Gate
- `REVIEW_PIPELINE.md` — when and how to create review items

Do not proceed until these are loaded. They are the governance layer for every decision in this skill.

---

### Step 2 — Load Evidence Outputs

Read all provided input files. For each file, identify:

- **Entities** — what things are being described (regulations, concepts, sessions, orgs, OEMs)
- **Relationships** — what connections between entities are asserted
- **Sources** — what document, section, and paragraph supports each claim
- **Timeline events** — what dated milestones are confirmed
- **Open questions** — what could not be resolved from the evidence

Build a working merge plan before touching any file:

```
Entity A  →  update note [path]  →  add [claim]  →  evidence [source §X]
Entity B  →  create note         →  template: [type]
Relationship X→Y  →  evidence_strength: [level]  →  merge or route
Timeline event  →  [14 Timeline/X.md]  →  confirmed or pending
```

---

### Step 3 — Match Existing Notes

For each entity in the evidence:

1. Search the vault by entity name and known aliases
2. **If the note exists:** open it, read it fully, then append new knowledge
3. **If the note does not exist:** create it using the appropriate template from `11 Templates/`

Template assignment:

| Entity type | Template |
|---|---|
| Regulation | `11 Templates/Regulation Template.md` |
| Working Group | `11 Templates/Working Group Template.md` |
| Meeting / Session | `11 Templates/Meeting Template.md` |
| Concept | `11 Templates/Technical Concept Template.md` |
| OEM | `11 Templates/OEM Template.md` |
| Organization | `11 Templates/Organization Template.md` |
| Proposal | `11 Templates/Proposal Template.md` |
| Research Note | `11 Templates/Research Note Template.md` |

Do not create a note if the entity is already covered under a different name — add an alias instead.

---

### Step 4 — Evidence Gate

**This step is mandatory for every claim and every relationship.**

Before writing any statement into a note, answer all five questions:

**Q1. Is this claim explicitly stated in a named source document?**
- YES → `evidence_strength: explicit` — write with inline citation
- NO → proceed to Q2

**Q2. Does it follow clearly from document structure or institutional process?**
- YES → `evidence_strength: derived` — write with citation noting derivation
- NO → proceed to Q3

**Q3. Is it a logical inference across two or more documents?**
- YES → `evidence_strength: inferred` — do NOT write in entity note; route to `11 Review/Pending/`
- NO → proceed to Q4

**Q4. Is it the author's own analysis or hypothesis?**
- YES → Personal Insight — write only in `10 Research Notes/`; never in entity notes

**Q5. Is the confidence level?**
- `high` or `medium` with `explicit` or `derived` strength → merge
- `low` or `needs_review` → route to `11 Review/Pending/` regardless of strength

**Forbidden transformation — always block:**
> "Entity A and Entity B share concept C" → "Entity A requires / depends on / derives from Entity B"

This is the most common source of inference drift. It is blocked at this gate unconditionally.

---

### Step 5 — Merge Knowledge

Add knowledge into the note under the correct section. Use the section headings from the relevant template. The standard section order is:

```
## Summary          ← one or two sourced sentences
## Scope            ← what the entity covers (regulation) or what it does (WG, concept)
## Key Requirements / Key Facts   ← sourced facts only; inline citations required
## Relationships    ← evidence-backed relationships only
## Timeline / Regulatory History  ← dated events with sources
## Related Concepts ← wiki links with relationship labels
## Open Questions   ← [VERIFY] items and unresolved gaps
## Sources          ← primary source documents
```

Epistemic labeling rules:
- Sourced fact → no label; include inline citation
- Logical conclusion → `*Interpretation:* …`
- Personal analysis → `*Insight:* …` (Research Notes only)
- Unverified → `[VERIFY]`

Never mix labeled and unlabeled content in the same paragraph.

---

### Step 6 — Update Relationships

Add only relationships with `evidence_strength: explicit` or `derived`.

Use the four relationship classes from `RELATIONSHIPS.md §0.6`:

| Class | Requirement | Storage |
|---|---|---|
| Class 1 — Official | Explicit or derived evidence; cite source | Entity notes |
| Class 2 — Structural | Document structure basis; cite document | Entity notes |
| Class 3 — Conceptual | Must be labeled `*Interpretation:*` | Concept notes only |
| Class 4 — Interpretive | No explicit evidence | Research Notes or Review Queue only |

Required inline evidence format for Class 1–2 relationships:

```
**Fact (ECE/TRANS/WP.29/2026/139, §4.3.2, explicit, high):** [quote or paraphrase]
→ [[Entity A]] `requires` [[Entity B]]
```

Do not add a wiki link for a relationship that cannot pass the Evidence Gate.

---

### Step 7 — Update Timeline

In `14 Timeline/`, add confirmed milestone entries only when:

- A specific date is stated in the source
- The event is described as having occurred (not planned or expected)
- The source can be cited

Format:

```markdown
| YYYY-MM-DD | Event description | Document number | Source |
```

For uncertain dates or future events, use the **Pending Milestones** table with `[VERIFY]`.

Never add a timeline entry based on inference. If the date is inferred from context ("this was probably in 2024"), mark `[VERIFY]` and note the inference.

---

### Step 8 — Route to Review Queue

Create a review item in `11 Review/Pending/` for any of the following:

- A relationship with `evidence_strength: inferred` or `unsupported`
- A claim with `confidence: low` or `needs_review`
- A date that cannot be confirmed
- A cross-regulation dependency with no explicit citation
- A conflicting claim (evidence from two sources that contradict each other)
- A Class 3 or Class 4 relationship that might be important

Review item filename format: `[EntityA]-[EntityB]-[topic]-review.md`

Each review item must include:
- The claim or relationship that was blocked
- Why it was blocked (missing evidence, low confidence, inference)
- Safer alternative wording
- What specific evidence would confirm it
- Resolution options (Approve / Reject / Defer)

---

### Step 9 — Changelog

After all merges are complete, append a new entry to `CHANGELOG.md`:

```markdown
## Merge — YYYY-MM-DD | [Topic or Source Document]

### Files Updated
- `path/to/note.md` — [what was added]

### Files Created
- `path/to/new-note.md` — [entity type, why created]

### Relationships Added
- Entity A → relationship → Entity B [source]

### Review Items Created
- `11 Review/Pending/[filename].md` — [reason]

### Claims Rejected (Evidence Gate)
- [claim] — [reason blocked]

### Remaining Evidence Gaps
- [gap description] — [what evidence would resolve it]
```

---

## Output

After skill execution, report:

| Output | Description |
|---|---|
| Created notes | New entity notes added to vault |
| Updated notes | Existing notes that received new content |
| Relationships merged | Class 1–2 relationships added to graph |
| Review items created | Items routed to `11 Review/Pending/` |
| Claims rejected | Claims blocked by Evidence Gate |
| Evidence gaps | Knowledge that could not be merged due to missing sources |

---

## Constraints

- This skill only writes to vault Markdown files
- It never downloads files, fetches URLs, or reads binary files
- It never calls external APIs
- It never generates knowledge without a source
- It never deletes or renames existing files
- It never changes the `created` field in YAML frontmatter
- It defers to the user on any irreversible action (note deletion, major restructuring)
