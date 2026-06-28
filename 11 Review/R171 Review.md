---
review_type: knowledge_review
scope: "single note"
reviewed_paths:
  - "01 Regulations/R171.md"
  - "14 Timeline/R171 Timeline.md"
  - "11 Review/Pending/R157-R171-evidence-review.md"
  - "11 Review/Pending/R171-copilot-context-mismatch.md"
  - "11 Review/Pending/R171-persistent-context-error.md"
generated: 2026-06-28
review_status: active
---

# R171 Review

## Summary

`01 Regulations/R171.md` is a strong, active regulation note with official R171 evidence for scope, definitions, DCAS requirements, driver monitoring, prerequisite systems, RMF, validation, in-service monitoring, and GDPR/data-protection implications. It is not complete as a full lifecycle regulation note because several historical, amendment, EU-applicability, and linked-entity gaps remain unresolved.

No research was performed. This review uses only current Vault content.

## Knowledge Score

**88 / 100**

Previous score before GDPR section: **84 / 100**

| Dimension | Score | Status | Notes |
|---|---:|---|---|
| Completeness | 23 / 25 | Warning | Core regulation content is strong and now includes GDPR implications; amendment history still needs work. |
| Evidence Quality | 23 / 25 | OK | Official R171 and GDPR evidence are strong; supplement and EU type-approval applicability remain weak. |
| Relationship Coverage | 13 / 15 | OK | Rich related graph, but some linked entities are placeholders or pending evidence. |
| Timeline Coverage | 6 / 10 | Warning | Entry into force is sourced; adoption session, Supplement 2, Phase 2, and Phase 3 official document number remain unresolved. |
| Cross References | 9 / 10 | OK | Strong links to regulations, concepts, and working groups. |
| Verification Status | 14 / 15 | Warning | GDPR gap reduced; several non-GDPR lifecycle questions remain material. |
| **Total** | **88 / 100** | **Good** | Useful and trustworthy for original R171 DCAS text and GDPR implications; incomplete for amendment lifecycle and external applicability. |

## Coverage

| Area | Status | Notes |
|---|---|---|
| Overview | OK | Summary identifies R171, DCAS, entry into force, and authentic text. |
| Scope | OK | Scope and R79 exclusion are present with citations. |
| Definitions | OK | Key official definitions from §2 are present. |
| Key Requirements | OK | Prerequisite systems, software updates, RMF, driver monitoring, validation, and reporting are covered. |
| Amendment History | Warning | Original version is sourced; Supplement 2, 01 series, 02 series, and Phase 4 are incomplete. |
| Relationships | Warning | Major relationships are present; some linked context notes remain placeholders or pending. |
| References | Warning | Document References exist, but there is no dedicated consolidated References/Evidence section. |
| Evidence | Warning | R171/GDPR evidence is strong; local DOCX/EU raw PDFs and GRVA/WP.29 amendment sources are not processed. |

## Knowledge Gaps

| Priority | Gap | Current Vault Evidence | Suggested Source |
|---|---|---|---|
| ★★★★ Important | WP.29 adoption session for original R171 | Entry into force is confirmed; adoption session is `[VERIFY]` in timeline and open questions. | Official WP.29 report or adoption document |
| ★★★★ Important | Supplement 2 / 01 series content | Local DOCX exists but is not processed. | Local `raw/ADAS-37-02...docx` |
| ★★★★ Important | R171 02 series / Phase 3 official document number | EME document confirms GRVA 24th progress, but official document number is missing. | Official GRVA/WP.29 working document or report |
| ★★★ Useful | EU applicability / mandate | EU context raw PDFs are listed but unread; mandatory applicability is unresolved. | Official EU regulations already in `raw/` |
| ★★★ Useful | GDPR implementation detail | GDPR implications are now covered at principle level; concrete retention periods and authority expectations are not specified. | Type approval authority guidance or implementation documentation |
| ★★★ Useful | Linked working group context | `ADAS TF.md` and `DCAS.md` are still thin/placeholder-like. | Existing local notes plus official working documents |
| ★★ Optional | OEM context | NIO/Xpeng type approval interest is open, not evidenced. | Official type approval records or OEM submissions |

## Missing Evidence

| Claim / Area | Current Status | Evidence Needed |
|---|---|---|
| WP.29 adoption session date | Needs Verification | Named WP.29 session/report that adopted R171 original version. |
| Supplement 2 changes | Needs Verification | Parsed content and source mapping from local ADAS-37-02 DOCX. |
| 01 series / Phase 2 consideration | Needs Verification | Official meeting or working document confirming consideration/adoption. |
| 02 series / Phase 3 official document number | Needs Verification | Official GRVA/WP.29 document number and decision record. |
| EU mandatory applicability | Needs Verification | Official EU legal basis and applicability dates, if any. |
| GDPR retention / reporting schema | Needs Verification | Concrete retention period, anonymisation/pseudonymisation practice, and expected reporting schema for R171 in-service monitoring. |
| OEM type-approval relevance | Needs Verification | Official approval record, submission, or OEM source. |

## Missing Relationships

| Candidate Relationship | Status | Evidence Needed |
|---|---|---|
| [[WP29]] -> adopts -> [[R171]] | Recommended, pending | Official WP.29 adoption report/session reference. |
| [[ADAS TF]] -> develops/modifies -> [[R171]] amendments | Recommended, partial | Official ADAS TF/GRVA documents for Supplement 2 and later amendment series. |
| [[E-Mobility Europe]] -> contributes_to -> [[R171]] Phase 3/4 | Present in EME review, but not yet mirrored in R171 note | Evidence already in local ADAS-45-07, plus merge decision. |
| [[NIO]] / [[Xpeng]] -> implements or engages with -> [[R171]] | Needs Verification | Official type approval record or submission. |

## Missing Timeline

| Milestone | Current Status | Evidence Needed |
|---|---|---|
| Original adoption by WP.29 | Missing | WP.29 session/date/document. |
| Supplement 2 / 01 series | Partial | Confirmed source and adoption/consideration dates. |
| R171 02 series / Phase 3 | Partial | Official document number and decision record. |
| Phase 4 / 03 series outlook | Partial | Official mandate/timeline beyond EME proposal context. |
| EU applicability | Missing | EU legal basis and dates. |
| GDPR retention/reporting practice | Missing | Authority or implementation guidance for R171 in-service monitoring data. |

## Duplicate Candidates

| Candidate Notes | Risk | Recommendation |
|---|---|---|
| `05 Concepts/DCAS.md` / `04 Working Groups/DCAS.md` | Medium | Keep separate if one is concept and one is working group; review titles and aliases to avoid ambiguity. |
| `07 Organizations/GRVA.md` / `03 GRVA/GRVA.md` | Medium | Known duplicate candidate from `REVIEW_PIPELINE.md`; affects R171 graph context. |

## Suggested Improvements

| Priority | Improvement | Owner Skill | Notes |
|---|---|---|---|
| ★★★★ Important | Process local ADAS-37-02 DOCX and extract Supplement 2 changes. | Acquire Knowledge / Knowledge Merge | Local source exists; no web research needed if processing local file. |
| ★★★★ Important | Confirm WP.29 adoption session and R171 02 series official document number. | Acquire Knowledge | Requires official meeting/working document evidence. |
| ★★★ Useful | Add a dedicated `References` / `Evidence` section to R171. | Knowledge Merge | Current Document References are useful but not a full evidence register. |
| ★★★ Useful | Review and improve ADAS TF / DCAS working group notes. | Acquire Knowledge / Knowledge Merge | R171 relies on these graph neighbors. |
| ★★ Optional | Verify EU applicability and OEM context. | Acquire Knowledge | Useful for deployment relevance, not required for core R171 text. |

## Backlog Items

| Priority | Topic | Missing Knowledge | Suggested Source | Estimated Difficulty |
|---|---|---|---|---|
| ★★★★ Important | R171 | WP.29 adoption session/date for original regulation | Official WP.29 report or adoption document | Medium |
| ★★★★ Important | R171 Supplement 2 | Content and legal effect of ADAS-37-02 Supplement 2 / 01 series | Local ADAS-37-02 DOCX | Medium |
| ★★★★ Important | R171 02 series | Official document number and decision record for Phase 3 / 02 series | Official GRVA/WP.29 working document or meeting report | Medium |
| ★★★ Useful | R171 EU context | EU mandatory applicability and relationship to EU DMS/DDAW/ELKS/ISA acts | Official EU regulations already in `raw/` | Medium |
| ★★★ Useful | R171 GDPR implementation | Retention, reporting schema, and anonymisation/pseudonymisation expectations for in-service monitoring data | Type approval authority guidance or implementation documentation | Medium |
| ★★★ Useful | R171 graph context | ADAS TF and DCAS working group notes need fuller evidence | Official working documents | Medium |

## Review Update — 2026-06-28 — GDPR Section

The GDPR section was added to `01 Regulations/R171.md` after acquiring the missing section from official GDPR text and existing R171 Vault evidence.

| Score | Value |
|---|---:|
| Before GDPR section | 84 / 100 |
| After GDPR section | 88 / 100 |

Improvement drivers:
- Added GDPR/data-protection coverage for R171 driver monitoring, safety-critical occurrence notification, periodic reporting, and in-service monitoring.
- Grounded GDPR implications in Regulation (EU) 2016/679 Articles 4, 5, 6, 25, and 35.
- Preserved distinction between official facts and interpretations.

Remaining GDPR-specific gap:
- Concrete retention periods, reporting schemas, and anonymisation/pseudonymisation expectations for R171 in-service monitoring data remain `[VERIFY]`.

## Review Notes

- `01 Regulations/R171.md` was modified before this review update to add the GDPR/data-protection section.
- External lookup was limited to official GDPR text for the missing GDPR section.
- The review phase updated review/backlog artifacts under `11 Review/`.
