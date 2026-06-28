---
type: review_artifact
status: active
tags: [review, ontology, compliance, knowledge-quality]
related: [KNOWLEDGE_ONTOLOGY, Dashboard, Knowledge Backlog]
source: "Governance/KNOWLEDGE_ONTOLOGY.md"
created: 2026-06-28
last_updated: 2026-06-28
---

# Ontology Compliance Report

## Summary

| Field | Value |
|---|---|
| Review Date | 2026-06-28 |
| Ontology Source of Truth | `Governance/KNOWLEDGE_ONTOLOGY.md` |
| Review Scope | Canonical Vault Markdown in governance, knowledge, review, template, resource, archive, and timeline folders |
| Research Performed | No |
| Knowledge Notes Modified | No |
| Files Evaluated | 100 Markdown files |

## Overall Compliance Score

**66 / 100 — Partially Compliant**

The Vault is structurally close to the ontology at the folder and graph-navigation level, but many files predate `Governance/KNOWLEDGE_ONTOLOGY.md`. The largest compliance gaps are legacy entity types, missing required ontology metadata, untyped relationship semantics, and incomplete evidence metadata.

| Dimension | Score | Status |
|---|---:|---|
| Entity Compliance | 68 / 100 | Partial |
| Relationship Compliance | 55 / 100 | Partial |
| Folder Compliance | 78 / 100 | Mostly compliant |
| Evidence Compliance | 52 / 100 | Partial |
| Naming Compliance | 75 / 100 | Mostly compliant |

## Entity Compliance

| Metric | Value |
|---|---:|
| Markdown files evaluated | 100 |
| Files using ontology-supported type directly | 71 |
| Files using unsupported or legacy type | 29 |
| Files missing `type` entirely | 3 |
| Files with required metadata gaps | 80 |

### Supported Entity Types Observed

| Type | Count | Notes |
|---|---:|---|
| `concept` | 30 | Generally aligned with `05 Concepts/`, but many lack required evidence metadata. |
| `regulation` | 8 | Folder aligned; several lack `knowledge_type` and `evidence_level`. |
| `working_group` | 10 | Folder aligned; several lack `parent_body`, `knowledge_type`, and `evidence_level`. |
| `organization` | 13 | Mostly folder aligned; many lack `org_type`, `knowledge_type`, and `evidence_level`. |
| `meeting` | 4 | Body-specific meeting folders are acceptable under the ontology. |
| `proposal` | 1 | Present only as a template. |
| `research_note` | 4 | Ontology recognizes research notes through folder ontology. |
| `governance` | 1 | `Governance/KNOWLEDGE_ONTOLOGY.md` is compliant. |

### Entity Violations

| Violation | Files / Examples | Impact |
|---|---|---|
| Unsupported entity type `oem` | `06 OEM/*.md`, `11 Templates/OEM Template.md` | The new ontology does not define OEM as a supported entity type. These should become `organization` or the ontology should formally add an OEM/entity subtype. |
| Legacy type `meta` | `ONTOLOGY.md`, `SCHEMA.md`, `RELATIONSHIPS.md`, timeline files, resource/archive README files | `meta` is not an allowed ontology entity type. Governance/resource/archive artifacts need normalized types. |
| Home/dashboard type not defined | `00 Home/*.md` use `home` | The ontology does not define home/dashboard notes as entity types. They should be excluded from entity scoring or assigned a governance/navigation type. |
| Review artifact types are not normalized | `review_dashboard`, `review_backlog`, `review_item`, `test_report` | The ontology defines `review_artifact` as the canonical review type. Existing review subtypes are useful but not ontology-normalized. |
| Missing frontmatter type | `11 Review/Driver Availability Review.md`, `11 Review/E-Mobility Europe Review.md`, `11 Review/R171 Review.md` | Review reports cannot be classified cleanly by ontology-aware tooling. |

## Relationship Compliance

| Metric | Value |
|---|---:|
| Wiki links observed | 769 |
| Files with wiki links | 80 |
| Notes using untyped `related` metadata plus wiki links | 77 |
| Non-ontology relationship terms detected in code-style relationship mentions | 5 |

The Vault has strong navigational linking, but most links are not expressed with explicit ontology relationship semantics. `related` lists and ordinary wiki-links are useful for navigation, but they do not state whether an edge means `references`, `defines`, `supported_by`, `participates_in`, or another allowed relationship.

### Relationship Violations

| Violation | Files / Examples | Impact |
|---|---|---|
| Untyped relationship edges | Most entity notes use `related: [...]` and body wiki-links without relationship semantics | Skills cannot reliably distinguish evidence support, participation, definition, dependency, and general navigation. |
| Legacy relationship vocabulary | `requires`, `supports`, and older relationship terms appear in some files | These terms are not in the canonical relationship vocabulary unless mapped to `depends_on`, `supported_by`, `documents`, or another allowed edge. |
| `related_to` risk | Several notes use broad related links where a more specific relationship likely exists | The ontology says `related_to` must not hide legal, amendment, evidence, or participation semantics. |
| Relationship evidence not consistently attached | Many links have no explicit evidence record near the relationship | Graph edges may be useful but are not fully evidence-backed. |

### Positive Findings

- Existing reviews already identify unsupported relationship drift, especially around R157/R171 and stale R171/DSSAD confusion.
- The graph is dense enough to support review and navigation.
- Several high-value notes label facts and interpretations separately.

## Folder Compliance

| Area | Status | Notes |
|---|---|---|
| `01 Regulations/` | Compliant | Contains regulation-type notes; ADS UN GTR is represented as `regulation`, though ontology allows a distinct UN GTR type. |
| `04 Working Groups/` | Compliant | Contains working-group notes. |
| `05 Concepts/` | Compliant | Contains concept notes. |
| `07 Organizations/` | Compliant | Contains organization notes. |
| `02 WP29/` and `03 GRVA/` | Acceptable legacy/body-specific folders | Ontology permits body-specific meeting folders where established, but organization duplicates should be resolved. |
| `06 OEM/` | Non-compliant / ontology gap | The ontology does not define `OEM` as an entity type or folder. |
| `11 Review/` | Partially compliant | Correct folder for review artifacts, but review types are inconsistent. |
| `11 Templates/` | Partially compliant | Correct folder for templates, but template frontmatter often uses entity types rather than `template`. |
| `14 Timeline/` | Partially compliant | Correct folder, but timeline notes use `meta` rather than `timeline_event`. |
| `Governance/` | Compliant | New ontology file is correctly placed. |

## Evidence Compliance

| Metric | Value |
|---|---:|
| Files with empty, missing, or `source_pending` source metadata | 57 |
| Files with required metadata gaps | 80 |
| Notes commonly missing `knowledge_type` / `evidence_level` | Regulations, concepts, working groups, organizations |

Evidence compliance is the weakest major dimension. Many high-value notes contain useful evidence in prose, but the ontology requires metadata-level evidence classification through fields such as `knowledge_type`, `evidence_level`, and source authority. Many older placeholder notes use `source: ""` or `source_pending`.

### Evidence Violations

| Violation | Files / Examples | Impact |
|---|---|---|
| Empty source fields | R157, many organizations, OEM notes, placeholders | These entities cannot be treated as evidence-backed. |
| `source_pending` fields | R155, R156, R79, ADS, Type Approval, several research notes | Signals known evidence incompleteness. |
| Missing `knowledge_type` | Many active and draft knowledge notes | Skills cannot consistently distinguish official fact, interpretation, draft, or review material. |
| Missing `evidence_level` | Many entity notes | Evidence hierarchy from Level A-E cannot be evaluated mechanically. |
| Broad website citation | E-Mobility Europe uses general website evidence for some organization facts | Review already flags need for precise page URLs or local captures. |

## Naming Compliance

| Area | Status | Notes |
|---|---|---|
| Regulation names | Mostly compliant | Short identifiers such as `R171` match current Vault convention. |
| Organization names | Mostly compliant | Names are generally human-readable and stable. |
| Meeting names | Mostly compliant | `GRVA 24th Session` and similar names match ontology pattern. |
| Concept names | Mostly compliant | Concept notes mostly use full concept names. |
| Timeline names | Mostly compliant | Timeline notes use entity + `Timeline` pattern. |
| Alias discipline | Partial | Alias and duplicate handling needs cleanup for WP.29/WP29, GRVA, DCAS, DSSAD, and ADS. |

### Naming Violations / Risks

| Risk | Examples | Impact |
|---|---|---|
| Duplicate canonical candidates | `02 WP29/WP29.md` / `07 Organizations/WP.29.md`; `03 GRVA/GRVA.md` / `07 Organizations/GRVA.md` | Splits canonical identity and backlinks. |
| Concept / working-group title overlap | `05 Concepts/DCAS.md` / `04 Working Groups/DCAS.md`; `05 Concepts/DSSAD.md` / `04 Working Groups/DSSAD.md` | Acceptable only if aliases and roles clearly separate concept from group. |
| Abbreviation/full-name overlap | `05 Concepts/ADS.md` / `05 Concepts/Automated Driving System.md` | Risk of definition drift. |
| Unsupported aliases must stay excluded | Historical R171 = DSSAD confusion is correctly isolated in review diagnostics, not current aliases | This is compliant behavior and should be preserved. |

## Violations

| Priority | Violation | Scope | Suggested Owner |
|---|---|---|---|
| Critical | Unsupported `oem` entity type and `06 OEM/` folder are not defined in ontology | 9 files plus template | Governance / Knowledge Merge |
| Critical | Evidence metadata missing across many canonical entities | 80 files with some required metadata gaps | Knowledge Merge |
| Important | Empty or pending source metadata | 57 files | Acquire Knowledge / Knowledge Merge |
| Important | Review artifacts use inconsistent or missing ontology types | `11 Review/` reports and pending items | Knowledge Review |
| Important | Timeline notes use `meta` rather than `timeline_event` | `14 Timeline/*.md` | Knowledge Merge |
| Important | Relationships are mostly untyped wiki-links | 77 linked notes with untyped `related` style | Knowledge Merge / Review |
| Useful | Legacy governance docs use `meta` | `ONTOLOGY.md`, `SCHEMA.md`, `RELATIONSHIPS.md`, etc. | Governance |
| Useful | Duplicate canonical candidates remain unresolved | WP.29, GRVA, DCAS, DSSAD, ADS | Knowledge Review / Merge |

## Suggested Fixes

### Critical

1. Decide whether `OEM` is a first-class ontology entity.
   - Option A: Add `OEM` or `Product Developer` to `Governance/KNOWLEDGE_ONTOLOGY.md`.
   - Option B: Reclassify `06 OEM/*.md` as `organization` with `org_type: oem`.
   - Do not leave `oem` as an unsupported type.

2. Normalize required metadata on canonical knowledge notes.
   - Add `knowledge_type` and `evidence_level` where evidence is known.
   - Preserve `source_pending` or open questions where evidence is not known.
   - Do not upgrade placeholders without evidence.

### High

3. Normalize review artifacts.
   - Use `type: review_artifact` for reports, dashboard, backlog, pending review items, and test reports.
   - Preserve subtype information in a separate field such as `review_type`.

4. Normalize timeline notes.
   - Use `type: timeline_event` or an approved timeline aggregate type.
   - Add `date` or `date_range` when the note represents a single event; use a governance-approved field for aggregate timelines.

5. Add explicit relationship semantics.
   - Convert important links from generic `related` lists into relationship tables or evidence-backed relationship blocks.
   - Use only ontology relationships unless Governance explicitly extends the vocabulary.

### Medium

6. Resolve duplicate canonical candidates.
   - WP.29 and GRVA should each have one canonical institutional page.
   - DCAS and DSSAD should explicitly distinguish concept vs working group.
   - ADS abbreviation/full-name pages should be merged or clearly separated.

7. Improve evidence source granularity.
   - Replace broad website references with precise URLs or local captures.
   - Add source authority levels using the ontology evidence hierarchy.

### Low

8. Decide whether navigation/home notes should be excluded from ontology scoring or assigned a `navigation` / `governance` type.

9. Update templates so new notes are ontology-compliant by default.

## Conclusion

The Vault is usable as a knowledge graph, but it is not yet fully compliant with `Governance/KNOWLEDGE_ONTOLOGY.md`. The most important next step is not rewriting knowledge content; it is normalizing structure: entity types, metadata, evidence levels, and relationship semantics. Once templates and merge behavior produce ontology-compliant notes by default, future reviews can focus on knowledge quality instead of structural cleanup.
