---
type: meta
status: active
tags: [relationships, reasoning-guide, knowledge-graph, claude-instructions]
related: [SCHEMA, ONTOLOGY, KNOWLEDGE_RULES, CLAUDE]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# RELATIONSHIPS — Claude Reasoning Guide

**This file is not documentation. It is an operational reasoning guide for Claude.**

Load this file before performing any knowledge graph update. Reason through every operation using the Entity → Relationship → Entity model defined here.

---

## 0. Evidential Constraint — Relationships Must Be Supported

**This file records graph structure, not inferences.**

Every relationship entered into this file or expressed as a wiki link in a note must be supported by evidence from a named source document. Relationships derived by reasoning — plausible but not explicitly stated anywhere — are **Interpretations** and must not be stored as graph structure facts.

### Three Tiers of Relationship Evidence

| Tier | Description | How to Store |
|---|---|---|
| **Explicit** | The source document directly states the relationship | Store as normal relationship. Cite source. |
| **Structural** | The relationship is definitionally true from the process itself (e.g., GRVA always reports to WP.29 — stated in the GRVA mandate) | Store as normal relationship. Cite mandate or procedure document. |
| **Inferred** | The relationship is logically plausible but not stated in any source | Do NOT store as a graph relationship. Record in a Research Note as `*Interpretation:*` with reasoning. |

### Inference Drift in Relationships

Common inference drift patterns to avoid:

- **Unstated prerequisites:** "R155 is a prerequisite for R157" — this may be true in practice, but unless a source document states it explicitly, it should be labeled *Interpretation:* in notes, not stored as a `requires` relationship in the graph.
- **Implied companions:** "R155 and R156 are companion regulations" — this framing does not appear in official documents; it is interpretive shorthand.
- **Assumed implementations:** "BMW implements R157" — only store this if BMW has actually sought or received type approval under R157 (confirmed by a source), not because their product appears to qualify.
- **Regulatory intent:** "R171 was designed to fill the gap between ADAS and ADS" — this describes intent or purpose, which is an interpretation unless a WP.29 document explicitly states it.

When uncertain whether a relationship is evidenced: **omit it from the graph and note it as `[VERIFY]` in the relevant note.**

---

## 0.5 Evidence-backed Relationships — Required Fields

Every meaningful relationship in the knowledge graph must be backed by evidence. The standard triple

```
Entity A  →  Relationship  →  Entity B
```

is extended with a mandatory evidence record:

```
Entity A  →  Relationship  →  Entity B  →  Evidence
```

### Evidence Record Fields

| Field | Description | Example |
|---|---|---|
| `source_document` | Name or title of the source | "ADS UN GTR" |
| `document_number` | Official document number | `ECE/TRANS/WP.29/2026/139` |
| `evidence_location` | Section, paragraph, page, or annex | `§4.3.2`, `cover page`, `Annex 6` |
| `evidence_quote` | Short verbatim quote or paraphrase | `"The ADS shall be protected from cyber threats."` |
| `evidence_strength` | See below | `explicit` |
| `confidence` | See below | `high` |

### Evidence Strength Values

| Value | Meaning | May be stored as graph relationship? |
|---|---|---|
| `explicit` | The document directly states this relationship in its own text | Yes — cite source |
| `derived` | The relationship follows clearly from document structure or process | Yes — cite document; note it is derived |
| `inferred` | The relationship is a logical conclusion not directly stated | No — route to `*Interpretation:*` label or Review Queue |
| `unsupported` | No source found; relationship exists only by analogy or assumption | No — do not store; route to Review Queue |

### Confidence Values

| Value | Meaning | Action |
|---|---|---|
| `high` | Source is unambiguous; quote is direct | Store relationship |
| `medium` | Source is probably correct; paraphrase is reasonable | Store with `[VERIFY]` flag; seek confirmation |
| `low` | Source is uncertain or indirect | Do not store — route to Review Queue |
| `needs_review` | Evidence is conflicting, missing, or ambiguous | Route to `11 Review/Pending/` |

### Inline Evidence Format

When recording an evidence-backed relationship inside a note:

```markdown
**Fact (ECE/TRANS/WP.29/2026/139, §4.3.2, explicit, high):**
"The manufacturer shall document and implement processes for managing 
cyber security across the development, production, and post-deployment phases."
→ Relationship: ADS UN GTR `requires` Cybersecurity
```

When a relationship cannot reach `explicit` or `derived` strength, it must be labeled `*Interpretation:*` and either kept only in Research Notes or sent to `11 Review/Pending/`.

---

## 0.6 Relationship Classes

Relationships fall into four classes. The class determines where the relationship may be stored and what evidence is required.

### Class 1 — Official Relationships
**Require `explicit` or `derived` evidence strength.**
These describe legal, regulatory, or procedural connections stated in official documents.
May be stored as graph relationships in entity notes.

| Relationship | Direction | Evidence required |
|---|---|---|
| `references` | Any → Any | Document explicitly cites target |
| `modifies` | Proposal → Regulation | Document states amendment scope |
| `supersedes` | Regulation → Regulation | Document states replacement |
| `adopts` | Meeting → Regulation | Session report or cover page |
| `requires` | Regulation → Concept | Regulation text mandates it |
| `mandates` | Regulation → Requirement | Regulation text uses "shall" for target |
| `submits_to` | Organization → Meeting | Official submission record |
| `approved_by` | Regulation → Organization | Adoption document |
| `defines` | Regulation → Concept | Formal definition present in text |
| `implements` | OEM → Regulation | Type approval confirmed by source |

---

### Class 2 — Structural Relationships
**Based on document structure or institutional process.**
These are definitionally true from how UNECE bodies operate.
May be stored as graph relationships. Cite the document establishing the structure.

| Relationship | Direction | Basis |
|---|---|---|
| `discussed_at` | Proposal → Meeting | Listed in session agenda or report |
| `submitted_by` | Proposal → Organization | Cover page or session document |
| `developed_by` | Regulation → Working Group | Mandate document |
| `belongs_to` | WG → Organization | Terms of Reference or mandate |
| `part_of` | IWG → Working Group | Established within parent body |
| `hosts` | Organization → Meeting | Session document |
| `publishes` | Organization → Regulation | Adoption record |
| `drafts` | WG → Proposal | Session document |
| `develops` | WG → Regulation | Mandate or work programme |

---

### Class 3 — Conceptual Relationships
**Must never be treated as legal dependency.**
These describe thematic or technical similarity between entities.
May only appear in concept notes with explicit `*Interpretation:*` labeling.
**Must never be elevated to Class 1 or Class 2 without explicit evidence.**

| Relationship | Direction | Meaning |
|---|---|---|
| `shares_concept_with` | Regulation → Regulation | Both address a common technical concept |
| `conceptually_related_to` | Concept → Concept | Topics overlap without formal dependency |
| `uses_similar_concept_as` | Regulation → Regulation | Similar terminology or approach |

**Forbidden transformation:** Conceptual similarity must never become legal dependency.

> ❌ "R157 and R171 both involve event recording" → "R171 is the data-recording companion of R157."
> ❌ "R157 and R171 both discuss driver monitoring" → "R171 derives from R157."
> ❌ "R155 and R156 address related topics" → "R155 is a prerequisite for R157."

These transformations are prohibited even when the conclusion seems logical. **Conceptual co-occurrence ≠ legal dependency.**

---

### Class 4 — Interpretive Relationships
**Must be placed in Research Notes or Review Queue.**
These represent inferred, potential, or analytical relationships that have not been confirmed by official evidence.
**Must never appear in entity notes (regulation notes, concept notes, working group notes, organization notes).**

| Relationship | Direction | Meaning |
|---|---|---|
| `builds_on` | Regulation → Regulation | Later instrument draws on earlier approach |
| `influenced_by` | Concept → Concept | Analytical lineage |
| `could_impact` | Regulation → OEM | Speculative regulatory impact |
| `may_enable` | Concept → Concept | Potential enabling relationship |

**Storage rule:** Class 4 relationships belong only in:
- `10 Research Notes/` (labeled `*Interpretation:*` or `*Insight:*`)
- `11 Review/Pending/` (awaiting evidence to upgrade to Class 1–2)

---

## 1. Purpose

Every Markdown file in this vault is a **knowledge entity**. Knowledge is not stored in paragraphs — it is stored in entities and the relationships between them. A note about R157 is only as valuable as the links connecting it to working groups, concepts, meetings, and OEMs.

**Claude must reason in triples, not files:**

```
Entity  →  Relationship  →  Entity
R157    →  defines       →  MRM         [Fact: ECE/TRANS/WP.29/2026/139 §82 cites R157]
GRVA    →  hosts         →  GRVA 24th Session  [Structural: GRVA is the body]
BMW     →  implements    →  R157        [Only if type approval confirmed by source]
```

Before touching any file, identify: *what entities are involved, what relationships connect them, which relationships are explicitly evidenced, and which are inferences.* Only then act.

---

## 2. Relationship Types

| Relationship | Direction | Meaning |
|---|---|---|
| `drafts` | WG → Proposal | The working group authored this proposal |
| `modifies` | Proposal → Regulation | The proposal changes text or requirements of the regulation |
| `discusses` | Meeting → Proposal | The meeting considered this proposal on its agenda |
| `adopts` | Meeting → Regulation | The meeting voted to adopt or advance this regulation |
| `defines` | Regulation → Concept | The regulation contains a formal definition of this concept |
| `requires` | Regulation → Concept | The regulation mandates this concept be implemented or demonstrated |
| `references` | Any → Any | One entity cites or links to another without a stronger semantic |
| `supersedes` | Regulation → Regulation | A newer version or amendment replaces prior text |
| `belongs_to` | WG → Organization | The working group operates under this body |
| `extends` | Concept → Concept | One concept is a specialization or elaboration of another |
| `depends_on` | Concept → Concept | One concept presupposes another to function |
| `implements` | OEM → Regulation | The OEM has sought or holds type approval under this regulation |
| `develops` | WG → Regulation | The working group is the primary body developing this regulation |
| `satisfies` | OEM → Requirement | An OEM system or submission addresses a specific regulatory requirement |
| `hosts` | Organization → Meeting | The organization is the secretariat or venue for the meeting |
| `publishes` | Organization → Regulation | The organization formally issues or administers the regulation |
| `analyzes` | Research Note → Any | The research note investigates this entity in depth |
| `summarizes` | Research Note → Meeting | The research note captures the substance of a session |
| `references_research` | Personal Insight → Research Note | The personal insight builds on prior research |
| `questions` | Personal Insight → Regulation | The personal insight challenges or interrogates a regulatory provision |
| `supports` | Any → Any | Evidence or reasoning that reinforces a claim or position |
| `contradicts` | Any → Any | Evidence or reasoning that conflicts with a claim or position |
| `impacts` | Regulation → OEM | The regulation materially affects this OEM's products or strategy |
| `related_to` | Any → Any | General topical connection when no stronger relationship applies — use sparingly |

---

## 3. Entity Relationship Matrix

The canonical connections Claude must maintain. When any of these relationships exist in source material, they must be reflected in the graph.

| From | Relationship | To |
|---|---|---|
| Working Group | `drafts` | Proposal |
| Working Group | `develops` | Regulation |
| Working Group | `belongs_to` | Organization |
| Proposal | `modifies` | Regulation |
| Proposal | `drafted_by` | Working Group |
| Proposal | `discussed_at` | Meeting |
| Meeting | `discusses` | Proposal |
| Meeting | `adopts` | Regulation |
| Meeting | `hosted_by` | Organization |
| Regulation | `defines` | Concept |
| Regulation | `requires` | Concept |
| Regulation | `supersedes` | Regulation |
| Regulation | `complements` | Regulation |
| Concept | `extends` | Concept |
| Concept | `depends_on` | Concept |
| Concept | `defined_in` | Regulation |
| OEM | `implements` | Regulation |
| OEM | `develops` | Concept *(system / function)* |
| OEM | `belongs_to` | Organization |
| OEM | `submits` | Proposal |
| Organization | `hosts` | Meeting |
| Organization | `publishes` | Regulation |
| Organization | `supervises` | Working Group |
| Research Note | `analyzes` | Regulation |
| Research Note | `analyzes` | Concept |
| Research Note | `summarizes` | Meeting |
| Personal Insight | `references_research` | Research Note |
| Personal Insight | `questions` | Regulation |
| Personal Insight | `supports` | Regulation |
| Personal Insight | `contradicts` | Regulation |

---

## 4. Claude Update Rules

Follow this sequence exactly whenever processing a new UNECE document.

**Step 1 — Identify all entities.**
Read the document. List every entity it touches: regulations mentioned, concepts defined or used, working groups involved, organizations submitting, meetings referenced, OEMs named.

**Step 2 — Determine which relationships are affected.**
For each entity pair in Step 1, identify the relationship type from §2. Write the triples mentally before opening any file:
```
GRVA 25th Session  →  discusses  →  GRVA-25-0043
GRVA-25-0043       →  modifies   →  R171
R171               →  requires   →  Driver Monitoring
```

**Step 3 — Update existing entities first.**
Open each affected note. Add new facts, update status fields, add missing wiki links. This is the default action. Do not create new notes until Step 4.

**Step 4 — Create missing entities only when necessary.**
If the document introduces an entity with no existing note — a new working group, a new concept, a new OEM — create a note using the appropriate template from `11 Templates/`. Do not create notes for entities already covered under a different name; find the existing note and add an alias.

**Step 5 — Create missing wiki links.**
After updating all notes, scan for unlinked references. Every entity named in a note's body should be a `[[wiki link]]` unless it appears only as metadata context.

**Step 6 — Check graph consistency.**
Verify: no orphan nodes, no broken link text, no duplicate entities, YAML `related` fields mirror the wiki links in the note body, `last_updated` reflects today's date on every touched note.

**Never create duplicate entities. Never create isolated notes.**

---

## 5. Entity Update Priority

When new knowledge arrives, update entities in this order:

```
1. Proposal          ← the atomic unit of change in the UNECE process
2. Regulation        ← primary long-term knowledge asset
3. Concept           ← shared vocabulary; ripples across everything
4. Working Group     ← tracks mandate and deliverable evolution
5. Meeting           ← contextualizes when things happened
6. Organization      ← stable; changes rarely
7. OEM               ← implementation and engagement tracker
8. Research Notes    ← volatile; consolidate into permanent notes ASAP
9. Personal Insights ← subjective; update last, after facts are stable
```

**Why this order minimizes duplicated knowledge:**

Proposals are the document-level unit of change. Updating them first establishes the factual record before any downstream note is touched. Regulations are updated next because they are the primary authoritative entities — every concept, meeting, and OEM note derives its relevance from regulations. Concepts come before working groups because a concept update may cascade across multiple working groups and regulations simultaneously. Working groups and meetings are contextual rather than definitional, so they change after the substantive content is settled. Organizations change rarely. OEM notes depend on knowing what the regulation now says before recording what the OEM implements. Research Notes and Personal Insights are always secondary to the factual record and should be updated last, or consolidated into primary entity notes.

---

## 6. Relationship Rules

### Every Regulation Must Connect To:
- At least one **Working Group** (`belongs_to` or `develops`)
- Any **Meetings** where it was materially advanced
- Any **Proposals** that modified it
- At minimum two **Concepts** it defines or requires
- Any **OEMs** that implement or have sought type approval under it
- The primary **source document** in the `source` YAML field

### Every Proposal Must Connect To:
- The **Working Group** that drafted it
- The **Meeting** where it was discussed
- The **Regulation** it modifies (if applicable)

### Every Meeting Must Connect To:
- The **Working Group** or body that held it
- All **Proposals** considered on its agenda
- All **Regulations** formally advanced or adopted
- The previous and next session (continuity chain)

### Every Concept Must Connect To:
- The **Regulation(s)** that define or heavily rely on it
- **Related concepts** (upstream depended-on concepts, downstream extending concepts)
- Any **Working Group** where it is primarily debated
- Any **OEM** implementation where the concept is instantiated in a real system

### Every OEM Must Connect To:
- **Regulations** for which it holds or has sought type approval
- **Organizations** (industry associations) it belongs to
- **Proposals** it has submitted to GRVA or WP.29
- Key **Concepts** relevant to its technical approach

**Avoid orphan nodes.** A note with no incoming links is invisible to the graph and useless for reasoning. Whenever creating a new note, add at least one link *to it* from an existing note.

**Prefer updating over creating.** If the concept already exists under a different name or abbreviation, add an alias — do not create a duplicate.

---

## 7. Knowledge Evolution

A new PDF arrives. The wrong response is to create a standalone summary note. The correct response is:

1. **Identify entities.** What regulations, concepts, working groups, organizations, OEMs does this document concern?
2. **Identify relationships.** What does this document assert about how those entities connect?
3. **Update existing nodes.** Add new facts to existing notes. Append — do not overwrite. Update `last_updated`.
4. **Create missing nodes.** Only for genuinely new entities not yet in the vault.
5. **Add missing links.** Ensure every named entity in every touched note has a `[[wiki link]]`.
6. **Preserve history.** If a regulation was amended, add the change to a **Regulatory History** section. Do not silently rewrite prior content.

A growing vault does not mean more notes. It means more **connected** notes. The goal is density of relationships, not volume of files.

---

## 8. Reasoning Examples

### Example 1 — New GRVA Proposal Modifying R171

*Scenario: A new proposal (GRVA-25-0043) submitted by Germany proposes to amend R171 to tighten driver monitoring requirements.*

**Entity triples to establish:**
```
Germany (org)        →  submits       →  GRVA-25-0043 (proposal)
GRVA-25-0043         →  modifies      →  R171
GRVA 25th Session    →  discusses     →  GRVA-25-0043
R171                 →  requires      →  Driver Monitoring
Driver Monitoring    →  depends_on    →  Driver Availability
```

**Update sequence:**
1. Create or update `09 Proposals/GRVA-25-0043.md` with full YAML, link to R171, Germany, GRVA 25th Session
2. Update `01 Regulations/R171.md` — add proposal reference, update Regulatory History section
3. Update `05 Concepts/Driver Monitoring.md` — add any new definitional content from the proposal
4. Update `05 Concepts/Driver Availability.md` — check if the proposal affects this concept
5. Update `03 GRVA/GRVA 25th Session.md` — add proposal to agenda/documents section
6. Scan OEM notes (BMW, Mercedes-Benz, NIO, etc.) — flag if the amendment affects implementation notes

---

### Example 2 — BMW Announces a New DCAS Implementation

*Scenario: BMW announces a Level 2+ system that implements DCAS functions and seeks type approval under R171.*

**Entity triples to establish:**
```
BMW          →  implements    →  R171
BMW          →  develops      →  DCAS (concept / function)
BMW          →  impacts       →  Driver Monitoring
BMW          →  belongs_to    →  OICA
```

**Update sequence:**
1. Update `06 OEM/BMW.md` — add system description, link to R171, add to type approvals section
2. Update `01 Regulations/R171.md` — add BMW to OEM implementations section
3. Update `05 Concepts/DCAS.md` — note BMW as an OEM implementation reference
4. Update `04 Working Groups/DCAS.md` — if BMW is known to participate, reflect that
5. Check `05 Concepts/Driver Monitoring.md` and `Driver Availability.md` — link to BMW implementation if relevant

---

### Example 3 — ADS IWG Working Document Introduces a New Definition

*Scenario: ADS IWG publishes a working document that formally defines "Remote Assistance" for the first time in the GTR context.*

**Entity triples to establish:**
```
ADS IWG          →  drafts        →  Working Document
Working Document →  modifies      →  ADS UN GTR
ADS UN GTR       →  defines       →  Remote Assistance
Remote Assistance →  depends_on   →  ODD
Remote Assistance →  depends_on   →  Cybersecurity
```

**Update sequence:**
1. Create `09 Proposals/[document-number].md` for the working document
2. Update `01 Regulations/ADS UN GTR.md` — add Remote Assistance to definitions section, link to document
3. Update `05 Concepts/Remote Assistance.md` — add formal definition with source citation, update status from `placeholder` to `draft`
4. Update `04 Working Groups/ADS IWG.md` — note the definition as a work item milestone
5. Update `05 Concepts/ODD.md` and `Cybersecurity.md` — add `[[Remote Assistance]]` as a forward link
6. Scan `06 OEM/` notes — any OEM developing remote assistance capabilities should link to this concept

---

### Example 4 — Reading ECE/TRANS/WP.29/2026/139 (ADS UN GTR)

*Scenario: The full ADS UN GTR proposal is ingested from local file. Source: `12 Attachments/UNECE/ECE-TRANS-WP.29-2026-139e.pdf`*

**Key triples established:**
```
GRVA 24th Session     →  recommends       →  ADS UN GTR
WP29 199th Session    →  considers        →  ADS UN GTR (AC.3 vote)
ADS IWG               →  drafts           →  ADS UN GTR
ADS UN GTR            →  defines          →  MRC
ADS UN GTR            →  defines          →  ADS Fallback Response
ADS UN GTR            →  defines          →  ADSF-1 and ADSF-2
ADS UN GTR            →  defines          →  Safety Case
ADS UN GTR            →  defines          →  Safety Management System
ADS UN GTR            →  defines          →  Behavioural Competency
ADS UN GTR            →  defines          →  OEDR
ADS UN GTR            →  defines          →  ISMR
ADS UN GTR            →  requires         →  DSSAD (Annex 6)
ADS UN GTR            →  references       →  R157 (ALKS)
ADS UN GTR            →  references       →  R155 (cybersecurity — not directly ref'd)
ADS UN GTR            →  complements      →  New UN Regulation on ADS
FRAV/VMAD Integrated  →  provides_basis   →  ADS UN GTR
AVC                   →  reports_to       →  ADS IWG
FADS                  →  reports_to       →  ADS IWG
OICA                  →  supports         →  ADS IWG (secretariat)
Canada/China/EC/Japan/UK/US  →  sponsors  →  ADS IWG
```

**New entities created:**
- `05 Concepts/MRC.md`
- `05 Concepts/Safety Case.md`
- `05 Concepts/Safety Management System.md`
- `05 Concepts/Behavioural Competency.md`
- `05 Concepts/OEDR.md`
- `05 Concepts/ISMR.md`
- `05 Concepts/ADS Fallback Response.md`
- `05 Concepts/ADSF-1 and ADSF-2.md`
- `04 Working Groups/AVC.md`
- `04 Working Groups/FADS.md`
- `10 Research Notes/2026-06 ADS GTR Reading.md`

**Existing entities substantially updated:**
- `01 Regulations/ADS UN GTR.md` — full sourced content from document
- `03 GRVA/GRVA 24th Session.md` — confirmed recommendation fact
- `02 WP29/WP29 199th Session.md` — confirmed submission, date, agenda item
- `04 Working Groups/ADS IWG.md` — confirmed leadership, structure, two-track mandate
- `04 Working Groups/VMAD.md` — confirmed NATM deliverables, multi-pillar approach
- `04 Working Groups/FRAV.md` — confirmed FRAV/VMAD Integrated Document
- `04 Working Groups/DSSAD.md` — confirmed Annex 6 data requirements
- `05 Concepts/Automated Driving System.md` — official §2.1 definition, ADSF types
- `05 Concepts/DDT.md` — official §2.3 definition with subcategories
- `05 Concepts/ODD.md` — official §2.12 definition, ODD exit
- `05 Concepts/MRM.md` — clarified MRM vs MRC terminology
- `05 Concepts/Validation.md` — four-pillar approach, NATM basis
- `05 Concepts/DSSAD.md` — official §2.11 definition, Annex 6 data elements
