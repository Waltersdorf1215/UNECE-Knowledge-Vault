---
type: concept
status: active
tags: [concept, safety-case, ADS, evidence, compliance]
related: [ADS UN GTR, Safety Management System, Validation, VMAD, FRAV, ADS, ODD, Behavioural Competency, OEDR, DSSAD]
source: "ECE/TRANS/WP.29/2026/139, §2.31"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.31"
aliases: [Safety Case]
---

# Safety Case

## Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.31):**
> "Structured documentation that provides a compelling, comprehensible, and valid case that the ADS meets the relevant ADS requirements of this Regulation and is free from unreasonable risks to the ADS vehicle user(s) and other road users."

### Sub-definitions (§2.31.1–2.31.3):
- **Argument (§2.31.1):** Written explanation capturing logical connections between a claim and evidence.
- **Claim (§2.31.2):** A verifiable statement within a safety case.
- **Evidence (§2.31.3):** Material demonstrating the validity of a claim (physical test results, simulation results, analyses).

**Safety concept (§2.32):** Description of measures designed into the ADS so it operates free of unreasonable safety risks in every condition relevant to the ODD.

---

## Role in the ADS GTR

**Fact (§5.3):** The manufacturer must create, maintain, and submit a complete safety case. It must include:
- Description of the ADS system
- ODD description
- Behavioural competencies and scenarios
- Testing evidence (virtual, track, real-world)
- Independent self-assessment
- Evidence that the ADS is free from unreasonable risk

**Fact (§6.3):** The safety case is the primary object of compliance assessment. Assessors verify:
1. **Completeness** — all GTR requirements addressed by claims
2. **Robustness** — all risks mitigated below unreasonable threshold; evidence reproducible

---

## Structure: Claim–Argument–Evidence

The safety case follows a structured claim–argument–evidence architecture:
```
Requirement (from GTR §4)
    → Claim (verifiable statement that requirement is met)
        → Argument (explanation of why evidence supports claim)
            → Evidence (test results, simulation outputs, analyses)
```

**Fact (§5.3.4):** An independent self-assessment by the manufacturer is required before submission to the authority.

---

## Key Links

- [[Safety Management System]] — the SMS framework within which the safety case is developed
- [[Validation]] — testing evidence forms the core of the safety case
- [[VMAD]] — validation methodology determines how evidence is generated
- [[ODD]] — ODD description is a required element
- [[Behavioural Competency]] — competencies are the functional basis for safety case claims
- [[OEDR]] — OEDR performance must be evidenced in the safety case
- [[DSSAD]] — DSSAD description is required in the safety case (§5.3.1.13)
