---
type: concept
status: active
tags: [concept, MRM, minimal-risk-maneuver, fallback, ADS, R157, SAE]
related: [DDT, ODD, ADS, R157, Transition Demand, FRAV, New UN Regulation on ADS, Driver Availability, MRC, ADS Fallback Response, Automated Driving System]
source: "SAE J3016 / R157"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "SAE J3016 / R157"
aliases: [Minimal Risk Maneuver, Minimum Risk Maneuver]
---

# MRM — Minimal Risk Maneuver

## Definition

**Fact (SAE J3016 / R157 context):**
The Minimal Risk Maneuver (MRM) is the fallback maneuver performed by an ADS to bring the vehicle to a minimal risk condition when it cannot continue the DDT safely.

**Source:** SAE J3016 terminology. Used in [[R157]] (ALKS).

---

## Terminology Note: MRM (R157/SAE) vs. MRC (ADS UN GTR)

The [[ADS UN GTR]] (ECE/TRANS/WP.29/2026/139) uses a different but related terminology:
- **GTR terminology:** "[[ADS Fallback Response]]" (the process) → "[[MRC]] — Mitigated Risk Condition" (the end state)
- **R157/SAE terminology:** "MRM — Minimal Risk Maneuver" (the process) → "Minimal Risk Condition" (the end state)

*Interpretation:* These describe the same regulatory concept — the ADS taking control to bring the vehicle to a safe stopped state. The GTR terminology is more precise. For notes on the GTR instrument, prefer [[MRC]] and [[ADS Fallback Response]] terminology. For R157-specific notes, MRM terminology is appropriate.

---

## MRM in R157

**Fact:** [[R157]] (ALKS) requires the ALKS to perform an MRM when:
- The driver fails to respond to a Transition Demand within the required time
- An ALKS failure occurs
- ODD conditions are no longer met

---

## MRM Trigger Chain (R157 context)

```
Driver unavailability detected
    ↓
Transition Demand issued → wait period
    ↓ (if no driver response)
MRM initiated → vehicle decelerates and stops in lane / moves to shoulder
    ↓
Minimal Risk Condition achieved
```

---

## Key Links

- [[MRC]] — GTR equivalent end-state concept (preferred for ADS UN GTR context)
- [[ADS Fallback Response]] — GTR equivalent process concept
- [[DDT]] — MRM is triggered when DDT cannot continue
- [[ODD]] — MRM triggered at ODD boundary breach
- [[R157]] — primary regulation defining MRM requirements
- [[Transition Demand]] — precedes MRM if driver unresponsive
- [[Driver Availability]] — assessed to determine if Transition Demand is needed
