---
type: concept
status: active
tags: [concept, validation, ADS-validation, testing, SOTIF, multi-pillar, NATM]
related: [VMAD, FRAV, ADS IWG, ADS UN GTR, New UN Regulation on ADS, SOTIF, Functional Safety, ODD, DDT, MRC, R157, Safety Case, Behavioural Competency, OEDR, ISMR]
source: "ECE/TRANS/WP.29/2026/139, §34–39 and §5.2"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139"
---

# Validation

## Role in the ADS GTR

**Fact (ECE/TRANS/WP.29/2026/139, §34):** "Validating the ADS's capabilities is a highly complex task which cannot be done comprehensively nor effectively through one validation methodology alone. As a result, it is necessary to adopt a multi-pillar approach for the validation of ADS."

---

## Four Validation Pillars

**Fact (§36–39, §5.2):**

| Pillar | Description | GTR Requirement Section |
|---|---|---|
| **Virtual testing** | Simulation toolchains testing wide range of scenarios including rare/impossible real-world scenarios | §5.2.1, §6.2.1 |
| **Track testing** | Closed-access testing ground with scenario elements | §5.2.2, §6.2.2 |
| **Real-world testing** | Public road testing under real traffic conditions | §5.2.3, §6.2.3 |
| **Audit** | SMS and safety case audit; validates hazard identification and safety-by-design | §6.1, §6.3 |

---

## NATM — New Assessment/Test Method

**Fact:** [[VMAD]] and [[FRAV]] developed the NATM (New Assessment/Test Method for Automated Driving):
- **First version:** ECE/TRANS/WP.29/1159 (adopted 184th WP.29, June 2021)
- **FRAV/VMAD Integrated Document:** ECE/TRANS/WP.29/2024/39 (approved June 2024) — the direct technical basis for the GTR validation framework

---

## Virtual Testing Requirements (§5.2.1)

**Fact:** Manufacturer must demonstrate simulation toolchain suitability:
- Data management (input, output, uncertainty quantification)
- Competency of personnel
- Release management (lifecycle of toolchain)
- Description including limitations and assumptions
- Credibility framework for simulation toolchain

---

## Scenario Generation (Annex 5)

**Fact:** Three complementary methods:
1. **Knowledge-based** — domain expertise, functional safety requirements, SOTIF
2. **Data-based** — accident databases, naturalistic driving data, in-service monitoring data
3. **Goal-based** — training data from ADS development

Scenarios span four abstraction levels: functional → abstract → logical → concrete.

---

## Simulation Toolchain Credibility

**Fact (§64–65):** High confidence in simulation credibility is required. The GTR requires a harmonized credibility framework including assumptions, limitations, uncertainty quantification, scope, criticality analysis, sensitivity analysis, V&V.

---

## AI-Based Validation Challenge

*Interpretation:* The GTR's exclusion of "online in-vehicle learning" (§41n) significantly constrains the applicability of this validation framework to AI-native ADS. End-to-end systems that update continuously cannot be validated under a static safety case paradigm. This is a key open question for the regulatory community.

---

## Key Links

- [[VMAD]] — developed this multi-pillar methodology
- [[FRAV]] — developed functional requirements that validation must cover
- [[Safety Case]] — validation evidence forms the safety case
- [[Behavioural Competency]] — competencies are the basis for scenario generation
- [[SOTIF]] — ISO 21448 alignment required
- [[ISMR]] — post-deployment monitoring extends validation into operation
