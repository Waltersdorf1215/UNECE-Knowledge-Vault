---
name: knowledge_evolution
description: Modernize existing UNECE Knowledge OS notes to match current Governance without creating new knowledge; use for ontology/schema/metadata/folder/relationship/naming migrations, migration plans, evolution reports, and compliance cleanup after governance changes.
---

# Skill: Knowledge Evolution

**Version:** 1.0.0
**Category:** Governance Migration + Structural Modernization
**Depends on:** Governance documents, `knowledge_review`

---

## Purpose

`knowledge_evolution` modernizes existing Vault knowledge so it conforms to the current Governance layer.

It does **not** acquire new knowledge.
It does **not** merge newly researched evidence.
It does **not** evaluate knowledge quality as its primary task.

Its only responsibility is to evolve existing knowledge structure while preserving meaning and information.

> **Guiding principle:** Knowledge Evolution makes the Vault cleaner, more consistent, and easier to maintain over many years. It must never make the Vault larger merely for its own sake.

---

## When to Invoke This Skill

Use this skill when the user asks to:

- Upgrade the Vault to a new ontology or governance version
- Normalize metadata fields across notes
- Normalize legacy entity types
- Normalize relationship vocabulary
- Normalize review artifacts
- Prepare the Vault for a governance/schema change
- Detect legacy structures without modifying knowledge
- Create a migration plan before structural changes
- Apply an approved structural migration
- Generate an evolution report after migration

Example prompts:

- "Upgrade Vault to Ontology v1.1"
- "Normalize evidence metadata"
- "Normalize relationship vocabulary"
- "Normalize review artifacts"
- "Prepare Vault for the new Governance version"
- "Detect legacy structures without modifying knowledge"

---

## When NOT to Use This Skill

Do **not** use this skill to:

- Research external sources
- Create new knowledge from missing information
- Merge newly acquired facts
- Evaluate note quality for scoring only
- Fill missing factual sections
- Upgrade evidence automatically
- Convert uncertain relationships
- Move files without approval
- Rewrite manually authored prose
- Change the meaning of a note

Use:

- `acquire_knowledge` to create or acquire knowledge
- `knowledge-merge` to integrate verified new knowledge
- `knowledge_review` to evaluate quality
- `knowledge_evolution` to modernize existing structure

---

## Required Governance Inputs

Before any substantial evolution task, read the latest available Governance documents in this session:

1. `Governance/KNOWLEDGE_ONTOLOGY.md`
2. `Governance/QUALITY_POLICY.md` if present
3. `Governance/WORKFLOW.md` if present

Also read supporting legacy rules when needed:

- `KNOWLEDGE_RULES.md`
- `SCHEMA.md`
- `RELATIONSHIPS.md`
- `REVIEW_PIPELINE.md`
- Current relevant review artifacts under `11 Review/`

Governance is the source of truth. Legacy documents are context, not authority, when they conflict with Governance.

---

## Operating Rules

These rules are absolute:

1. **Inspect before acting.** Never assume compliance.
2. **Plan before modifying.** Always generate a migration plan before any change.
3. **Approval required.** Do not apply migration until the user approves the plan.
4. **Never invent facts.** Missing evidence remains missing.
5. **Never upgrade evidence automatically.** Evidence metadata may be normalized only when current note content already supports it.
6. **Never convert uncertain relationships.** Recommend uncertain changes instead.
7. **Never delete knowledge.** Preserve existing content and history.
8. **Never overwrite manual notes.** Only normalize structure around content unless a user explicitly approves a targeted edit.
9. **Never change meaning.** Structural modernization must preserve semantics.
10. **Prefer recommendation over mutation when uncertain.**

---

## Workflow

### Step 1 — Load Governance

Read current Governance documents and extract:

- Supported entity types
- Required metadata fields
- Evidence model
- Relationship vocabulary
- Folder ontology
- Naming and alias rules
- Review artifact rules

Record the governance version/date if available.

### Step 2 — Inspect Target Notes

Support these scopes:

| Scope | Examples | Required Action |
|---|---|---|
| Single file | "Evolve R171" | Read the full file and linked governance requirements. |
| Folder | "Normalize all Regulations" | Inspect every note in the folder. |
| Entire Vault | "Upgrade Vault to Ontology v1.1" | Inspect all canonical Vault folders. |

Canonical folders commonly include:

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
- `11 Review/`
- `13 Resources/`
- `14 Timeline/`
- `Governance/`

Do not inspect ignored local cache/history folders unless the user explicitly requests it.

### Step 3 — Detect Evolution Opportunities

Detect structural drift only. Do not judge knowledge completeness unless needed to avoid unsafe migration.

#### Metadata

Find:

- Missing fields: `knowledge_type`, `evidence_level`, `review_status`, `confidence`
- Deprecated fields
- Duplicate metadata
- Empty `source`
- `source_pending`
- Missing `created` or `last_updated`
- Type-specific fields missing under Governance

#### Entity Types

Find obsolete or unsupported entity types.

Example:

```text
type: oem
```

may evolve to:

```yaml
type: organization
org_type: OEM
```

Only do this when the semantic meaning is preserved. Otherwise recommend ontology extension.

#### Relationships

Find legacy relationship vocabulary and generic relationship storage.

Examples:

| Legacy / Weak Form | Possible Governance Form | Rule |
|---|---|---|
| `requires` | `depends_on` | Only if the source content supports dependency. |
| `supports` | `supported_by` | Only when evidence direction is clear. |
| Generic `related` list | Explicit relationship table | Only when current evidence supports each edge. |

Never convert uncertain or inferred relationships into graph facts.

#### Naming

Find:

- Duplicate canonical pages
- Legacy abbreviations
- Inconsistent aliases
- Unsupported aliases
- Abbreviation/full-name drift

Recommend canonical names. Do not rename files without approval.

#### Folder Structure

Find:

- Entities outside canonical folders
- Legacy folders not recognized by Governance
- Review artifacts using inconsistent locations

Recommend migrations. Never move files without approval.

### Step 4 — Generate Migration Plan

Before modifying anything, create a migration plan using:

`templates/migration_plan.md`

The plan must include:

- Summary
- Governance basis
- Files affected
- Fields affected
- Proposed changes
- Risk level
- Rollback complexity
- Expected benefit
- Items requiring approval
- Items recommended but not safe to automate

If the user asked only to detect legacy structures, stop after the plan/report and do not modify files.

### Step 5 — Apply Migration After Approval

Only after explicit user approval:

- Apply the approved changes exactly.
- Preserve all manually written content.
- Preserve `created` dates.
- Update `last_updated` only on touched files.
- Add migration notes only when useful and non-invasive.
- Do not move files unless approved.
- Do not delete files.
- Do not change unsupported or uncertain claims.

If a planned change becomes unsafe during application, stop and report the blocker.

### Step 6 — Generate Evolution Report

After applying an approved migration, save a report under `11 Review/`.

Example filename:

```text
11 Review/Evolution Report 2026-06-28.md
```

Use:

`templates/evolution_report.md`

Include:

- Migration Summary
- Before / After
- Metadata Changes
- Relationship Changes
- Naming Changes
- Folder Changes
- Ontology Compliance Improvement
- Remaining Issues
- Rollback Notes

### Step 7 — Update Dashboard and Backlog

If migration improves ontology compliance:

- Update `11 Review/Dashboard.md`
- Update `11 Review/Knowledge Backlog.md`
- Update compliance score if an ontology compliance report exists

Do not claim quality improvement unless the migration directly supports it.

---

## Safety Examples

### Safe Automatic Changes After Approval

- Add missing `review_status` to review artifacts when status is clear from existing frontmatter.
- Normalize `type: review_dashboard` to `type: review_artifact` while preserving `review_type: dashboard`.
- Add `org_type: OEM` when changing `type: oem` to `type: organization`.
- Add `last_updated` when missing and the file is touched.

### Recommend, Do Not Modify

- Convert broad `related` lists into explicit relationships when evidence is not visible.
- Add `evidence_level: official` when the note has no concrete source.
- Merge duplicate canonical pages.
- Rename files.
- Move files across folders.
- Convert `source_pending` into a source.

### Never Do

- Invent missing sources.
- Reclassify uncertain evidence as verified.
- Delete stale content.
- Remove open questions.
- Turn a concept overlap into a legal dependency.
- Rewrite prose for style.

---

## Deliverables

Depending on the task, produce one or more:

- Migration plan
- Approved structural edits
- Evolution report
- Dashboard/backlog updates
- List of recommendations that were intentionally not applied

Every deliverable must state that no new knowledge was created.
