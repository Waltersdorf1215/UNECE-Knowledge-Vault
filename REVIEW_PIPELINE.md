---
type: meta
status: active
tags: [review, maintenance, knowledge-quality, pipeline]
related: [IMPORT_PIPELINE, KNOWLEDGE_RULES, SCHEMA, CLAUDE, CHANGELOG]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# REVIEW_PIPELINE — Monthly Knowledge Maintenance Workflow

This document defines how Claude periodically reviews and improves the UNECE Knowledge OS. Run this pipeline at least once per month, or after any large batch of imports.

---

## When to Run

- Monthly scheduled review
- After importing 3 or more documents in one session
- After a GRVA or WP.29 session produces major outcomes
- When the graph feels fragmented or inconsistent

---

## Stage 1 — Detect Duplicate Entities

**Goal:** Find notes that cover the same entity under different names or locations.

**Actions:**
1. Search for notes with overlapping titles (e.g., `DSSAD.md` in both `04 Working Groups/` and `05 Concepts/`)
2. Search for notes with the same `aliases` field
3. Check whether any concept note is essentially a redirect to another note
4. Identify cases where the same working group, regulation, or concept has two notes

**Resolution:**
- Keep the richer note; update the other to redirect via `[[canonical note name]]`
- Add `aliases` to the canonical note
- Remove the duplicate once all incoming links are redirected

**Known candidates to check:**
- `05 Concepts/DCAS.md` vs `04 Working Groups/DCAS.md` — same acronym, different entities (concept vs. working group)
- `07 Organizations/GRVA.md` vs `03 GRVA/GRVA.md` — two notes for same body
- `07 Organizations/WP.29.md` vs `02 WP29/WP29.md` — two notes for same body
- `05 Concepts/DSSAD.md` vs `04 Working Groups/DSSAD.md` — concept and working group share a name

---

## Stage 2 — Detect Orphan Notes

**Goal:** Find notes with no incoming wiki links (invisible in the graph).

**Actions:**
1. List all notes in the vault
2. For each note, check whether any other note links to it
3. Flag notes with zero incoming links

**Resolution:**
- Identify why the note is orphaned (new entity, not yet linked)
- Add links from at least one related note
- If truly unused: move to `99 Archive/`

**Priority orphan candidates:** `08 Meetings/`, `09 Proposals/` (empty folders)

---

## Stage 3 — Detect Broken Wiki Links

**Goal:** Find `[[links]]` that point to notes that do not exist.

**Actions:**
1. Grep all `.md` files for `[[...]]` patterns
2. For each link target, verify a file with that name exists in the vault
3. Flag broken links

**Resolution:**
- If the target should exist: create a placeholder note
- If it was a rename: update the link to the new name
- If it was in error: remove the link

---

## Stage 4 — Detect Inconsistent Metadata

**Goal:** Ensure all notes follow the YAML schema defined in SCHEMA.md.

**Actions:**
1. Check every note for presence of required YAML fields: `type`, `status`, `tags`, `related`, `source`, `last_updated`, `created`
2. Flag notes missing any required field
3. Flag notes where `type` value does not match the allowed values in SCHEMA.md
4. Flag notes where `status` is still `placeholder` but contains substantive content (should be upgraded to `draft` or `active`)
5. Flag notes where `status` is `active` but `source` is empty or `source_pending`

**Resolution:**
- Add missing fields with appropriate values
- Upgrade `placeholder` status where content has been added
- Flag unresolved `source_pending` entries for follow-up

---

## Stage 5 — Detect Missing Sources

**Goal:** Ensure every factual claim is traceable to a source.

**Actions:**
1. Search for `[VERIFY]` or `source_pending` tags in note bodies
2. List all notes where `source` field is empty or `source_pending`
3. Flag factual paragraphs (unmarked by *Interpretation:* or *Insight:*) that lack an inline citation

**Resolution:**
- For each unverified fact, either locate the source or label as `[VERIFY]`
- Update `source` field when source is confirmed
- Move from `source_pending` to actual document reference

---

## Stage 6 — Detect Outdated Timeline Entries

**Goal:** Ensure timeline notes in `14 Timeline/` are current.

**Actions:**
1. Review each timeline note (`ADS Timeline.md`, `GRVA Timeline.md`, etc.)
2. Check whether recent sessions, adoptions, or milestones are captured
3. Compare against `CHANGELOG.md` — every import should reflect in the timeline

**Resolution:**
- Add missing milestone entries with proper dates and document references
- Mark superseded entries as outdated with a note

---

## Stage 7 — Detect Fragmented Knowledge

**Goal:** Find concepts or facts that appear in multiple notes but haven't been consolidated.

**Actions:**
1. Search for repeated inline definitions of the same term across notes
2. Find notes that contain long explanatory paragraphs about concepts that already have a dedicated concept note
3. Find meeting notes that re-explain regulations already documented in regulation notes

**Resolution:**
- Replace repeated inline content with a wiki link to the canonical note
- Add missing links; remove duplicated prose

---

## Stage 8 — Merge Duplicated Knowledge

**Goal:** Consolidate any remaining duplicate content.

**Actions:**
1. For each duplicate identified in Stages 1 and 7:
   - Compare both notes
   - Select the canonical note (richer, better sourced, more linked)
   - Merge unique content from the secondary note into the canonical
   - Update the secondary note to redirect
2. Update all incoming links to point to canonical note

---

## Stage 9 — Refactor Note Structure

**Goal:** Improve notes that have grown unwieldy or diverged from the templates.

**Actions:**
1. Identify notes longer than ~3 pages (may need splitting)
2. Identify notes that don't follow their template structure
3. Check that section headings are consistent across notes of the same type

**Resolution:**
- Split overly broad notes into focused atomic notes
- Refactor structure to match template
- Do not lose content in the process

---

## Stage 10 — Produce Review Summary

After completing the above stages, write a brief summary in `CHANGELOG.md`:

```
## Review — YYYY-MM-DD

### Issues Found
- X orphan notes
- Y broken links
- Z notes with missing sources
- N status inconsistencies

### Actions Taken
- Fixed: ...
- Deferred: ...

### Notes Still Requiring Attention
- [ ] ...
```

---

## Checklist

- [ ] Duplicate entities checked
- [ ] Orphan notes identified and resolved
- [ ] Broken wiki links found and fixed
- [ ] Metadata consistency verified
- [ ] Sources reviewed
- [ ] Timelines updated
- [ ] Fragmented knowledge consolidated
- [ ] Review summary written in CHANGELOG.md
