---
type: governance
status: active
tags: [ontology, governance, knowledge-graph, architecture]
related: [ONTOLOGY, SCHEMA, RELATIONSHIPS, KNOWLEDGE_RULES]
source: "internal architecture specification"
ontology_version: "1.2"
created: 2026-06-28
last_updated: 2026-06-28
---

# KNOWLEDGE_ONTOLOGY

## 1. Purpose

This ontology defines the structural model of the Knowledge OS. It specifies what kinds of knowledge entities may exist, how they may relate, how evidence is represented, and how future skills must preserve graph integrity.

The Vault is an evidence-driven knowledge graph, not a note collection. A Markdown file is only the storage representation of an entity. The entity, its metadata, its evidence, and its graph relationships are the knowledge object.

### Ontology vs Templates

The ontology defines the allowed entity types, relationship semantics, evidence hierarchy, lifecycle states, and quality attributes. Templates define one possible Markdown layout for writing an entity note. Templates may evolve for usability; the ontology defines the stable conceptual contract.

### Ontology vs Skills

Skills are operational procedures. They acquire, merge, review, or maintain knowledge. The ontology is the structural specification those skills must obey. A skill may create or update an entity, but it must not invent entity types or relationship semantics outside this ontology.

### Ontology vs Knowledge

The ontology contains structure only. It does not contain domain facts, regulatory conclusions, organization claims, or technical interpretations. Knowledge belongs in entity notes and must be supported by evidence.

## 2. Repository Layer Model

Ontology v1.1 introduced repository layers. Ontology v1.2 adds Knowledge Views as a presentation/query layer over canonical knowledge.

The repository contains multiple artifact classes. Only one of them is canonical domain knowledge. Repository layers are **not** knowledge entity types. They are architectural scopes that determine which rules apply before entity-level ontology validation begins.

```text
Repository
|
+-- Knowledge Layer
+-- Governance Layer
+-- Automation Layer
+-- Project Layer
+-- Knowledge Views Layer
```

### Layer 1 — Knowledge Layer

**Purpose:** Contains canonical domain knowledge and evidence-bearing knowledge artifacts.

Typical folders:

- `01 Regulations/`
- `02 WP29/`
- `03 GRVA/`
- `04 Working Groups/`
- `05 Concepts/`
- `06 OEM/`
- `07 Organizations/`
- `08 Meetings/`
- `09 Proposals/`
- `10 Research Notes/`
- `12 Attachments/`
- `13 Resources/`
- `14 Timeline/`

Rules:

- Governed by the knowledge entity ontology.
- Acquire creates knowledge here.
- Merge updates knowledge here.
- Review evaluates this layer by default.
- Evolution migrates this layer by default.
- Only this layer participates in ontology compliance scoring.

### Layer 2 — Governance Layer

**Purpose:** Defines rules, policies, workflow boundaries, and system architecture.

Canonical folder:

- `Governance/`

Examples:

- `KNOWLEDGE_ONTOLOGY`
- `QUALITY_POLICY`
- `WORKFLOW`
- `ROADMAP`

Rules:

- Governance documents define policy.
- Governance documents are not knowledge entities.
- Acquire must never modify Governance.
- Merge must not merge domain knowledge into Governance.
- Review may validate Governance separately when explicitly requested.
- Evolution may update Governance only through explicit version upgrades.

### Layer 3 — Automation Layer

**Purpose:** Contains Claude Code implementation, prompts, skills, scripts, and operational automation.

Typical folders:

- `.claude/`
- `Skills/`
- `copilot/`

Rules:

- Automation artifacts are operational infrastructure.
- Automation artifacts are not knowledge.
- Ontology compliance must ignore this layer by default.
- Knowledge Review must not score this layer.
- Knowledge Evolution must not migrate this layer unless explicitly requested.
- Changes to this layer are software/tooling changes, not knowledge evolution.

### Layer 4 — Project Layer

**Purpose:** Contains repository management and project administration artifacts.

Examples:

- `README`
- `LICENSE`
- `CHANGELOG`
- `.github/`
- `.gitignore`

Rules:

- Project artifacts are outside the knowledge graph.
- Project artifacts never contribute to ontology compliance scoring.
- Knowledge Skills should not treat project artifacts as knowledge entities.
- Project artifacts may be maintained by ordinary repository management workflows.

### Layer 5 — Knowledge Views Layer

**Purpose:** Provides user-oriented exploration surfaces, dashboards, and reusable graph queries over canonical knowledge.

Canonical folder:

- `15 Views/`

Examples:

- `DCAS`
- `ADS`
- `Cybersecurity`
- `Software Update`
- `Driver Monitoring`
- `Timeline`
- `R171 Evolution`
- `GRVA Overview`

Rules:

- Knowledge Views are not canonical knowledge.
- Views do not introduce facts.
- Views link to canonical entities rather than duplicating them.
- Views may contain generated summaries, timelines, comparison tables, diagrams, Dataview queries, and navigation indexes.
- Views are excluded from ontology compliance scoring.
- Views may be regenerated at any time.
- A View must never become an additional source of truth.

### Layer Responsibilities

| Layer | Responsibility | Ontology Entity Rules Apply | Compliance Scoring |
|---|---|---|---|
| Knowledge Layer | Domain knowledge and evidence-bearing knowledge graph | Yes | Yes |
| Governance Layer | Rules and architecture | No, governance validation only | Separate governance validation |
| Automation Layer | Skills, prompts, scripts, tool configuration | No | Excluded |
| Project Layer | Repository management and project metadata | No | Excluded |
| Knowledge Views Layer | Presentation, exploration, and reusable graph views | No, view validation only | Excluded |

## 3. Ontology Compliance Scope

Ontology compliance tools must determine repository layer before applying entity rules.

Only the **Knowledge Layer** participates in ontology compliance scoring.

Governance may be validated separately for policy completeness, versioning, internal consistency, and compatibility with existing skills. Governance validation is not knowledge ontology scoring.

Automation artifacts are excluded from ontology compliance scoring. Skill files, prompt files, local automation instructions, scripts, and tool configuration must not be counted as missing knowledge metadata.

Project artifacts are excluded from ontology compliance scoring. Repository management files must never reduce the Vault's knowledge compliance score.

Knowledge Views are excluded from ontology compliance scoring. Views may be validated for broken links, missing references, stale generated content, and alignment with their declared scope, but they must not be scored as canonical knowledge.

Compliance workflow:

1. Classify artifact by repository layer.
2. If Knowledge Layer, apply entity ontology, evidence ontology, relationship ontology, folder ontology, and naming rules.
3. If Governance Layer, apply governance validation only when explicitly requested.
4. If Automation Layer, exclude unless the user requests an automation review.
5. If Project Layer, exclude unless the user requests repository hygiene review.
6. If Knowledge Views Layer, validate view integrity only when explicitly requested or during view maintenance.

## 4. Knowledge Views

The Knowledge OS distinguishes canonical knowledge from knowledge views.

### Canonical Knowledge

Canonical knowledge contains facts. Each fact should exist exactly once, in the correct canonical entity.

Examples of canonical knowledge entities:

- `R171`
- `R157`
- `GRVA`
- `GRVA 24th Session`
- `E-Mobility Europe`
- `Driver Availability`
- `ADAS-45-07`

Canonical knowledge is maintained by:

- Acquire
- Merge
- Evolution
- Review

### Knowledge Views

Knowledge Views organize existing canonical knowledge from a specific perspective. They are reusable query definitions over the knowledge graph.

Views do **not** introduce new facts. A View should never duplicate or overwrite canonical knowledge. If a View reveals missing knowledge, the missing knowledge must be acquired or merged into the canonical entity, not stored only in the View.

### View Characteristics

A View:

- Aggregates existing knowledge.
- Links rather than duplicates.
- May contain lightweight summaries.
- May contain generated timelines.
- May contain generated comparison tables.
- May contain generated diagrams.
- Should reference canonical entities.
- Should remain lightweight.
- Must not become a source of truth.

### Repository Location

Knowledge Views live in:

```text
15 Views/
```

This folder is outside the canonical knowledge hierarchy. Views are generated and maintained separately from canonical knowledge.

### Suggested Initial Views

| View | Purpose | Typical User Questions |
|---|---|---|
| `DCAS.md` | Provide a unified perspective on Driver Control Assistance Systems. | Complete DCAS timeline; organizations submitting DCAS proposals; R171 evolution. |
| `ADS.md` | Provide a cross-entity view of Automated Driving Systems regulation and concepts. | ADS regulatory evolution; ADS concepts; related working groups. |
| `Cybersecurity.md` | Navigate cybersecurity-related regulations, concepts, and evidence. | Which regulations address cybersecurity; how cybersecurity interacts with software updates. |
| `Software Update.md` | Navigate software-update requirements and related regulations. | Timeline of software update regulation; related concepts and evidence. |
| `Driver Monitoring.md` | Explore driver monitoring across regulations, concepts, and meetings. | Driver monitoring requirements; relationship to driver availability. |
| `Timeline.md` | Aggregate major milestones across the Vault. | What happened when; which entities changed over time. |
| `R171 Evolution.md` | Present R171 development and amendment history as a generated view. | How R171 evolved; open proposals; relevant meetings. |
| `GRVA Overview.md` | Provide a navigational overview of GRVA sessions, groups, and outputs. | GRVA discussions; session outcomes; related documents. |

### Example: DCAS View

**Purpose:** Provide a unified perspective on Driver Control Assistance Systems.

Referenced entities:

| Category | Canonical Entities |
|---|---|
| Regulations | `R171` |
| Working Groups | `DCAS IWG` or other approved canonical DCAS working-group entity |
| Organizations | `E-Mobility Europe`, `OICA`, `CLEPA` |
| Meetings | `GRVA 24th Session`, `GRVA 25th Session`, ADAS session entities when present |
| Concepts | `Driver Availability`, `Driver Engagement`, `Driver Override` when canonical entities exist |

Typical queries:

- Show the complete DCAS timeline.
- Which meetings discussed Driver Availability?
- Which organizations submitted DCAS proposals?
- How has R171 evolved?
- Which proposals are still open?

The View itself must not contain duplicated regulatory knowledge. It should link to canonical notes and use generated summaries only as navigation aids.

### View Lifecycle

Views have a lifecycle distinct from canonical knowledge:

```text
Created -> Referenced -> Updated -> Regenerated -> Archived
```

| State | Meaning |
|---|---|
| Created | View definition exists and references canonical entities. |
| Referenced | View is used by users or linked from navigation surfaces. |
| Updated | View structure or scope changes manually. |
| Regenerated | View content is refreshed from canonical knowledge. |
| Archived | View is retired or superseded. |

Unlike canonical knowledge, Views may be regenerated at any time.

### Relationship with Obsidian

Views are intended for exploration. They may use:

- Dataview dashboards.
- Timeline summaries.
- Cross-regulation navigation.
- Meeting navigation.
- Domain overviews.
- Generated diagrams.

Views provide entry points for exploration without becoming additional sources of truth.

### View Compliance

Knowledge Views are excluded from ontology compliance scoring. Only canonical knowledge is evaluated for completeness and quality.

Views may be evaluated only for:

- Broken links.
- Missing references.
- Outdated generated content.
- Scope drift.
- References to non-canonical or duplicate entities.

## 5. Knowledge Entity Types

Every knowledge entity must have exactly one primary type. Additional nuance may be expressed through metadata, tags, aliases, and relationships.

### Regulation

| Attribute | Specification |
|---|---|
| Purpose | Represent a legally or procedurally bounded regulatory instrument. |
| Definition | A regulation, rule, act, standard-setting instrument, or adopted regulatory text with a defined scope and issuing body. |
| Typical Examples | Numbered regulations, implementing regulations, type-approval rules. |
| Folder Location | `01 Regulations/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Scope, Definitions, Key Requirements, Amendment History, Relationships, References, Evidence, Open Questions |
| Typical Relationships | `created_by`, `approved_at`, `references`, `amends`, `supersedes`, `defines`, `depends_on`, `supported_by` |

### UN GTR

| Attribute | Specification |
|---|---|
| Purpose | Represent a Global Technical Regulation or equivalent globally harmonized technical instrument. |
| Definition | A technical regulation developed through a global harmonization process and tracked separately from ordinary regulations when process or legal status differs. |
| Typical Examples | Global technical regulations, draft global technical regulations. |
| Folder Location | `01 Regulations/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `instrument_family`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Scope, Definitions, Requirements Structure, Development History, Relationships, References, Evidence, Open Questions |
| Typical Relationships | `created_by`, `approved_at`, `references`, `defines`, `depends_on`, `supported_by`, `resulted_in` |

### Working Group

| Attribute | Specification |
|---|---|
| Purpose | Represent a formal or semi-formal body responsible for developing knowledge, proposals, regulations, or technical material. |
| Definition | A group with a recognizable mandate, parent body, participants, and output. |
| Typical Examples | Working parties, expert groups, technical subgroups. |
| Folder Location | `04 Working Groups/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `parent_body`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Mandate, Parent Body, Participation, Deliverables, Meetings, Relationships, References, Evidence |
| Typical Relationships | `belongs_to`, `created_by`, `documents`, `resulted_in`, `references`, `supported_by` |

### Task Force / IWG

| Attribute | Specification |
|---|---|
| Purpose | Represent a scoped task force, informal working group, or subgroup operating within a parent body. |
| Definition | A group with a bounded work item, output, or technical mandate under a larger group. |
| Typical Examples | Task forces, informal working groups, drafting groups. |
| Folder Location | `04 Working Groups/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `parent_body`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Mandate, Parent Body, Work Items, Participants, Outputs, Relationships, References, Evidence |
| Typical Relationships | `belongs_to`, `participates_in`, `created_by`, `documents`, `resulted_in`, `supported_by` |

### Organization

| Attribute | Specification |
|---|---|
| Purpose | Represent an institution, public body, association, company, authority, or stakeholder organization. |
| Definition | A durable entity that participates in, publishes, submits, approves, or is referenced by the knowledge graph. |
| Typical Examples | Authorities, industry associations, standards bodies, companies, public institutions. |
| Folder Location | `07 Organizations/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `org_type`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Role, Participation, Submitted Documents, Relationships, References, Evidence, Open Questions |
| Typical Relationships | `participates_in`, `submitted_by`, `created_by`, `approved_at`, `documents`, `supported_by`, `related_to` |

### Meeting

| Attribute | Specification |
|---|---|
| Purpose | Represent a session, meeting, hearing, vote, workshop, or formal event where knowledge changes or is discussed. |
| Definition | A time-bound event with participants, documents, decisions, or outcomes. |
| Typical Examples | Sessions, committee meetings, task force meetings, workshops. |
| Folder Location | `08 Meetings/`, or a body-specific folder when already established |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `date`, `body`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Summary, Decisions, Documents, Participants, Timeline, Relationships, References, Evidence |
| Typical Relationships | `belongs_to`, `discussed_at`, `approved_at`, `resulted_in`, `documents`, `supported_by` |

### Meeting Document

| Attribute | Specification |
|---|---|
| Purpose | Represent a document submitted to, discussed at, or produced by a meeting. |
| Definition | A discrete document with a document number, title, submitter, date, or official source identity. |
| Typical Examples | Working documents, informal documents, reports, agendas, official decisions, slide decks. |
| Folder Location | `09 Proposals/` for substantive proposals, `12 Attachments/` for source files, or a dedicated document folder if introduced later |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `document_number`, `document_kind`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Summary, Document Identity, Submitter, Meeting Context, Affected Entities, Evidence, References |
| Typical Relationships | `submitted_by`, `discussed_at`, `references`, `amends`, `documents`, `supported_by`, `resulted_in` |

### Proposal

| Attribute | Specification |
|---|---|
| Purpose | Represent a proposed change, new work item, amendment, or formal contribution. |
| Definition | A submitted or tracked proposal that can be discussed, adopted, rejected, deferred, or merged into another entity. |
| Typical Examples | Amendment proposals, new regulation proposals, technical contributions. |
| Folder Location | `09 Proposals/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `submitted_by`, `submitted_to`, `document_number`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Summary, Proposed Change, Rationale, Affected Entities, Meeting History, Outcome, Evidence, References |
| Typical Relationships | `submitted_by`, `discussed_at`, `amends`, `supersedes`, `resulted_in`, `supported_by` |

### Concept

| Attribute | Specification |
|---|---|
| Purpose | Represent reusable technical, legal, procedural, or analytical vocabulary. |
| Definition | A term or idea that appears across multiple entities and needs a canonical definition or usage map. |
| Typical Examples | Technical concepts, procedural concepts, safety concepts, data concepts. |
| Folder Location | `05 Concepts/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Definition, Regulatory Usage, Related Concepts, Related Entities, Evidence, References, Open Questions |
| Typical Relationships | `defines`, `depends_on`, `related_to`, `derived_from`, `supported_by`, `references` |

### Timeline Event

| Attribute | Specification |
|---|---|
| Purpose | Represent a dated milestone or sequence of dated milestones. |
| Definition | A point or period in time that records adoption, publication, entry into force, meeting action, amendment, review, or archival transition. |
| Typical Examples | Adoption dates, publication dates, meeting milestones, amendment dates. |
| Folder Location | `14 Timeline/` |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `date` or `date_range`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Timeline, Event Details, Affected Entities, Evidence, References, Open Questions |
| Typical Relationships | `documents`, `resulted_in`, `approved_at`, `discussed_at`, `supported_by`, `related_to` |

### Person

| Attribute | Specification |
|---|---|
| Purpose | Represent a person only when their role is structurally important and evidence-supported. |
| Definition | An individual with a documented role in a body, organization, document, meeting, or decision. |
| Typical Examples | Chairs, secretaries, named submitters, official representatives. |
| Folder Location | Future canonical folder, or embedded in Organization/Meeting notes until person notes are introduced |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `role`, `affiliation`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Overview, Role, Affiliation, Participation, Documents, Evidence, References |
| Typical Relationships | `belongs_to`, `participates_in`, `submitted_by`, `created_by`, `supported_by` |

### Evidence Source

| Attribute | Specification |
|---|---|
| Purpose | Represent source material used to support knowledge claims. |
| Definition | A document, dataset, webpage, report, official text, or other source from which evidence can be extracted. |
| Typical Examples | PDFs, working documents, official webpages, reports, presentations, standards. |
| Folder Location | `12 Attachments/`, `13 Resources/`, or source registry notes |
| Required Metadata | `type`, `status`, `tags`, `related`, `source`, `created`, `last_updated`, `source_kind`, `authority_level`, `knowledge_type`, `evidence_level` |
| Recommended Sections | Source Identity, Authority, Access Path, Extracted Claims, Linked Entities, Citation Format, Review Status |
| Typical Relationships | `supports`, `supported_by`, `documents`, `references` |

### Adding New Entity Types

New entity types may be introduced only when all of the following are true:

- The entity cannot be accurately represented by an existing type.
- It has stable semantics independent of one domain note.
- It has a canonical folder location or an approved embedded representation.
- It has required metadata, recommended sections, and relationship rules.
- Existing entities can remain valid without migration, or a migration plan is defined.

## 6. Relationship Ontology

Every relationship must have explicit semantics. A relationship is a directed edge unless stated otherwise. If evidence is missing or ambiguous, the relationship must not be stored as a graph fact.

| Relationship | Meaning | Direction | Allowed Source Entities | Allowed Target Entities | Example |
|---|---|---|---|---|---|
| `belongs_to` | Source is institutionally, procedurally, or structurally part of target. | child -> parent | Working Group, Task Force / IWG, Person, Meeting | Organization, Working Group, Task Force / IWG | Task Force `belongs_to` Working Group |
| `participates_in` | Source participates in target without necessarily owning or creating it. | participant -> forum/activity | Organization, Person, Working Group, Task Force / IWG | Meeting, Working Group, Task Force / IWG, Process | Organization `participates_in` Task Force |
| `created_by` | Target created or authored source. | created entity -> creator | Regulation, UN GTR, Proposal, Meeting Document, Concept, Working Group | Organization, Working Group, Task Force / IWG, Person | Proposal `created_by` Working Group |
| `submitted_by` | Source was submitted by target. | submitted item -> submitter | Proposal, Meeting Document | Organization, Person, Working Group, Task Force / IWG | Meeting Document `submitted_by` Organization |
| `discussed_at` | Source was discussed at target. | discussed item -> meeting | Proposal, Meeting Document, Regulation, UN GTR, Concept | Meeting | Proposal `discussed_at` Meeting |
| `approved_at` | Source was approved, adopted, endorsed, or decided at target. | approved item -> meeting/decision point | Regulation, UN GTR, Proposal, Meeting Document | Meeting, Timeline Event | Regulation `approved_at` Meeting |
| `references` | Source explicitly cites, mentions, or points to target without a more specific relationship. | citing entity -> cited entity | Any entity | Any entity | Regulation `references` Evidence Source |
| `amends` | Source changes target. | amendment -> amended entity | Proposal, Meeting Document, Regulation | Regulation, UN GTR, Proposal | Proposal `amends` Regulation |
| `supersedes` | Source replaces target as the current authority or version. | newer entity -> older entity | Regulation, UN GTR, Proposal, Meeting Document | Regulation, UN GTR, Proposal, Meeting Document | Regulation `supersedes` earlier Regulation |
| `implements` | Source realizes, applies, or conforms to target in a concrete way. | implementer -> implemented entity | Organization, Product, System, Process | Regulation, UN GTR, Concept, Requirement | Organization `implements` Regulation |
| `defines` | Source contains a formal or authoritative definition of target. | defining source -> defined entity | Regulation, UN GTR, Meeting Document, Evidence Source | Concept, Term | Regulation `defines` Concept |
| `depends_on` | Source requires target to exist, function, or be satisfied. | dependent -> dependency | Regulation, UN GTR, Concept, Proposal, System | Regulation, Concept, Evidence Source, Requirement | Concept `depends_on` Concept |
| `related_to` | Source has a meaningful but non-specific relationship to target. | either direction, but choose one canonical direction | Any entity | Any entity | Concept `related_to` Concept |
| `derived_from` | Source is based on, extracted from, or adapted from target. | derived entity -> source entity | Concept, Research Note, Proposal, Regulation, UN GTR | Evidence Source, Meeting Document, Proposal, Regulation, UN GTR | Concept `derived_from` Evidence Source |
| `supported_by` | Source claim or entity is supported by target evidence. | claim/entity -> evidence | Any entity | Evidence Source, Meeting Document, Regulation, UN GTR, Official Website | Regulation `supported_by` Evidence Source |
| `documents` | Source records, reports, or describes target. | document/source -> documented entity | Evidence Source, Meeting Document, Meeting, Timeline Event | Any entity | Meeting Report `documents` Decision |
| `resulted_in` | Source produced target as an outcome. | cause/process/event -> outcome | Meeting, Proposal, Working Group, Task Force / IWG, Timeline Event | Regulation, UN GTR, Proposal, Concept, Timeline Event | Meeting `resulted_in` Proposal status |

### Avoiding Duplicate Semantics

Use the most specific relationship available. Do not store both a broad and narrow relationship for the same edge unless both are independently useful and evidenced.

- Use `submitted_by`, not `created_by`, when the key fact is submission.
- Use `approved_at`, not `discussed_at`, when the key fact is approval.
- Use `supported_by`, not `references`, when evidence support is the purpose of the edge.
- Use `amends`, not `related_to`, when a proposal changes a target.

### Use of `related_to`

`related_to` is allowed only when:

- A meaningful connection exists.
- No more specific relationship applies.
- The relationship is useful for navigation.
- The edge is not being used to smuggle in an unsupported dependency.

`related_to` must not be used for:

- Legal dependency.
- Amendment or supersession.
- Authorship, submission, approval, or participation.
- Speculative similarity.
- Relationship types that require evidence but do not yet have evidence.

## 7. Evidence Ontology

Evidence levels describe authority, not convenience. Lower-level evidence may supplement higher-level evidence but must never replace it when higher-level evidence is required.

| Level | Evidence Type | Description | Authority Level | Typical Examples | Suggested Confidence | Suggested Citation Format |
|---|---|---|---|---|---|---|
| A | UNECE Regulations | Official adopted regulatory text or equivalent legal instrument. | Highest | Official regulation addenda, adopted text, consolidated regulation. | High | `Fact (Document Number, section/paragraph): ...` |
| A | UN GTR | Official global technical regulation text or formal draft under decision process. | Highest | Adopted GTR, formal working document. | High | `Fact (Document Number, section/paragraph): ...` |
| A | Official Meeting Reports | Official record of decisions, agenda items, adoption, deferral, or endorsement. | Highest | Session reports, official minutes. | High | `Fact (Report Number, agenda item/paragraph): ...` |
| A | Official Working Documents | Officially submitted working documents, formal proposals, official reports. | Highest | Working documents, proposals, official annexes. | High | `Fact (Document Number, page/paragraph): ...` |
| A | Official Decisions | Formal decision records or adoption notices. | Highest | Decisions, voting results, adoption notices. | High | `Fact (Decision Reference, date/paragraph): ...` |
| B | UNECE Wiki | Official or semi-official process workspace used to coordinate work. | High but operational | Wiki pages, meeting pages, agenda trackers. | Medium to High | `Fact (UNECE Wiki, page title, access date): ...` |
| B | Official Organization Websites | Official pages from entities represented in the graph. | High for self-descriptive facts | Organization profile pages, membership pages, announcements. | Medium to High | `Fact (Organization Website, page title/URL, access date): ...` |
| B | Official Presentations | Slides or presentations from official meetings or official participants. | Medium to High | Meeting slides, official presentations. | Medium | `Fact (Presentation Title, page/slide): ...` |
| B | Official Slides | Slide decks with known authorship and meeting context. | Medium to High | Informal documents, meeting slides. | Medium | `Fact (Document Title, slide/page): ...` |
| C | Academic Publications | Peer-reviewed or scholarly sources. | Medium | Journal papers, conference papers. | Medium | `Evidence (Author, Year, page/section): ...` |
| C | Industry White Papers | Technical or policy papers from industry bodies or companies. | Medium | White papers, technical reports. | Medium | `Evidence (Publisher, Title, page/section): ...` |
| C | Standards | Standards and technical specifications. | Medium to High depending on context | ISO, SAE, CEN, ETSI standards. | Medium to High | `Fact/Evidence (Standard, clause): ...` |
| D | News | Journalistic or media reporting. | Low to Medium | Trade press, news reports. | Low to Medium | `Context (Publication, date): ...` |
| D | Conference Talks | Public talks without formal decision status. | Low to Medium | Keynotes, panels, conference decks. | Low | `Context (Talk, speaker, date): ...` |
| D | Vendor Blogs | Vendor-produced explanatory material. | Low | Product blogs, marketing posts. | Low | `Context (Vendor Blog, URL, access date): ...` |
| E | LLM Prior Knowledge | Model memory or generated content without source retrieval. | Lowest | Unsourced generated text. | Low | Must not be cited as fact. |
| E | Personal Notes | Personal observations, draft ideas, or working hypotheses. | Lowest | Notes, brainstorming, unsourced interpretations. | Low | `Interpretation:` or `Open Question:` only. |
| E | Draft Ideas | Early thoughts not yet supported by evidence. | Lowest | Draft claims, unverified graph edges. | Low | `Draft Idea:` only. |

### Evidence Rules

- Level A evidence overrides lower-level evidence when they conflict.
- Level B evidence can support organization, participation, and process facts, but official decisions should still use Level A evidence where possible.
- Level C evidence can explain technical background but should not establish official regulatory status.
- Level D evidence can identify leads for acquisition but should not be used as primary support for canonical facts.
- Level E evidence must never be stored as official fact.

## 8. Knowledge Status Model

Knowledge status describes lifecycle maturity. It is distinct from evidence level.

```text
Missing -> Stub -> Acquired -> Merged -> Reviewed -> Verified -> Maintained -> Archived
```

| State | Meaning | Entry Criteria | Exit Criteria |
|---|---|---|---|
| Missing | Entity or section is known to be absent. | Search or review identifies a gap. | Stub is created or acquisition begins. |
| Stub | Entity exists as a placeholder with minimal metadata. | Canonical home and type are known. | Evidence-backed content is acquired. |
| Acquired | Evidence has been collected and extracted, but not fully integrated. | Source material exists and claims are identified. | Merge into canonical entity is complete. |
| Merged | Knowledge has been integrated into the canonical entity. | Entity note contains updated content and links. | Review evaluates quality. |
| Reviewed | Knowledge quality has been assessed. | Review report, score, or backlog item exists. | Verification resolves material gaps. |
| Verified | Core claims and relationships are supported by sufficient evidence. | Material claims have citations and uncertain claims are separated. | Maintenance cycle begins. |
| Maintained | Entity is current and monitored for change. | Entity is verified and has ownership/review expectations. | New changes require acquisition or review; obsolete entities move to archive. |
| Archived | Entity is no longer active but retained for history. | Entity is superseded, merged, dissolved, rejected, or deprecated. | Reactivation requires explicit review. |

## 9. Knowledge Quality Attributes

Quality attributes may appear in review artifacts, dashboards, or entity metadata. They must be scored on knowledge quality, not writing style.

| Attribute | Meaning |
|---|---|
| Completeness | Degree to which expected sections and required metadata exist for the entity type. |
| Evidence Coverage | Degree to which factual claims and relationships are supported by appropriate evidence. |
| Relationship Coverage | Degree to which important incoming and outgoing graph edges are present or identified as gaps. |
| Review Status | Current review state, including whether gaps, conflicts, or pending items exist. |
| Confidence | Assessment of how reliable the entity's claims are based on evidence quality and ambiguity. |
| Freshness | Assessment of whether the entity is current relative to known dates, amendments, or review cycles. |
| Last Verified | Date when the entity or claim was last checked against evidence. |
| Owner | Person, role, skill, or process responsible for maintaining the entity or review item. |
| Knowledge Source | Primary source or source class supporting the entity or claim. |

## 10. Folder Ontology

Each entity should have a single canonical home. Cross-links are preferred over duplication. A note may reference many folders, but its primary file location must match its primary entity type.

| Entity Type | Canonical Location |
|---|---|
| Regulation | `01 Regulations/` |
| UN GTR | `01 Regulations/` |
| Working Group | `04 Working Groups/` |
| Task Force / IWG | `04 Working Groups/` |
| Organization | `07 Organizations/` |
| Meeting | `08 Meetings/`, or existing body-specific folders where already established |
| Meeting Document | `09 Proposals/` for tracked substantive documents; `12 Attachments/` for source files |
| Proposal | `09 Proposals/` |
| Concept | `05 Concepts/` |
| Timeline Event | `14 Timeline/` |
| Person | No standalone folder until approved; embed in Organization or Meeting notes |
| Evidence Source | `12 Attachments/` for files; `13 Resources/` for registries and source indexes |
| Review Artifact | `11 Review/` |
| Template | `11 Templates/` |
| Research Note | `10 Research Notes/` |
| Knowledge View | `15 Views/` |

## 11. Cross-linking Rules

Wiki-links are graph edges. They must be created deliberately.

### When Wiki-links Should Be Created

Create a wiki-link when:

- The target is a canonical entity.
- The source and target have a meaningful relationship.
- The link supports navigation, evidence tracing, review, or future acquisition.
- The relationship is factual, structural, or explicitly marked as pending/interpretive.

Do not create a wiki-link merely because a word appears in text. Avoid linking every mention.

### Backlinks

Backlinks are expected when:

- The relationship is durable and important to both entities.
- The target entity would be incomplete without knowing the relationship.
- Review identifies a one-way link that should be navigable from both sides.

Backlinks should not be added automatically when evidence is incomplete. They may be recommended in review artifacts.

### Aliases

Aliases represent alternate names, abbreviations, spellings, or historical names for the same canonical entity. Aliases must not be used to merge distinct entities.

Use aliases when:

- A source uses a different but equivalent name.
- An abbreviation is common and unambiguous.
- Historical names should resolve to the same entity.

Do not use aliases when:

- Two entities are related but distinct.
- A name is unsupported, stale, or known to be incorrect.
- The alias would create domain confusion.

### Canonical Names

Canonical names should be stable, human-readable, and specific enough to avoid ambiguity. Prefer the official name where it is concise. Use common short names only when they are unambiguous and operationally dominant.

### Abbreviations

Abbreviations should be aliases, not canonical names, unless the abbreviation is the official or overwhelmingly dominant name. Ambiguous abbreviations require disambiguation in the note title or metadata.

Example pattern:

| Field | Value |
|---|---|
| Canonical Title | `UN Regulation No. 171` or locally approved short title |
| Aliases | `R171`, `UN R171`, `Regulation No. 171` |
| Excluded Aliases | Any stale or unsupported name must not be stored as an alias. |

## 12. Naming Conventions

Names must be consistent, stable, and graph-friendly.

| Entity Type | Naming Rule | Example Pattern |
|---|---|---|
| Regulation | Use short regulatory identifier when it is the Vault convention; include official full name in heading. | `R171` |
| UN GTR | Use concise official instrument name. | `ADS UN GTR` |
| Organization | Use official organization name. | `E-Mobility Europe` |
| Working Group | Use official group name or stable abbreviation if official. | `ADS IWG` |
| Task Force | Use official task force name or stable abbreviation if official. | `ADAS TF` |
| Meeting | Use body and session number. | `GRVA 24th Session` |
| Meeting Document | Use document number or short title; avoid long filenames as note titles when possible. | `Document Number` or `Short Title` |
| Proposal | Use document number plus concise proposal topic when needed. | `Proposal for ...` |
| Concept | Use full concept name; abbreviation may be alias. | `Operational Design Domain` |
| Timeline Event | Use entity plus timeline or dated event name. | `R171 Timeline` |
| Person | Use full name plus disambiguator only if needed. | `Full Name` |
| Evidence Source | Use official document title or document number. | `Document Number` |

Avoid inconsistent naming across notes, aliases, frontmatter, and links. If a canonical title changes, update aliases and incoming links through a controlled merge operation.

## 13. Extensibility

The ontology is extensible but must remain backward compatible whenever possible.

New entity types, relationships, evidence levels, or status values require:

- A clear gap that cannot be solved by existing ontology elements.
- A definition independent of one entity or one document.
- Required metadata.
- Folder or storage rules.
- Relationship rules.
- Review criteria.
- Migration guidance for any affected existing notes.

Backward compatibility should be preserved by adding optional fields before replacing required fields. Deprecated fields should remain readable until a migration is complete.

## 14. Examples

The examples below demonstrate ontology structure. They are not a substitute for evidence in entity notes.

### Example: Regulation Entity

| Field | Value |
|---|---|
| Entity | `R171` |
| Entity Type | Regulation |
| Canonical Home | `01 Regulations/` |
| Required Metadata | `type: regulation`, `status`, `source`, `related`, `created`, `last_updated` |

Example relationships:

| Relationship | Target | Evidence Requirement |
|---|---|---|
| `references` | Another Regulation | Explicit citation in regulation text |
| `discussed_at` | Meeting | Meeting agenda or report |
| `supported_by` | Official Regulation PDF | Source file or official document record |
| `defines` | Concept | Formal definition in text |

### Example: Organization Entity

| Field | Value |
|---|---|
| Entity | `EME` |
| Entity Type | Organization |
| Canonical Home | `07 Organizations/` |
| Required Metadata | `type: organization`, `status`, `source`, `related`, `org_type`, `created`, `last_updated` |

Example relationships:

| Relationship | Target | Evidence Requirement |
|---|---|---|
| `participates_in` | Task Force / IWG | Participant list, official document, or meeting record |
| `submitted_by` | Organization as submitter of Meeting Document | Document cover page or metadata |
| `related_to` | Concept | Use only when no more specific relationship applies |
| `supported_by` | Official website or meeting document | Official source path or captured document |

### Example: Concept Entity

| Field | Value |
|---|---|
| Entity | `Driver Availability` |
| Entity Type | Concept |
| Canonical Home | `05 Concepts/` |
| Required Metadata | `type: concept`, `status`, `source`, `related`, `created`, `last_updated` |

Example relationships:

| Relationship | Target | Evidence Requirement |
|---|---|---|
| `defined_by` equivalent | Use `defines` from source to concept | Prefer source -> concept direction |
| `depends_on` | Related Concept | Explicit technical or procedural dependency |
| `related_to` | Related Concept | Navigational relationship only |
| `supported_by` | Evidence Source | Source material supporting the concept |

### Example: Evidence Source Entity

| Field | Value |
|---|---|
| Entity | Official PDF or Web Source |
| Entity Type | Evidence Source |
| Canonical Home | `12 Attachments/` or `13 Resources/` |
| Required Metadata | `type: evidence_source`, `source_kind`, `authority_level`, `created`, `last_updated` |

Example relationships:

| Relationship | Target | Evidence Requirement |
|---|---|---|
| `documents` | Regulation, Meeting, Proposal, Concept | The source directly records the target |
| `supports` / inverse `supported_by` | Any Entity | The source supports claims in the target entity |
| `references` | Any Entity | The source cites the target |

## 15. Guidance for Claude Skills

All Claude Skills must treat this ontology as the structural specification for the Knowledge OS.

### Acquire Knowledge

- Must determine whether the target belongs to the Knowledge Layer before creating knowledge.
- Must create entities according to this ontology.
- Must not create Views.
- Must create canonical knowledge only.
- Must not invent entity types.
- Must search for existing canonical entities before creating new ones.
- Must classify evidence according to the evidence ontology.
- Must mark unknowns as missing or open questions rather than inventing claims.
- Must never modify Governance.
- Must ignore Automation and Project layers unless the user explicitly requests a non-knowledge task.

### Knowledge Merge

- Must operate only inside the Knowledge Layer.
- Must never merge into Views.
- Must preserve canonical relationships.
- Must avoid duplicate entities.
- Must merge new claims into the correct canonical home.
- Must preserve aliases and update them only when evidence supports the change.
- Must not promote inferred relationships to graph facts.
- Must not merge domain knowledge into Governance, Automation, or Project artifacts.

### Knowledge Review

- Must review only the Knowledge Layer by default.
- May support optional Governance review when explicitly requested.
- May validate whether Views still reference existing canonical entities.
- Must not score Views as canonical knowledge.
- Must ignore Automation and Project layers by default.
- Must evaluate ontology completeness only for Knowledge Layer artifacts.
- Must identify missing relationships.
- Must identify missing evidence, duplicate entities, stale aliases, and incorrect folder placement.
- Must never rewrite ontology definitions during an ordinary review.
- Must recommend ontology changes only through explicit governance backlog items.

### Knowledge Evolution

- Must evolve only the Knowledge Layer by default.
- May regenerate View structures when explicitly requested.
- Must never migrate View content as if it were canonical knowledge.
- May support Governance evolution only through explicit approval and versioned ontology/governance updates.
- Must never modify Automation artifacts unless the user explicitly requests automation-layer migration.
- Must never modify Project artifacts unless the user explicitly requests repository/project maintenance.
- Must classify repository layer before proposing migration actions.
- Must preserve backward compatibility whenever possible.

## 16. Migration Notes

Ontology v1.1 introduced repository layers. Ontology v1.2 introduces Knowledge Views as a presentation/query layer. Existing knowledge remains compatible with the entity ontology introduced in v1.0.

Future compliance tools must first classify each artifact by repository layer before applying ontology rules. This prevents skills, operational prompts, project files, and governance documents from being incorrectly scored as missing or malformed knowledge entities.

Existing compliance reports that counted Automation, Project, Governance, or View files as ontology violations should be treated as pre-v1.2 diagnostics. Future reports should score only the Knowledge Layer unless the user explicitly requests a broader architecture audit.

No existing knowledge facts need to change because of v1.2. The migration is architectural: it separates canonical storage from user-oriented exploration.

Future View generators should build from canonical entities. If a generated View exposes a gap, the fix belongs in canonical knowledge or review backlog, not only in the View.

## 17. Version History

| Version | Change |
|---|---|
| 1.0 | Introduced entity ontology, relationship ontology, evidence ontology, lifecycle states, quality attributes, folder ontology, cross-linking rules, naming conventions, extensibility, examples, and skill guidance. |
| 1.1 | Introduced repository architecture layers. Separated Knowledge from Governance, Automation, and Project artifacts. Defined ontology compliance scope. Updated skill behavior for Acquire, Merge, Review, and Evolution. Improved the compliance model by excluding non-knowledge artifacts from knowledge scoring. |
| 1.2 | Introduced Knowledge Views. Separated canonical storage from user-oriented exploration. Defined Views as a presentation layer rather than a Knowledge Layer. Excluded Views from ontology compliance scoring while allowing view integrity validation. |

## 18. Ontology v1.2 Skill Behavior Summary

| Skill / Output | Behavior Change |
|---|---|
| Acquire | Must classify the target layer first and create canonical knowledge only in the Knowledge Layer. It must not create Views. |
| Merge | Must operate only inside the Knowledge Layer and never merge newly acquired facts into Views. |
| Review | Must review the Knowledge Layer by default, support optional Governance review, and validate Views only for link/reference freshness when requested. |
| Evolution | Must evolve the Knowledge Layer by default, require explicit approval for Governance evolution, and may regenerate View structures only when explicitly requested. |
| Future Compliance Reports | Must classify repository layer first, score only the Knowledge Layer, validate Governance separately, exclude Automation and Project artifacts, and exclude Views from canonical ontology scores. |
| Obsidian | Should use Views for Dataview dashboards, timelines, navigation, and exploration without treating them as sources of truth. |

## Why this ontology matters

This ontology makes the Knowledge OS scalable. It lets acquisition add knowledge without creating duplicates, lets merge preserve canonical graph structure, and lets review evaluate quality against stable rules. Because entity types, relationships, evidence levels, and lifecycle states are explicit, the Vault can grow from a small regulatory notebook into a maintainable knowledge graph without losing trust, provenance, or navigability.

Ontology v1.1 also makes compliance measurement stable. By separating repository architecture from knowledge architecture, it prevents operational files and project infrastructure from polluting knowledge scores. This lets the project pause system expansion when appropriate and focus on using the Knowledge OS for real domain acquisition, review, and maintenance.

Ontology v1.2 adds an exploration layer. Future Claude Skills and Obsidian workflows should use Knowledge Views as lightweight, regenerable entry points into canonical knowledge. Views should help users ask cross-entity questions, browse timelines, compare regulations, and navigate meetings without duplicating facts or weakening the single-source-of-truth model.
