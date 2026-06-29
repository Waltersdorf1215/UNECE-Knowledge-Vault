---
type: governance
status: active
tags: [governance, extraction, meetings, evidence, knowledge-objects]
related: [MEETING_KNOWLEDGE_MODEL, KNOWLEDGE_ONTOLOGY]
source: internal governance specification
created: 2026-06-29
last_updated: 2026-06-29
---

# Knowledge Extraction Specification

## Purpose

Knowledge Extraction transforms meeting evidence into structured knowledge objects.

This document is implementation-neutral. It is not a Skill. It defines the specification that future Skills, scripts, or agents must implement when converting meeting material into evidence-backed extraction outputs.

Extraction must preserve the distinction between facts, discussion, decisions, interpretations, unknowns, acquisition candidates, and merge candidates.

## Input Types

Supported inputs:

- Meeting invitation
- Agenda
- Presentation
- Meeting notes
- Minutes
- Follow-up email
- PDF
- DOCX
- Screenshot
- Pasted text

Inputs may be private, public, official, informal, or unknown. Source authority must be classified before extraction output is trusted.

## Extraction Pipeline

```text
Input
  |
  v
Source Classification
  |
  v
Evidence Parsing
  |
  v
Entity Detection
  |
  v
Object Classification
  |
  v
Decision / Discussion Separation
  |
  v
Action Item Extraction
  |
  v
Timeline Extraction
  |
  v
Knowledge Gap Detection
  |
  v
Merge Candidate Detection
  |
  v
Output Package
```

## Source Classification Rules

Classify each input as one of:

- `invitation`
- `agenda`
- `meeting_note`
- `minutes`
- `presentation`
- `follow_up_email`
- `attachment`
- `unknown`

Classification should use source metadata, filename, content structure, user context, and explicit labels. If source type is uncertain, use `unknown` and mark extraction outputs `needs_review`.

## Evidence Parsing

Parsing extracts source-local evidence while preserving provenance.

For each parsed item, record:

- Source document or source description
- Source type
- Source section, page, slide, paragraph, timestamp, or screenshot area when available
- Extracted text or summarized evidence
- Privacy or sensitivity flags
- Confidence
- Verification status

Do not normalize away uncertainty. Ambiguous source material remains ambiguous.

## Entity Detection

Detect references to:

- Regulations
- UN GTRs
- Organizations
- Working groups
- Task forces
- Initiatives
- Proposals
- Concepts
- Persons
- Timeline references

Detected entities must be checked against the Vault when possible.

Outcomes:

| Outcome | Meaning |
| --- | --- |
| `matched_existing_entity` | Entity appears to exist in the Vault. |
| `possible_existing_entity` | Candidate match exists but confidence is not high. |
| `missing_entity` | No clear Vault entity found. |
| `unknown_entity` | Mention is too ambiguous to classify. |

Missing entities should become acquisition candidates, not automatically created notes.

## Object Classification

Classify extracted content into the Meeting Knowledge Objects defined in `Governance/MEETING_KNOWLEDGE_MODEL.md`:

- `discussion_point`
- `decision`
- `action_item`
- `deliverable`
- `open_question`
- `issue`
- `proposal`
- `position`
- `timeline_event`
- `regulation_reference`
- `concept_reference`
- `organization_reference`
- `working_group_reference`
- `acquisition_candidate`
- `merge_candidate`

If content does not fit a known object type, classify it as `needs_review` rather than inventing a new object type.

## Evidence Rules

Every extracted object must include:

- Source document
- Source section, page, slide, paragraph, timestamp, or screenshot context when available
- Confidence
- Verification status

If the source is unclear, mark `verification_status: needs_review`.

Recommended verification statuses:

| Status | Meaning |
| --- | --- |
| `verified_from_source` | Directly supported by the input source. |
| `partially_supported` | Source supports part of the object but not all fields. |
| `needs_review` | Source or interpretation is unclear. |
| `conflict` | Source conflicts with another Vault or source claim. |

## Decision Extraction Rules

A decision may only be extracted if explicitly supported.

Do not infer decisions from:

- Discussion
- Agenda topics
- Intentions
- Future plans
- Suggestions
- Drafts
- Implied agreement

Decision indicators may include explicit language such as approved, agreed, decided, adopted, rejected, endorsed, confirmed, assigned, or equivalent source wording.

When in doubt, classify as `discussion_point`, `proposal`, or `open_question`, not `decision`.

## Action Item Extraction Rules

Only extract action items if there is an explicit action, request, assignment, or agreed follow-up.

An action item should include:

- Action
- Owner
- Due date
- Status
- Source
- Related entities
- Confidence

Unknown owner or due date must be marked `unknown`. Do not invent ownership from context.

## Timeline Extraction Rules

Extract explicit:

- Dates
- Months
- Date ranges
- Meeting dates
- Deadlines
- Expected future milestones
- Adoption, endorsement, publication, or entry-into-force references

Relative dates must remain relative unless the anchor date is clear.

Examples:

| Source Phrase | Extraction |
| --- | --- |
| `29 June 2026` | `date_or_date_range: 2026-06-29` |
| `September 2026 GRVA session` | `date_or_date_range: 2026-09`, with context preserved |
| `next meeting` | Relative milestone; anchor required before conversion |

Do not create timeline events from vague sequencing unless the event is meaningful and source-supported.

## Knowledge Gap Detection Rules

Check whether extracted entities already exist in the Vault.

Create acquisition candidates when:

- An entity is mentioned but not found in the Vault.
- A concept is unclear.
- A regulation is referenced but not linked.
- An organization is unknown.
- An initiative is not yet acquired.
- Evidence is missing.

Do not automatically create canonical notes.

## Merge Candidate Detection Rules

If an entity already exists, identify possible canonical updates.

Merge candidates should include:

- Target note
- Proposed update
- Reason
- Source
- Confidence
- Risk
- Whether review is required

Do not apply merge candidates automatically. Output candidates only.

## Output Files

Knowledge Extraction should generate the following files when supported by the workflow stage:

```text
knowledge-extraction.md
knowledge-gap-analysis.md
merge-suggestions.md
timeline-events.md
review-report.md
```

These files belong inside the relevant meeting folder:

```text
08 Meetings/<Organizer>/<Working Group or General>/<YYYY-MM>/<YYYY-MM-DD Meeting Title>/
```

## Output Quality Rules

Outputs must distinguish:

- Facts
- Discussion
- Decisions
- Interpretations
- Unknowns

Each output should preserve source traceability and avoid unsupported synthesis.

Use `unknown` for missing fields. Use `needs_review` for uncertain classification, ambiguous evidence, or medium/low confidence entity matching.

## Interaction with Skills

| Capability | Responsibility |
| --- | --- |
| Meeting Intake | Creates meeting folders and stores meeting artifacts. |
| Knowledge Extraction | Extracts structured knowledge objects from meeting artifacts. |
| Acquire Knowledge | Acquires missing canonical entities. |
| Knowledge Merge | Applies approved merge candidates to canonical notes. |
| Knowledge Review | Reviews completeness, correctness, evidence, and gaps. |
| Knowledge Evolution | Migrates structures if Governance changes. |

Knowledge Extraction is a specification boundary. A future Skill may implement it, but the extraction rules must remain governed by this document and `Governance/MEETING_KNOWLEDGE_MODEL.md`.

## Safety Rules

- Never invent facts.
- Never convert discussion into decision.
- Never update canonical notes directly.
- Never expose private meeting links in public summaries.
- Never infer attendees, owners, deadlines, or regulatory outcomes.
- Prefer unknown over unsupported inference.
- Treat private or non-public material conservatively.
- Route missing canonical entities to Acquire Knowledge.
- Route existing-note updates to Knowledge Merge.
