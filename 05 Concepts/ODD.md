---
type: concept
status: active
tags: [concept, ODD, operational-design-domain, ADS, core-concept]
related: [DDT, MRC, ADS, ADS UN GTR, R157, FRAV, New UN Regulation on ADS, Automated Driving System, VMAD, Behavioural Competency, ADS Fallback Response]
source: "ECE/TRANS/WP.29/2026/139, §2.12"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.12 (based on SAE J3016 / FRAV framework)"
aliases: [Operational Design Domain]
---

# ODD — Operational Design Domain

## Official Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.12):**
> "The operating conditions under which an ADS feature is specifically designed to function."

### ODD Exit (§2.12.1):
> "(a) the presence of one or more ODD conditions outside the limits defined for use of the ADS feature, and/or
> (b) the absence of one or more conditions required to fulfil the ODD conditions of the ADS feature."

---

## ODD Parameters Required by Manufacturer (§41(e))

**Fact:** The ODD description must include at minimum:
- Roadway types
- Geographic area
- Speed range
- Environmental conditions (weather, daytime/nighttime)
- Other domain constraints

---

## ODD in Current Regulations

| Regulation | ODD Scope |
|---|---|
| [[R157]] ALKS | Motorway, ≤60 km/h (original), amendments extend to 130 km/h |
| [[ADS UN GTR]] | Manufacturer-defined; GTR is ODD-agnostic — applies to any ODD |

*Note: The GTR's generic requirements apply regardless of ODD (highway, urban, parking). The manufacturer defines the ODD; the ADS must perform safely within it and respond to ODD exits.*

---

## ODD and Validation (Annex 5)

**Fact:** The ODD description is the starting point for the [[Behavioural Competency]] identification process and [[Validation]] scenario generation:

```
ODD description
    → ODD Analysis (characteristics, constraints, dynamic elements)
        → Driving Interactions Analysis (actor behaviours)
            → OEDR Analysis → Behavioural Competencies
                → Scenario generation → Testing
```

---

## ODD Boundary Requirements (§4.1.5)

**Fact:** ADS must:
- Recognise ODD conditions and boundaries
- Prevent activation outside ODD
- Execute fallback response when ODD conditions no longer met
- Anticipate and safely respond to foreseeable ODD exits

For **ADSF-2**: On ODD exit, must aim to bring vehicle to stop in safe location complying with traffic rules (§4.1.5.4.1).

---

## Key Links

- [[DDT]] — performed within ODD
- [[ADS Fallback Response]] — triggered by ODD exit
- [[MRC]] — target state when ODD is exited
- [[R157]] — defines specific ODD (motorway, ≤130 km/h)
- [[Behavioural Competency]] — derived from ODD analysis
- [[VMAD]] — validation methodology operates within ODD framework
