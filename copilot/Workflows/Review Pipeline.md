# Workflow: Review Pipeline

**Type:** Multi-step SOP
**Vault Reference:** `REVIEW_PIPELINE.md` (authoritative definition)
**Cadence:** Monthly, or after any batch of 3+ imports
**Duration:** One to two sessions
**Output:** Review summary in CHANGELOG.md + resolved issues across the vault

---

## Purpose

This workflow guides Claude through the 10-stage monthly knowledge quality review for the UNECE Knowledge OS. It sequences the review from `REVIEW_PIPELINE.md` with explicit decision points and output criteria.

---

## Pre-Flight Checks

Before starting, confirm:
- [ ] `REVIEW_PIPELINE.md` read this session
- [ ] `CLAUDE.md` read this session
- [ ] `KNOWLEDGE_RULES.md` Rule Zero recalled
- [ ] `10 Research Notes/Inference Drift Report.md` checked for any unresolved items

---

## Stage 1 — Duplicate Entities
*Uses: `Tasks/Fix Inference Drift.md` if merge is needed*

Known candidates:
- `07 Organizations/GRVA.md` vs `03 GRVA/GRVA.md`
- `07 Organizations/WP.29.md` vs `02 WP29/WP29.md`

Action: For each duplicate pair, compare content. Decide: which is canonical? Merge into canonical. Update incoming links. Update secondary to redirect.

Record findings: ___

---

## Stage 2 — Orphan Notes

Action: Search for notes in `01 Regulations/` through `09 Proposals/` that have no incoming wiki links. For each orphan: either add a link from a related note, or move to `99 Archive/` if obsolete.

Record findings: ___

---

## Stage 3 — Broken Wiki Links

Action: Grep for `[[...]]` patterns across all non-template notes. For each link target, confirm the file exists. Fix or flag each broken link.

Bash command to assist:
```bash
grep -roh '\[\[.*\]\]' --include="*.md" . | sort -u
```

Record findings: ___

---

## Stage 4 — Inconsistent Metadata

Check all notes for:
- Missing required YAML fields (`type`, `status`, `tags`, `related`, `source`, `last_updated`, `created`)
- `status: placeholder` notes that now have substantive content → upgrade to `draft`
- `status: active` notes with `source: ""` or `source: source_pending` → flag for sourcing

Record findings: ___

---

## Stage 5 — Missing Sources and Unverified Claims

Action: Search for `[VERIFY]`, `source_pending`, and unlabeled factual paragraphs.

Prioritize:
- Regulation notes with unsourced factual claims (highest risk of drift)
- Concept notes with unsourced definitions

For each: either source it or label `*Interpretation:*`.

Record findings: ___

---

## Stage 6 — Timeline Updates
*Uses: `Tasks/Update Timeline.md`*

Action: Review each `14 Timeline/` note. Compare confirmed milestones against CHANGELOG.md. Add any missing confirmed entries. Move any speculative entries to Pending.

Record findings: ___

---

## Stage 7 — Fragmented Knowledge

Action: Find concepts or facts that appear inline in multiple notes but have a dedicated concept note. Replace duplicated prose with wiki links.

Record findings: ___

---

## Stage 8 — Merge Duplicates

Action on Stage 1 findings: execute any merges identified. Update all incoming links. Verify the canonical note is complete.

Record findings: ___

---

## Stage 9 — Refactor Candidates

Action: Identify notes that have grown broad or diverged from their template. List candidates. Do not refactor without user approval — propose instead.

Record findings: ___

---

## Stage 10 — Review Summary

Write a review entry in `CHANGELOG.md`:

```
## Review — YYYY-MM-DD

### Issues Found
- X duplicate entity pairs
- Y orphan notes
- Z broken wiki links
- N missing source citations
- M status inconsistencies

### Actions Taken
- Fixed: ...
- Merged: ...
- Proposed for user review: ...

### Deferred / Pending User Approval
- [ ] ...

### Updated ROADMAP
- Added: ...
```

---

## Exit Criteria

- [ ] All 10 stages documented
- [ ] 🔴 issues resolved or escalated
- [ ] CHANGELOG.md entry written
- [ ] ROADMAP.md updated with any new follow-up items
