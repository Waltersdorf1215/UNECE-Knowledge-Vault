---
type: review_item
review_status: partially_resolved
entities: [R157, R171]
proposed_relationship: "companion | data-recording companion | derives from | is prerequisite of"
evidence_strength: unsupported
confidence: needs_review
created: 2026-06-27
source_of_concern: "Generated during vault knowledge synthesis — these relationships were written as analytical shorthand without explicit source citations"
related: [R157, R171, DCAS, Driver Monitoring, Driver Availability, Event Data Recorder, DSSAD]
tags: [review, evidence-gate, R157, R171, inference-drift]
last_updated: 2026-06-28
---

# R157–R171 Evidence Review

This review item was created because previously generated knowledge claims presented inferred relationships between R157 (ALKS) and R171 (DCAS) as if they were official regulatory facts. Those claims have been blocked from the main knowledge graph pending evidence confirmation.

---

## Unsupported Claims Previously Generated

The following statements appeared in vault notes or session outputs without explicit source citations:

1. **"R157 is the first regulation that mandatorily references R171."**
   — No source document found. No official UNECE text reviewed in this vault states this.

2. **"R171 is the data-recording companion regulation of R157."**
   — No source document found. "Companion regulation" is informal shorthand; no official UNECE document reviewed uses this phrase.

3. **"R171 derives from R157's driver monitoring requirements."**
   — No source document found. This is an inferred developmental lineage with no citation.

4. **"R155 and R156 are prerequisites for R157 type approval."**
   — The ADS UN GTR (ECE/TRANS/WP.29/2026/139, Section F, category c) lists R155 and R156 as "other standards identified" but NOT as directly referenced requirements in the GTR text. Whether R155/R156 are formal prerequisites for R157 type approval requires reading the R157 text, which has not been ingested into this vault.

---

## Why These Claims Are Unsafe

### Conceptual Co-occurrence ≠ Legal Dependency

R157 (ALKS) and R171 (DCAS) share several technical concepts:
- Driver monitoring
- Driver availability
- System status indicators
- Fallback behavior
- Event recording / data storage

This conceptual overlap is real. However, the existence of shared concepts does **not** mean:
- That one regulation cites or depends on the other
- That one was developed because of the other
- That they form part of a coordinated regulatory package
- That compliance with one is required for compliance with the other

These conclusions require explicit statements in official UNECE documents. None have been found.

### The Forbidden Transformation in Action

The following chain of reasoning was detected and is now prohibited:

```
Observation (Class 3 — Conceptual):
"R157 and R171 both address event recording and driver monitoring."

↓ Forbidden transformation (generates unsupported Class 1 relationship):

False conclusion:
"R171 is the data-recording companion of R157."
```

This transformation converts a conceptual observation into a legal claim. It is the core pattern that the Evidence Gate (IMPORT_PIPELINE.md Stage 7.2) is designed to prevent.

---

## Accurate Description of the R157–R171 Relationship

**Fact (source: ECE/TRANS/WP.29/2026/139, §82):**
> "Currently, there is only one specific ADS application for which a UN ADS regulation has been developed (ALKS/R157)."
This confirms R157 is the ALKS regulation. R171 is not mentioned in this context.

**Safe wording — currently supportable:**

> R157 and R171 address different regulatory objects. R157 concerns Automated Lane Keeping Systems (ALKS), while R171 concerns Driver Control Assistance Systems (DCAS). They may share concepts such as driver monitoring, driver availability, system status, fallback behaviour, and event-related evidence, but this conceptual similarity must not be treated as a legal dependency unless explicitly supported by official UNECE text.

This wording:
- States what each regulation covers (factual, based on their titles and scope)
- Acknowledges conceptual overlap without asserting dependency
- Does not imply one is a companion of, predecessor to, or prerequisite for the other
- Does not assert any citation or cross-reference between them

---

## Relationship Status

| Proposed Relationship | Class | Status |
|---|---|---|
| R157 `companion` R171 | Class 3 (Conceptual) | Blocked — no evidence |
| R157 `references` R171 | Class 1 (Official) | Blocked — no evidence |
| R171 `derives_from` R157 | Class 4 (Interpretive) | Blocked — no evidence |
| R157 `requires` R155/R156 | Class 1 (Official) | Blocked — requires reading R157 text |
| R157 `shares_concept_with` R171 | Class 3 (Conceptual) | Permitted with `*Interpretation:*` label in concept notes |

---

## Evidence Needed to Resolve This Review

To upgrade any blocked relationship from this list to an official graph relationship, the following evidence is required:

| Claim to confirm | Evidence needed |
|---|---|
| R157 cites or references R171 | Read R157 full text — find explicit cross-reference to R171 |
| R171 cites or references R157 | Read R171 full text — find explicit cross-reference to R157 |
| R155/R156 are prerequisites for R157 | Read R157 type approval provisions — find explicit precondition language |
| R157 and R171 share a coordinated scope | Read WP.29 or GRVA documents that discuss both regulations together |

**Priority:** Ingest R157 text (currently not in vault) and R171 text (partial — ADAS-37-02 supplement available locally but unread).

---

## Resolution Options

**Option A — Confirm as Class 3 (Conceptual)**
If R157 and R171 share concepts but no official cross-reference is found after reading both texts, write in the relevant concept notes:
`*Interpretation:* Both [[R157]] and [[R171]] address [concept]; this conceptual overlap does not constitute a legal cross-reference.`

**Option B — Upgrade to Class 1 (Official)**
If R157 or R171 explicitly references the other in its text, store the relationship with full citation:
`R157 → references → R171 [Fact: R157 text, §X.Y, explicit, high]`

**Option C — Reject permanently**
If after reading both regulation texts no cross-reference is found, move this review item to `Rejected/` with the note: "No cross-reference found in either text. Conceptual overlap only."

---

## Open Questions

1. Does R157 contain any explicit reference to R171 or DCAS?
2. Does R171 contain any explicit reference to R157 or ALKS?
3. Do any GRVA session documents discuss R157 and R171 together as a regulatory package?
4. Does any WP.29 or GRVA decision describe R171 as a "companion" to R157?
5. Are R155 and R156 formally listed as preconditions in the R157 type approval provisions?

---

## Partial Resolution — 2026-06-28

**R171 full text read (E/ECE/TRANS/505/Rev.3/Add.170) on 2026-06-28.**

**Finding:** R171 contains **no cross-reference to R157** anywhere in its 80 pages. The words "R157", "Regulation No. 157", "ALKS", or "Automated Lane Keeping" do not appear in the R171 text.

**Status update:**
- Option A (confirm as Class 3 conceptual): applicable — both share concepts (driver monitoring, fallback, lane keeping) but R171 makes no legal reference to R157
- Option C (reject permanently): also applicable for the specific proposed relationships (companion, prerequisite, derives from)

**Recommended resolution:** Move to `Rejected/` with the note: "R171 full text confirms no cross-reference to R157. The proposed relationship types (companion, data-recording companion, derives from, prerequisite) are all unsupported. Conceptual overlap (driver monitoring, lane keeping, fallback) is acknowledged but does not constitute legal dependency."

**Still pending:**
- R157 full text not yet ingested — cannot confirm whether R157 references R171
- Add R157 full text ingestion to `ROADMAP.md` High Priority

## Next Action

- Move this review item to `11 Review/Rejected/` with the resolution note above
- Keep `R157 → references → R171` as `[VERIFY]` until R157 is read
- Add R157 text ingestion to `ROADMAP.md`
