---
type: concept
status: active
tags: [concept, ADSF-1, ADSF-2, ADS-feature-type, fallback-user, driverless]
related: [ADS UN GTR, ADS Fallback Response, MRC, ODD, DDT, Driver Availability, Driver Monitoring, Automated Driving System, Safety Case]
source: "ECE/TRANS/WP.29/2026/139, §2.6.1–2.6.2"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.6.1–2.6.2"
aliases: [ADSF-1, ADSF-2, ADS feature type 1, ADS feature type 2]
---

# ADSF-1 and ADSF-2 — ADS Feature Types

## Definitions

**Fact (ECE/TRANS/WP.29/2026/139):**

### ADSF-1 (§2.6.1)
> "An ADS feature which includes an ADS fallback response requiring a fallback user."

### ADSF-2 (§2.6.2)
> "An ADS feature which does not include an ADS fallback response requiring a fallback user."

### Fallback User (§2.14.3)
> "An occupant designated to perform the DDT pursuant to an ADS fallback response."

---

## Practical Interpretation

| | ADSF-1 | ADSF-2 |
|---|---|---|
| Human fallback required? | Yes — fallback user must be present | No — fully driverless operation |
| SAE Level analogy | Level 3 (driver must be ready to take over) | Level 4/5 (no driver needed within ODD) |
| Monitoring requirement (§4.2.2.1.6) | Continuously assess fallback user availability | No equivalent |
| MRC fallback | If fallback user unavailable after system-initiated deactivation | Always falls back to MRC |
| Direct view requirement | May reduce direct view of outside | Direct view may be reduced (§4.2.2.1.2(c)) |

---

## ADSF-1 Specific Requirements (§4.2.2.1.6)

**Fact:** While ADSF-1 is active, the ADS shall:
- Continuously assess whether the fallback user is available (at least awake and correctly seated)
- Provide procedures to re-engage unavailable fallback user
- Trigger MRC fallback if re-engagement is not possible, feasible, or safe
- Ensure system-initiated deactivation includes sufficient time for fallback user to perceive and respond

---

## ADSF-2 Specific Requirements (§4.2.3)

**Fact:** For ADSF-2:
- Passengers can request to stop the vehicle (§4.2.3.1)
- Safety-related information must be provided to passengers (§4.2.3.2)
- If an ADSF-2 feature transitions to an ADSF-1, passenger consent must be obtained first (§4.2.2.2.5)

---

## Key Links

- [[ADS Fallback Response]] — the mechanism that differs between types
- [[MRC]] — both types ultimately fall back to MRC
- [[Driver Availability]] — assessed continuously for ADSF-1
- [[Driver Monitoring]] — monitoring mechanism for ADSF-1 fallback user
- [[ODD]] — both types operate only within ODD
- [[Automated Driving System]] — parent concept
