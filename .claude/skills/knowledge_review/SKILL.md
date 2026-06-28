# Skill: Knowledge Review

**Version:** 1.0.0
**Category:** Review + Quality Control
**Depends on:** `acquire_knowledge` skill, `knowledge-merge` skill

---

## Purpose

`knowledge_review` is the **Quality Control engine** of the UNECE Knowledge OS.

It does **not** perform research.

It does **not** acquire new knowledge.

It does **not** modify knowledge notes automatically.

Instead, it evaluates the quality, completeness, consistency, evidence coverage, relationship coverage, timeline coverage, and trustworthiness of the Vault after acquisition or merge work.

> **Guiding principle:** The Vault is always the primary source of truth. A review evaluates what is present in the Vault and identifies what is missing, uncertain, duplicated, unsupported, or ready for improvement.

---

## When to Invoke This Skill

Use this skill when the user asks to:

- Review a note, folder, knowledge domain, or the entire Vault
- Audit evidence quality after acquisition or merge work
- Find missing sections or weak notes
- Find unsupported factual claims
- Find likely missing relationships
- Check timeline completeness
- Detect duplicated notes or duplicated concepts
- Generate a Knowledge Score
- Create or update review artifacts in `11 Review/`
- Maintain `11 Review/Dashboard.md`
- Maintain `11 Review/Knowledge Backlog.md`

Example prompts:

- "Review R171"
- "Review all Regulations"
- "Review Organizations"
- "Review entire UNECE Vault"
- "Run a knowledge quality review after this acquisition"
- "Generate the knowledge review dashboard"

---

## When NOT to Use This Skill

Do **not** use this skill to:

- Browse the web or fetch URLs
- Search external sources
- Download or inspect new online documents
- Create new knowledge notes
- Rewrite knowledge notes
- Merge evidence into entity notes
- Fill missing sections directly
- Invent missing evidence
- Assert unverified relationships as facts

If a review finds missing knowledge, create review artifacts only. Use `acquire_knowledge` to gather new knowledge and `knowledge-merge` to merge verified evidence.

---

## Operating Rules

These rules are absolute:

1. **Vault first, Vault only.** Review only local Vault content and local attachments already present in the workspace.
2. **No research.** Do not use web browsing or external lookup while running this skill.
3. **No automatic note edits.** Do not modify files in `01 Regulations/`, `02 WP29/`, `03 GRVA/`, `04 Working Groups/`, `05 Concepts/`, `06 OEM/`, `07 Organizations/`, `08 Meetings/`, `09 Proposals/`, `10 Research Notes/`, or `14 Timeline/` unless the user explicitly asks for a separate merge/fix task.
4. **Review artifacts only.** Write outputs under `11 Review/`, including reports, dashboard, backlog, and pending review items.
5. **Do not overwrite user content.** When updating `11 Review/Dashboard.md` or `11 Review/Knowledge Backlog.md`, preserve existing manually written content. Append dated sections or update clearly marked generated sections.
6. **Never invent evidence.** If a claim lacks source support, mark it `Needs Verification`.
7. **Recommend missing relationships only.** Do not add links to knowledge notes. Do not state that a relationship is confirmed unless the Vault contains evidence.
8. **Never merge automatically.** Duplicate detection produces merge recommendations only.
9. **Score knowledge quality only.** Never score writing style, prose polish, or formatting aesthetics.
10. **Prefer uncertainty over false certainty.** Any uncertain claim, relationship, or date is a review finding, not a fact.

---

## Required Governance Documents

Before running a substantial review, read these files in the current session:

- `CLAUDE.md`
- `KNOWLEDGE_RULES.md`
- `SCHEMA.md`
- `RELATIONSHIPS.md`
- `REVIEW_PIPELINE.md`

For acquisition or merge context, also read:

- `.claude/skills/acquire_knowledge/SKILL.md`
- `.claude/skills/knowledge-merge/SKILL.md`

---

## Review Workflow

### Step 1 — Review Scope

Determine the review scope from the user's request:

| Scope | Examples | Expected Inputs |
|---|---|---|
| Single note | `Review R171` | One matching note path |
| Folder | `Review all Regulations` | A folder such as `01 Regulations/` |
| Domain | `Review Organizations`, `Review ADS domain` | Multiple folders or notes linked by topic |
| Entire Vault | `Review entire UNECE Vault` | All knowledge folders |

Resolve the scope by searching the Vault:

- Match exact note titles first
- Then match aliases, YAML `related`, tags, and wiki links
- For domain reviews, include notes that are strongly connected by existing Vault links

Do not browse the web to expand scope.

---

### Step 2 — Knowledge Completeness

Evaluate whether each note contains the expected sections for its type.

#### Regulation

Expected sections:

- Overview
- Scope
- Definitions
- Key Requirements
- Amendment History
- Relationships
- References
- Evidence

#### Organization

Expected sections:

- Overview
- Role
- Participation
- Submitted Documents
- Relationships
- References

#### Meeting

Expected sections:

- Summary
- Decisions
- Documents
- Participants
- Timeline
- References

#### Working Group

Expected sections:

- Overview
- Mandate
- Work Items
- Deliverables
- Participants
- Relationships
- Timeline
- References

#### Concept

Expected sections:

- Overview
- Definition
- Regulatory Usage
- Related Regulations
- Related Concepts
- Evidence
- References

Missing expected sections are **Knowledge Gaps**. Empty or placeholder sections count as missing.

---

### Step 3 — Evidence Review

Check factual statements for support from evidence already present in the Vault.

Recognized official evidence types:

- UNECE Regulation
- UNECE Wiki
- Official Meeting Report
- Official Working Document
- Official Organization Website
- Other Official Evidence

For each substantive factual claim, classify evidence status:

| Status | Meaning |
|---|---|
| `Supported` | The claim has a named source, inline citation, document number, or local attachment reference |
| `Partially Supported` | The note has a source field but the specific claim lacks inline traceability |
| `Needs Verification` | No evidence is visible in the note or linked Vault context |
| `Conflict` | Two Vault claims appear to contradict each other |

Never add evidence that is not already in the Vault. Never infer evidence from memory.

---

### Step 4 — Relationship Review

Check whether relationships are present, relevant, and evidence-aware.

For a single note:

1. Read YAML `related`
2. Read all body wiki links
3. Compare against relationship expectations in `KNOWLEDGE_RULES.md` and `RELATIONSHIPS.md`
4. Check whether important nearby Vault entities are missing from the relationship set
5. Classify relationship findings as confirmed, suggested, unsupported, or duplicated

Example R171 relationship candidates to check against local Vault context:

- `[[GRVA]]`
- `[[DCAS]]`
- `[[Driver Monitoring]]`
- `[[Driver Availability]]`
- `[[ADS TF]]`
- `[[VMAD]]`
- `[[R79]]`
- `[[R130]]`
- `[[R152]]`

Do **not** invent links. If a relationship seems likely but the Vault lacks evidence, record it as a **Missing Relationship Recommendation** with status `Needs Verification`.

---

### Step 5 — Timeline Review

Determine whether historical milestones are documented in the note and relevant timeline files under `14 Timeline/`.

Check for:

- Adoption
- Entry into force
- Revision history
- Major amendments
- WP.29 endorsement
- GRVA recommendation or endorsement
- Major working group milestones

If timeline information is missing, recommend adding it. Do not add timeline entries directly unless the user explicitly starts a merge/fix task.

---

### Step 6 — Duplicate Detection

Detect likely duplicated:

- Concepts
- Organizations
- Regulations
- Meeting pages
- Working groups
- Proposal pages

Methods:

- Compare note titles and aliases
- Search for repeated acronyms
- Compare YAML `type`, `source`, and `related`
- Check overlapping definitions or summaries
- Review known duplicate candidates in `REVIEW_PIPELINE.md`

Output merge recommendations only. Never merge automatically.

---

### Step 7 — Knowledge Score

Generate an overall score from `0 / 100` using `scoring.md`.

Required score dimensions:

- Completeness
- Evidence Quality
- Relationship Coverage
- Timeline Coverage
- Cross References
- Verification Status

Never score writing style.

Use this display format:

```markdown
## Knowledge Score

**88 / 100**

| Area | Status | Notes |
|---|---:|---|
| Overview | OK | Present and sourced |
| Definitions | OK | Present |
| Requirements | Warning | Some claims need inline citations |
| Relationships | OK | Strong outgoing links |
| Timeline | Missing | Entry into force present; adoption history missing |
| Evidence | OK | Primary source listed |
| References | Warning | References are incomplete |
```

Status labels:

- `OK`
- `Warning`
- `Missing`
- `Needs Verification`
- `Conflict`

---

### Step 8 — Review Report

Generate a review report under `11 Review/`.

Filename pattern:

```text
11 Review/[Topic] Review.md
```

Example:

```text
11 Review/R171 Review.md
```

Use `templates/review_report.md`.

Each report must include:

- Summary
- Knowledge Score
- Strengths
- Weaknesses
- Missing Knowledge
- Missing Evidence
- Missing Relationships
- Missing Timeline
- Duplicate Candidates
- Suggested Improvements
- Backlog Items

If the file already exists, preserve user content and append a dated review section unless the user explicitly asks to regenerate it.

---

### Step 9 — Dashboard

Maintain:

```text
11 Review/Dashboard.md
```

Use `templates/dashboard.md`.

Include statistics such as:

- Knowledge Coverage
- Regulations
- Organizations
- Meetings
- Concepts
- Working Groups
- Evidence Coverage
- Relationship Density
- Timeline Coverage
- Duplicate Candidates
- Needs Verification count

When updating the dashboard, prefer a dated snapshot:

```markdown
## Snapshot — YYYY-MM-DD
```

---

### Step 10 — Knowledge Backlog

Maintain:

```text
11 Review/Knowledge Backlog.md
```

Use `templates/backlog.md`.

Priority levels:

- ★★★★★ Critical
- ★★★★ Important
- ★★★ Useful
- ★★ Optional
- ★ Nice to Have

Each backlog item must include:

- Topic
- Missing Knowledge
- Suggested Source
- Estimated Difficulty
- Review Source
- Status

Suggested sources must be source categories, not invented citations. Examples:

- Official UNECE regulation
- Official meeting report
- Official working document
- UNECE wiki
- Official organization website

---

## Output Contract

Every Knowledge Review run should report:

- Scope reviewed
- Files read
- Review artifacts created or updated
- Overall score or score range
- Critical findings
- Backlog additions
- What was not changed

Use this closing note when relevant:

> No knowledge notes were modified. This review only generated review artifacts under `11 Review/`.

---

## Integration With Knowledge Lifecycle

Knowledge Review is the third stage in the Knowledge Lifecycle:

1. **Acquire Knowledge** — finds or creates knowledge from Vault-first research
2. **Knowledge Merge** — merges verified evidence into notes
3. **Knowledge Review** — audits the resulting Vault and produces quality-control artifacts

Review findings should feed future acquisition and merge work, but this skill itself remains read-only with respect to knowledge notes.
