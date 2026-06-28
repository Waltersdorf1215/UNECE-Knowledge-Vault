---
type: concept
status: active
tags: [concept, ADS, SAE-L3, SAE-L4, SAE-L5, automated-driving]
related: [ADS, DDT, ODD, MRC, ADS Fallback Response, ADSF-1 and ADSF-2, FRAV, ADS IWG, ADS UN GTR, New UN Regulation on ADS, R157, SOTIF, Functional Safety, Validation, DSSAD, Remote Assistance, Safety Case, Safety Management System, OEDR, Behavioural Competency]
source: "ECE/TRANS/WP.29/2026/139, §2.1"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.1 (based on SAE J3016 and ISO/PAS 22736)"
aliases: [ADS]
---

# Automated Driving System

## Official Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.1):**
> "The vehicle hardware and software that are collectively capable of performing the entire Dynamic Driving Task (DDT) on a sustained basis."

**Source footnote:** Based on SAE J3016 and ISO/PAS 22736. "The term 'Automated Driving System' is used specifically to describe a Level 3, 4, or 5 driving automation system."

---

## ADS Feature Types

**Fact:** The GTR distinguishes two types of ADS features based on whether a human fallback is required:
- **[[ADSF-1]]** — includes fallback response requiring a fallback user (corresponds to Level 3)
- **[[ADSF-2]]** — does not include fallback requiring a fallback user (corresponds to Level 4/5)

---

## When ADS Feature is Active

**Fact (§2.3.1):** "When the ADS feature is active, the DDT is always performed in its entirety by the ADS which means the whole of the tactical and operational functions necessary to operate the vehicle."

---

## Regulatory Coverage

| SAE Level | Regulation | Status |
|---|---|---|
| L1–L2 (lateral) | [[R79]] (ACSF) | Active |
| L2 (combined) | [[R171]] (DCAS) | Active |
| L3 (highway, limited ODD) | [[R157]] (ALKS) | Active |
| L3+ (broader ODD) | [[New UN Regulation on ADS]] | Submitted to WP.29 199th |
| Global standard | [[ADS UN GTR]] (ECE/TRANS/WP.29/2026/139) | Submitted to WP.29 199th |

---

## General Safety Requirement

**Fact (§3.1):** "As a general concept, the safety level of ADS shall be at least to the level of a competent and careful human driver."

---

## Critical AI Constraint

**Fact (§41n):** "The requirements in this Regulation are written with the expectation that ADS software does not include the use of online in-vehicle learning that self-modifies system behaviour."

*Interpretation:* AI-native ADS using continuous in-field learning (e.g., some end-to-end systems) may not be covered by the current GTR framework. See [[Wayve]] for example.

---

## Distinction from Assisted Driving

- **[[Assisted Driving]]** / **[[ADAS]]** / **[[DCAS]]**: Driver retains DDT responsibility; system assists
- **ADS**: System performs **entire** DDT; driver may not be required within ODD

---

## Key Developing Bodies

- [[ADS IWG]] — IWG developing the ADS regulatory framework
- [[FRAV]] — functional requirements
- [[VMAD]] — validation methodology
- [[GRVA]] — parent body
