---
type: meta
status: active
tags: [rules, methodology, knowledge-management, constitution]
related: [CLAUDE, Home]
source: "LLM Wiki method, Andrej Karpathy"
last_updated: 2026-06-27
---

# Knowledge Rules

The permanent constitution of this UNECE automated driving regulation knowledge base.

---

## Rule Zero — Never Elevate Inference to Fact

**This is the highest-priority rule in the vault. It overrides all other conventions.**

An **official fact** requires explicit evidence from an official UNECE document. The evidence must be traceable to a specific paragraph, section, or page of a named source.

An **inferred relationship** — one derived by reasoning across multiple documents, or by logical extension from a premise — is an **Interpretation**, never a Fact. It must be labeled `*Interpretation:*` and must not appear in authoritative regulation or concept notes without that label.

A **personal analysis, hypothesis, or strategic observation** is a **Personal Insight**. It belongs only in Research Notes (`10 Research Notes/`) and must never appear in regulation notes, concept notes, or working group notes.

### The Inference Drift Test

Before writing any statement into the vault, ask:

1. **Is this explicitly stated in a specific, named source document?**
   - If YES → it is an Official Fact. Cite the source inline.
   - If NO → it is not a Fact. Continue below.

2. **Is this a logical conclusion drawn from combining two or more documents?**
   - If YES → it is an Interpretation. Label it `*Interpretation:*`.
   - If NO → continue.

3. **Is this my own analysis or hypothesis?**
   - If YES → it is a Personal Insight. Write it in a Research Note only.

4. **Am I unsure which category applies?**
   - Default to `[VERIFY]` and do not merge until the source is confirmed.

**Prefer acknowledged uncertainty over false certainty.**

### Examples of Inference Drift to Avoid

| Statement | Problem | Correct Form |
|---|---|---|
| "R155 and R156 are companion regulations to R157." | No official document uses this phrase. | *Interpretation:* R155 and R156 compliance is required before R157 type approval, per GTR §4.3. |
| "R171 is the data recording companion of R157." | No explicit statement found. | *Interpretation:* Both R171 and R157 include data recording requirements; their relationship requires [VERIFY]. |
| "VMAD's methodology is adequate for AI-based ADS." | Personal analysis, not stated anywhere. | Research Note only, labeled *Insight:*. |

---

## Core Philosophy

### Knowledge Over Documents
This vault exists to capture **knowledge** — not to store documents. Raw UNECE documents, PDFs, and Word files belong in `raw/` or `12 Attachments/`. What belongs here is synthesis: distilled facts, interpreted meaning, and connected understanding.

### Atomic Notes
Every note represents **one concept, one entity, or one event**. A note about R157 covers R157. A note about ODD covers ODD. If a note is growing too broad, it should be split. The atomic structure is what makes the graph useful — fine-grained nodes connect more richly than coarse ones.

### Wiki Links Over Folder Hierarchy
The folder structure is a shallow scaffold, not the primary navigation system. **The graph is the primary navigation method.** Relationships between notes — expressed through `[[wiki links]]` — carry more meaning than folder location. A note in `05 Concepts/` is not isolated; it should be reachable from regulations, working groups, meetings, and OEM notes.

### The Graph Is the Knowledge
When you open the Obsidian graph view, you should be able to see the regulatory landscape: how GRVA connects to working groups, how working groups produce regulations, how regulations rely on concepts, how OEMs implement or engage with those regulations. If the graph looks sparse, knowledge is missing or disconnected.

### AI Should Understand Relationships
This vault is designed for both human and AI navigation. Claude and future AI tools should be able to traverse the graph and understand not just individual notes, but the **web of dependencies** between regulations, concepts, bodies, and stakeholders. Every wiki link is a machine-readable relationship.

---

## Writing Principles

### Never Copy Entire UNECE Documents
Do not paste verbatim paragraphs from official documents. Summarize, extract, and synthesize. The one exception is short definitional quotes — a single sentence from a regulation that defines a term precisely. These must always be attributed.

### Summarize and Extract Knowledge
Ask: *what does this document tell me that I didn't know before?* Write that. A note on a GRVA session should capture the key decisions and open questions, not reproduce the agenda.

### Distinguish Facts, Interpretations, and Personal Insights
Every substantive claim should be marked by epistemic status:

| Type | Label | Meaning |
|---|---|---|
| **Fact** | *(unmarked, or cited)* | Directly stated in a source document. Always include a citation. |
| **Interpretation** | *Interpretation:* | Your reading of what a provision or outcome means. Reasonable people may disagree. |
| **Insight** | *Insight:* | Your own analysis, hypothesis, or strategic observation. Clearly personal. |

Never present an interpretation or insight as a fact. This is especially important in regulatory analysis where ambiguity is common.

### Always Reference Original Sources
Every factual claim needs a traceable source:
- Use the `source` field in YAML frontmatter for the primary source
- Inline citations: `**Source:** GRVA-24-0012e` or `**Source:** R157, Annex 4, para. 5.3`
- For documents in the vault: link to the attachment note or `raw/` file

### Keep Notes Concise and Evergreen
Write notes as if they will be read two years from now. Avoid time-relative language ("recently", "last session", "upcoming"). Use specific dates. Avoid narrative that ties the note to the moment it was written. A note about ODD should explain ODD, not tell the story of when you learned about ODD.

---

## Linking Principles

### Minimum Three Wiki Links Per Note
Every substantive note should link to at least three related notes. This is the floor, not the ceiling. A well-developed note on a regulation should link to five or more related notes across different categories.

### For Regulation Notes, Always Link To:
- The **working group** responsible for it (e.g., `[[GRVA]]`, `[[DCAS]]`)
- At least two **technical concepts** it defines or relies on (e.g., `[[ODD]]`, `[[DDT]]`, `[[MRM]]`)
- At least one **related regulation** (e.g., `[[R155]]` links to `[[R156]]`)
- Any **meeting sessions** where key decisions were made
- Any **OEM** known to have sought type approval or submitted proposals under it

### For Concept Notes, Always Link To:
- The regulation(s) that define or use the concept
- Related concepts (upstream, downstream, or parallel)
- The working group(s) where the concept is debated

### For Meeting Notes, Always Link To:
- The body hosting the meeting (e.g., `[[GRVA]]`, `[[WP29]]`)
- Regulations on the agenda
- Proposals discussed
- Working group reports presented

### Backlinks Matter
When you create a new note, go back to at least one existing related note and add a link to the new note. Orphan notes — notes with no incoming links — are invisible in the graph and defeat the purpose of the vault.

---

## Metadata Principles

### Every Note Must Have YAML Frontmatter
No exceptions. A note without frontmatter is not part of the knowledge system — it is just a file.

### Standard Fields

```yaml
---
type:           # See Knowledge Types below
status:         # placeholder | draft | active | archived
working_group:  # e.g., GRVA, ADS IWG, VMAD (if applicable)
keywords:       []
related:        []
source:         ""
last_updated:   YYYY-MM-DD
---
```

### Field Definitions

| Field | Required | Values |
|---|---|---|
| `type` | Yes | `regulation`, `working_group`, `meeting`, `proposal`, `concept`, `oem`, `organization`, `research_note`, `personal_insight` |
| `status` | Yes | `placeholder` → `draft` → `active` → `archived` |
| `working_group` | If applicable | Name of the responsible UNECE body |
| `keywords` | Yes | Flat list of searchable terms |
| `related` | Yes | List of related note names (mirrors wiki links in body) |
| `source` | Yes | Primary source document or URL |
| `last_updated` | Yes | ISO date `YYYY-MM-DD` |

### Status Lifecycle
- `placeholder` — structure only, no real content yet
- `draft` — content started, not yet reliable
- `active` — content is current and trustworthy
- `archived` — superseded or no longer relevant

---

## Knowledge Types

### Regulation
A UN Regulation (Rx) or UN Global Technical Regulation (GTR) adopted or under development under the WP.29 framework. Covers scope, key requirements, regulatory history, and links to concepts and working groups. Examples: `[[R157]]`, `[[R171]]`, `[[ADS UN GTR]]`.

### Working Group
An informal working group (IWG), task force (TF), or subsidiary body operating under GRVA or WP.29. Covers mandate, work items, deliverables, and key contributors. Examples: `[[ADS IWG]]`, `[[VMAD]]`, `[[DCAS]]`.

### Meeting
A session of a UNECE body (WP.29, GRVA) or working group. Covers agenda, key decisions, documents discussed, and outcomes. Should link to proposals discussed and regulations affected. Examples: `[[GRVA 24th Session]]`, `[[WP29 199th Session]]`.

### Proposal
A submitted document — an informal document (INF), working document (WP), or formal proposal — submitted to a UNECE session. Covers the submitter, objective, proposed text, and outcome. Examples: `GRVA-24-0012`, `ECE/TRANS/WP.29/2024/XX`.

### Technical Concept
A regulatory, technical, or safety concept used across multiple regulations or working groups. Should include a formal definition (sourced), regulatory usage, and related concepts. Examples: `[[ODD]]`, `[[DDT]]`, `[[MRM]]`, `[[SOTIF]]`.

### OEM
An automotive manufacturer or technology developer with a stake in UNECE automated driving regulation. Covers relevant products, type approvals held, regulatory positions, and key submissions. Examples: `[[BMW]]`, `[[Wayve]]`, `[[Mobileye]]`.

### Research Note
A working note for active research — questions being explored, findings being synthesized, open hypotheses. Not intended to be a permanent authoritative note. May be promoted to a Concept, Regulation, or other type when mature. Lives in `10 Research Notes/`.

### Personal Insight
A clearly marked note capturing your own analytical conclusion, strategic observation, or hypothesis. Must be labeled as personal insight throughout. Not suitable as a citation source. May link to Regulation and Concept notes as supporting context.

---

## AI Collaboration

When Claude or any AI tool works in this vault, the following rules apply:

### Maintain Consistency
- Use the same note structure, YAML fields, and formatting as existing notes
- Match the tone: concise, precise, regulatory in register
- Do not introduce new metadata fields without updating this document

### Never Duplicate Existing Notes
Before creating any note, search for an existing note on the same topic. If one exists, extend it. Two notes on the same concept break the graph — links will split between them and context will fragment.

### Prefer Extending to Creating
An existing note with three new sentences is more valuable than a new note with three sentences. Add to existing notes wherever possible. Create new notes only when the topic is genuinely new and atomic.

### Suggest New Links Whenever Appropriate
When reading or editing any note, identify wiki link opportunities and add them. A passage that mentions "Minimal Risk Maneuver" without linking to `[[MRM]]` is a missed connection.

### Keep the Graph Highly Connected
Target: no note with fewer than three outgoing links. Identify orphaned or weakly-connected notes and propose links. The graph should be navigable from any node to any other node within a few hops.

### Separate Epistemic Layers
Never mix facts, interpretations, and insights without clear labeling. If uncertain whether a claim is sourced, label it `[VERIFY]` rather than presenting it as fact.

### Ask Before Destructive Actions
- Never delete a note without explicit user instruction
- Never rename a file without confirming with the user
- Never overwrite a non-empty note without reading it first
- Always summarize what was changed after each operation

---

## What Does NOT Belong Here

- Raw PDFs, DOCX files, or unprocessed document dumps → use `raw/` or `12 Attachments/`
- Verbatim multi-paragraph excerpts from UNECE documents
- Duplicate notes for a concept already covered
- Notes with no wiki links
- Notes without YAML frontmatter
- Time-sensitive content written as if it will always be current (use specific dates)
