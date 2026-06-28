---
type: concept
status: active
tags: [concept, driver-monitoring, DMS, driver-state, SAE-L2, SAE-L3, HOR, EOR, DCA]
related: [Driver Availability, Risk Mitigation Function, R171, R157, DCAS, ADAS, Assisted Driving]
source: "E/ECE/TRANS/505/Rev.3/Add.170, §5.5.4.2"
last_updated: 2026-06-28
created: 2026-06-27
defined_in: "R171 §5.5.4.2; R157; R(EU) 2021:1341"
aliases: [DMS, Driver Monitoring System]
knowledge_type: official_fact
evidence_level: official
---

# Driver Monitoring

## Summary

Driver Monitoring (DM) — implemented through a Driver Monitoring System (DMS) — assesses whether the driver is in a state to supervise or resume the dynamic driving task. It is a core requirement of both [[R171]] (DCAS, Level 2) and [[R157]] (ALKS, Level 3).

---

## What DCAS Monitors (R171) — Official Requirements

**Fact (R171, §5.5.4.2.1):** "The system shall be equipped with means to appropriately detect driver disengagement as specified in the following paragraphs."

**Fact (R171, §5.5.4.2.1.1):** "The system shall monitor if the driver is motorically (i.e., hand(s) on the steering control) and visually (e.g. gaze direction and/or head posture) disengaged."

### Assessment of Motoric Disengagement (§5.5.4.2.4.1)
**Fact:** "The driver shall be deemed to be motorically disengaged when the driver has removed their hands from the steering control."

### Assessment of Visual Disengagement (§5.5.4.2.5.1–5.5.4.2.5.2)
**Fact:** The system "shall detect the driver's visual disengagement at a minimum based on the detection of the driver's eye gaze. Head posture may also be used if the driver's eye gaze cannot be determined."

**Fact (§5.5.4.2.5.2):** "The driver shall be deemed to be visually disengaged when the driver's eye gaze and/or head posture…is directed away from any currently driving task relevant area." The dashboard and instrument panel are **not** a driving task relevant area.

**Fact (§5.5.4.2.5.2.1):** Re-engagement requires gaze/head posture directed toward a driving-relevant area for **at least 200 milliseconds**.

---

## Warning Escalation Sequence (R171 §5.5.4.2.6)

**Fact:** R171 defines three warning types and a mandated escalation timeline:

### Warning Types (§5.5.4.2.3)

| Warning | Abbrev. | Description |
|---|---|---|
| Hands On Request | HOR | Continual visual information; confirmed when driver places hand(s) on steering |
| Eyes On Request | EOR | Continual visual + at least one other modality; confirmed when driver is no longer visually disengaged |
| Direct Control Alert | DCA | Clear prominent instruction to immediately resume lateral (or lateral + longitudinal) control; visual + at least one other modality |

### Timing Requirements (§5.5.4.2.6)

| Trigger | Warning | Latest Timing |
|---|---|---|
| Motorically disengaged > 5s (may be delayed up to 5s if visually engaged) | HOR | 5s after detection |
| No HOR response | Escalated HOR (+acoustic/haptic) | 10s after initial HOR |
| Visually disengaged > 5s | EOR | 5s after visual disengagement |
| No EOR response | Escalated EOR (increased intensity, must include acoustic/haptic) | 3s after initial EOR |
| No escalated EOR response | DCA | 5s after escalated EOR |
| No DCA response | Driver Unavailability Response (→ RMF) | 10s after first escalated request/alert |

All timing thresholds apply **at speeds above 10 km/h**.

---

## Role in DCAS vs ADS

| Regulation | DM Purpose |
|---|---|
| [[R171]] DCAS (L2) | Detect driver disengagement; escalate warnings; trigger [[Risk Mitigation Function]] if unresponsive |
| [[R157]] ALKS (L3) | Assess driver availability for system-initiated deactivation (transition demand) |

*Interpretation:* In DCAS (R171), driver monitoring enforces continuous engagement — the driver must remain alert at all times. In ALKS (R157), driver monitoring assesses readiness for takeover. The R171 system is more stringent in requiring ongoing hands-on/eyes-on contact; the R157 system accepts a brief period of disengagement before issuing a transition demand.

---

## EU Context

**R(EU) 2021:1341** — Driver Monitoring System regulation — is present as a local raw file: `raw/R(EU) 2021:1341 DMS.pdf`. This EU implementing regulation mandates DMS for new vehicles in the EU. The relationship between EU 2021:1341 and R171's DMS requirements has not yet been verified — see [[R171]] open questions.

---

## Key Links

- [[Driver Availability]] — the state assessed by driver monitoring
- [[Risk Mitigation Function]] — activated when driver unavailability is confirmed
- [[R171]] — DCAS regulation with full DM specification
- [[R157]] — ALKS regulation (DM for transition demand)
- [[DCAS]] — working group
