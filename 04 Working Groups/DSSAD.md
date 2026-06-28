---
type: working_group
status: active
tags: [working-group, data-storage, DSSAD, ADS, EDR]
related: [GRVA, R157, EDR-DSSAD, Event Data Recorder, ADS IWG, ADS UN GTR, New UN Regulation on ADS, Functional Safety, MRC]
source: "ECE/TRANS/WP.29/2026/139 (Annex 6)"
last_updated: 2026-06-27
created: 2026-06-27
parent_body: GRVA
---

# DSSAD — Data Storage System for Automated Driving

## Summary

**Fact:** DSSAD is the informal working group under [[GRVA]] whose work is reflected in **Annex 6** of the [[ADS UN GTR]] (ECE/TRANS/WP.29/2026/139). Annex 6 specifies mandatory data recording requirements for ADS vehicles.

The [[DSSAD]] concept note covers the technical concept. This note covers the working group.

---

## Annex 6 of the ADS UN GTR — Confirmed Requirements

**Fact (Annex 6, ECE/TRANS/WP.29/2026/139):**

### Mandatory DSSAD Capability (§4.3.1)
Every ADS vehicle must be equipped with a DSSAD monitoring the safety performance of the ADS.

### Time-Stamped Events to Record (Annex 6, §5.2.1)
- ADS feature activation / deactivation
- ODD exit
- Start of ADS fallback to user (ADSF-1)
- Start of ADS fallback to MRC
- User input to driving controls (brake, acceleration, steering, direction indicator)
- Passenger stop request
- Prevention of user takeover
- Detection that fallback user is not available
- Start and end of Emergency Manoeuvre
- EDR trigger input
- Detected collision
- MRC achieved
- Detected failure compromising DDT capability
- Remote intervention in a tactical function

### Time-Series Data at Triggering Events (Annex 6, §5.3.2)
Window: **−7 to +7 seconds** around trigger events (detected collision, EDR trigger):
- Visual images (−7 to +7s)
- Detected object distances and velocities (longitudinal and lateral, −7 to 0s)
- Detected object classification (−7 to 0s)
- Sensor data (if detected object elements unavailable, −7 to 0s)
- ADS-requested demands: acceleration, service brake, parking brake, steering (−7 to +7s)
- Vehicle acceleration (longitudinal and lateral, −7 to +7s)
- ADS-determined vehicle speed (−7 to +7s)

### Data Format (Annex 6, §3.1)
Open standard format required: **JSON, CSV, or XML** (except sensor data and visual images).

### Data Accessibility (Annex 6, §4)
- Retrievable even without main power
- Retrievable after impact
- Electronic communication interface compliant with publicly available standard

---

## Relationship to EDR

[[Event Data Recorder]] (EDR) trigger inputs are referenced in DSSAD time-series data (excluding last stop trigger). DSSAD requirements for ADS go significantly beyond conventional EDR scope — they capture the ADS operational state, not just physical crash dynamics.

---

## Open Questions

- What is the IWG's ongoing mandate post-GTR adoption?
- How does the DSSAD Annex 6 relate to the [[EDR-DSSAD]] IWG's separate work on a standalone EDR/DSSAD instrument?
- How does data protection law (e.g., GDPR) apply to DSSAD data access by authorized entities?
- What constitutes "publicly available interface standard" for data retrieval?
