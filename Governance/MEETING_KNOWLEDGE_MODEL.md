---
type: governance
status: active
tags: [governance, meetings, knowledge-model, extraction, evidence]
related: [KNOWLEDGE_ONTOLOGY, KNOWLEDGE_EXTRACTION_SPEC]
source: internal governance specification
created: 2026-06-29
last_updated: 2026-06-29
---

# Meeting Knowledge Model

## Purpose

Meeting knowledge needs its own model because a meeting is not just a note. A meeting is a knowledge event that may produce evidence, decisions, action items, deliverables, timeline events, knowledge gaps, merge candidates, and acquisition candidates.

Meeting artifacts must preserve the lifecycle context of the meeting while keeping canonical regulatory knowledge separate. Meeting-derived material can support future acquisition or merge work, but it must not create canonical facts directly.

## Meeting Lifecycle

Use conservative lifecycle states:

| State | Meaning |
| --- | --- |
| `invited` | Invitation exists; core metadata may be incomplete. |
| `planned` | Meeting metadata is sufficiently known and meeting has not occurred. |
| `agenda_available` | Agenda source exists. |
| `background_prepared` | Pre-meeting context has been prepared from existing Vault knowledge. |
| `held` | Meeting occurred, but notes or minutes may not be available. |
| `notes_available` | Informal meeting notes exist. |
| `minutes_available` | Official or circulated minutes exist. |
| `knowledge_extracted` | Structured knowledge objects have been extracted from meeting artifacts. |
| `merge_reviewed` | Merge candidates have been reviewed. |
| `knowledge_merged` | Approved candidates have been merged into canonical notes. |
| `closed` | Meeting lifecycle is complete. |

Do not advance a meeting state by inference alone.

## Meeting Metadata

Standard meeting metadata:

| Field | Meaning |
| --- | --- |
| `title` | Human-readable meeting title. |
| `organizer` | Organization or body responsible for the meeting. |
| `working_group` | Relevant working group, task force, or internal group. |
| `parent_body` | Parent organization or institutional body. |
| `date` | Scheduled meeting date. |
| `month` | Scheduled meeting month in `YYYY-MM` format. |
| `time` | Scheduled time or time range. |
| `timezone` | Timezone explicitly stated or derived from source. |
| `location` | Physical or online location summary. |
| `format` | Online, in-person, hybrid, or unknown. |
| `source_type` | Source evidence type. |
| `visibility` | Public, private, internal, restricted, or unknown. |
| `sensitivity` | Whether sensitive meeting information exists. |
| `status` | Current lifecycle state. |

Unknown fields must be marked `unknown`.

## Meeting Evidence Types

| Evidence Type | Purpose | Authority Level | Expected Output | Limitations |
| --- | --- | --- | --- | --- |
| `invitation` | Establish planned meeting metadata and stated purpose. | Low to medium | Pre-meeting record and source inventory. | Does not prove discussion, decisions, attendance, or outcomes. |
| `agenda` | Establish planned discussion topics. | Medium | Agenda artifact and preparation questions. | Agenda items are not decisions. |
| `presentation` | Capture presented topics, proposals, or supporting material. | Medium, unless official status is clear | Source summary and extraction candidates. | Slide claims may need verification. |
| `meeting_note` | Capture informal notes or participant observations. | Low to medium | Meeting notes and candidate objects. | May be incomplete or subjective. |
| `minutes` | Capture official or circulated record of discussion, decisions, and actions. | Medium to high depending on issuer | Minutes, decisions, actions, merge candidates. | Must still distinguish discussion from decisions. |
| `follow_up_email` | Capture post-meeting updates, assignments, attachments, or next steps. | Medium | Follow-up artifact, action candidates, source updates. | Decisions only count if explicitly stated. |
| `recording` | Preserve audio/video evidence. | Medium | Source inventory and possible transcript-derived objects. | Requires careful privacy and transcript validation. |
| `attachment` | Preserve supporting file evidence. | Depends on attachment | Source inventory and relevant artifact updates. | Type and authority must be classified. |
| `external_link` | Reference external meeting material. | Depends on source | Source inventory and verification target. | Link rot and access restrictions are likely. |

## Meeting Knowledge Objects

### `discussion_point`

Meaning: A topic discussed or planned for discussion.

Required fields: `topic`, `source`, `evidence_reference`, `confidence`, `review_status`.

Optional fields: `related_entities`, `speaker`, `summary`.

Evidence requirement: Explicit agenda, minutes, notes, or source text.

Example:

```yaml
object_type: discussion_point
topic: Review member survey results
source: Outlook invitation screenshot / email invitation
confidence: medium
review_status: needs_review
```

### `decision`

Meaning: An explicitly agreed or recorded decision.

Required fields: `decision_text`, `date`, `meeting`, `source`, `affected_entities`, `confidence`, `review_status`.

Optional fields: `decision_owner`, `implementation_timing`, `conditions`.

Evidence requirement: Explicit decision language in minutes, official record, or follow-up.

Example:

```yaml
object_type: decision
decision_text: unknown
source: unknown
confidence: unknown
review_status: needs_review
```

### `action_item`

Meaning: An explicit task, assignment, request, or agreed follow-up.

Required fields: `action`, `owner`, `due_date`, `status`, `source`, `related_entities`, `confidence`.

Optional fields: `priority`, `deliverable`, `notes`.

Evidence requirement: Explicit action or assignment in source material.

Example:

```yaml
object_type: action_item
action: Circulate updated draft
owner: unknown
due_date: unknown
status: open
source: follow_up_email
confidence: medium
```

### `deliverable`

Meaning: A tangible expected output from the meeting process.

Required fields: `deliverable`, `owner`, `expected_timing`, `related_entities`, `source`, `confidence`.

Optional fields: `format`, `target_body`, `review_status`.

Evidence requirement: Explicit source reference to a deliverable or output.

Example:

```yaml
object_type: deliverable
deliverable: Working group work plan
owner: unknown
expected_timing: unknown
source: minutes
confidence: medium
```

### `open_question`

Meaning: An unresolved question requiring follow-up, evidence, or clarification.

Required fields: `question`, `source`, `related_entities`, `review_status`.

Optional fields: `owner`, `due_date`, `resolution_path`.

Evidence requirement: May come from explicit source text or from documented missing metadata.

Example:

```yaml
object_type: open_question
question: Will meeting minutes be circulated?
source: invitation
review_status: open
```

### `issue`

Meaning: A problem, concern, conflict, blocker, or risk identified in meeting material.

Required fields: `issue`, `source`, `affected_entities`, `confidence`, `review_status`.

Optional fields: `severity`, `owner`, `proposed_resolution`.

Evidence requirement: Explicit source mention.

Example:

```yaml
object_type: issue
issue: Scheduling clash with another meeting
source: invitation
confidence: high
review_status: recorded
```

### `proposal`

Meaning: A proposed change, document, regulatory direction, or work item.

Required fields: `proposal`, `source`, `proposed_by`, `affected_entities`, `confidence`, `review_status`.

Optional fields: `document_reference`, `target_meeting`, `status`.

Evidence requirement: Explicit proposal language or document reference.

Example:

```yaml
object_type: proposal
proposal: unknown
proposed_by: unknown
source: presentation
confidence: unknown
review_status: needs_review
```

### `position`

Meaning: A stated view or stance by an organization, group, or participant.

Required fields: `position_text`, `holder`, `source`, `related_entities`, `confidence`.

Optional fields: `scope`, `date`, `review_status`.

Evidence requirement: Explicit attribution in source material.

Example:

```yaml
object_type: position
holder: E-Mobility Europe
position_text: unknown
source: minutes
confidence: unknown
```

### `timeline_event`

Meaning: A dated or date-range event relevant to the knowledge graph.

Required fields: `date_or_date_range`, `event`, `source`, `affected_entities`, `confidence`, `review_status`.

Optional fields: `event_type`, `future_or_past`, `notes`.

Evidence requirement: Explicit date, month, range, or milestone.

Example:

```yaml
object_type: timeline_event
date_or_date_range: 2026-06-29
event: EME WG SDV/AVS/AI kick-off meeting
source: invitation
confidence: high
review_status: needs_review
```

### Reference Objects

Reference objects link meeting material to existing or candidate canonical entities.

| Object | Meaning | Required Fields | Evidence Requirement | Example |
| --- | --- | --- | --- | --- |
| `regulation_reference` | A regulation mentioned or implicated. | `entity`, `source`, `context`, `confidence` | Explicit mention or clearly stated source context. | `R171` |
| `concept_reference` | A concept mentioned or implicated. | `entity`, `source`, `context`, `confidence` | Explicit mention or clearly stated source context. | `Software-Defined Vehicle` |
| `organization_reference` | An organization mentioned. | `entity`, `source`, `role`, `confidence` | Explicit mention. | `E-Mobility Europe` |
| `working_group_reference` | A working group or task force mentioned. | `entity`, `source`, `role`, `confidence` | Explicit mention. | `WG SDV-AVS-AI` |

### `acquisition_candidate`

Meaning: A missing canonical entity or context item that may require Acquire Knowledge.

Required fields: `candidate`, `candidate_type`, `reason`, `source`, `confidence`, `requires_research`.

Optional fields: `suggested_folder`, `related_entities`.

Evidence requirement: Entity or topic appears in source material but is missing or unclear in the Vault.

Example:

```yaml
object_type: acquisition_candidate
candidate: Software-Defined Vehicle
candidate_type: concept
reason: Mentioned in meeting invitation but no canonical note found
source: invitation
confidence: medium
requires_research: true
```

### `merge_candidate`

Meaning: A proposed update to an existing canonical note.

Required fields: `target_note`, `proposed_update`, `reason`, `source`, `confidence`, `risk`, `requires_review`.

Optional fields: `affected_section`, `evidence_reference`, `priority`.

Evidence requirement: Evidence-backed update candidate from meeting material.

Example:

```yaml
object_type: merge_candidate
target_note: 07 Organizations/E-Mobility Europe.md
proposed_update: Add confirmed WG SDV/AVS/AI activity after source review
reason: Meeting source indicates new working group activity
source: invitation
confidence: medium
risk: medium
requires_review: true
```

## Decision Model

A decision differs from discussion because it records an explicit agreement, conclusion, approval, rejection, or adopted course of action.

Rules:

- A decision must be explicitly stated.
- Discussion is not a decision.
- Intentions are not decisions.
- Future plans are not decisions unless explicitly agreed.
- Agenda items are not decisions.
- Draft language is not a decision unless adopted or approved.

## Action Item Model

Required fields:

- `action`
- `owner`
- `due_date`
- `status`
- `source`
- `related_entities`
- `confidence`

Unknown owner or due date must be marked `unknown`.

## Deliverable Model

Required fields:

- `deliverable`
- `owner`
- `expected_timing`
- `related_entities`
- `source`
- `confidence`

Unknown owner or expected timing must be marked `unknown`.

## Timeline Event Model

Required fields:

- `date_or_date_range`
- `event`
- `source`
- `affected_entities`
- `confidence`
- `review_status`

Dates may be exact, month-level, range-based, or relative. Relative dates must preserve their anchor context.

## Knowledge Gap Model

Meeting material creates a knowledge gap when:

- An entity is mentioned but not found in the Vault.
- A concept is unclear.
- A regulation is referenced but not linked.
- An organization is unknown.
- An initiative is not yet acquired.
- Evidence is missing or incomplete.

Knowledge gaps should produce acquisition candidates or review items, not invented facts.

## Merge Candidate Model

Merge candidates propose canonical updates without applying them.

Required fields:

- `target_note`
- `proposed_update`
- `reason`
- `source`
- `confidence`
- `risk`
- `requires_review`

Merge candidates must be reviewed and then applied through Knowledge Merge only when approved.

## Meeting Folder Output

Expected meeting package structure:

```text
08 Meetings/
└── <Organizer>/
    └── <Working Group or General>/
        └── <YYYY-MM>/
            └── <YYYY-MM-DD Meeting Title>/
                ├── pre-meeting-record.md
                ├── agenda.md
                ├── meeting-notes.md
                ├── minutes.md
                ├── decisions.md
                ├── action-items.md
                ├── knowledge-extraction.md
                ├── knowledge-gap-analysis.md
                ├── merge-suggestions.md
                ├── timeline-events.md
                ├── source-materials.md
                └── review-report.md
```

Create only files supported by available source material or workflow stage.

## Privacy and Sensitivity

Meeting material may contain private Teams links, meeting IDs, passcodes, personal email addresses, attendee names, internal notes, and non-public materials.

Rules:

- Do not expose private Teams links in public summaries.
- Do not commit private links, meeting IDs, passcodes, or personal attendee details to public repositories unless explicitly approved.
- Mark private or non-public artifacts with `sensitive: true`.
- Prefer source summaries over raw private invite text.
- Preserve enough provenance to support review without exposing unnecessary private data.
- Treat internal notes as private unless the user explicitly marks them public.

## Relationship with Existing Ontology

This specification depends on `Governance/KNOWLEDGE_ONTOLOGY.md`.

Meeting objects are not automatically canonical facts. They are structured, evidence-backed objects that can produce candidates for Acquire Knowledge, Knowledge Merge, Knowledge Review, or timeline updates.

Canonical facts must still live in canonical Knowledge Layer entities. Meeting-derived objects may support those facts only after review and merge.
