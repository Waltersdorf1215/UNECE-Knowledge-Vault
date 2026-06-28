# Task: Fix Inference Drift

**Type:** One-off task
**Output:** Corrected notes with proper epistemic labeling

---

## Instructions for Claude

You are acting on findings from `10 Research Notes/Inference Drift Report.md`.

**Read that report before touching any note.**

### Step 1 — Load the Report

Open `10 Research Notes/Inference Drift Report.md`.
Identify all items in the **Priority Action Queue** (🔴 High, 🟡 Medium, 🟢 Low).
Work from highest severity to lowest.

### Step 2 — For Each Flagged Item

Read the current state of the flagged note. Then apply the appropriate correction:

#### Option A — Statement is clearly an Interpretation (no source)
- Keep the statement
- Prefix with `*Interpretation:*`
- Example: change `"R155 is a prerequisite for R157"` → `*Interpretation:* R155 is widely understood as a prerequisite for R157 type approval. [VERIFY — read R157 text for explicit precondition language]`

#### Option B — Statement can be sourced
- Find the source document and paragraph
- Keep the statement
- Add inline citation: `**Fact (document, §X.Y):**`
- Remove any `[VERIFY]` flag

#### Option C — Statement is unsourceable and misleading
- Remove the statement
- If it has analytical value, move it to the relevant Research Note as `*Interpretation:*`

#### Option D — Statement is a Personal Insight in an authoritative note
- Move it to `10 Research Notes/` as a Personal Insight
- Replace original location with a link: `→ See Research Note: [[Note Name]]`

### Step 3 — Terminology Replacements

Replace these specific terms everywhere they appear without a source citation:

| Problematic phrase | Safe replacement |
|---|---|
| "companion regulation" | Describe the actual relationship explicitly |
| "foundational enabler" | `*Interpretation:*` + describe why |
| "regulatory ladder" | `*Interpretation:* In the analytical framework of this vault...` |
| "upper/lower boundary of X" | `*Interpretation:*` + cite SAE level basis |
| "prerequisite for type approval" | `[VERIFY]` until regulation text is read |
| "enablement stack" | `*Interpretation:*` + describe what this means |
| "was designed to" | `[VERIFY]` unless a WP.29 document states the design intent |

### Step 4 — Update the Drift Report

After correcting each item, mark it as resolved in `10 Research Notes/Inference Drift Report.md` by appending `✓ Resolved YYYY-MM-DD` to the item.

### Step 5 — CHANGELOG

Add a brief entry to `CHANGELOG.md` listing which notes were corrected and what changes were made.

---

## Definition of Done

- [ ] All 🔴 High items corrected
- [ ] All 🟡 Medium items corrected or explicitly deferred with reason
- [ ] Terminology replacements applied
- [ ] Inference Drift Report updated with resolution status
- [ ] CHANGELOG.md entry added
