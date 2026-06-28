---
type: concept
status: active
tags: [concept, fallback, ADS-fallback-response, MRC, ADSF-1, ADSF-2, safety]
related: [ADS UN GTR, MRC, MRM, ADSF-1, ADSF-2, ODD, DDT, Driver Availability, Transition Demand, Automated Driving System, DSSAD]
source: "ECE/TRANS/WP.29/2026/139, §2.15"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.15"
aliases: [ADS Fallback, Fallback Response]
---

# ADS Fallback Response

## Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.15):**
> "A system-initiated deactivation procedure or an ADS-controlled procedure to place the vehicle in a mitigated risk condition (MRC)."

---

## Two Types of Fallback Response

| Feature Type | Fallback Response |
|---|---|
| **ADSF-1** (has fallback user) | **System-initiated deactivation** — transfers DDT to fallback user; falls back to [[MRC]] if user does not respond |
| **ADSF-2** (no fallback user) | **ADS-controlled MRC procedure** — brings vehicle to MRC directly |

---

## System-Initiated Deactivation (ADSF-1, §2.16)

**Fact (§2.16):** "A procedure by which the ADS initiates the transfer of performance of the DDT from an ADSF-1 to a fallback user."

Corresponds to what [[R157]] and SAE J3016 call a **Transition Demand**: the ADS requests the fallback user (driver) to take over.

---

## Fallback to MRC (§4.1.6)

**Fact:** For both feature types, the ultimate fallback is to [[MRC]]:
- ADSF-2: Always falls back to MRC when fallback response is triggered
- ADSF-1: Falls back to MRC if system-initiated deactivation could not be completed (fallback user unavailable)

---

## Relationship to MRM

*Interpretation:* The GTR's "ADS fallback response → MRC" corresponds to SAE J3016's "Minimal Risk Maneuver → Minimal Risk Condition." The GTR uses more precise terminology separating the procedure (ADS fallback response) from the end state ([[MRC]]). See [[MRM]] for the SAE/R157 terminology.

---

## Triggers for Fallback Response (DSSAD Annex 6)

**Fact:** An ADS fallback response is triggered by:
- ODD exit
- ADS failure
- Collision detected
- Detection that fallback user is not available
- Failure of fallback user to take control after system-initiated deactivation

---

## Key Links

- [[MRC]] — the end state achieved by a fallback response
- [[MRM]] — related SAE J3016 / R157 concept
- [[ADSF-1]] / [[ADSF-2]] — feature types with different fallback responses
- [[Driver Availability]] — assessed for ADSF-1 to determine if system-initiated deactivation is possible
- [[Transition Demand]] — R157/SAE terminology for ADSF-1 system-initiated deactivation
- [[DSSAD]] — records fallback response events
