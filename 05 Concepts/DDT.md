---
type: concept
status: active
tags: [concept, DDT, dynamic-driving-task, SAE, core-concept]
related: [ODD, MRC, ADS, ADAS, R157, R171, ADS Fallback Response, Driver Availability, Automated Driving System, FRAV, OEDR, Behavioural Competency]
source: "ECE/TRANS/WP.29/2026/139, §2.3"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.3 (based on SAE J3016)"
aliases: [Dynamic Driving Task]
---

# DDT — Dynamic Driving Task

## Official Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.3):**
> "The real-time operational and tactical functions required to operate the vehicle."

**Excludes strategic functions (§2.3.5)** such as trip planning and destination selection.

---

## DDT Subcategories (§2.3.1–2.3.4)

**Fact:** The DDT is grouped into three interdependent categories:

### Sensing and Perception (§2.3.2)
- Monitoring driving environment via object/event detection, recognition, classification
- Perceiving other vehicles, road users, roadway, objects, environmental conditions
- Sensing ODD boundaries
- Positional awareness

### Planning and Decision (§2.3.3)
- Predicting actions of other road users
- Response preparation
- Manoeuvre planning

### Control (§2.3.4)
- Object and event response execution
- Lateral vehicle motion control (steering)
- Longitudinal vehicle motion control (acceleration/deceleration)
- Enhancing conspicuity via lighting and signalling

---

## DDT and ADS

**Fact (§2.3.1):** "When the ADS feature is active, the DDT is always performed in its entirety by the ADS."

**Fact (§2.5.1–2.5.2):**
- **Operational functions** = real-time vehicle motion control (split-second reactions)
- **Tactical functions** = perceive environment, plan, decide, execute manoeuvres (seconds timescale)

---

## Who Performs the DDT

| Regulation | DDT Performer |
|---|---|
| [[R79]] ACSF (L1–L2 lateral) | Driver (system assists lateral only) |
| [[R171]] DCAS (L2 combined) | Driver (system assists lateral + longitudinal) |
| [[R157]] ALKS (L3) | System within ODD; driver on system-initiated deactivation request |
| [[ADS UN GTR]] ADSF-1 | System; transfers to fallback user via system-initiated deactivation |
| [[ADS UN GTR]] ADSF-2 | System; falls back to [[MRC]] — no human DDT transfer |

---

## DDT Fallback Chain

```
ADS performing DDT within ODD
    ↓ ODD exit / failure / fallback user unavailable
ADS Fallback Response:
    ADSF-1: System-initiated deactivation → fallback user takes DDT
    ADSF-2: ADS-controlled procedure → MRC
    (If ADSF-1 deactivation impossible) → MRC
```

---

## Key Links

- [[ODD]] — DDT is performed within ODD; ODD exit triggers fallback
- [[MRC]] — target state when ADS cannot continue DDT
- [[ADS Fallback Response]] — mechanism for DDT transition
- [[OEDR]] — component of DDT sensing and perception
- [[Behavioural Competency]] — verifiable DDT performance criteria
