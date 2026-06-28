# Knowledge Review — Skill README

## What This Skill Does

`knowledge_review` is the Quality Control engine of the UNECE Knowledge OS. It audits the Vault after knowledge has been acquired or merged.

It evaluates:

- Completeness
- Evidence quality
- Relationship coverage
- Timeline coverage
- Cross references
- Verification status
- Duplicate candidates

It produces review artifacts in `11 Review/`.

## What This Skill Does Not Do

This skill does not perform research, fetch sources, create new knowledge notes, modify existing knowledge notes, or merge evidence. It only evaluates what is already in the Vault.

If the review finds missing knowledge, use:

- `acquire_knowledge` to collect or create knowledge
- `knowledge-merge` to merge verified evidence
- `knowledge_review` to audit the result

## Common Uses

- `Review R171`
- `Review all Regulations`
- `Review Organizations`
- `Review entire UNECE Vault`
- `Create a review dashboard`
- `Add review findings to the Knowledge Backlog`

## Review Outputs

| File | Purpose |
|---|---|
| `11 Review/[Topic] Review.md` | Review report for a note, folder, domain, or Vault scope |
| `11 Review/Dashboard.md` | Quality dashboard and dated coverage snapshots |
| `11 Review/Knowledge Backlog.md` | Prioritized queue of knowledge improvements |
| `11 Review/Pending/*.md` | Optional evidence-pending review items for claims or relationships |

## Skill Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow specification |
| `README.md` | Quick reference |
| `examples.md` | Worked review examples |
| `scoring.md` | Scoring rubric |
| `templates/review_report.md` | Review report template |
| `templates/dashboard.md` | Dashboard template |
| `templates/backlog.md` | Knowledge backlog template |

## Core Principle

The Vault is the primary source of truth. Review never upgrades uncertainty into fact. Missing evidence is marked `Needs Verification`.
