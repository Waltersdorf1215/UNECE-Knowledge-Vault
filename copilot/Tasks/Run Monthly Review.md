# Task: Run Monthly Review

**Type:** One-off task (intended to be run monthly)
**Output:** Review summary in CHANGELOG.md + resolved issues in vault

---

## Instructions for Claude

You are running the monthly knowledge quality review for the UNECE Knowledge OS.

**Read `REVIEW_PIPELINE.md` before starting.** That document defines the full 10-stage review process. This task file is the execution checklist.

### Checklist

Run each stage and record findings below.

#### Stage 1 — Duplicate Entities
- [ ] Searched for notes covering the same entity under different names
- [ ] Checked known duplicates: `07 Organizations/GRVA.md` vs `03 GRVA/GRVA.md`, `07 Organizations/WP.29.md` vs `02 WP29/WP29.md`
- Findings: ___

#### Stage 2 — Orphan Notes
- [ ] Identified notes with no incoming wiki links
- [ ] Resolved or flagged for archiving
- Findings: ___

#### Stage 3 — Broken Wiki Links
- [ ] Scanned for `[[links]]` pointing to non-existent files
- [ ] Fixed or flagged each broken link
- Findings: ___

#### Stage 4 — Inconsistent Metadata
- [ ] Checked all notes for required YAML fields
- [ ] Upgraded `placeholder` notes where content has been added
- [ ] Flagged `active` notes with empty `source` fields
- Findings: ___

#### Stage 5 — Missing Sources
- [ ] Scanned for `[VERIFY]` and `source_pending` tags
- [ ] Found any unlabeled factual claims without citations
- Findings: ___

#### Stage 6 — Outdated Timelines
- [ ] Reviewed `14 Timeline/` notes
- [ ] Compared against CHANGELOG.md for missing milestones
- Findings: ___

#### Stage 7 — Fragmented Knowledge
- [ ] Found repeated inline definitions of concepts that have dedicated notes
- [ ] Replaced duplicated prose with wiki links where appropriate
- Findings: ___

#### Stage 8 — Merge Duplicates
- [ ] Acted on any duplicates found in Stage 1
- [ ] Merged unique content into canonical note
- Findings: ___

#### Stage 9 — Refactor
- [ ] Identified notes that have grown too broad or diverged from templates
- [ ] Proposed splits or restructuring (do not execute without user approval)
- Findings: ___

#### Stage 10 — Summary
Write a review summary entry in `CHANGELOG.md`:

```
## Review — YYYY-MM-DD

### Issues Found
- X orphan notes
- Y broken links
- Z missing source citations
- N status inconsistencies

### Actions Taken
- Fixed: ...
- Deferred: ...

### Notes Still Requiring Attention
- [ ] ...
```

---

## Definition of Done

- [ ] All 10 stages completed
- [ ] Findings documented per stage
- [ ] Review summary written in CHANGELOG.md
- [ ] ROADMAP.md updated if new follow-up items emerged
