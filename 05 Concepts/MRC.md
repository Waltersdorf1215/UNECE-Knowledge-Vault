---
type: concept
status: active
tags: [concept, MRC, mitigated-risk-condition, fallback, ADS, safety]
related: [ADS UN GTR, ADS Fallback Response, ODD, DDT, ADSF-1, ADSF-2, Automated Driving System, R157, DSSAD]
source: "ECE/TRANS/WP.29/2026/139, §2.20"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.20"
aliases: [Mitigated Risk Condition]
---

# MRC — Mitigated Risk Condition

## Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.20):**
> "A stable and stopped state of the vehicle that reduces the risk of a crash."

---

## Terminology Note: MRC vs. MRM

The [[ADS UN GTR]] (ECE/TRANS/WP.29/2026/139) uses **MRC** (Mitigated Risk Condition) as the target end-state, reached via an **[[ADS Fallback Response]]**.

The existing vault note [[MRM]] (Minimal Risk Maneuver) uses the SAE J3016 terminology. The regulatory distinction:
- **MRC** = the **state** achieved (stable, stopped, reduced crash risk) — used in the GTR
- **MRM** = the **maneuver** performed to reach a safe state — SAE J3016 term, used in R157

*Interpretation:* The GTR's "ADS fallback to MRC" corresponds to what is called "MRM" in the R157 context and SAE J3016. Both describe the ADS taking control to bring the vehicle to a safe stopped state. The GTR uses more precise terminology separating the process (fallback response) from the end state (MRC).

---

## MRC Requirements in the GTR (§4.1.6)

**Fact:**
- **ADSF-2 (§4.1.6.1):** The ADS fallback response shall be to place the vehicle in an MRC. The ADS feature may permit user-initiated deactivation to interrupt the fallback to an MRC.
- **ADSF-1 (§4.1.6.2):** If system-initiated deactivation has not been possible, the ADS shall execute a fallback to an MRC.
- **Post-MRC (§4.1.6.3):** Upon MRC completion, a user may be permitted to assume control.

## MRC Triggers

**Fact (from DSSAD Annex 6):** An MRC fallback is triggered by:
- ODD exit
- ADS failure
- Collision detected
- Detection that fallback user is not available
- Failure of fallback user to take control following system-initiated deactivation

---

## Key Links

- [[ADS Fallback Response]] — the process of reaching MRC
- [[ADSF-1]] / [[ADSF-2]] — MRC requirements differ by feature type
- [[ODD]] — ODD exit can trigger MRC fallback
- [[DSSAD]] — MRC achievement is a time-stamped DSSAD event
- [[MRM]] — related concept (SAE J3016 / R157 terminology)
