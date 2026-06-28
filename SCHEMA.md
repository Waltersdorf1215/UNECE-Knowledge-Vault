---
type: meta
status: active
tags: [schema, ontology, data-model, knowledge-graph]
related: [KNOWLEDGE_RULES, CLAUDE, ONTOLOGY, Home]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# SCHEMA — UNECE Automated Driving Knowledge OS

Official ontology and data model of this knowledge base.

---

## 1. Knowledge Philosophy

This vault is not a document repository. It is a **knowledge graph** — a network of entities and the relationships between them.

### Entities, Not Documents
Every Markdown note is a **knowledge entity**: a discrete, identifiable thing in the UNECE automated driving regulatory world. A regulation is an entity. A working group is an entity. A concept like ODD is an entity. A meeting session is an entity. Each entity has properties (YAML frontmatter) and relationships (wiki links to other entities).

Documents — PDFs, Word files, official UNECE papers — are **source material**, not knowledge. They live in `raw/` or `12 Attachments/`. Knowledge is what you extract from them.

### The Graph Is the Primary Representation
The folder structure provides a shallow filing scaffold. The **graph** — the network of `[[wiki links]]` connecting entities — is the actual representation of knowledge. When you understand the relationships in this domain (which working groups produce which regulations, which concepts underpin which requirements, which OEMs engage with which bodies), those relationships should be visible and navigable in the graph.

### Knowledge Should Be Evergreen
Notes should be written to remain accurate and useful over time. Avoid time-relative language. Write with specific dates. A note on R157 should describe R157 as it currently stands, updated in place as the regulation evolves — not layered with dated commentary.

### Knowledge Evolves, It Does Not Duplicate
When the regulatory landscape changes, existing notes are updated. New notes are created only for genuinely new entities. Duplication — two notes covering the same concept — breaks the graph and creates inconsistency. The rule is: **find and update, not find and create**.

---

## 2. Entity Types

### 2.1 Regulation

**Purpose:** Represents a UN Regulation (e.g., R157) or UN Global Technical Regulation (GTR) adopted or under development through the WP.29 framework.

**Create when:** A regulation is formally adopted, or is sufficiently developed to have a document number and substantive scope.

**Do not create when:** A proposed amendment is minor enough to be captured as a section update to the existing regulation note. Do not create separate notes for supplements unless the supplement is substantive enough to warrant its own analysis.

**Required properties:**
```yaml
type: regulation
status: placeholder | draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
regulation_number: "157"
regulation_series: "UN Regulation"   # or "UN GTR"
entry_into_force: YYYY-MM-DD
responsible_body: "GRVA"
keywords: []
aliases: ["ALKS", "Automated Lane Keeping Systems"]
```

---

### 2.2 Working Group

**Purpose:** Represents an informal working group (IWG), task force (TF), or formal subsidiary body operating under GRVA or WP.29. Working groups are the primary mechanism through which regulations and technical documents are developed.

**Create when:** A group has a formal mandate, a name, and produces documents submitted to GRVA or WP.29.

**Do not create when:** A single delegation or small ad hoc group meets informally without a formal mandate or document output.

**Required properties:**
```yaml
type: working_group
status: placeholder | draft | active | dissolved
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
parent_body: "GRVA"
mandate: ""
co_chairs: []
primary_deliverable: ""
keywords: []
```

---

### 2.3 Meeting

**Purpose:** Represents a session of a UNECE body (WP.29, GRVA) or informal working group. Captures decisions, documents discussed, and outcomes of a specific meeting.

**Create when:** A session has taken place and there is substantive content to record — decisions made, proposals adopted or rejected, reports received.

**Do not create when:** A session is scheduled but has not yet occurred. Create a placeholder only if there are pre-session documents worth linking.

**Required properties:**
```yaml
type: meeting
status: placeholder | draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
date: YYYY-MM-DD
session_number: ""
body: ""
```

**Optional properties:**
```yaml
location: ""
chair: ""
documents_considered: []
keywords: []
```

---

### 2.4 Proposal

**Purpose:** Represents a submitted document — an informal document (INF), working document (WP), or formal proposal — submitted to a UNECE body for consideration. Proposals are the unit of change in the regulatory process.

**Create when:** A document has been submitted to a session and is substantive enough to track separately (regulatory amendment proposals, major technical contributions, new work items).

**Do not create when:** A document is purely administrative (corrections, procedural notes) or when its content is fully captured within a Meeting note.

**Required properties:**
```yaml
type: proposal
status: placeholder | draft | active | adopted | rejected | deferred
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
document_number: ""
submitted_by: ""
submitted_to: ""
session: ""
date: YYYY-MM-DD
```

**Optional properties:**
```yaml
outcome: ""
keywords: []
affects_regulation: []
```

---

### 2.5 Concept

**Purpose:** Represents a technical, regulatory, or safety concept that appears across multiple regulations, working groups, or OEM implementations. Concepts are the shared vocabulary of the domain.

**Create when:** A term or concept is used across multiple notes and warrants a canonical definition, regulatory usage mapping, and relationship to other concepts.

**Do not create when:** A term is used only once in a single regulation note and is simple enough to define inline. Reserve concept notes for terms that connect across the graph.

**Required properties:**
```yaml
type: concept
status: placeholder | draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
defined_in: ""          # primary source of formal definition
aliases: []             # alternative names or abbreviations
sae_level: ""           # if concept is SAE-level-specific
keywords: []
```

---

### 2.6 OEM

**Purpose:** Tracks an automotive manufacturer or technology developer with a stake in UNECE automated driving regulation. Covers relevant products, type approvals sought or held, and regulatory engagement.

**Create when:** An OEM has submitted proposals, sought type approval, or is otherwise materially engaged in the regulatory process covered by this vault.

**Do not create when:** An OEM is merely tangentially mentioned. If the mention is brief, link to an existing note or leave it as an unresolved link.

**Required properties:**
```yaml
type: oem
status: placeholder | draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
headquarters: ""
industry_associations: []   # e.g., OICA, CLEPA
type_approvals: []
keywords: []
aliases: []
```

---

### 2.7 Organization

**Purpose:** Represents a regulatory body, standards organization, government agency, or industry association with a formal role in the UNECE regulatory process.

**Create when:** An organization has a named, formal role — as a contracting party, observer, or secretariat — in WP.29 or GRVA proceedings.

**Do not create when:** An organization is mentioned in passing without a specific regulatory role. Use inline text or an unresolved link.

**Required properties:**
```yaml
type: organization
status: placeholder | draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
org_type: "regulatory_body | standards_body | industry_association | government_agency | testing_body"
country: ""
role_in_wp29: ""
keywords: []
aliases: []
```

---

### 2.8 Research Note

**Purpose:** A working note for active, in-progress research. Used to explore a question, gather findings, and work toward synthesis. Research Notes are ephemeral — they should be promoted, merged into authoritative notes, or archived once the research is complete.

**Create when:** Investigating a new question that spans multiple existing notes. Useful for tracking an evolving understanding before it is mature enough to update authoritative notes.

**Do not create when:** The finding is simple enough to add directly to an existing note. Do not accumulate Research Notes indefinitely; they should resolve into updates to authoritative notes.

**Required properties:**
```yaml
type: research_note
status: draft | active | resolved | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
question: ""        # the research question driving this note
resolution: ""      # what note(s) this was merged into
keywords: []
```

---

### 2.9 Personal Insight

**Purpose:** Captures personal analytical conclusions, strategic observations, or hypotheses that go beyond documented facts and interpretations. Clearly marked as personal.

**Create when:** A conclusion or hypothesis is significant enough to preserve but is not appropriate to insert into an authoritative note as fact or interpretation.

**Do not create when:** The observation is a brief annotation that fits inline in another note (use *Insight:* label there instead).

**Required properties:**
```yaml
type: personal_insight
status: draft | active | archived
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
```

**Optional properties:**
```yaml
confidence: "low | medium | high"
keywords: []
```

---

## 3. YAML Metadata Standard

### Common Fields (All Entities)

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Entity type. See §2. |
| `status` | string | Yes | Lifecycle stage. See per-entity values. |
| `tags` | list | Yes | Flat keyword list for search and filtering. |
| `related` | list | Yes | Names of related notes (mirrors wiki links). |
| `source` | string | Yes | Primary source document or URL. Empty string if none. |
| `last_updated` | date | Yes | ISO 8601 date of last substantive edit. |
| `created` | date | Yes | ISO 8601 date of note creation. |
| `knowledge_type` | string | Recommended | Epistemic classification of the primary content. See §3.1. |
| `evidence_level` | string | Recommended | Strength of evidential basis. See §3.1. |

### §3.1 — Epistemic Metadata Fields

#### `knowledge_type`

Classifies the dominant epistemic character of the note's content.

| Value | Meaning | When to Use |
|---|---|---|
| `official_fact` | Note contains primarily statements directly sourced from official documents | Regulation notes with sourced definitions and requirements |
| `structural_relationship` | Note primarily describes explicitly documented relationships between entities | Working group notes; meeting notes; org notes |
| `interpretation` | Note contains primarily conclusions derived by reasoning across documents | Analysis notes; concept notes explaining regulatory significance |
| `personal_insight` | Note contains primarily the author's own analysis | Research Notes and Personal Insight notes only |

Notes that mix types should use the dominant type and label individual paragraphs with `*Interpretation:*` or `*Insight:*` as appropriate.

#### `evidence_level`

Indicates the strength and directness of the evidential basis for the note's content.

| Value | Meaning | When to Use |
|---|---|---|
| `official` | Content is directly sourced from official UNECE or equivalent documents | Note content has inline citations to named documents |
| `derived` | Content is inferred from or synthesised across multiple documents | Note contains interpretations that require labeling |
| `personal` | Content reflects the author's own analysis, not tied to specific documents | Research Notes; Personal Insight notes |

#### Usage in YAML

```yaml
knowledge_type: official_fact   # official_fact | structural_relationship | interpretation | personal_insight
evidence_level: official         # official | derived | personal
```

These fields are optional but strongly recommended for any note containing substantive content beyond placeholder status.

### Optional Fields by Entity Type

| Field | Entities | Description |
|---|---|---|
| `aliases` | Regulation, Concept, OEM, Organization | Alternative names; enables Obsidian alias resolution. |
| `keywords` | All | Domain-specific search terms, broader than tags. |
| `date` | Meeting, Proposal | Date of session or submission. |
| `session_number` | Meeting | Ordinal session number (e.g., `"25"`). |
| `body` | Meeting | Hosting body (e.g., `"GRVA"`, `"WP.29"`). |
| `document_number` | Proposal | Official UNECE document number. |
| `submitted_by` | Proposal | Submitting delegation or organization. |
| `submitted_to` | Proposal | Target body and session. |
| `outcome` | Proposal | `adopted`, `rejected`, `deferred`, `referred`. |
| `regulation_number` | Regulation | Numeric identifier (e.g., `"157"`). |
| `entry_into_force` | Regulation | Date regulation became binding. |
| `responsible_body` | Regulation | Body owning the regulation (e.g., `"GRVA"`). |
| `parent_body` | Working Group | Supervisory body. |
| `defined_in` | Concept | Primary document containing formal definition. |
| `sae_level` | Concept | SAE automation level, if relevant. |
| `headquarters` | OEM | Country of HQ. |
| `org_type` | Organization | Category of organization. |
| `question` | Research Note | The research question being explored. |
| `resolution` | Research Note | Note(s) this was promoted into. |
| `confidence` | Personal Insight | Author's confidence level. |

### Dataview Compatibility
All YAML fields are designed to be queryable via Obsidian Dataview. Example queries:

```dataview
TABLE status, responsible_body, last_updated
FROM "01 Regulations"
WHERE type = "regulation"
SORT last_updated DESC
```

```dataview
LIST
FROM "04 Working Groups"
WHERE status = "active"
```

---

## 4. Relationship Model

Relationships are expressed through `[[wiki links]]` in note bodies. The following table defines the canonical relationship vocabulary. Using consistent verbs in link contexts makes the graph semantically richer.

---

### §4.1 — Edge Metadata Schema

Every meaningful relationship in the knowledge graph should be backed by an evidence record. This schema defines the metadata that may accompany any relationship stored in a note.

#### Edge Metadata Fields

```yaml
relationship_type: ""       # e.g., requires, defines, references, submits_to
source_entity: ""           # name of the originating entity note
target_entity: ""           # name of the target entity note
evidence_source: ""         # document title or name
evidence_location: ""       # section / paragraph / page / annex
evidence_strength: ""       # explicit | derived | inferred | unsupported
confidence: ""              # high | medium | low | needs_review
last_verified: YYYY-MM-DD
review_status: ""           # verified | pending | rejected | needs_review
```

#### Evidence Strength

| Value | Meaning |
|---|---|
| `explicit` | The source document directly states this relationship |
| `derived` | Follows clearly from document structure or institutional process |
| `inferred` | Logical conclusion not directly stated in any source |
| `unsupported` | No source found; relationship exists by analogy or assumption only |

Only `explicit` and `derived` relationships may be stored directly in entity notes. `inferred` relationships must be labeled `*Interpretation:*`. `unsupported` relationships must not be stored — route to `11 Review/Pending/`.

#### Confidence

| Value | Meaning |
|---|---|
| `high` | Source is unambiguous; direct quote available |
| `medium` | Source is probable; paraphrase is reasonable |
| `low` | Source is indirect or uncertain |
| `needs_review` | Evidence is missing, conflicting, or ambiguous |

#### Storage Options

Edge metadata may be stored in any of four ways, depending on the context:

1. **Inline citation** — cite directly after the relationship statement in a note body: `**Fact (ECE/TRANS/WP.29/2026/139, §4.3.2, explicit, high):**`
2. **Relationship table** — a structured table in the note body listing entity triples with evidence columns
3. **Review note** — a dedicated review item in `11 Review/Pending/` for relationships awaiting evidence
4. **Future edge registry** — a dedicated YAML or Markdown registry for systematic relationship tracking (reserved for future development)

#### Forbidden: Conceptual Similarity as Legal Dependency

The most dangerous failure mode is converting conceptual co-occurrence into a legal dependency claim:

| Observation (acceptable) | Forbidden transformation |
|---|---|
| "R157 and R171 both address driver monitoring" | "R171 is derived from R157" |
| "R155 and R157 address related topics" | "R155 is a prerequisite for R157 type approval" |
| "ADS UN GTR and R157 both mention DSSAD" | "ADS UN GTR supersedes R157's data recording provisions" |

These transformations are **prohibited** regardless of how logical they appear. Conceptual similarity requires Class 3 relationship handling (see RELATIONSHIPS.md §0.6). Legal dependency requires Class 1 with `explicit` evidence.

| From Entity | Relationship | To Entity | Example |
|---|---|---|---|
| Working Group | **creates** | Proposal | `[[ADS IWG]]` creates `[[GRVA-24-0012]]` |
| Working Group | **develops** | Regulation | `[[DCAS]]` develops `[[R171]]` |
| Working Group | **reports to** | Organization | `[[VMAD]]` reports to `[[GRVA]]` |
| Proposal | **modifies** | Regulation | Proposal modifies `[[R157]]` |
| Proposal | **introduced by** | Organization | Proposal introduced by `[[European Commission]]` |
| Proposal | **discussed at** | Meeting | Proposal discussed at `[[GRVA 25th Session]]` |
| Meeting | **hosted by** | Organization | `[[GRVA 25th Session]]` hosted by `[[UNECE]]` |
| Meeting | **considers** | Proposal | Meeting considers `[[Proposal]]` |
| Meeting | **advances** | Regulation | Meeting advances `[[R171]]` |
| Regulation | **defines** | Concept | `[[R157]]` defines `[[MRM]]` |
| Regulation | **requires** | Concept | `[[R157]]` requires `[[Driver Availability]]` |
| Regulation | **supersedes** | Regulation | Amendment supersedes prior version of `[[R157]]` |
| Regulation | **complements** | Regulation | `[[R155]]` complements `[[R156]]` |
| Concept | **is component of** | Concept | `[[DDT]]` is component of `[[ADS]]` |
| Concept | **precedes** | Concept | `[[Transition Demand]]` precedes `[[MRM]]` |
| Concept | **enables** | Concept | `[[Driver Monitoring]]` enables `[[Driver Availability]]` |
| OEM | **implements** | Regulation | `[[Mercedes-Benz]]` implements `[[R157]]` |
| OEM | **submits** | Proposal | `[[BMW]]` submits proposal to `[[GRVA]]` |
| OEM | **member of** | Organization | `[[BMW]]` member of `[[OICA]]` |
| Organization | **hosts** | Meeting | `[[UNECE]]` hosts `[[GRVA 25th Session]]` |
| Organization | **submits** | Proposal | `[[European Commission]]` submits proposal |
| Organization | **observes** | Organization | `[[OICA]]` observes `[[WP.29]]` |
| Research Note | **analyzes** | Regulation | Research Note analyzes `[[R171]]` |
| Research Note | **references** | Concept | Research Note references `[[ODD]]` |
| Personal Insight | **concerns** | Regulation | Personal Insight concerns `[[ADS UN GTR]]` |
| Personal Insight | **builds on** | Research Note | Personal Insight builds on Research Note |

---

## 5. Folder Mapping

Folders provide a coarse organizational scaffold. They are **not** the primary navigation mechanism and should not be treated as a taxonomy.

| Folder | Entity Types Stored |
|---|---|
| `00 Home/` | Navigation hub only |
| `01 Regulations/` | `regulation` |
| `02 WP29/` | `organization` (WP.29 body), `meeting` (WP.29 sessions) |
| `03 GRVA/` | `organization` (GRVA body), `meeting` (GRVA sessions) |
| `04 Working Groups/` | `working_group` |
| `05 Concepts/` | `concept` |
| `06 OEM/` | `oem` |
| `07 Organizations/` | `organization` |
| `08 Meetings/` | `meeting` (working group sessions) |
| `09 Proposals/` | `proposal` |
| `10 Research Notes/` | `research_note` |
| `11 Templates/` | Templates only — not knowledge entities |
| `12 Attachments/` | Raw source files — not knowledge entities |
| `13 Resources/` | External references — not knowledge entities |

**Why folders are not the knowledge structure:** A note about R157 in `01 Regulations/` connects to notes in `04 Working Groups/`, `05 Concepts/`, `06 OEM/`, `08 Meetings/`, and `09 Proposals/`. None of those relationships are visible from the folder path. The wiki links are. Navigate by the graph, not the folder tree.

---

## 6. Linking Rules

### Every Regulation Note Should Link To:
- The **working group** primarily responsible (e.g., `[[GRVA]]`, `[[DCAS]]`)
- At minimum **two technical concepts** it defines or relies on
- At minimum **one related regulation** (companion, predecessor, or complement)
- Any **meeting sessions** where key decisions were made
- Any **OEM** known to have type approval or a material proposal under it

### Every Working Group Note Should Link To:
- Its **parent body** (e.g., `[[GRVA]]`, `[[WP.29]]`)
- Its **primary deliverable** (regulation or GTR under development)
- **Sibling working groups** contributing to the same regulation
- Key **concepts** central to its mandate

### Every Meeting Note Should Link To:
- The **hosting body** (e.g., `[[GRVA]]`, `[[WP.29]]`)
- **Proposals** considered at the meeting
- **Regulations** advanced or discussed
- **Working group reports** received (link to the working group)
- Previous and next session (chain of continuity)

### Every Proposal Note Should Link To:
- The **regulation** it seeks to modify
- The **organization** that submitted it
- The **meeting** at which it was considered
- The **working group** it originated from (if applicable)

### Every Concept Note Should Link To:
- The **regulation(s)** where it is formally defined or heavily used
- **Related concepts** (upstream, downstream, parallel)
- The **working group(s)** where it is primarily debated
- Any **OEM** implementation examples where relevant

### Every OEM Note Should Link To:
- **Regulations** for which it holds or has sought type approval
- **Organizations** (industry associations) it belongs to
- **Proposals** it has submitted
- **Working groups** it participates in

### Semantic Links Over Navigation Links
A link should express a **relationship**, not just provide a path to another file. The reader should understand why the link exists. If a regulation note links to a concept note, the surrounding sentence should make clear the nature of that relationship: "R157 requires the ADS to execute a `[[MRM]]` when the driver fails to respond to a `[[Transition Demand]]`."

---

## 7. Naming Conventions

### Regulations
Use the short-form UN Regulation number as the filename: `R79`, `R155`, `R156`, `R157`, `R171`.
For GTRs with no number yet: use a descriptive short name: `ADS UN GTR`.

### Sessions
Format: `[Body] [Nth] Session` — e.g., `GRVA 25th Session`, `WP29 199th Session`.
Use ordinal suffixes: 1st, 2nd, 3rd, 4th, 24th, 25th.

### Working Groups
Use the official acronym: `ADS IWG`, `VMAD`, `FRAV`, `DSSAD`, `DCAS`, `ADAS TF`, `EDR-DSSAD`.

### Concepts
Use the full English term in title case: `Driver Monitoring`, `Operational Design Domain`, `Minimal Risk Maneuver`.
Abbreviation notes may be created as thin aliases pointing to the full concept: `ODD.md` → points to `Operational Design Domain.md`.

### OEMs
Use the official legal short name: `BMW`, `Mercedes-Benz`, `Volkswagen`, `NIO`, `Tesla`, `Xpeng`, `Wayve`, `Mobileye`.

### Organizations
Use the official English name or widely-used acronym: `UNECE`, `WP.29`, `GRVA`, `OICA`, `CLEPA`, `European Commission`, `RDW`, `BASt`, `TÜV`.

### Proposals
When creating dedicated proposal notes, use the official document number as the filename: `GRVA-25-0012`, `ECE-TRANS-WP29-2024-75`.

### General Rules
- Prefer **full official names** over invented abbreviations
- Avoid creating two notes whose names could be confused
- Use `aliases` in YAML frontmatter for alternative spellings or acronyms
- File names are case-sensitive in Obsidian on macOS/Linux — use consistent capitalization

---

## 8. Knowledge Lifecycle

### When New UNECE Documents Arrive

Do **not** create an isolated note per document. Documents are source material; they are processed into the knowledge graph.

Follow this sequence:

1. **Read the document.** Understand what it contains before touching the vault.
2. **Identify affected entities.** Which regulations, concepts, working groups, or OEMs does this document concern?
3. **Update existing notes first.** Add new information, update status fields, add or update links. This is the default action.
4. **Create missing entities only if necessary.** If the document introduces a genuinely new concept, a new working group, or a new regulation, create a note using the appropriate template. Do not create notes for things already covered.
5. **Create missing links.** After updating or creating notes, scan for unlinked references and add wiki links.
6. **Preserve history.** Do not erase prior content when updating a note. Add to it. If something has changed (e.g., a regulation was amended), note the change with dates — do not silently rewrite.

### Status Transitions

Notes move through lifecycle stages:

```
placeholder → draft → active → archived
```

- A note becomes `draft` when substantive content is added.
- A note becomes `active` when its content is reliable and current.
- A note becomes `archived` when the entity it represents is superseded, dissolved, or no longer relevant to active research.

Archived notes should not be deleted. They preserve historical context and may be referenced by meeting notes, proposals, and research notes.

### Handling Amendments and Supplements
When a regulation is amended:
- Update the regulation note in place
- Add a **Regulatory History** section if one does not exist, recording the amendment with date and description
- Update `last_updated` in YAML
- Do not create a new note for the amended version unless it represents a genuinely different regulatory instrument

---

## 9. Claude Operating Rules

Claude Code sessions operating in this vault must follow these rules. They apply regardless of what the user has asked — they are constraints on *how* Claude works, not on *what* Claude produces.

### Preserve Consistency
Match the note structure, YAML fields, formatting, and tone of existing notes. Read several existing notes of the same type before creating a new one of that type. Do not introduce new metadata fields without also updating this SCHEMA.md.

### Never Duplicate Knowledge
Before creating any note, search for an existing note on the same topic. If one exists, extend it. Two notes covering the same entity are worse than one imperfect note. Links will fragment, context will diverge, and the graph will degrade.

### Update Instead of Rewrite
When new information arrives, **add** to existing notes. Do not erase or restructure a note's existing content to accommodate new information unless the existing content is factually wrong. Append, annotate, or update specific sections.

### Suggest Missing Links
When reading or editing any note, identify opportunities for wiki links that are not yet present. A sentence mentioning "Minimal Risk Maneuver" without `[[MRM]]` is an incomplete link. A regulation note that does not link to its responsible working group is under-connected.

### Preserve YAML
Never remove YAML frontmatter fields. Never change `created` dates. Update `last_updated` when content changes. If a field value is unknown, use an empty string `""` — do not remove the field.

### Preserve Note History
Do not silently overwrite prior content. If information has changed, preserve the prior state in a dated note (e.g., in a **Regulatory History** section) and update the current state. Context is valuable.

### Distinguish Facts from Interpretation
Apply the three-tier epistemic labeling consistently:
- Unmarked or cited text = **Fact** (sourced)
- *Interpretation:* label = your reading of what something means
- *Insight:* label = personal analysis or hypothesis

Never present an interpretation as a fact. Flag uncertain claims with `[VERIFY]` rather than omitting them.

### Maintain Source Traceability
Every factual claim must be traceable to a source. Use `source` in YAML for the primary source. Use inline citations for specific claims. If a source is unknown, note it as `[SOURCE NEEDED]` rather than asserting the claim.

### Ask Before Destructive Actions
- Never delete a note or folder without explicit user instruction
- Never rename a file without confirming the change
- Never overwrite a non-empty note without reading it first
- Always summarize what was created, updated, or linked after each operation

---

## 10. Future Expansion

The following entity types are **reserved** for future development. Notes for these types should not be created yet. The schema entries below define their intended purpose and properties so they can be introduced consistently when needed.

### Test Method
A specific validation or verification method used to demonstrate regulatory compliance. Distinct from a Concept; a Test Method is procedural and linked to specific regulatory requirements.

```yaml
type: test_method
regulation: ""
standard: ""     # e.g., ISO 26262, ISO 21448
```

### Scenario
A specific traffic or operational scenario used in validation or type approval. Links to Test Methods, Concepts (ODD, DDT), and Regulations.

```yaml
type: scenario
scenario_category: ""    # e.g., cut-in, lane change, MRM trigger
odd_context: ""
```

### Use Case
A high-level operational use case for an ADS or ADAS system. Broader than a Scenario; narrower than an ODD.

```yaml
type: use_case
sae_level: ""
```

### Function
A specific system function (e.g., lane centering, emergency braking, remote monitoring) referenced in regulations or working group documents.

```yaml
type: function
system: ""
regulation_reference: ""
```

### Requirement
A specific regulatory or technical requirement extracted from a regulation or standard. Enables fine-grained traceability.

```yaml
type: requirement
source_regulation: ""
paragraph: ""
requirement_type: "functional | performance | procedural"
```

### Country
A contracting party to the 1958 Agreement, relevant as an approving authority or regulatory position holder.

```yaml
type: country
contracting_party: true | false
approval_authority: ""
```

### Approval Authority
A national technical authority responsible for granting type approvals under a UN Regulation (e.g., KBA in Germany, RDW in the Netherlands, VCA in the UK).

```yaml
type: approval_authority
country: ""
regulations_covered: []
```

### Certification
A specific type approval or certification granted to a specific vehicle or system under a specific regulation.

```yaml
type: certification
regulation: ""
oem: ""
system: ""
approval_authority: ""
date_granted: YYYY-MM-DD
```

### Safety Case
A structured safety argument supporting the approval of an ADS or ADAS system. Links to Regulations, Concepts (SOTIF, Functional Safety), and Test Methods.

```yaml
type: safety_case
oem: ""
system: ""
regulation: ""
standard: ""
```
