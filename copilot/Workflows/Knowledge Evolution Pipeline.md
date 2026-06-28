# Workflow: Knowledge Evolution Pipeline

**Type:** Multi-step SOP
**Vault Reference:** No single document — spans IMPORT_PIPELINE.md, REVIEW_PIPELINE.md, ROADMAP.md
**Cadence:** Per regulatory cycle (GRVA session cycle, WP.29 session cycle)
**Duration:** Multiple sessions
**Output:** Vault that tracks a regulatory development from proposal to adoption

---

## Purpose

The UNECE regulatory process is iterative. A regulation evolves over many sessions:

```
Informal document → Working document → Draft text →
GRVA recommendation → WP.29 adoption → Entry into force
```

This workflow maintains a coherent knowledge base across that full lifecycle — ensuring that each new document at each stage updates the same set of notes progressively, rather than creating parallel, fragmented summaries.

---

## When to Use This Workflow

Use this workflow when tracking a specific regulatory instrument across multiple sessions. Examples:
- Following the ADS UN GTR from IWG drafting through WP.29 adoption
- Tracking R171 Supplement 2 from ADAS TF proposal through GRVA adoption
- Following a new IWG from establishment through first deliverables

---

## Lifecycle Stages

### Stage A — Instrument Registration

When a new regulatory instrument enters development:
1. Create a placeholder note in `01 Regulations/` with `status: placeholder`
2. Link it from `00 Home/Home.md` under Current Focus
3. Add to `ROADMAP.md` High Priority
4. Create a skeleton in the relevant `14 Timeline/` note

**Output:** Placeholder note, ROADMAP entry, timeline skeleton

---

### Stage B — Working Group Phase

For each working group session that produces documents related to the instrument:

1. Run `Workflows/Import Pipeline.md` for each new document
2. Update `04 Working Groups/[IWG Name].md` with session outcomes
3. Update the regulation note in `01 Regulations/` — append new content, never overwrite
4. Update the relevant `14 Timeline/` note with confirmed milestones
5. Upgrade regulation note `status` from `placeholder` → `draft` when substantive content is added

**Output:** Updated working group note, updated regulation note, updated timeline

---

### Stage C — GRVA Recommendation

When GRVA formally recommends the instrument to WP.29:

1. Update the GRVA session note in `03 GRVA/` with the recommendation fact (cite cover page)
2. Update the regulation note:
   - Add "GRVA recommendation" to the Procedural History section
   - Record the basis document number
   - Set `status: draft` if not already
3. Update `14 Timeline/ADS Timeline.md` and `14 Timeline/GRVA Timeline.md`
4. Update `ROADMAP.md` — move from High Priority to In Progress

**Output:** Updated GRVA session note, updated regulation note, updated timelines

---

### Stage D — WP.29 Session / AC.3 Vote

When WP.29 considers the instrument:

1. Update the WP.29 session note in `02 WP29/`
2. If adopted: update regulation note — set `status: active`, add adoption date, update source field
3. If deferred: update regulation note — add deferral note, keep `status: draft`, add `[VERIFY]` for vote outcome
4. Update `14 Timeline/WP29 Timeline.md` with the session outcome
5. If adopted: update `ROADMAP.md` — move to Completed

**Output:** Updated WP.29 session note, updated regulation note (status change), updated timelines

---

### Stage E — Implementation Monitoring

After adoption:

1. Track national implementation in relevant OEM or Organization notes
2. Track EU transposition in `07 Organizations/European Commission.md`
3. Create Research Notes for any implementation questions or anomalies
4. Run `Tasks/Update Timeline.md` as implementation milestones are confirmed

**Output:** Updated OEM/Organization notes, Research Notes, updated timelines

---

## Multi-Session State Management

When resuming work on a tracked instrument across sessions:

1. Start by reading the existing regulation note — it is the single source of truth for the instrument's current state
2. Check the instrument's `status` field — it tells you where the instrument is in the lifecycle
3. Check the relevant `14 Timeline/` note — it tells you what has been confirmed
4. Check `ROADMAP.md` — it tells you what's next
5. Check `CHANGELOG.md` — it tells you what was done in prior sessions

**Never derive the current state from memory or the conversation history. Always read the vault.**

---

## Currently Tracked Instruments

| Instrument | Note | Current Stage | Status |
|---|---|---|---|
| ADS UN GTR | `01 Regulations/ADS UN GTR.md` | D — WP.29 199th session | active |
| New UN Regulation on ADS | `01 Regulations/New UN Regulation on ADS.md` | D — WP.29 199th session | placeholder |
| R171 Supplement 2 | `01 Regulations/R171.md` | B — ADAS TF 37th | draft |

---

## Exit Criteria for a Lifecycle Tracking

A regulatory instrument is considered fully tracked in the vault when:
- [ ] Regulation note is `status: active`
- [ ] All procedural milestones documented in relevant Timeline notes
- [ ] Adoption document number confirmed and cited in note
- [ ] OEM implementation notes updated (where applicable)
- [ ] Instrument moved to Completed in ROADMAP.md
