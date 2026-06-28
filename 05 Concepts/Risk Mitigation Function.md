---
type: concept
status: active
tags: [concept, RMF, risk-mitigation-function, fallback, DCAS, R171, R79]
related: [R171, R79, DCAS, Driver Monitoring, Driver Availability, MRM, MRC, ADS Fallback Response]
source: "E/ECE/TRANS/505/Rev.3/Add.170, §5.3.7.3"
last_updated: 2026-06-28
created: 2026-06-28
defined_in: "R171 §5.3.7.3; UN Regulation No. 79 (04-series amendments)"
aliases: [RMF, Risk Mitigation Function]
knowledge_type: official_fact
evidence_level: official
---

# Risk Mitigation Function (RMF)

## Summary

The **Risk Mitigation Function (RMF)** is the fallback mechanism activated by a DCAS system when the driver has been determined to be unavailable following the warning escalation sequence. Its purpose is to bring the vehicle to a **safe stop**. It is defined within [[R79]] (04-series amendments) and cross-referenced as a mandatory requirement in [[R171]] (DCAS).

---

## Regulatory Basis

**Fact (R171, §5.3.7.3.1):** "The system shall comply with the technical requirements and transitional provisions of the **04 or later series of amendments to UN Regulation No. 79** with respect to the Risk Mitigation Function (RMF). In the event that the driver has been determined to be unavailable following a driver disengagement warning escalation sequence as defined in paragraph 5.5.4.2.6., the system shall appropriately activate the Risk Mitigation Function in order to come to a safe stop."

**Fact (R171, §5.3.7.3.2):** Where the system has a driver-confirmed or system-initiated lane change feature, "the RMF shall be capable of performing lane changes during an intervention on a highway. The system shall be designed to perform lane changes towards a slower or emergency lane where it is possible and safe to do so, taking into account surrounding traffic and road infrastructure in order to come to a safe stop."

---

## Triggering Conditions

**Fact (R171, §5.5.4.2.6.4.1):** The Driver Unavailability Response (i.e., RMF activation) occurs "at the latest 10 seconds after the first escalated request or alert."

See the full warning escalation sequence in [[Driver Monitoring]] for the preceding steps (HOR → EOR → DCA → RMF).

---

## Relationship to MRM and MRC

The RMF in R171 is conceptually equivalent to the Minimal Risk Maneuver (MRM) in R157 and the ADS Fallback Response leading to an MRC in the ADS UN GTR:

| Term | Regulation | Level | Trigger | End State |
|---|---|---|---|---|
| RMF (Risk Mitigation Function) | [[R171]] (DCAS) / [[R79]] | SAE L2 | Driver unavailability after escalation | Safe stop |
| MRM (Minimal Risk Maneuver) | [[R157]] (ALKS) | SAE L3 | Driver unresponsive to transition demand | Minimal Risk Condition |
| ADS Fallback Response | [[ADS UN GTR]] | SAE L3–5 | ODD exit, failure, or user unavailable | [[MRC]] (Mitigated Risk Condition) |

*Interpretation:* All three are fallback-to-safe-stop mechanisms at different automation levels. They are defined in separate regulations under different terminology; they are not legally cross-referenced unless explicitly stated.

---

## Key Links

- [[R171]] — requires RMF compliance (§5.3.7.3.1)
- [[R79]] — defines RMF technical requirements (04-series amendments)
- [[Driver Monitoring]] — warning escalation triggers RMF activation
- [[MRM]] — analogous concept in R157/SAE J3016 context
- [[MRC]] — analogous end-state concept in ADS UN GTR context
