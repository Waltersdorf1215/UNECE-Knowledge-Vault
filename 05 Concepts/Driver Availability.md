---
type: concept
status: active
tags: [concept, driver-availability, driver-state, driver-disengagement, SAE-L2, DCAS, R171]
related: [Driver Monitoring, Risk Mitigation Function, Transition Demand, MRM, DDT, R157, R171, DCAS, ADAS, Assisted Driving]
source: "E/ECE/TRANS/505/Rev.3/Add.170, §2.4, §2.6, §5.1.1, §5.3.7.3.1, §5.5.4.2"
last_updated: 2026-06-28
created: 2026-06-27
defined_in: "R171 §2.6 and §5.5.4.2"
aliases: [Driver State, Driver Engagement, Driver Disengagement, Driver Unavailability]
knowledge_type: official_fact
evidence_level: official
---

# Driver Availability

## Summary

In UNECE DCAS, **Driver Availability** is the working concept for whether the driver remains able to supervise and intervene while a [[DCAS]] feature assists with longitudinal and lateral control. R171 does not define a standalone term called "driver availability"; it defines **driver disengagement** and specifies how [[Driver Monitoring]] detects disengagement and escalates warnings.

**Fact (R171, §2.4):** Only the driver is in charge of and responsible for vehicle dynamic control while DCAS provides assistance.

**Fact (R171, §2.6):** Driver disengagement is the system's determination that the driver is currently unable to safely perform perception, planning, decision-making, and intervention for DCAS operation.

**Fact (R171, §5.1.1):** The DCAS must be designed so that the driver remains engaged with the driving task.

---

## DCAS Meaning

For [[R171]] DCAS, driver availability is not a permission for the driver to disengage. It is the continuing condition that the driver must remain engaged and able to intervene because DCAS is SAE Level 2 assistance, not automated driving.

**Fact (R171, Introduction §4):** DCAS is treated as SAE Level 2 partial automation, requiring the driver to perform the remaining dynamic control and supervise system operation and the vehicle environment.

**Fact (R171, Introduction §5):** DCAS does not replace the driver and does not transfer responsibility for control of the vehicle.

*Interpretation:* In DCAS, "driver availability" is best understood as the inverse of R171's sourced concept of driver disengagement. A driver is available when they are not motorically or visually disengaged in a way that prevents safe supervision and intervention.

---

## How R171 Assesses Availability

R171 operationalizes driver availability through [[Driver Monitoring]].

**Fact (R171, §5.5.4.2.1):** DCAS must detect driver disengagement.

**Fact (R171, §5.5.4.2.1.1):** The system monitors whether the driver is motorically disengaged, meaning hands removed from steering control, and visually disengaged, meaning eye gaze or head posture away from driving-task-relevant areas.

**Fact (R171, §5.5.4.2.5.2.1):** Visual re-engagement requires gaze or head posture toward a driving-task-relevant area for at least 200 milliseconds.

---

## Warning Escalation and Unavailability Response

If the driver becomes unavailable, R171 requires a warning escalation sequence before fallback.

| Driver State / Trigger | R171 Response | Evidence |
|---|---|---|
| Motoric disengagement | Hands On Request (HOR), then escalated HOR if no response | R171 §5.5.4.2.6 |
| Visual disengagement | Eyes On Request (EOR), then escalated EOR if no response | R171 §5.5.4.2.6 |
| No response after escalated EOR | Direct Control Alert (DCA) | R171 §5.5.4.2.6 |
| No response to DCA | Driver Unavailability Response, activating [[Risk Mitigation Function]] | R171 §5.5.4.2.6 and §5.3.7.3.1 |

**Fact (R171, §5.3.7.3.1):** When the driver is determined unavailable after the warning escalation sequence, the system must activate the [[Risk Mitigation Function]] to come to a safe stop.

---

## Relationship to Driver Monitoring and RMF

[[Driver Monitoring]] is the system capability that assesses driver state. Driver Availability is the assessed state. [[Risk Mitigation Function]] is the fallback response when the driver remains unavailable after escalation.

```
Driver Monitoring system
    -> assesses
Driver Availability (available / unavailable)
    -> if unavailable in DCAS
HOR / EOR warning escalation
    -> if no recovery
DCA
    -> if no response
Risk Mitigation Function -> safe stop
```

---

## Regulatory Usage

| Regulation / Instrument | Usage |
|---|---|
| [[R171]] DCAS | Driver must remain engaged; unavailability triggers warning escalation and RMF fallback. |
| [[R157]] ALKS | Placeholder note currently links driver availability to transition demand, but R157 has not been fully ingested in this Vault. |
| [[New UN Regulation on ADS]] | [VERIFY - relevance differs for driverless ADSF-2 use cases where no fallback user is expected.] |

---

## Related Concepts

- [[Driver Monitoring]] — detects motoric and visual disengagement.
- [[Risk Mitigation Function]] — DCAS fallback when the driver remains unavailable.
- [[DCAS]] — SAE Level 2 assistance context where driver engagement is continuous.
- [[Transition Demand]] — related Level 3 concept; not the primary DCAS mechanism.
- [[MRM]] — related Level 3 fallback concept; separate from R171's RMF terminology.

---

## Evidence

| Source | Evidence Used |
|---|---|
| `E/ECE/TRANS/505/Rev.3/Add.170` | R171 authentic addendum for DCAS driver responsibility, driver disengagement, monitoring, escalation, and RMF response. |
| `01 Regulations/R171.md` | Local Vault synthesis of R171 official text. |
| `05 Concepts/Driver Monitoring.md` | Local Vault synthesis of R171 driver monitoring requirements. |
| `05 Concepts/Risk Mitigation Function.md` | Local Vault synthesis of R171 RMF fallback requirements. |

---

## References

- `12 Attachments/UNECE/R171e.pdf`
- `01 Regulations/R171.md`
- `05 Concepts/Driver Monitoring.md`
- `05 Concepts/Risk Mitigation Function.md`

---

## Open Questions

- What is the technical definition of "available" in R157 — what gaze, posture, or response criteria?
- How does R171's driver disengagement model compare with R157's driver availability requirements after R157 is fully ingested?
- For [[New UN Regulation on ADS]] use cases without a human driver: is "driver availability" still a relevant concept?
- How does availability detection interact with distraction and drowsiness monitoring (R(EU) 2023:2590)?
