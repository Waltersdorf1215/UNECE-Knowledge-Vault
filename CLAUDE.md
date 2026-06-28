# Claude Code Instructions — UNECE Knowledge Vault

This file governs the behavior of any Claude Code session operating inside this Obsidian vault.

---

## Purpose

This is a long-term, structured knowledge base for UNECE / WP.29 / GRVA automated driving regulation research. It is maintained using the LLM Wiki method. Claude's role is to **extend and maintain** this knowledge base accurately and consistently — not to generate speculative content.

---

## Absolute Rules

### Preservation
- **Never overwrite a non-empty file** without explicit user instruction.
- **Never delete or rename files or folders** without asking the user first.
- If a file exists and has real content, read it before touching it.
- **Never rename or move original source files** in `12 Attachments/Inbox/`. They are permanent references. All processing is done in Markdown manifests, not by modifying the source files.

### Accuracy
- **Do not invent regulatory facts.** If you don't know whether a provision exists, say so.
- Clearly distinguish: **Fact** (sourced), **Interpretation** (your reading), **Insight** (analysis).
- Do not hallucinate document numbers, session dates, or regulatory timelines.

### Duplication
- Before creating any new note, check whether a note for that concept already exists.
- If it does, update the existing note rather than creating a duplicate.

### Document Classification — Claude's Responsibility

**The user is never required to classify, rename, sort, or pre-process documents before importing.**

When the user provides a file or drops files into `12 Attachments/Inbox/`, Claude performs all classification automatically:

1. **Document Type** — inferred from filename, folder location, document number pattern, and cover page content. Possible types: Regulation, Working Document, Informal Document, Meeting Report, Agenda, Presentation, Blog, Academic Paper, Other.

2. **Authority Level** — inferred from the document's source and type. Levels: UNECE Official, UNECE Working Document, UNECE Informal Document, UNECE Meeting Report, OEM Official, Academic, Personal.

3. **Confidence Assessment** — Claude must honestly assess classification confidence:
   - `high` — unambiguous from document number or cover page → proceed
   - `medium` — probable but not certain → proceed with note in manifest
   - `low` — cannot be reliably determined → **mark `needs_review`, stop, report to user**
   - `needs_review` — classification failed or is ambiguous → **do not guess; ask the user**

**Guessing is not permitted when confidence is insufficient.** A wrong classification corrupts the knowledge graph. When in doubt, flag `needs_review` and ask for clarification before proceeding.

Authority level determines how content may be cited in vault notes (see IMPORT_PIPELINE.md Stage 3 for the citation treatment per level).

---

## Standard Workflow for Adding Knowledge

1. Identify the relevant note type (regulation, concept, OEM, etc.)
2. Check if the note already exists
3. If not, copy the appropriate template from `11 Templates/`
4. Fill in YAML frontmatter completely
5. Write atomic, sourced content
6. Add at least **three wiki links** to related notes
7. Update at least **one existing related note** to link back to the new note
8. Report what was created or changed in a brief summary

---

## YAML Frontmatter Standard

Every note must have:

```yaml
---
type: regulation | working_group | concept | oem | organization | meeting | proposal | research_note
status: placeholder | draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
---
```

Do not omit any of these fields.

---

## Wiki Link Style

- Use `[[Note Name]]` for all internal links
- Use display text where needed: `[[Note Name|Display Text]]`
- Prefer linking to concept notes over inline explanation
- Every note should link to at least three others

---

## Folder Assignments

| Content | Folder |
|---|---|
| UN Regulations (Rx) | `01 Regulations/` |
| WP.29 body and sessions | `02 WP29/` |
| GRVA body and sessions | `03 GRVA/` |
| Informal working groups | `04 Working Groups/` |
| Technical / regulatory concepts | `05 Concepts/` |
| OEM / supplier tracker | `06 OEM/` |
| Regulatory bodies and orgs | `07 Organizations/` |
| Meeting notes | `08 Meetings/` |
| Submitted proposals | `09 Proposals/` |
| Personal research notes | `10 Research Notes/` |
| Note templates | `11 Templates/` |
| Raw source files | `12 Attachments/` or `raw/` |
| External links / references | `13 Resources/` |

---

## After Each Operation

Always end with a brief summary:
- Files created
- Files modified
- Wiki links added
- Any open questions or TODOs flagged

---

## Intuition-Free Graph Completion

**Claude must not complete the knowledge graph by intuition, pattern recognition, or conceptual similarity.**

### The Core Prohibition

When two entities share a concept, topic, or technical theme, Claude must not infer a legal or regulatory dependency between them without explicit evidence from a named source document.

**Specifically prohibited:**

1. **Conceptual co-occurrence → legal dependency**
   If Regulation A and Regulation B both discuss the same concept (e.g., driver monitoring, event recording, fallback behavior), Claude must not conclude that A and B are legally related, companion regulations, or that one is a prerequisite for the other. Conceptual overlap is not regulatory dependency.

2. **Pattern completion from analogous cases**
   If Regulation A explicitly references Regulation B, Claude must not assume Regulation A also references Regulation C based on structural similarity. Each reference must come from a named source.

3. **Regulatory "ladder" filling**
   Claude must not construct a regulatory hierarchy (e.g., R79 → R171 → R157 → ADS Reg) as if each step legally builds on the previous one, unless this is explicitly stated in official documents. The analytical ladder framing is a Research Note interpretation, not a graph fact.

### What Claude May Do

- **Suggest** inferred relationships in `10 Research Notes/` labeled `*Interpretation:*`
- **Route** uncertain relationships to `11 Review/Pending/` with a clear explanation of what evidence is needed
- **Ask** the user whether a suspected relationship has a source, rather than inventing one

### What Claude Must Never Do

- Store an inferred relationship as an official relationship in any entity note
- Write a relationship between two regulations without citing the specific document and section that establishes it
- Use the phrase "companion regulation", "data-recording companion", "prerequisite regulation", or "derives from" unless these exact relationships are stated in an official source
- Treat the absence of contradiction as evidence of support ("they're compatible, so they must be related")

### Handling Inferred Relationships

When Claude encounters what appears to be a meaningful relationship but lacks explicit evidence:

```
CORRECT process:
1. Note the two entities
2. Note what relationship seems plausible
3. Note why it seems plausible (conceptual similarity, pattern, etc.)
4. Label it *Interpretation:* 
5. Place it in 10 Research Notes/ or 11 Review/Pending/
6. Record what specific evidence would be needed to confirm it

INCORRECT process:
1. Note the two entities
2. Conclude the relationship exists
3. Store it in an entity note
```

---

## Inference Drift Prevention

**This is the most important reasoning discipline in this vault.**

Inference drift occurs when a logically reasonable conclusion — not explicitly stated in any source — is written into a regulation note, concept note, or working group note as if it were an official fact. This corrupts the knowledge graph over time.

### The Mandatory Pre-Write Check

Before writing any statement into any note, ask exactly these four questions in order:

**1. Is this explicitly stated in a specific named source document?**
- If YES → write it as a Fact with an inline citation: `**Fact (source, §X.Y):**`
- If NO → do not call it a fact. Proceed to question 2.

**2. Is this derived by combining information from two or more documents?**
- If YES → it is an Interpretation. Label it: `*Interpretation:*`
- If NO → proceed to question 3.

**3. Is this my own analysis or hypothesis?**
- If YES → it is a Personal Insight. Write it in `10 Research Notes/` only. Never in regulation or concept notes.

**4. Am I unsure?**
- Default to `[VERIFY]`. Do not merge unverified content.

### Hard Rules

- **Never** write an inferred relationship as an official fact in a regulation note, concept note, or working group note.
- **Never** describe the relationship between two regulations as "companion" or "prerequisite" unless the source document uses those words or explicitly states the dependency.
- **Never** characterize an OEM's position, a regulation's intent, or a working group's philosophy without a direct citation.
- **Always** label interpretation sections with `*Interpretation:*` at the start of the paragraph.
- **Always** label insight sections with `*Insight:*` at the start of the paragraph.
- Unlabeled text in a regulation or concept note is understood to be a **sourced Fact**. If it cannot be sourced, it must be labeled or moved.

### Classification Summary

| Content Type | Label | Location |
|---|---|---|
| Explicitly stated in source document | `**Fact (source §X):**` or unmarked with citation | Any note |
| Describes explicit document structure (X drafts Y, X adopted by Y) | No label needed — cite document | Any note |
| Logical conclusion from multiple documents | `*Interpretation:*` | Any note — clearly marked |
| Personal analysis or hypothesis | `*Insight:*` | Research Notes only |
| Unverified — needs source | `[VERIFY]` | Any note — flagged for follow-up |

---

## Escalation

If uncertain about:
- Whether a fact is accurate → do not write it, flag it as `[VERIFY]`
- Whether a statement is a fact or interpretation → apply the Inference Drift Pre-Write Check above
- Whether a file should be overwritten → ask the user
- Whether a note should be split or merged → propose the change before acting
