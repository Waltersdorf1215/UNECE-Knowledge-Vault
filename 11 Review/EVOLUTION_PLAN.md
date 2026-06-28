---
type: review_artifact
review_type: migration_plan
status: draft
tags: [evolution, migration-plan, ontology, preview]
related: [KNOWLEDGE_ONTOLOGY, ONTOLOGY_COMPLIANCE_REPORT, Knowledge Backlog, Dashboard]
source: "Governance/KNOWLEDGE_ONTOLOGY.md"
created: 2026-06-28
last_updated: 2026-06-28
---

# Knowledge Evolution Plan — Preview Mode — 2026-06-28

## 1. Executive Summary

This is a **preview-only** Knowledge Evolution plan. No knowledge notes were modified. No research was performed. No new knowledge was created.

The active Governance source is `Governance/KNOWLEDGE_ONTOLOGY.md`. `Governance/QUALITY_POLICY.md` and `Governance/WORKFLOW.md` were requested by the skill workflow but are not currently present, so they were not used.

The Vault is structurally functional but not yet Governance-clean. The main evolution opportunities are:

- Normalize legacy entity types and review artifact types.
- Add missing ontology metadata without upgrading evidence beyond what current notes support.
- Decide how to handle `06 OEM/` and `type: oem`.
- Convert template files to template artifacts rather than entity instances.
- Normalize timeline aggregate notes.
- Separate operational skill/prompt Markdown from canonical knowledge-entity scoring.
- Replace generic relationship storage with explicit ontology relationship blocks only where evidence is visible.
- Resolve duplicate canonical candidates through approved merge/rename plans.

## 2. Estimated Compliance Improvement

Baseline from latest ontology compliance report:

| Metric | Current | After Stage 1 | After Stage 2 | After Stage 3 |
|---|---:|---:|---:|---:|
| Overall Compliance Score | 66 / 100 | 74 / 100 | 83 / 100 | 90 / 100 |
| Entity Compliance | 68 / 100 | 80 / 100 | 86 / 100 | 92 / 100 |
| Relationship Compliance | 55 / 100 | 57 / 100 | 66 / 100 | 82 / 100 |
| Folder Compliance | 78 / 100 | 82 / 100 | 86 / 100 | 92 / 100 |
| Evidence Compliance | 52 / 100 | 56 / 100 | 76 / 100 | 82 / 100 |
| Naming Compliance | 75 / 100 | 76 / 100 | 82 / 100 | 90 / 100 |

These are estimates. Actual score changes should be measured by rerunning ontology compliance after each approved stage.

## 3. Estimated Number of Files

| Scope | Count | Notes |
|---|---:|---|
| Markdown files scanned, excluding ignored local chat/cache folders | 160 | Includes canonical notes, governance, review artifacts, skills, prompts, workflows, templates, and operational docs. |
| Core governance / knowledge / review Markdown surface | about 100 | Matches latest ontology compliance report scope. |
| Files with unsupported or legacy `type` in broad scan | 82 | Many are operational skill/prompt docs that may need exclusion rather than migration. |
| Files with metadata gaps in broad scan | 131 | Includes skill docs and operational prompts without knowledge frontmatter. |
| Files with source gaps in broad scan | 113 | Includes files that are not knowledge entities and should not necessarily have evidence metadata. |
| Core files with required metadata gaps | 80 | From latest compliance report. |
| Core files with empty or pending source metadata | 57 | From latest compliance report. |
| Notes with generic `related` + wiki-link graph style | 94 broad / 77 core | Relationship semantics are mostly navigational, not ontology-typed. |

## 4. Risk Assessment

| Risk | Level | Reason | Mitigation |
|---|---|---|---|
| Evidence over-upgrade | High | Adding `evidence_level` can imply confidence not supported by the note. | Only add high-confidence evidence metadata when source and claim support are visible; otherwise use `needs_review`, `source_pending`, or leave for acquisition. |
| Semantic drift in entity type normalization | High | `oem` could be a subtype of organization or a first-class ontology type. | Require governance decision before changing `06 OEM/`. |
| Relationship conversion drift | High | Generic links may not indicate `depends_on`, `supported_by`, or `references`. | Convert only relationships with visible evidence and clear direction; otherwise recommend only. |
| Duplicate page merging | High | WP.29, GRVA, DCAS, DSSAD, and ADS duplicates may contain non-identical content. | Create separate merge plans; never merge automatically. |
| Review artifact normalization | Low | Review files are review artifacts by folder and purpose. | Preserve subtype in `review_type`. |
| Template normalization | Low | Templates should not masquerade as actual entities. | Use `type: template` and preserve intended entity type in `template_for`. |
| Timeline normalization | Medium | Current timeline notes are aggregate timelines, while ontology defines timeline events. | Either introduce `timeline` aggregate type in Governance or use `type: timeline_event` with `timeline_kind: aggregate`. |
| Operational docs classification | Medium | `.claude/skills/`, `Skills/`, and `copilot/` Markdown are operational, not knowledge entities. | Exclude from knowledge ontology scoring or add `operational_artifact` governance type. |

## 5. Proposed Evolution Stages

## Stage 1 — Low-Risk Structural Normalization

Goal: Normalize artifacts that are clearly structural without touching knowledge meaning.

Estimated affected files: **about 25–35 files**

Expected compliance lift: **66 → 74**

Actions:

- Normalize review artifacts to `type: review_artifact` while preserving subtype.
- Normalize templates to `type: template`.
- Normalize governance/resource/archive README-style files or exclude them from knowledge-entity scoring.
- Decide how operational Markdown files should be scoped: excluded from knowledge ontology or assigned an operational artifact type.
- Do not change knowledge note facts, relationships, or evidence confidence.

Risk: **Low to Medium**

Rollback complexity: **Low**

## Stage 2 — Metadata and Evidence Metadata Normalization

Goal: Add missing ontology metadata where current content already supports it.

Estimated affected files: **about 60–90 files**

Expected compliance lift: **74 → 83**

Actions:

- Add missing `created` fields where they can be inferred from existing Vault history or file history only if approved.
- Add `knowledge_type` and `evidence_level` only when source support is visible.
- Add `review_status` and `confidence` to review artifacts and active knowledge notes where status is explicit.
- Preserve `source_pending`, empty sources, and open questions where evidence is absent.
- Do not upgrade placeholder notes to active.

Risk: **Medium**

Rollback complexity: **Medium**

## Stage 3 — Relationship, Naming, and Canonical Structure Normalization

Goal: Improve graph semantics and canonical identity after explicit approval.

Estimated affected files: **about 40–90 files**, depending on how many relationship conversions are approved.

Expected compliance lift: **83 → 90**

Actions:

- Convert evidence-supported relationship statements to ontology vocabulary.
- Create explicit relationship tables or relationship blocks for high-value notes.
- Resolve duplicate canonical candidates through separate merge plans.
- Decide `OEM` ontology strategy.
- Decide timeline aggregate strategy.
- Recommend folder moves or renames, but do not execute without approval.

Risk: **High**

Rollback complexity: **Medium to High**

## 6. Detailed Migration Actions

### Action 1 — Normalize Review Artifact Types

| Field | Value |
|---|---|
| Affected Files | `11 Review/Dashboard.md`; `11 Review/Knowledge Backlog.md`; `11 Review/TEST_REPORT.md`; `11 Review/Driver Availability Review.md`; `11 Review/E-Mobility Europe Review.md`; `11 Review/R171 Review.md`; `11 Review/Pending/R157-R171-evidence-review.md`; `11 Review/Pending/R171-copilot-context-mismatch.md`; `11 Review/Pending/R171-persistent-context-error.md`; `11 Review/ONTOLOGY_COMPLIANCE_REPORT.md`; `11 Review/EVOLUTION_PLAN.md` |
| Expected Changes | Set `type: review_artifact`; preserve current subtype in `review_type` such as `dashboard`, `backlog`, `test_report`, `knowledge_review`, `pending_review_item`, `ontology_compliance_report`, or `migration_plan`. Add missing standard review metadata where absent. |
| Risk Level | Low |
| Notes | Safe after approval because folder and purpose make these clearly review artifacts. Does not alter knowledge content. |

### Action 2 — Normalize Template Files

| Field | Value |
|---|---|
| Affected Files | `11 Templates/Meeting Template.md`; `11 Templates/OEM Template.md`; `11 Templates/Organization Template.md`; `11 Templates/Proposal Template.md`; `11 Templates/Regulation Template.md`; `11 Templates/Research Note Template.md`; `11 Templates/Technical Concept Template.md`; `11 Templates/Working Group Template.md` |
| Expected Changes | Set `type: template`; add `template_for` with intended entity type. Preserve body placeholders and instructions. |
| Risk Level | Low |
| Notes | Current template frontmatter often looks like actual entity frontmatter, causing false ontology violations. |

### Action 3 — Decide Operational Markdown Scope

| Field | Value |
|---|---|
| Affected Files | `.claude/skills/**/*.md`; `Skills/**/*.md`; `copilot/Prompts/**/*.md`; `copilot/Tasks/**/*.md`; `copilot/Workflows/**/*.md`; `copilot/copilot-custom-prompts/**/*.md`; `copilot/README.md`; `Skills/README.md` |
| Expected Changes | Option A: exclude operational Markdown from knowledge ontology scoring. Option B: add a Governance entity type such as `operational_artifact` and normalize metadata. |
| Risk Level | Medium |
| Notes | These files are part of the Vault repository but not knowledge entities. Applying knowledge-entity metadata to them may be noisy and low value. |

### Action 4 — Normalize Legacy Governance / Resource / Archive Types

| Field | Value |
|---|---|
| Affected Files | `ONTOLOGY.md`; `SCHEMA.md`; `RELATIONSHIPS.md`; `REVIEW_PIPELINE.md`; `IMPORT_PIPELINE.md`; `KNOWLEDGE_RULES.md`; `CLAUDE.md`; `ROADMAP.md`; `13 Resources/Source Registry.md`; `99 Archive/README.md`; `11 Review/README.md` |
| Expected Changes | Replace legacy `type: meta` with `type: governance`, `type: evidence_source`, `type: review_artifact`, or another approved Governance type. Preserve existing content. |
| Risk Level | Low to Medium |
| Notes | `Governance/KNOWLEDGE_ONTOLOGY.md` is canonical; older meta docs can be normalized or gradually superseded. |

### Action 5 — Resolve `OEM` Ontology Strategy

| Field | Value |
|---|---|
| Affected Files | `06 OEM/BMW.md`; `06 OEM/Mercedes-Benz.md`; `06 OEM/Mobileye.md`; `06 OEM/NIO.md`; `06 OEM/Tesla.md`; `06 OEM/Volkswagen.md`; `06 OEM/Wayve.md`; `06 OEM/Xpeng.md`; `11 Templates/OEM Template.md` |
| Expected Changes | Option A: migrate `type: oem` to `type: organization` plus `org_type: OEM`. Option B: extend Governance to define `OEM` as a first-class entity type and preserve `06 OEM/`. |
| Risk Level | High |
| Notes | Do not silently change. This is a governance decision because `06 OEM/` is not currently a canonical ontology folder. |

### Action 6 — Normalize Timeline Aggregate Notes

| Field | Value |
|---|---|
| Affected Files | `14 Timeline/ADS Timeline.md`; `14 Timeline/GRVA Timeline.md`; `14 Timeline/R157 Timeline.md`; `14 Timeline/R171 Timeline.md`; `14 Timeline/WP29 Timeline.md` |
| Expected Changes | Option A: add Governance type `timeline` for aggregate timelines. Option B: use `type: timeline_event` only for atomic event notes and classify these as `review_artifact` or `governance` aggregates. Option C: use `type: timeline_event` plus `timeline_kind: aggregate`, if Governance approves. |
| Risk Level | Medium |
| Notes | Current notes are timeline aggregates, not single events. The ontology currently defines `Timeline Event`, so direct conversion may be semantically imprecise. |

### Action 7 — Normalize Core Entity Metadata

| Field | Value |
|---|---|
| Affected Files | Approximately 80 core files with missing required fields, including notes in `01 Regulations/`, `02 WP29/`, `03 GRVA/`, `04 Working Groups/`, `05 Concepts/`, `06 OEM/`, `07 Organizations/`, `11 Review/`, `11 Templates/`, and `99 Archive/`. |
| Expected Changes | Add or normalize `knowledge_type`, `evidence_level`, `review_status`, `confidence`, `created`, `last_updated`, and type-specific fields only where semantically clear. |
| Risk Level | Medium |
| Notes | Do not add `evidence_level: official` to notes with empty source or `source_pending`. Use conservative values or leave unresolved for Acquire/Review. |

### Action 8 — Preserve and Flag Source Gaps

| Field | Value |
|---|---|
| Affected Files | Approximately 57 core files with empty, missing, or `source_pending` source metadata, including `01 Regulations/R157.md`, `01 Regulations/R155.md`, `01 Regulations/R156.md`, `01 Regulations/R79.md`, `01 Regulations/New UN Regulation on ADS.md`, many `06 OEM/*.md`, many `07 Organizations/*.md`, and several placeholder concepts. |
| Expected Changes | Preserve source gaps. Add `evidence_level: needs_review` or equivalent only if Governance approves. Add backlog/review references rather than inventing sources. |
| Risk Level | Medium |
| Notes | This is structural evidence hygiene, not evidence acquisition. Missing sources remain missing. |

### Action 9 — Normalize High-Confidence Active Notes First

| Field | Value |
|---|---|
| Affected Files | `01 Regulations/R171.md`; `05 Concepts/Driver Availability.md`; `07 Organizations/E-Mobility Europe.md`; `01 Regulations/ADS UN GTR.md`; active ADS-derived concept notes with visible sources. |
| Expected Changes | Add missing ontology metadata where current evidence visibly supports it. Preserve facts and prose. |
| Risk Level | Low to Medium |
| Notes | This is the safest metadata normalization set because evidence is already visible and reviewed. |

### Action 10 — Normalize Review Status and Confidence Fields

| Field | Value |
|---|---|
| Affected Files | Active review reports, reviewed active notes, and pending review items under `11 Review/`. |
| Expected Changes | Add `review_status` and `confidence` where clearly supported by existing review status and scores. |
| Risk Level | Low |
| Notes | Useful for dashboards and future Knowledge Review. |

### Action 11 — Relationship Vocabulary Migration: Safe Subset

| Field | Value |
|---|---|
| Affected Files | Notes with explicit relationship statements, especially `01 Regulations/R171.md`, `05 Concepts/Driver Availability.md`, `07 Organizations/E-Mobility Europe.md`, `11 Review/Pending/R157-R171-evidence-review.md`, `RELATIONSHIPS.md`, and selected reviewed notes. |
| Expected Changes | Map legacy terms only where direction and evidence are clear. Examples: evidence support -> `supported_by`; document citation -> `references`; definition source -> `defines`; dependency -> `depends_on`. |
| Risk Level | High |
| Notes | Do not mass-convert every wiki-link or `related` entry. Generic links remain navigational until evidence is reviewed. |

### Action 12 — Convert Generic `related` Lists to Explicit Relationship Blocks

| Field | Value |
|---|---|
| Affected Files | Up to 77 core files with generic `related` metadata plus wiki links; broad scan found 94 files. |
| Expected Changes | For high-value notes only, add explicit relationship tables while preserving `related` as navigation metadata. |
| Risk Level | High |
| Notes | This requires evidence review per edge. Most links should be recommended, not automatically converted. |

### Action 13 — Duplicate Canonical Entity Plans

| Field | Value |
|---|---|
| Affected Files | `02 WP29/WP29.md` and `07 Organizations/WP.29.md`; `03 GRVA/GRVA.md` and `07 Organizations/GRVA.md`; `04 Working Groups/DCAS.md` and `05 Concepts/DCAS.md`; `04 Working Groups/DSSAD.md` and `05 Concepts/DSSAD.md`; `05 Concepts/ADS.md` and `05 Concepts/Automated Driving System.md`. |
| Expected Changes | Generate separate merge/alias plans. Recommend canonical title and alias direction. Do not merge or rename without approval. |
| Risk Level | High |
| Notes | Some pairs may be valid distinct entities if roles are clearly separated. |

### Action 14 — Naming and Alias Normalization

| Field | Value |
|---|---|
| Affected Files | Duplicate candidates above plus abbreviation-heavy notes such as `R171`, `ADS`, `ADAS TF`, `ADS IWG`, `WP.29`, and `GRVA`. |
| Expected Changes | Ensure canonical name, aliases, and excluded aliases follow Governance. Preserve explicit exclusion of stale R171 = DSSAD aliases. |
| Risk Level | Medium to High |
| Notes | Rename only after approved canonical decision. |

### Action 15 — Folder Structure Recommendations

| Field | Value |
|---|---|
| Affected Files | `06 OEM/*.md`; body-specific meeting/organization folders under `02 WP29/` and `03 GRVA/`; `14 Timeline/*.md`; operational docs under `.claude/`, `Skills/`, and `copilot/`. |
| Expected Changes | Recommend folder strategy. Do not move files in preview mode or without approval. |
| Risk Level | High |
| Notes | Folder moves affect wiki links, backlinks, and user workflows. |

### Action 16 — Template Upgrade for Future Compliance

| Field | Value |
|---|---|
| Affected Files | `11 Templates/*.md`; `.claude/skills/acquire_knowledge/templates/*.md`; `.claude/skills/knowledge_evolution/templates/*.md`; `.claude/skills/knowledge_review/templates/*.md`. |
| Expected Changes | Align templates with Governance so future notes include required metadata and do not reproduce legacy schema gaps. |
| Risk Level | Medium |
| Notes | This prevents future drift, but skill-owned templates should preserve their operational purpose. |

### Action 17 — Dashboard / Backlog Update After Approved Migration

| Field | Value |
|---|---|
| Affected Files | `11 Review/Dashboard.md`; `11 Review/Knowledge Backlog.md`; `11 Review/ONTOLOGY_COMPLIANCE_REPORT.md` or a future rerun report. |
| Expected Changes | Update compliance score and backlog only after an approved migration is applied and compliance is remeasured. |
| Risk Level | Low |
| Notes | Not applicable in preview mode. No dashboard/backlog edits should happen now. |

## Preview Mode Boundary

This plan intentionally does not:

- Modify knowledge notes.
- Modify review artifacts other than creating this plan.
- Update dashboard or backlog.
- Rename or move files.
- Add sources.
- Upgrade evidence.
- Convert uncertain relationships.
- Merge duplicate pages.

## Recommended Approval Path

Approve stages separately:

1. **Approve Stage 1** for low-risk artifact and template normalization.
2. Rerun ontology compliance.
3. **Approve Stage 2** for metadata normalization with conservative evidence handling.
4. Rerun ontology compliance.
5. Review duplicate/canonical decisions.
6. **Approve specific Stage 3 sub-actions** one at a time.

This sequence gives the Vault measurable improvement while preserving the evidence gate and avoiding semantic drift.
