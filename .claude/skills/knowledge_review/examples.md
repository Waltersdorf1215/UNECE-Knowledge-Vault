# Knowledge Review — Examples

## Example 1 — Review R171

**User request:** Review R171.

**Scope resolution:**

- Locate `01 Regulations/R171.md`
- Check related local notes and timeline context:
  - `14 Timeline/R171 Timeline.md`
  - `05 Concepts/DCAS.md`
  - `05 Concepts/Driver Monitoring.md`
  - `05 Concepts/Driver Availability.md`
  - `04 Working Groups/DCAS.md`
  - `04 Working Groups/ADAS TF.md`

**Review checks:**

- Regulation sections: Overview, Scope, Definitions, Key Requirements, Amendment History, Relationships, References, Evidence
- Evidence traceability for factual claims
- Relationship coverage against local context
- Timeline milestones: adoption, entry into force, amendments, WP.29/GRVA decisions
- Duplicate risks with DCAS concept and working group notes

**Outputs:**

- `11 Review/R171 Review.md`
- Add relevant backlog items to `11 Review/Knowledge Backlog.md`
- Update `11 Review/Dashboard.md` if requested or if running a formal review cycle

**Important constraint:** Do not edit `01 Regulations/R171.md`.

---

## Example 2 — Review All Regulations

**User request:** Review all Regulations.

**Scope resolution:**

- Review every Markdown file in `01 Regulations/`
- Include related timeline files from `14 Timeline/`
- Include directly linked concept and working group notes only for context

**Review checks:**

- Completeness by regulation template
- Missing or weak evidence
- Sparse wiki links
- Missing timeline entries
- Inconsistent metadata
- Duplicate or near-duplicate regulation notes

**Outputs:**

- `11 Review/Regulations Review.md`
- `11 Review/Dashboard.md` snapshot
- `11 Review/Knowledge Backlog.md` prioritized improvements

**Example backlog item:**

| Priority | Topic | Missing Knowledge | Suggested Source | Estimated Difficulty |
|---|---|---|---|---|
| ★★★★ Important | R171 | Amendment history needs fuller source traceability | Official UNECE regulation / working document | Medium |

---

## Example 3 — Review Organizations

**User request:** Review Organizations.

**Scope resolution:**

- Review files in `07 Organizations/`
- Compare against organization-like notes in `02 WP29/` and `03 GRVA/`

**Review checks:**

- Expected sections: Overview, Role, Participation, Submitted Documents, Relationships, References
- Duplicate candidates:
  - `07 Organizations/GRVA.md` vs `03 GRVA/GRVA.md`
  - `07 Organizations/WP.29.md` vs `02 WP29/WP29.md`
- Evidence status for organizational role statements
- Relationship links to meetings, working groups, proposals, and regulations

**Outputs:**

- `11 Review/Organizations Review.md`
- Backlog items for duplicate resolution recommendations

**Important constraint:** Recommend merges only. Do not merge.

---

## Example 4 — Review Entire UNECE Vault

**User request:** Review entire UNECE Vault.

**Scope resolution:**

- Review all knowledge folders:
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
  - `14 Timeline/`

**Review checks:**

- Coverage by type
- Evidence coverage
- Relationship density
- Timeline coverage
- Broken or weak cross references
- Duplicate candidates
- Notes with `source_pending`, empty source fields, or `[VERIFY]`

**Outputs:**

- `11 Review/UNECE Vault Review.md`
- `11 Review/Dashboard.md`
- `11 Review/Knowledge Backlog.md`

**Final response should include:**

- Total notes reviewed
- Score range by domain
- Critical gaps
- Review artifacts updated
- Confirmation that no knowledge notes were modified

---

## Example 5 — Evidence-Only Review

**User request:** Check whether the ADS UN GTR note is properly evidenced.

**Scope resolution:**

- Review `01 Regulations/ADS UN GTR.md`
- Read linked source references only if they are local Vault files or local attachments

**Review checks:**

- Source field populated
- Inline citations present for factual claims
- Claims without citations identified
- Claims relying on interpretation labeled correctly

**Output finding examples:**

- `Supported`: Claim cites `ECE/TRANS/WP.29/2026/139`
- `Partially Supported`: Source exists in frontmatter, but paragraph lacks inline citation
- `Needs Verification`: Claim has no visible source

**Important constraint:** Do not browse for the GTR document.

---

## Example 6 — Duplicate Review

**User request:** Find duplicate knowledge notes.

**Scope resolution:**

- Search all `.md` notes for overlapping titles, aliases, YAML types, and repeated definitions
- Check known duplicate candidates from `REVIEW_PIPELINE.md`

**Likely findings to evaluate:**

- `05 Concepts/DCAS.md` vs `04 Working Groups/DCAS.md`
- `07 Organizations/GRVA.md` vs `03 GRVA/GRVA.md`
- `07 Organizations/WP.29.md` vs `02 WP29/WP29.md`
- `05 Concepts/DSSAD.md` vs `04 Working Groups/DSSAD.md`

**Outputs:**

- Duplicate candidates table
- Recommended canonical note
- Merge rationale
- Evidence or review status

**Important constraint:** Never merge automatically.
