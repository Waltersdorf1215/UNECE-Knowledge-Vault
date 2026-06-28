---
review_type: knowledge_review
scope: "single note"
reviewed_paths:
  - "05 Concepts/Driver Availability.md"
  - "01 Regulations/R171.md"
  - "05 Concepts/Driver Monitoring.md"
  - "05 Concepts/Risk Mitigation Function.md"
  - "05 Concepts/DCAS.md"
  - "01 Regulations/R157.md"
generated: 2026-06-28
review_status: active
---

# Driver Availability Review

## Summary

`05 Concepts/Driver Availability.md` has been upgraded from draft/source-pending to an active, R171-sourced concept note for the UNECE DCAS context. The note now correctly treats Driver Availability as a working concept grounded in R171's official provisions on driver responsibility, driver disengagement, driver monitoring, warning escalation, and Risk Mitigation Function activation.

The main remaining gap is outside the DCAS scope: R157 is still a placeholder note, so the ALKS/transition-demand side of Driver Availability remains pending.

## Knowledge Score

**88 / 100**

| Dimension | Score | Status | Notes |
|---|---:|---|---|
| Completeness | 23 / 25 | OK | Concept sections are now substantive and DCAS-focused. |
| Evidence Quality | 22 / 25 | OK | R171 evidence is strong; R157 comparison remains pending. |
| Relationship Coverage | 14 / 15 | OK | Strong links to Driver Monitoring, RMF, DCAS, R171, Transition Demand, MRM, and R157. |
| Timeline Coverage | 8 / 10 | OK | Timeline is not central for this concept; regulatory provenance is clear through R171. |
| Cross References | 10 / 10 | OK | The note is well integrated into the concept graph. |
| Verification Status | 11 / 15 | Warning | Four open questions remain, mainly around R157, ADS, and EU DMS interaction. |
| **Total** | **88 / 100** | **Good** | Good knowledge with manageable gaps. |

## Coverage

| Area | Status | Notes |
|---|---|---|
| Overview | OK | Summary explains the DCAS meaning and limits of the term. |
| Definition | OK | Anchored to R171's `driver disengagement` definition rather than inventing a formal `driver availability` definition. |
| Regulatory Usage | OK | R171 DCAS usage is clear; R157/ADS items are marked pending. |
| Related Regulations | OK | R171 is primary; R157 and ADS are contextual. |
| Related Concepts | OK | Links to Driver Monitoring, RMF, DCAS, Transition Demand, and MRM. |
| Evidence | OK | Evidence table and source field point to R171 and local Vault notes. |
| References | OK | References section lists local source and supporting notes. |

## Strengths

- Avoids inventing a formal R171 definition for "driver availability"; it uses R171's sourced term "driver disengagement".
- Explains DCAS-specific driver availability without importing unsupported R157 assumptions.
- Clearly separates facts from interpretation.
- Connects the concept to the operational chain: Driver Monitoring -> warning escalation -> DCA -> RMF safe stop.

## Weaknesses

- R157 remains a placeholder, so the ALKS comparison is not yet authoritative.
- EU driver monitoring interaction is still unresolved because the EU DMS raw PDF has not been processed.
- The note is strong for DCAS but not yet complete as a cross-regulation concept.

## Missing Knowledge

| Topic | Gap | Impact | Suggested Source |
|---|---|---|---|
| R157 driver availability | R157 note is placeholder; ALKS availability criteria are not sourced. | Limits cross-regulation comparison. | Official UNECE R157 text |
| ADS fallback-user availability | Driver availability relevance for ADSF-1 vs ADSF-2 is unresolved. | Limits ADS concept integration. | ADS UN GTR / New UN Regulation on ADS |
| EU DMS interaction | Relationship to R(EU) 2023:2590 and R(EU) 2021:1341 is not verified. | Limits EU regulatory context. | EU official regulations already present in raw files |

## Missing Evidence

| Claim / Area | Current Status | Evidence Needed | Suggested Source |
|---|---|---|---|
| R157 availability / transition demand | Needs Verification | Specific R157 clauses defining driver availability or takeover readiness. | Official UNECE R157 text |
| ADS driverless relevance | Needs Verification | ADS clauses distinguishing fallback-user availability from driverless operation. | ADS UN GTR / New UN Regulation on ADS |
| EU DMS interaction | Needs Verification | Clauses connecting EU DMS/DDAW requirements to UNECE DCAS driver monitoring. | Official EU regulations |

## Missing Relationships

| Candidate Relationship | Status | Why It Matters | Evidence Needed |
|---|---|---|---|
| [[R157]] -> [[Driver Availability]] | Recommended, pending | R157 placeholder currently links the concept but lacks sourced detail. | Official UNECE R157 text |
| [[New UN Regulation on ADS]] -> [[Driver Availability]] | Needs Verification | Fallback-user availability may matter for ADSF-1 but not ADSF-2. | ADS UN GTR / New UN Regulation on ADS |

## Missing Timeline

| Milestone | Current Status | Evidence Needed | Suggested Source |
|---|---|---|---|
| R171 source provenance | Present | No further action needed for DCAS scope. | R171 official text |
| R157 source provenance | Missing | Date/source for the R157 driver availability clauses after ingestion. | Official UNECE R157 text |

## Duplicate Candidates

| Candidate Notes | Risk | Recommendation |
|---|---|---|
| `05 Concepts/Driver Availability.md` / `05 Concepts/Driver Monitoring.md` | Low | Keep separate: Driver Monitoring is the system capability; Driver Availability is the assessed state. |
| `Driver Availability` / `Driver Disengagement` future note | Medium | Do not create a separate note unless R171/R157 evidence requires a distinct canonical concept. Keep `Driver Disengagement` as an alias for now. |

## Suggested Improvements

| Priority | Improvement | Owner Skill | Notes |
|---|---|---|---|
| ★★★★ Important | Ingest/update R157 to source the ALKS driver availability and transition demand relationship. | Acquire Knowledge | Needed for cross-regulation completeness. |
| ★★★ Useful | Review ADS UN GTR / New UN Regulation on ADS for fallback-user availability language. | Acquire Knowledge | Clarifies ADSF-1 vs ADSF-2 relevance. |
| ★★ Optional | Process EU DMS/DDAW raw PDFs for EU context. | Acquire Knowledge | Useful but not required for UNECE DCAS answer. |

## Backlog Items

| Priority | Topic | Missing Knowledge | Suggested Source | Estimated Difficulty |
|---|---|---|---|---|
| ★★★★ Important | Driver Availability / R157 | Source ALKS driver availability and transition demand requirements. | Official UNECE R157 text | Medium |
| ★★★ Useful | Driver Availability / ADS | Clarify fallback-user availability in ADSF-1 vs ADSF-2. | ADS UN GTR / New UN Regulation on ADS | Medium |
| ★★ Optional | Driver Availability / EU DMS | Verify EU DMS and DDAW interaction with DCAS driver monitoring. | Official EU regulations | Medium |

## Review Notes

- Knowledge note `05 Concepts/Driver Availability.md` was updated before this review.
- Review artifacts only were created or updated during the review phase.
