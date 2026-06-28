---
type: concept
status: active
tags: [concept, DSSAD, data-storage, automated-driving, black-box, ADS]
related: [Event Data Recorder, R157, DSSAD, EDR-DSSAD, ADS IWG, ADS UN GTR, New UN Regulation on ADS, Functional Safety, MRC, ISMR]
source: "ECE/TRANS/WP.29/2026/139, §2.11 and Annex 6"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.11"
aliases: [Data Storage System for Automated Driving]
---

# DSSAD — Data Storage System for Automated Driving

## Official Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.11):**
> "The capability to record and store data concerning the safety performance of a vehicle's ADS."

### Sub-definitions:
- **DSSAD triggering event (§2.11.1):** Time-stamped data element triggering recording of time-series data.
- **Emergency manoeuvre (§2.11.2):** Manoeuvre to avoid/mitigate imminent collision risk (braking demand > 5 m/s²).
- **Imminent collision risk (§2.11.3):** Situation where collision cannot be avoided by braking demand < 5 m/s².
- **Detected object (§2.11.4):** Object detected and recognised as relevant for DDT.

---

## Mandatory DSSAD Requirement

**Fact (§4.3.1.1):** "The ADS vehicle shall be equipped with a DSSAD capable of monitoring the safety performance of the ADS."

---

## Time-Stamped Events (Annex 6, §5.2.1)

**Fact:** DSSAD must record time-stamped events including:
- ADS feature activation / deactivation (by system or user)
- ODD exit
- Start of ADS fallback to user (ADSF-1)
- Start of ADS fallback to [[MRC]]
- User input to driving controls
- Passenger stop request
- Prevention of user takeover
- Detection that fallback user unavailable
- Start / end of Emergency Manoeuvre
- EDR trigger input
- Detected collision
- MRC achieved
- Detected failure compromising DDT capability
- Remote intervention in a tactical function

---

## Time-Series Data at Triggering Events (Annex 6, §5.3.2)

**Fact:** Around detected collisions and EDR trigger inputs, the following are recorded in a **±7 second window**:

| Data Element | Condition | Window |
|---|---|---|
| Visual images | Mandatory | −7 to +7s |
| Detected object distance (long/lat) | If available | −7 to 0s |
| Detected object relative velocity (long/lat) | If available | −7 to 0s |
| Detected object classification | If available | −7 to 0s |
| Sensor data | If detected object elements unavailable | −7 to 0s |
| ADS-requested demands (accel/brake/steering) | Mandatory | −7 to +7s |
| Vehicle acceleration (long/lat) | Mandatory | −7 to +7s |
| ADS-determined vehicle speed | Mandatory | −7 to +7s |

---

## Data Format and Accessibility

**Fact (Annex 6, §3–4):**
- Format: **open standard** (JSON, CSV, XML) except sensor data/visual images
- Accessible even without main power and after impact
- Retrievable via publicly available interface standard
- Off-board storage allowed if on-board copy retained until successful upload

---

## See Also

- [[DSSAD]] (working group) — the IWG that developed these requirements
- [[EDR-DSSAD]] — combined EDR/DSSAD working group
- [[Event Data Recorder]] — conventional EDR (subset of DSSAD scope)
- [[ISMR]] — DSSAD data feeds the in-service monitoring and reporting system
