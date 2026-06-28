# Acquire Knowledge — Example Questions

Ten worked examples showing how the skill handles different query types, vault states, and research paths.

---

## Example 1 — "What is EME?"

**User question:** What is EME in the context of UNECE?

**Step 1 — Vault search:**
- Search `05 Concepts/`, `04 Working Groups/`, `01 Regulations/` for "EME"
- Expected result: `missing` — no EME note exists

**Step 3 — Invoke Deep Research:**
```
Query: "What is EME in UNECE vehicle regulations?
Disambiguate from electromagnetic emissions.
Find: full name, definition, relationship to WP.29/GRVA/DCAS/ADS,
official documents, regulatory status."
```

**Step 5 — Create note:**
- If EME = a working group → create `04 Working Groups/EME.md` using `templates/working_group.md`
- If EME = a concept → create `05 Concepts/EME.md` using `templates/concept.md`
- If EME = a regulation → create `01 Regulations/EME.md` using `templates/regulation.md`

**Step 10 — Answer format:**
```
## Answer
EME stands for [full name]. In the UNECE context, it refers to [definition].
[Sourced from: [source]]

## Vault State After This Acquisition
- Notes created: 05 Concepts/EME.md
- Relationships added: EME → related_to → [entity]
- Knowledge gaps remaining: [any missing fields]
```

---

## Example 2 — "What is DCAS?"

**User question:** What is DCAS?

**Step 1 — Vault search:**
- `05 Concepts/DCAS.md` → exists, `status: active`
- `04 Working Groups/DCAS.md` → exists, `status: draft`

**Vault state:** `exists_complete` for concept; `exists_incomplete` for working group

**Step 2 — Answer from vault (concept):**
- Answer directly from `05 Concepts/DCAS.md` (DCAS definition, SAE L2, R171 reference)
- Note that `04 Working Groups/DCAS.md` is incomplete

**Step 3 — Research gap (working group):**
- Optionally invoke `deep-research` to fill gaps in DCAS working group note
- Or flag the gap for a dedicated session

**Expected answer:** DCAS = Driver Control Assistance Systems. SAE Level 2. Governed by R171 (entry into force 2024-09-22). Distinction from ADS explicitly stated in R171 Introduction §5. [Source: E/ECE/TRANS/505/Rev.3/Add.170]

---

## Example 3 — "Explain R171"

**User question:** Explain R171.

**Step 1 — Vault search:**
- `01 Regulations/R171.md` → exists, `status: active`

**Vault state:** `exists_complete`

**Step 2 — Answer from vault:**
- Full answer from existing R171.md note
- Do NOT invoke deep-research
- Cite: E/ECE/TRANS/505/Rev.3/Add.170

**Expected answer:** R171 = UN Regulation No. 171 on Driver Control Assistance Systems (DCAS). Entered into force 22 September 2024. Authentic text: ECE/TRANS/WP.29/2024/37. Covers Category M and N vehicles. Requires R79, R130, R131/R152, R156 compliance. Driver monitoring: HOR/EOR/DCA escalation. [All from vault — no web research needed]

---

## Example 4 — "What happened at GRVA 25?"

**User question:** What happened at GRVA 25?

**Step 1 — Vault search:**
- `03 GRVA/GRVA 25th Session.md` → exists, `status: placeholder`
- All key sections empty

**Vault state:** `exists_incomplete`

**Step 3 — Invoke Deep Research:**
```
Query: "GRVA 25th session UNECE 2026 outcomes decisions
Automated Driving Systems ADS UN Regulation GTR
Find: date, agenda, key decisions, documents adopted,
IWG reports received. Official UNECE sources only."
```

**Step 5 — Update note:**
- Open `03 GRVA/GRVA 25th Session.md`
- Populate: date, body, agenda items, key decisions
- Upgrade status: `placeholder` → `draft` or `active`

**Evidence requirement:** Every decision must cite an official session report or document number.

---

## Example 5 — "What is VCTF?"

**User question:** What is VCTF?

**Step 1 — Vault search:**
- Search all folders for "VCTF"
- Expected result: `missing`

**Step 3 — Invoke Deep Research:**
```
Query: "VCTF UNECE WP.29 GRVA vehicle regulations
What does VCTF stand for? What is its mandate?
Relate to automated driving, ADAS, or ADS regulation."
```

**Step 5 — Create note:**
- Depending on research result: likely `04 Working Groups/VCTF.md`
- Use `templates/working_group.md`

**Gap detection (Step 9):**
- If VCTF is a task force: check for mandate document, parent body, deliverables
- Flag missing fields as `[VERIFY]`

---

## Example 6 — "What is ADS UN GTR?"

**User question:** What is ADS UN GTR?

**Step 1 — Vault search:**
- `01 Regulations/ADS UN GTR.md` → exists, `status: active`

**Vault state:** `exists_complete`

**Step 2 — Answer from vault:**
- Full answer from existing ADS UN GTR.md note
- Source: ECE/TRANS/WP.29/2026/139

**Expected answer:** ADS UN GTR = UN Global Technical Regulation on Automated Driving Systems. Submitted to WP.29 199th session (Geneva, June 23–26, 2026) under Agenda Item 14.1.1. Recommended by GRVA at its 24th session. Applies to vehicles of Categories 1 and 2. Defines ADSF-1 (with fallback user) and ADSF-2 (driverless). Requires SMS, Safety Case, DSSAD, multi-pillar validation. [All from vault]

---

## Example 7 — "Who submitted GRVA-25-xx?"

**User question:** Who submitted GRVA-25-0012?

**Step 1 — Vault search:**
- Search `09 Proposals/` for "GRVA-25-0012"
- Expected result: `missing` (specific proposal not yet indexed)

**Step 3 — Invoke Deep Research:**
```
Query: "GRVA-25-0012 UNECE GRVA 25th session
Find: submitting delegation or organization, document title,
subject matter, session outcome."
```

**Step 5 — Create note:**
- Create `09 Proposals/GRVA-25-0012.md` using `templates/entity.md`
- Fill: document_number, submitted_by, submitted_to, date, outcome

**Relationship update (Step 7):**
- Link from `03 GRVA/GRVA 25th Session.md` → discusses → `GRVA-25-0012`
- Link to affected regulation if applicable

---

## Example 8 — "Explain Driver Availability"

**User question:** Explain Driver Availability.

**Step 1 — Vault search:**
- `05 Concepts/Driver Availability.md` → exists, `status: active`

**Vault state:** `exists_complete`

**Step 2 — Answer from vault:**
- Answer directly from existing note

**Expected answer:** Driver Availability is the condition where the driver, as assessed by the Driver Monitoring system, is capable of responding to a Transition Demand (R157 context) or of supervising DCAS operation (R171 context). In R171: assessed via motoric disengagement (hands) and visual disengagement (eyes/head posture). Warning escalation: HOR → EOR → DCA → Driver Unavailability Response.

---

## Example 9 — "Explain VMAD"

**User question:** Explain VMAD.

**Step 1 — Vault search:**
- `04 Working Groups/VMAD.md` → exists, `status: active`

**Vault state:** `exists_complete`

**Step 2 — Answer from vault:**
- Answer from existing VMAD note

**Expected answer:** VMAD = Validation Method for Automated Driving. Informal working group under GRVA. Mandate: develop ADS validation methodology — multi-pillar approach (virtual, track, real-world, audit). Key output: NATM (New Assessment/Test Method for Automated Driving), first version ECE/TRANS/WP.29/1159. FRAV/VMAD Integrated Document: ECE/TRANS/WP.29/2024/39. Technical basis for ADS UN GTR validation framework. [All from vault]

---

## Example 10 — "What is ACPE?"

**User question:** What is ACPE?

**Step 1 — Vault search:**
- Search all folders for "ACPE"
- Check: `04 Working Groups/`, `05 Concepts/`, `01 Regulations/`
- Note: ACPE appears in `seed.json` as a GRVA programme area (id=192841078, "Acceleration Control for Pedal Error") but no note exists
- Expected vault state: `missing` (no note, but seed data available)

**Step 1b — Check seed.json:**
- `Skills/Acquire/output/seed.json` → contains ACPE as a top-level GRVA group
- Use as starting point before invoking deep-research

**Step 3 — Invoke Deep Research (if seed data insufficient):**
```
Query: "ACPE UNECE GRVA Acceleration Control for Pedal Error
What is it? Is it a regulation, working group, or technical topic?
Relationship to GRVA, automated driving, ADAS.
Official documents and status."
```

**Step 5 — Create note:**
- Depending on result: likely `04 Working Groups/ACPE.md` or concept note
- Use `templates/working_group.md` if it's a GRVA task force

**Key disambiguation:** ACPE is likely "Acceleration Control for Pedal Error" — a safety system preventing unintended acceleration from pedal misapplication. Confirm from research.

---

## Quick Reference: Query Construction

When invoking `deep-research`, always structure the query as:

```
[Entity name] [UNECE/WP.29/GRVA context]
Find:
(1) Full name and definition
(2) Regulatory status and document numbers
(3) Parent body and related entities
(4) Timeline / key milestones
(5) Distinguish from [similar or conflicting terms]
Sources: official UNECE documents only; no LLM speculation
```
