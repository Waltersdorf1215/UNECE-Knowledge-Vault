---
type: concept
status: active
tags: [concept, behavioural-competency, ADS-validation, ODD, scenarios]
related: [ADS UN GTR, ODD, DDT, Validation, VMAD, Safety Case, OEDR, Automated Driving System]
source: "ECE/TRANS/WP.29/2026/139, §2.22 and Annex 5"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.22"
aliases: [Behavioural Competencies]
---

# Behavioural Competency

## Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.22):**
> "An expected and verifiable capability of an ADS feature to operate a vehicle within the ODD of the feature."

---

## Role in Validation

**Fact (Annex 5):** Behavioural competencies are the bridge between ODD conditions and validation scenarios:

```
ODD description
    → Behavioural Competency Identification (via ODD analysis, Driving interactions, OEDR)
        → Scenario generation (functional → abstract → logical → concrete)
            → Testing (virtual, track, real-world)
                → Evidence for Safety Case
```

---

## Three Categories of Competency (Annex 5, §1.2)

**Fact:** Competencies track three driving situation categories:

| Category | Description |
|---|---|
| Nominal | Neither critical nor failure; other road users behave reasonably; no relevant failures |
| Critical | Requires prompt ADS action to avoid/mitigate crash risk; other road users may behave unreasonably |
| Failure | ADS or vehicle system failure compromises DDT capability |

---

## Competency Identification Approach (Annex 5, §2.1)

Three analytical frameworks:
1. **ODD Analysis** — identify ODD characteristics (infrastructure, environment, dynamic elements)
2. **Driving Interactions Analysis** — map actor behaviours and interactions within ODD
3. **OEDR Analysis** — map ADS response to each detected object/event → generates behavioural competency

---

## Example Competencies (Annex 5, Tables 2–4)

**Fact (Table 2 examples):**

| Event | Competency (Response) |
|---|---|
| Lead vehicle decelerating | Follow vehicle, decelerate, stop |
| Vehicle cutting in | Yield, decelerate, stop, follow vehicle |
| Pedestrian crossing road | Yield, decelerate, stop |
| Cyclist riding in lane | Yield, follow |

---

## Key Links

- [[ODD]] — ODD description determines which competencies are required
- [[OEDR]] — OEDR analysis generates competency specifications
- [[Validation]] — competencies are the basis for scenario-based validation
- [[Safety Case]] — competencies form the functional basis for safety case claims
- [[VMAD]] — developed the competency framework methodology
