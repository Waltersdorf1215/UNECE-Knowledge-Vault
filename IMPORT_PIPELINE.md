
# UNECE Knowledge OS
## Knowledge Ingestion Standard Operating Procedure (SOP)

---

# Purpose

This document defines the standard workflow for importing any new knowledge into the UNECE Knowledge OS.

The objective is **not** to summarize documents.

The objective is to continuously maintain and evolve the knowledge graph.

Claude should always think in terms of:

> **Knowledge Graph Maintenance**

instead of

> **Document Summarization**

---

# Rule Zero

Whenever a new document is received:

**DO NOT summarize it first.**

Instead:

1. Identify knowledge.
2. Merge knowledge.
3. Update the graph.
4. Preserve history.

---

# Rule: The User Does Not Classify Documents

**The user is never required to classify, rename, or sort documents before importing.**

Claude performs all classification automatically. If classification confidence is low, Claude marks the document `needs_review` and waits for human confirmation before proceeding to knowledge extraction. Guessing is not permitted when confidence is insufficient.

---

# Phase 1 — Batch Intake

Stages 1–3 apply to every session before any knowledge extraction begins.
They treat the meeting package as the input, not individual pre-classified PDFs.

---

# Stage 1 — Batch Discovery

Scan `12 Attachments/Inbox/` for all files that do not yet have a processing manifest in `12 Attachments/Processed/`.

**Actions:**

1. List all files recursively under `12 Attachments/Inbox/`
2. Check `12 Attachments/Processed/` for an existing manifest matching each file
3. Build a **discovery manifest** — a list of unprocessed files:

```
File: [inbox path]
Folder hint: [GRVA | WP29 | VMAD | FRAV | ADS | Misc]
File extension: [PDF | DOCX | PPTX | XLSX | other]
Status: new
```

4. Do not read any document's content yet — discovery is filename and path only

**Output:** Discovery manifest listing all new files to be processed

---

# Stage 2 — Document Classification

For each file in the discovery manifest, automatically determine the document type.

**Claude must infer the document type.** The user is not required to provide this.

**How to classify:**

| Signal | Method |
|---|---|
| Filename | Check for document number patterns (ECE/TRANS, GRVA-XX, WP.29-XXX, ADS-XX) |
| File path | The Inbox subfolder (GRVA/, WP29/, ADS/) provides a strong hint |
| Cover page | For PDFs/DOCX, read the first page to confirm type |
| Title line | "Agenda", "Report", "Proposal", "Regulation", "GTR", etc. |
| Document number format | ECE/TRANS/WP.29/YYYY/N → Working Document; GRVA-XX-NNN → Informal Document |

**Document Types:**

| Type | Description | Example |
|---|---|---|
| `Regulation` | A formally adopted UN Regulation or GTR | ECE/TRANS/WP.29/2026/139 |
| `Working Document` | Formal document submitted to a session | ECE/TRANS/WP.29/GRVA/2026/2 |
| `Informal Document` | Informal document (INF) submitted to a session | GRVA-24-0012 |
| `Meeting Report` | Official session report | Report of the 24th GRVA session |
| `Agenda` | Session agenda (provisional or final) | Provisional agenda, WP.29 199th |
| `Presentation` | Slide deck or briefing material | .pptx, branded deck |
| `Blog` | OEM or industry technical blog post | .html, .pdf editorial |
| `Academic Paper` | Peer-reviewed or preprint research | DOI-referenced paper |
| `Other` | Anything not matching the above | |

**Confidence levels:**

| Level | Meaning | Action |
|---|---|---|
| `high` | Type is unambiguous from document number or cover page | Proceed to Stage 3 |
| `medium` | Type is probable but not certain | Proceed with note in manifest |
| `low` | Type cannot be determined reliably | Mark `needs_review`; stop extraction |
| `needs_review` | Classification failed or is ambiguous | Report to user before proceeding |

**Output:** Each file in the discovery manifest now has `document_type` and `classification_confidence`

---

# Stage 3 — Authority Classification

For each classified document, assign an authority level that governs how its content may be cited in vault notes.

**Claude must infer the authority level from the document type and source.** The user does not need to provide this.

**Authority Levels:**

| Level | Description | Citation treatment |
|---|---|---|
| `UNECE Official` | Formally adopted UN Regulation or GTR (ECE/TRANS/WP.29/YYYY/N series) | May be cited as Official Fact |
| `UNECE Working Document` | Formal working document submitted to a GRVA or WP.29 session | May be cited as Official Fact or Structural Relationship |
| `UNECE Informal Document` | Informal document submitted to a session (INF series, GRVA-XX-NNN) | May be cited as Structural Relationship; interpretations require label |
| `UNECE Meeting Report` | Official session report (ECE/TRANS/WP.29/XXXX report series) | May be cited as Structural Relationship for decisions confirmed in report |
| `OEM Official` | Manufacturer press release, product announcement, or technical submission | Tier 3 — context only; label *Interpretation:* for all extracted claims |
| `Academic` | Peer-reviewed paper or technical report | Tier 3 — use for technical background; not for regulatory facts |
| `Personal` | User's own notes, analysis, or external summaries | Personal Insight only; Research Notes exclusively |

**How to assign:**

1. UNECE Official: document number is `ECE/TRANS/WP.29/YYYY/N` and describes an adopted regulation
2. UNECE Working Document: document number is `ECE/TRANS/WP.29/[GR]/YYYY/N` (formal GRVA/WP.29 doc)
3. UNECE Informal Document: number is `GRVA-XX-NNN`, `WP.29-XXX-NNN`, `ADS-XX-NNN`, etc.
4. UNECE Meeting Report: document is the official session report (ECE/TRANS/WP.29/XXXX, final)
5. OEM Official: source is a manufacturer, supplier, or industry association
6. Academic: source is a journal, conference, or research institution
7. Personal: no official source

**Output:** Each file now has `document_type`, `authority_level`, and `classification_confidence`

**Only documents with `classification_confidence: high` or `medium` proceed to Phase 2.**
Documents with `classification_confidence: low` or `needs_review` are held and reported to the user.

---

# Phase 2 — Knowledge Extraction

Stages 4–11 apply to each document after Phase 1 classification is complete.
These stages are unchanged in logic from prior pipeline versions — only their numbering has shifted.

---

# Stage 4 — Metadata Extraction

Extract full metadata for the document. Store in the processing manifest at `12 Attachments/Processed/`.

**Required metadata fields:**

```yaml
document_type: [from Stage 2]
authority_level: [from Stage 3]
classification_confidence: [from Stage 2]
title: ""
document_number: ""          # official document number (e.g., ECE/TRANS/WP.29/2026/139)
date: YYYY-MM-DD             # date of submission or publication
meeting: ""                  # associated session (e.g., WP.29 199th Session)
working_group: ""            # e.g., GRVA, ADS IWG, VMAD
status: ""                   # draft | adopted | proposed | superseded
source_url: ""               # URL where downloaded (if known)
inbox_path: ""               # relative path to original file
version: ""                  # amendment series or version number if applicable
```

Store metadata in the manifest — do not duplicate it across multiple vault notes.

---

# Stage 5 — Entity Discovery

Read the document and identify all knowledge entities.

Possible entity types include:

- Regulation
- Proposal
- Working Group
- Meeting
- Organization
- Concept
- Function
- Validation Method
- Requirement
- Scenario
- Test Method
- OEM
- Country

**Create a temporary entity list before modifying the vault.**

---

# Stage 6 — Existing Knowledge Check

For every discovered entity:

Search the vault.

If the entity already exists:

→ Update it.

If the entity does not exist:

→ Create it.

Update first. Create second. Avoid duplicate entities.

---

# Stage 7 — Relationship Discovery

Identify relationships between entities.

Examples:

Working Group → drafts → Proposal

Proposal → modifies → Regulation

Meeting → discusses → Proposal

Regulation → defines → Concept

OEM → implements → Regulation

Organization → hosts → Meeting

Concept → depends_on → Concept

Add missing wiki links.

Update RELATIONSHIPS.md only if a new relationship type is introduced.

---

# Stage 7.2 — Evidence Gate

**This stage is mandatory for every relationship. No relationship may be merged into the knowledge graph without passing this gate.**

Before storing any relationship between two entities, Claude must answer all five questions below. If any question cannot be answered satisfactorily, the relationship must not be merged — it must be routed to the Review Queue.

---

## The Five Evidence Gate Questions

**Question 1 — Is this relationship explicitly stated?**
- YES: the source document directly connects Entity A to Entity B in its own text.
- NO: the connection is implied, inferred, or constructed by comparing two sections.
- If NO: `evidence_strength = inferred` or `unsupported` → do not merge → route to Review Queue.

**Question 2 — Which document supports it?**
- Name the document: title, document number, date.
- If no document can be named: `evidence_strength = unsupported` → route to Review Queue.

**Question 3 — Where in the document is it supported?**
- Cite the section, paragraph, page, or annex.
- A general "it's somewhere in this document" is insufficient for `evidence_strength = explicit`.

**Question 4 — What is the relationship class?**

| Class | Type | May be stored in entity notes? |
|---|---|---|
| 1 — Official | `requires`, `defines`, `modifies`, `supersedes`, `implements`, `adopts`, `mandates`, `references`, `submits_to`, `approved_by` | Yes, with citation |
| 2 — Structural | `belongs_to`, `part_of`, `discussed_at`, `submitted_by`, `developed_by`, `drafts`, `hosts`, `publishes` | Yes, with citation |
| 3 — Conceptual | `shares_concept_with`, `conceptually_related_to`, `uses_similar_concept_as` | Concept notes only, labeled `*Interpretation:*` |
| 4 — Interpretive | `builds_on`, `influenced_by`, `could_impact`, `may_enable` | Research Notes or Review Queue only |

**Question 5 — Should this be stored in an entity note, or routed to Review Queue?**

Route to `11 Review/Pending/` if any of the following apply:
- `evidence_strength = inferred` or `unsupported`
- `confidence = low` or `needs_review`
- The relationship class is 3 or 4 and no `*Interpretation:*` label has been applied
- The relationship connects two regulations in a way that implies legal dependency without a direct citation

---

## Forbidden: Conceptual Similarity → Legal Dependency

The following transformation is explicitly prohibited at this gate:

> **Observation:** "Entity A and Entity B share a concept (e.g., driver monitoring, event recording, fallback behavior)"
> **Forbidden conclusion:** "Entity A is therefore the companion / predecessor / prerequisite of Entity B"

This transformation is the root cause of inference drift in regulatory graphs. It is forbidden regardless of how natural the conclusion seems.

**Examples of blocked transformations:**
- "R157 and R171 both discuss driver monitoring" → blocked from becoming → "R171 derives from R157's driver monitoring requirements"
- "R157 and R171 both involve event recording" → blocked from becoming → "R171 is the data-recording companion of R157"
- "R155 and R157 both address cybersecurity topics" → blocked from becoming → "R155 is a mandatory precondition for R157 type approval"

If the connection seems important, **route it to Review Queue** with the observation stated as a Class 3 (Conceptual) relationship pending evidence.

---

## Evidence Gate Decision Tree

```
Is the relationship explicitly stated in a named source document?
├── YES → evidence_strength = explicit
│         What is the relationship class?
│         ├── Class 1 or 2 → store in entity note with citation
│         └── Class 3 or 4 → label *Interpretation:* or route to Research Notes
│
└── NO → Can it be derived from document structure / institutional process?
         ├── YES → evidence_strength = derived
         │         Class 1 or 2 → store with citation noting derivation
         │         Class 3 or 4 → label *Interpretation:*
         │
         └── NO → evidence_strength = inferred or unsupported
                  → DO NOT store in entity note
                  → Route to 11 Review/Pending/ with:
                    - The two entities
                    - The proposed relationship
                    - Why it seemed plausible
                    - What evidence would be needed to confirm it
```

---

# Stage 7.5 — Knowledge Classification

**This stage is mandatory. No statement may be merged into the graph without passing it.**

Every statement extracted from the document must be classified into exactly one of the following four categories before it is written into any note.

---

## Classification Definitions

### Official Fact

A statement that is **explicitly written** in the source document, traceable to a specific paragraph, section, or page.

Requirements:
- The source document must be named
- The paragraph or section must be cited
- The statement must reflect what the document actually says — not a paraphrase that changes meaning
- Quotation marks are preferred for definitional statements

Label: Write without a special label, but always include an inline citation.
Example: `**Fact (ECE/TRANS/WP.29/2026/139, §2.1):** "The vehicle hardware and software..."`

---

### Structural Relationship

A statement about how two entities are explicitly connected in the regulatory process — confirmed by a source document.

Examples of structural relationships that may be stated as fact:
- "GRVA recommended the ADS UN GTR to WP.29 at its 24th session." *(stated on the cover page of ECE/TRANS/WP.29/2026/139)*
- "WP.29 adopts UN Regulations under the 1958 Agreement." *(structural — stated in the 1958 Agreement itself)*
- "ADS IWG was tasked with developing technical requirements." *(stated in §15 of ECE/TRANS/WP.29/2026/139)*

Requirements:
- The relationship must be stated in a named source document
- The source must be cited

Label: Cite the source. No special label needed if sourced.

---

### Interpretation

A logical conclusion **derived by reasoning** across multiple documents, or by inference from a stated fact.

Interpretations are valid and useful — but they must never be presented as official facts.

Signs that a statement is an interpretation:
- It combines information from two or more documents
- It uses language like "effectively", "in practice", "which means", "this implies"
- No single source explicitly states it
- It describes intent, purpose, or implication — not literal text
- It characterizes a relationship between entities not explicitly described in any source

Label: `*Interpretation:*` at the start of the paragraph.
Example: `*Interpretation:* R155 compliance is effectively a prerequisite for ADS type approval, since the GTR requires cybersecurity processes to be documented (§4.3.2), and separate R155 approval demonstrates this.`

---

### Personal Insight

The user's own analysis, hypothesis, strategic observation, or opinion.

Personal Insights are permitted — but only in Research Notes (`10 Research Notes/`). They must never appear in regulation notes, concept notes, working group notes, or organization notes.

Signs that a statement is a Personal Insight:
- It expresses an opinion or value judgment
- It predicts future events or implications
- It assesses adequacy, sufficiency, or quality
- It makes a recommendation

Label: `*Insight:*` at the start of the paragraph.
Location: Research Notes only.

---

## Classification Checklist

Before merging any statement, confirm:

- [ ] I can name the source document and the section
- [ ] I am not combining two documents to derive this statement
- [ ] I am not inferring intent, purpose, or implication not stated in the text
- [ ] If this is an Interpretation, it is labeled `*Interpretation:*`
- [ ] If this is a Personal Insight, it will go into a Research Note
- [ ] If I am unsure, I will flag it `[VERIFY]` and not merge it as a Fact

---

# Stage 8 — Knowledge Merge

Merge new knowledge into existing notes.

Never overwrite existing knowledge.

Prefer incremental updates.

Preserve previous history whenever possible.

Separate:

## Facts

Official information directly supported by evidence.

## Interpretation

Logical conclusions based on facts.

## Personal Insights

User's own analysis.

Never mix these sections.

---

# Stage 9 — Knowledge Validation

Before finishing, verify the graph.

Check:

- duplicate entities
- duplicate concepts
- broken wiki links
- missing metadata
- isolated notes
- inconsistent naming
- missing sources

If problems exist:

Fix them before finishing.

---

# Stage 10 — Research Generation

Determine whether the document deserves a Research Note.

Create one only if the document introduces:

- new regulatory direction
- important design philosophy
- new concepts
- strategic impact
- unresolved issues

Research Notes should contain:

- Key observations
- Why this matters
- Open questions
- Future work

Do not duplicate factual knowledge already stored elsewhere.

---

# Stage 11 — Changelog

Produce a concise summary.

Include:

Created

Updated

Relationships Added

Concepts Added

Open Questions

Potential Follow-up Documents

Update the processing manifest `status` to `extracted` (or `partial` if only partially processed).

---

# Definition of Done

A document is considered fully ingested only if:

✓ Classification completed (document_type + authority_level assigned)

✓ Processing manifest created in `12 Attachments/Processed/`

✓ Metadata extracted and stored in manifest

✓ Evidence recorded

✓ Entities identified

✓ Existing notes updated

✓ New notes created only when necessary

✓ Every merged statement classified (Stage 7.5)

✓ Relationships established

✓ Wiki links added

✓ Graph validated

✓ Sources preserved

✓ Changelog generated

✓ Manifest status updated to `extracted`

---

# Guiding Principles

Knowledge over documents.

Entities over files.

Relationships over folders.

Update over duplication.

Evidence over memory.

Graph over hierarchy.

Evergreen knowledge over temporary summaries.

The user is never the classifier — Claude is.
