---
type: review_dashboard
status: active
tags: [review, dashboard, knowledge-quality]
related: [REVIEW_PIPELINE, KNOWLEDGE_RULES, SCHEMA, E-Mobility Europe, Driver Availability, R171, Knowledge Backlog]
source: ""
last_updated: 2026-06-28
created: 2026-06-28
---

# Knowledge Review Dashboard

## Snapshot — 2026-06-28

## Summary

| Metric | Value | Notes |
|---|---:|---|
| Total Notes Reviewed | 7 | EME-focused review scope |
| Primary Knowledge Score | 83 / 100 | `07 Organizations/E-Mobility Europe.md` |
| Notes Needing Verification | 4 | Open questions in EME note |
| Duplicate Candidates | 1 | Do not create separate `EME.md`; keep canonical note |
| Critical Backlog Items | 0 | No critical blocker found |

## Knowledge Coverage

| Domain | Notes Reviewed | Average Score | Complete | Needs Work | Critical Gaps |
|---|---:|---:|---:|---:|---:|
| Organizations | 1 | 83 | 1 | 1 | 0 |
| Regulations | 1 | Not rescored | 1 | 0 | 0 |
| Meetings | 1 | Not rescored | 1 | 1 | 0 |
| Concepts | 0 | N/A | 0 | 0 | 0 |
| Working Groups | 1 | Not rescored | 0 | 1 | 0 |
| OEMs | 2 | Not rescored | 0 | 2 | 0 |
| Timelines | 1 | Not rescored | 1 | 1 | 0 |

## Evidence Coverage

| Domain | Strong Evidence | Partial Evidence | Needs Verification | Conflicts |
|---|---:|---:|---:|---:|
| Organizations | 1 | 1 | 4 | 0 |
| Regulations | 1 | 0 | 0 | 0 |
| Meetings | 1 | 1 | 1 | 0 |
| Working Groups | 0 | 0 | 1 | 0 |
| OEMs | 0 | 0 | 2 | 0 |

## Relationship Density

| Domain | Avg Outgoing Links | Avg YAML Related | Orphan Candidates | Missing Relationship Recommendations |
|---|---:|---:|---:|---:|
| Organizations | 6 | 7 | 0 | 3 |
| Working Groups | 6 | 5 | 0 | 1 |
| OEMs | 5.5 | 5.5 | 0 | 2 |

## Timeline Coverage

| Domain | Timeline Complete | Partial Timeline | Missing Timeline | Notes |
|---|---:|---:|---:|---|
| Organizations | 0 | 1 | 0 | EME founding and ADAS 45th are present; ADAS 39/43 need stronger evidence. |
| Regulations | 0 | 1 | 0 | R171 timeline has known `[VERIFY]` milestones. |
| Working Groups | 0 | 0 | 1 | ADAS TF placeholder lacks timeline. |

## Duplicate Candidates

| Candidate | Type | Risk | Recommendation |
|---|---|---|---|
| `07 Organizations/E-Mobility Europe.md` / possible future `EME.md` | organization alias | Duplicate alias note could fragment links. | Keep `E-Mobility Europe.md` canonical with alias `EME`. |

## Review Reports

| Report | Scope | Score | Generated |
|---|---|---:|---|
| [[E-Mobility Europe Review]] | single note plus linked context | 83 / 100 | 2026-06-28 |

## Notes

- Dashboard statistics are generated from Vault content only.
- Review does not modify knowledge notes.

---

## Snapshot — 2026-06-28 — Driver Availability

## Summary

| Metric | Value | Notes |
|---|---:|---|
| Total Notes Reviewed | 6 | Driver Availability-focused review scope |
| Primary Knowledge Score | 88 / 100 | `05 Concepts/Driver Availability.md` |
| Notes Needing Verification | 3 | R157, ADS, and EU DMS/DDAW gaps |
| Duplicate Candidates | 2 | Keep Driver Availability separate from Driver Monitoring; avoid premature Driver Disengagement note |
| Critical Backlog Items | 0 | No critical blocker for DCAS answer |

## Knowledge Coverage

| Domain | Notes Reviewed | Average Score | Complete | Needs Work | Critical Gaps |
|---|---:|---:|---:|---:|---:|
| Concepts | 4 | 88 | 3 | 1 | 0 |
| Regulations | 2 | Not rescored | 1 | 1 | 0 |

## Evidence Coverage

| Domain | Strong Evidence | Partial Evidence | Needs Verification | Conflicts |
|---|---:|---:|---:|---:|
| Concepts | 3 | 1 | 3 | 0 |
| Regulations | 1 | 0 | 1 | 0 |

## Review Reports

| Report | Scope | Score | Generated |
|---|---|---:|---|
| [[Driver Availability Review]] | single concept plus linked context | 88 / 100 | 2026-06-28 |

---

## Snapshot — 2026-06-28 — Entire Vault

## Summary

| Metric | Value | Notes |
|---|---:|---|
| Total Notes Reviewed | 76 | Knowledge folders `01`-`07`, `10`, and `14`; review artifacts excluded |
| Vault Knowledge Score | 62 / 100 | Conservative vault-wide score based on completeness, evidence, relationships, timelines, and verification status |
| Active Notes | 30 | Notes marked `status: active` |
| Draft Notes | 13 | Notes marked `status: draft` |
| Placeholder Notes | 33 | Notes marked `status: placeholder` |
| Source Metadata Gaps | 35 | Empty `source` or `source_pending` metadata |
| Explicit Verification Flags | 12 | Notes containing `[VERIFY]`, `Needs Verification`, or `source_pending` |
| Duplicate Candidates | 5 | Canonical-note risks listed below |
| Critical Backlog Items | 2 | R157 and ADS Regulation placeholder coverage |

## Knowledge Coverage

| Domain | Notes Reviewed | Active | Draft | Placeholder | Coverage Assessment |
|---|---:|---:|---:|---:|---|
| Regulations | 7 | 2 | 3 | 2 | R171 and ADS UN GTR are strongest; R157 and New ADS Regulation need major completion. |
| WP29 | 2 | 1 | 0 | 1 | Canonical WP.29 page exists, but organization duplicate creates ambiguity. |
| GRVA | 3 | 1 | 1 | 1 | GRVA session coverage is uneven; duplicate organization note needs resolution. |
| Working Groups | 9 | 4 | 2 | 3 | Core groups exist, but ADAS TF, DCAS, and EDR-DSSAD remain underdeveloped. |
| Concepts | 29 | 18 | 2 | 9 | Strong central concept layer, with safety/software/data concepts still thin. |
| OEMs | 8 | 0 | 0 | 8 | Entire OEM layer is placeholder quality. |
| Organizations | 10 | 1 | 0 | 9 | E-Mobility Europe is strongest; most organization pages need evidence. |
| Research Notes | 3 | 2 | 1 | 0 | Useful supporting notes; one still contains source-pending material. |
| Timelines | 5 | 1 | 4 | 0 | Timeline pages exist but remain partial and weakly linked. |

## Evidence Coverage

| Evidence Area | Count | Assessment |
|---|---:|---|
| Notes with empty or pending source metadata | 35 | Major evidence-quality gap, concentrated in placeholders. |
| Notes with explicit verification markers | 12 | Known unresolved claims are visible and should remain unmerged into answers until verified. |
| Regulation notes needing evidence upgrade | 5 | R155, R156, R157, R79, and New ADS Regulation require official-source strengthening. |
| OEM notes needing evidence upgrade | 8 | All OEM notes are placeholders and should not be treated as authoritative. |
| Organization notes needing evidence upgrade | 9 | Most organization notes need official-source citations or de-duplication. |

## Relationship Density

| Metric | Value | Notes |
|---|---:|---|
| Average outgoing wiki links | 9.0 | Overall graph density is healthy, but uneven. |
| Notes with fewer than 3 outgoing links | 4 | All are timeline notes. |
| Notes with zero outgoing links | 4 | `ADS Timeline`, `R157 Timeline`, `R171 Timeline`, and `WP29 Timeline`. |
| Primary relationship risks | 5 | Duplicate canonical pages and placeholder relationship hubs. |

## Timeline Coverage

| Timeline | Status | Gap |
|---|---|---|
| [[ADS Timeline]] | draft | No outgoing links; needs sourced milestones and graph links. |
| [[GRVA Timeline]] | draft | Partial evidence; needs fuller milestone coverage. |
| [[R157 Timeline]] | draft | No outgoing links; needs sourced R157 milestone chain. |
| [[R171 Timeline]] | active | Contains `[VERIFY]` milestones requiring resolution. |
| [[WP29 Timeline]] | draft | No outgoing links; needs canonical WP.29 milestone structure. |

## Duplicate Candidates

| Candidate | Type | Risk | Recommendation |
|---|---|---|---|
| `02 WP29/WP29.md` / `07 Organizations/WP.29.md` | body / organization duplicate | Links may split between two canonical WP.29 pages. | Pick one canonical page and convert the other into an alias or merge candidate. |
| `03 GRVA/GRVA.md` / `07 Organizations/GRVA.md` | body / organization duplicate | GRVA relationships may fragment. | Keep one canonical GRVA page and merge evidence/relationships. |
| `04 Working Groups/DCAS.md` / `05 Concepts/DCAS.md` | working group / concept overlap | The acronym can refer to the group and the system concept. | Keep both only if roles are clearly separated and cross-linked. |
| `04 Working Groups/DSSAD.md` / `05 Concepts/DSSAD.md` | working group / concept overlap | Group and concept are easy to conflate. | Separate mandate from technical concept, then cross-link. |
| `05 Concepts/ADS.md` / `05 Concepts/Automated Driving System.md` | concept duplicate | Definitions may drift between abbreviation and full-name pages. | Choose canonical concept page and make the other an alias or narrow explainer. |

## Review Reports

| Report | Scope | Score | Generated |
|---|---|---:|---|
| [[E-Mobility Europe Review]] | single note plus linked context | 83 / 100 | 2026-06-28 |
| [[Driver Availability Review]] | single concept plus linked context | 88 / 100 | 2026-06-28 |
| [[R171 Review]] | single regulation plus linked context | 88 / 100 | 2026-06-28 |

## Notes

- This vault-wide review used only local Vault content.
- No research was performed.
- No knowledge notes were modified.
