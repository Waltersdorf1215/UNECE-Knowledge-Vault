---
type: research_note
status: active
tags: [review, inference-drift, quality-control, epistemics]
related: [KNOWLEDGE_RULES, CLAUDE, IMPORT_PIPELINE, RELATIONSHIPS, SCHEMA]
source: "Internal audit — vault scan 2026-06-27"
last_updated: 2026-06-27
created: 2026-06-27
question: "Which existing notes contain statements that may be inferred relationships presented as official facts?"
---

# Inference Drift Report

Internal audit of the UNECE Knowledge OS vault. Identifies statements in authoritative notes that may have been written as facts but are actually interpretations, inferences, or personal framings.

**No notes have been modified.** This report is for manual review and decision.

For each item: decide whether to (a) keep as-is with an added *Interpretation:* label, (b) find a source that confirms it, or (c) revise or remove.

---

## Severity Legend

| Level | Meaning |
|---|---|
| 🔴 High | Stated as established fact; likely to mislead; no source found |
| 🟡 Medium | Interpretive framing; useful but needs labeling |
| 🟢 Low | Analytical shorthand; correct in spirit but technically inferred |

---

## Audit Findings

---

### 1. R155.md — "Foundational Enabler" and "Prerequisites"

**File:** `01 Regulations/R155.md`
**Severity:** 🔴 High

**Statements flagged:**

> "R155 is a **foundational enabler**, not a function-specific regulation."

> "R156 (SUMS) ─── prerequisites for ADS type approval"

> "[[R156]] — companion software update regulation (both form prerequisites for ADS approval)"

**Why it may be inference:**
- The phrase "foundational enabler" does not appear in R155, the ADS UN GTR, or any other UNECE document reviewed. It is an analytical characterization.
- R155 and R156 as "prerequisites" for ADS type approval: the ADS UN GTR (§4.3.2–4.3.3) requires ADS to have cybersecurity and software update processes — but it does not explicitly state that R155 and R156 type approvals are required as preconditions. This may be true in the EU type-approval framework, but the GTR itself lists R155 and R156 only as "other standards identified" (Section F, category (c)), not as directly referenced.
- "Companion regulation" is shorthand with no official basis.

**Suggested correction:**
Replace unqualified assertions with: `*Interpretation:* R155 and R156 are widely understood as enabling conditions for ADS deployment, and the ADS UN GTR requires equivalent cybersecurity (§4.3.2) and software update management (§4.3.3) processes. Whether R155 and R156 type approval are formally required as preconditions requires [VERIFY — read R157/ADS UN Regulation type approval provisions].`

---

### 2. R156.md — "Companion Regulation" and "Precondition"

**File:** `01 Regulations/R156.md`
**Severity:** 🔴 High

**Statements flagged:**

> "It is the companion regulation to [[R155]] (cybersecurity) and forms part of the ADS regulatory enablement stack."

> "R156 compliance is a precondition for [[R157]] type approval"

> "expected to be a precondition for the [[New UN Regulation on ADS]]"

**Why it may be inference:**
- "Companion regulation" and "enablement stack" are analytical framings without official basis.
- "Precondition for R157 type approval" may be true under the R157 text — but R157 has not been read in this vault. The claim cannot be cited.
- "Expected to be a precondition for the New UN Regulation on ADS" is explicitly a prediction/inference.

**Suggested correction:**
Label the precondition statement as `*Interpretation:*` and add `[VERIFY — read R157 text for explicit precondition language]`.

---

### 3. R171.md — "Upper Boundary of Assisted Driving"

**File:** `01 Regulations/R171.md`
**Severity:** 🟡 Medium

**Statement flagged:**

> "R171 represents the **upper boundary of assisted driving** in the UNECE regulatory ladder, positioned directly below [[R157]] (ALKS, Level 3)."

**Why it may be inference:**
- "Upper boundary of assisted driving" and "regulatory ladder" are analytical frameworks developed in this vault. No UNECE document uses this framing.
- The characterization of R171 as "below" R157 in a hierarchy is an interpretation of the SAE Level system, not an official UNECE statement.

**Note:** The statement is analytically sound and useful. It should be preserved but labeled.

**Suggested correction:**
`*Interpretation:* In the SAE-level framework, R171 (DCAS, L2) sits below R157 (ALKS, L3) in terms of automation level, and together they represent a progression from assisted to automated driving. This "regulatory ladder" framing is not used in official UNECE documents.`

---

### 4. R79.md — "Foundational Regulation" / "Base of the Ladder"

**File:** `01 Regulations/R79.md`
**Severity:** 🟡 Medium

**Statement flagged:**

> "R79 is the foundational regulation for lateral vehicle control, sitting at the base of the UNECE automated driving regulatory ladder."

**Why it may be inference:**
- "Foundational regulation" and "base of the regulatory ladder" are analytical framings. No UNECE document uses this language.
- The "regulatory ladder" concept is a vault-internal analytical tool.

**Suggested correction:**
Label as `*Interpretation:* R79 governs steering equipment and its ACSF amendments cover lateral automation up to Level 2. In the analytical framework of this vault, it is the lowest rung of the automated driving regulatory stack, though this hierarchical framing does not appear in official UNECE documents.`

---

### 5. New UN Regulation on ADS.md — "Regulatory Ladder" Diagram

**File:** `01 Regulations/New UN Regulation on ADS.md`
**Severity:** 🟡 Medium

**Statement flagged:**

> "This regulation sits above [[R171]] (DCAS — assisted driving) and extends beyond [[R157]] (ALKS — limited L3 highway) in the regulatory ladder"

> "[[Cybersecurity]] — [[R155]] compliance expected as precondition"
> "[[Software Update]] — [[R156]] compliance expected as precondition"

**Why it may be inference:**
- The "regulatory ladder" is a vault-internal framework.
- R155/R156 as "expected preconditions" is speculative (uses "expected") — it should be labeled explicitly.

**Suggested correction:**
Add `*Interpretation:*` label before the ladder description and note that the ladder framing is analytical. Change "expected as precondition" to `[VERIFY — requires reading the 1958 Agreement UN Regulation text when available]`.

---

### 6. DCAS.md (Concept) — "Top of the Assisted Driving Tier"

**File:** `05 Concepts/DCAS.md`
**Severity:** 🟡 Medium

**Statement flagged:**

> "DCAS represents the regulatory concept at the top of the **assisted driving** tier in the UNECE framework — above simple lateral-only assistance ([[R79]] ACSF) and below automated driving ([[R157]] ALKS, [[New UN Regulation on ADS]])."

**Why it may be inference:**
- The "assisted driving tier" hierarchy is an analytical construct, not an official UNECE classification.

**Suggested correction:**
Label: `*Interpretation:* In the analytical framework of this vault, DCAS occupies the L2 tier between R79's L1–L2 lateral-only assistance and R157's L3 automated lane keeping.`

---

### 7. Software Update.md and Cybersecurity.md — "Companion" Cross-References

**Files:** `05 Concepts/Software Update.md`, `05 Concepts/Cybersecurity.md`
**Severity:** 🟢 Low

**Statements flagged:**
- `Software Update.md`: "[[R155]] — companion cybersecurity regulation"
- `Cybersecurity.md`: "[[R156]] — software update companion regulation"

**Why it may be inference:**
- "Companion regulation" is informal shorthand; no official document uses this phrase.

**Suggested correction:**
Replace with: "[[R155]] — the parallel cybersecurity regulation, both adopted alongside R156 in 2021." No label needed if phrased descriptively rather than categorically.

---

### 8. SOTIF.md — "Companion Standard (ISO 26262)"

**File:** `05 Concepts/SOTIF.md`
**Severity:** 🟢 Low

**Statement flagged:**

> "[[Functional Safety]] — companion standard (ISO 26262)"

**Why it may be inference:**
- "Companion standard" is informal; ISO documents describe ISO 21448 (SOTIF) and ISO 26262 (functional safety) as complementary but do not use the word "companion."

**Suggested correction:**
Replace with: "[[Functional Safety]] — related standard (ISO 26262); ISO 21448 addresses safety risks not covered by ISO 26262."

---

### 9. R155.md and R156.md — "ADS Regulatory Enablement Stack"

**Files:** `01 Regulations/R155.md`, `01 Regulations/R156.md`
**Severity:** 🟡 Medium

**Statement flagged (R155.md):**

> "It applies across all vehicles with automated or connected functions"

**Why it may be inference:**
- R155 applies to vehicles with certain connected functions as defined in the regulation. The phrase "all vehicles with automated or connected functions" may be broader than the actual scope. Requires reading the R155 text to confirm scope.

**Suggested correction:**
Add `[VERIFY — confirm scope from R155 text]` until R155 is read.

---

### 10. ADS UN GTR.md — "Trilogy" Language Absent; "Precondition" Usage

**File:** `01 Regulations/ADS UN GTR.md`
**Severity:** 🟢 Low

The ADS UN GTR note is largely well-sourced from ECE/TRANS/WP.29/2026/139. However, the statement:

> "This makes R155 a gating requirement for the entire ADS regulatory pathway."

appears in `R155.md` but derives from the GTR note's framing. The GTR (Section F, category c) lists R155 and R156 as "other standards identified" — not as directly referenced requirements. The GTR's own §4.3.2–4.3.3 requires cybersecurity and software update management processes, but does not cite R155 or R156 as the required instrument.

**Note:** The ADS UN GTR note itself is generally well-labeled. The drift occurs downstream in R155.md and R156.md which overstate the GTR's relationship to those regulations.

---

## Statements Confirmed as Facts (No Action Needed)

The following patterns were flagged by the keyword scan but are correctly written:

| Location | Statement | Why Confirmed |
|---|---|---|
| `Automated Driving System.md` | "When the ADS feature is active, the DDT is always performed in its entirety by the ADS **which means**..." | Labeled `**Fact (ECE/TRANS/WP.29/2026/139, §2.3.1):**` — the "which means" is a paraphrase of the official text, not an inference. Correct as labeled. |
| `IMPORT_PIPELINE.md`, `KNOWLEDGE_RULES.md`, `CLAUDE.md` | Various "which means", "in practice" etc. | These are meta-documents defining process, not regulatory claims. No issue. |
| `ONTOLOGY.md` | "designed to" | Refers to the vault's own design, not regulatory claims. No issue. |
| `10 Research Notes/` | All Interpretation/Insight-labeled content | Research notes are the intended home for interpreted content. Correct. |

---

## Priority Action Queue

In order of urgency (before next knowledge import):

1. **🔴 R155.md** — Remove "foundational enabler", label "prerequisites" as *Interpretation:*, add `[VERIFY]` for precondition claim
2. **🔴 R156.md** — Label "companion regulation" as shorthand, label "precondition" claims as *Interpretation:*, add `[VERIFY]`
3. **🟡 R171.md** — Label "upper boundary / regulatory ladder" as *Interpretation:*
4. **🟡 New UN Regulation on ADS.md** — Label ladder diagram as *Interpretation:*, change "expected as precondition" to `[VERIFY]`
5. **🟡 R79.md** — Label "foundational / base of ladder" as *Interpretation:*
6. **🟡 DCAS.md (concept)** — Label tier framing as *Interpretation:*
7. **🟢 Software Update.md, Cybersecurity.md** — Replace "companion" with descriptive language
8. **🟢 SOTIF.md** — Replace "companion standard" with "related standard"

---

## Notes on the "Regulatory Ladder" Framework

The "regulatory ladder" concept (R79 → R171 → R157 → New ADS Regulation) is a useful analytical tool that appears throughout the vault. It is **not stated anywhere in official UNECE documents**. It should be treated consistently as an *Interpretation:* — a synthesis of the regulatory landscape, not an official characterization.

Consider creating a dedicated Research Note: `10 Research Notes/Regulatory Ladder Framework.md` that houses this analytical construct explicitly, with all the ladder diagrams consolidated there as *Interpretation:* content.

---

## What Was Not Flagged

The following classes of statement passed review and do not require action:
- All statements labeled `**Fact (source §X):**` with inline citations
- All statements labeled `*Interpretation:*`
- All statements labeled `[VERIFY]`
- All statements in `10 Research Notes/` labeled as insights or interpretations
- Definitions quoted verbatim from ECE/TRANS/WP.29/2026/139 with citations
