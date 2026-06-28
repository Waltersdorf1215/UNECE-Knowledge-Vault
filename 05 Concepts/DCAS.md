---
type: concept
status: active
tags: [concept, DCAS, driver-control-assistance, SAE-L2, assisted-driving, driver-monitoring]
related: [R171, ADAS, DCAS, Driver Monitoring, Driver Availability, DDT, Assisted Driving, R79, Risk Mitigation Function, New UN Regulation on ADS]
source: "E/ECE/TRANS/505/Rev.3/Add.170 (authentic text: ECE/TRANS/WP.29/2024/37), §2.1"
last_updated: 2026-06-28
created: 2026-06-27
defined_in: "E/ECE/TRANS/505/Rev.3/Add.170, §2.1"
aliases: [Driver Control Assistance Systems]
knowledge_type: official_fact
evidence_level: official
---

# DCAS — Driver Control Assistance Systems

## Official Definition

**Fact (E/ECE/TRANS/505/Rev.3/Add.170, §2.1):**
> "Driver Control Assistance System (DCAS) means the hardware and software collectively capable of assisting a driver in controlling the longitudinal and lateral motion of the vehicle on a sustained basis."

See also: [[DCAS]] (working group note) and [[R171]].

---

## SAE Level

**Fact (R171, Introduction §4):** DCAS = **SAE Level 2** (partial automation). The driver must perform the remainder of dynamic control and supervise system operation and vehicle environment. Providing only lateral or only longitudinal control degrades DCAS from Level 2 to Level 1.

---

## Distinction from ADS — Officially Stated in R171

**Fact (R171, Introduction §5):** While both DCAS and ADS (SAE Levels 3–5) provide sustained lateral and longitudinal control, "only ADS may permit the driver to disengage from the driving task." DCAS "only assist the driver but never replace the driver. As a consequence, there is no transfer in the driver's responsibility for control of the vehicle."

---

## DCAS Features

**Fact (R171, §9.1.1):** Five declared feature types:
1. Positioning in the lane of travel
2. Driver-initiated lane change
3. Driver-confirmed lane change
4. System-initiated lane change
5. Other manoeuvres (turns, roundabouts, obstruction avoidance, parking)

---

## Key Regulatory Requirements

**Fact (R171, §5.1.1):** DCAS shall be designed to ensure the driver remains engaged.

**Fact (R171, §5.1.4):** Driver must be able to override or deactivate at any time. Maximum steering override force: 50 N (§5.5.3.4.1.4).

**Fact (R171, §5.3.7.3.1):** On driver unavailability, DCAS activates the [[Risk Mitigation Function]] under R79 04-series to bring the vehicle to a safe stop.

---

## System Boundaries

**Fact (R171, §2.5):** System Boundaries are manufacturer-declared conditions within which DCAS is designed to function. The system must detect approaching boundaries and warn the driver (§5.3.5.5). When boundaries are exceeded, the system transitions to stand-by mode.

---

## Relationship to R79

**Fact (R171, §1.2):** R171 does NOT apply to ACSF or RMF approved under [[R79]], unless the manufacturer declares them as DCAS.

**Fact (R171, §5.3.7.3.1):** R171 requires the Risk Mitigation Function to comply with "04 or later series of amendments to [[R79]]".

*Interpretation:* R171 fills the regulatory gap above R79's ACSF provisions (confirmed in Introduction §3), while the RMF requirement in §5.3.7.3.1 creates an explicit technical dependency on R79's 04-series amendments.

---

## Relationship to ADS

**Fact (R171, Introduction §5, as cited above):** The official R171 text explicitly distinguishes DCAS from ADS. DCAS does not replace the driver; ADS does.

*Interpretation:* This makes DCAS the regulatory ceiling for assisted driving and the boundary below which automated driving (governed by [[R157]] for ALKS, and the [[New UN Regulation on ADS]] for broader ADS) begins. However, R171 contains no cross-reference to R157 or any ADS regulation.

---

## Regulatory Note

**Fact (R171, Introduction §3):** R171 "aims to allow the approval of a variety of driver control assistance features, filling an existing regulatory gap" beyond the "03 series of amendments to UN Regulation No. 79." R171 provides minimum safety requirements for any DCAS.

---

## Key Links

- [[R171]] — the regulation governing DCAS
- [[ADAS]] — parent category
- [[Driver Monitoring]] — monitoring requirements (HOR/EOR/DCA escalation)
- [[Driver Availability]] — driver state monitoring
- [[DDT]] — driver retains DDT throughout DCAS operation
- [[Risk Mitigation Function]] — fallback when driver unavailable
- [[R79]] — ACSF/RMF underpinning
