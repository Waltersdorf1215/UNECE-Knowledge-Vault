---
type: regulation
status: active
tags: [regulation, ADS, UN-GTR, global-technical-regulation, 1998-agreement]
related: [ADS, ADS IWG, FRAV, VMAD, DSSAD, GRVA, WP.29, ODD, DDT, MRC, Safety Case, Safety Management System, Behavioural Competency, OEDR, ISMR, R157, New UN Regulation on ADS, SOTIF, Functional Safety, Cybersecurity, AVC, FADS]
source: "ECE/TRANS/WP.29/2026/139"
last_updated: 2026-06-27
created: 2026-06-27
regulation_series: "UN GTR"
responsible_body: GRVA
document_number: "ECE/TRANS/WP.29/2026/139"
session: "WP.29 199th session"
companion_document: "ECE/TRANS/WP.29/2026/142"
---

# ADS UN GTR — UN Global Technical Regulation on Automated Driving Systems

## Summary

**Fact:** A new United Nations Global Technical Regulation (GTR) on Automated Driving Systems, proposed for consideration and vote by AC.3 at the [[WP29 199th Session]] (Geneva, 23–26 June 2026). Submitted as document **ECE/TRANS/WP.29/2026/139**. Recommended by [[GRVA]] at its **[[GRVA 24th Session]]**.

The text contains provisions in [square brackets] aimed at being reconfirmed by GRVA at its **[[GRVA 25th Session]]**.

---

## Document References

| Document | Description |
|---|---|
| ECE/TRANS/WP.29/2026/139 | This GTR text (proposal) |
| ECE/TRANS/WP.29/2026/142 | Companion report (Article 6, para. 6.2.7 of 1998 Agreement) |
| ECE/TRANS/WP.29/GRVA/2026/2 | Basis document from GRVA |
| WP.29-198-07 | Informal document (basis) |
| ECE/TRANS/WP.29/2024/39 | FRAV/VMAD Integrated Document (June 2024) — primary technical basis |
| ECE/TRANS/WP.29/1159 | NATM first version (adopted June 2021, 184th WP.29 session) |

**Source:** **ECE/TRANS/WP.29/2019/34/Rev.2** — Framework Document on Automated Vehicles (adopted at 178th WP.29 session) — foundational document.

---

## Scope

**Fact (§1.1):** Applies to Automated Driving Systems of vehicles of **Categories 1 and 2** (as defined in the 1998 Agreement Special Resolution No. 1).

**Fact (§82):** ADS will not be mandatory. Currently ALKS ([[R157]]) is the only specific ADS application with a UN regulation; this GTR covers all other ADS applications.

---

## Key Definitions (Official, from §2)

### ADS (§2.1)
> "The vehicle hardware and software that are collectively capable of performing the entire Dynamic Driving Task (DDT) on a sustained basis."
— Based on SAE J3016 and ISO/PAS 22736. Applies to Level 3, 4, or 5 driving automation.

### DDT (§2.3)
> "The real-time operational and tactical functions required to operate the vehicle."
Three interdependent categories: **sensing and perception**, **planning and decision**, and **control**.

### ODD (§2.12)
> "The operating conditions under which an ADS feature is specifically designed to function."
- **ODD exit (§2.12.1):** presence of conditions outside ODD limits or absence of required conditions.

### ADS Feature Types (§2.6.1–2.6.2)
- **ADSF-1:** ADS feature that **includes** a fallback response requiring a **fallback user** (human takeover possible/required)
- **ADSF-2:** ADS feature that **does not** include an ADS fallback response requiring a fallback user (fully driverless)

### MRC — Mitigated Risk Condition (§2.20)
> "A stable and stopped state of the vehicle that reduces the risk of a crash."
See [[MRC]] for full note. Note: this regulation uses MRC not "MRM" for the end state.

### ADS Fallback Response (§2.15)
> "A system-initiated deactivation procedure or an ADS-controlled procedure to place the vehicle in a mitigated risk condition (MRC)."

### Safety Case (§2.31)
> "Structured documentation that provides a compelling, comprehensible, and valid case that the ADS meets the relevant ADS requirements of this Regulation and is free from unreasonable risks."

### Safety Management System — SMS (§2.27)
> "A systematic approach to managing safety that encompasses and integrates organisational, human, and technical factors."
See [[Safety Management System]].

### Behavioural Competency (§2.22)
> "An expected and verifiable capability of an ADS feature to operate a vehicle within the ODD of the feature."
See [[Behavioural Competency]].

### Functional Safety (§2.25)
> "The absence of unreasonable risks under the occurrence of hazards caused by a malfunctioning behaviour of electric/electronic systems."

### SOTIF (§2.26)
> "The absence of unreasonable risk due to hazards resulting from functional insufficiencies of the intended functionality or reasonably foreseeable misuse."

### Fallback User (§2.14.3)
> "An occupant designated to perform the DDT pursuant to an ADS fallback response."

### ISMR — In-Service Monitoring and Reporting (§5.1.8)
Manufacturer process to monitor ADS performance post-deployment. See [[ISMR]].

### OEDR — Object and Event Detection and Response (§4.1.2.4)
ADS capability to detect and respond to objects and events relevant to the DDT. See [[OEDR]].

---

## General Requirements (§3)

**Fact (§3.1):** "As a general concept, the safety level of ADS shall be at least to the level of a competent and careful human driver."

**Fact (§3.2):** "The ADS shall be free from unreasonable risk."

---

## ADS Requirements Structure (§4)

### DDT Performance (§4.1)
- **Nominal situations (§4.1.2):** No collision, adapt to safety risks, comply with traffic rules, interact safely with other road users, respond to priority vehicles and road safety agents.
- **Critical situations (§4.1.3):** Continue nominal requirements as far as reasonably practicable; when collision cannot be avoided, aim to mitigate.
- **Failure situations (§4.1.4):** Detect faults; execute fallback response or adapt performance. Capability for remote termination required.
- **ODD boundaries (§4.1.5):** Recognise ODD conditions; prevent activation outside ODD; execute fallback on ODD exit.
- **Fallback to MRC (§4.1.6):** ADSF-2 must fall back to MRC; ADSF-1 must execute MRC if system-initiated deactivation not completed.

### User Interactions (§4.2)
- **ADSF-1:** Continuously assess fallback user availability; trigger MRC fallback if fallback user unavailable.
- **ADSF-2:** Provide passenger stop request; manage non-DDT tasks.
- **Suitably engaged (§4.2.2.3.8.1):** User must be in contact with steering and gaze directed to driving task-relevant area.

### Other ADS Requirements (§4.3)
- DSSAD required (§4.3.1)
- Cybersecurity protection (§4.3.2)
- Software update support (§4.3.3)
- Protection from unauthorized access (§4.3.4)
- Maintenance interface (§4.3.5)

---

## Manufacturer Requirements Structure (§5)

### Five Pillars:
1. **Safety Management System — SMS (§5.1):** Safety policy, risk management, safety assurance, safety promotion, design/development management, production management, post-deployment management
2. **Test Environments (§5.2):** Virtual testing (simulation toolchain), track testing, real-world testing
3. **Safety Case (§5.3):** Safety concept, ODD description, behavioural competencies, testing evidence, independent self-assessment
4. **Post-Deployment Safety (§5.4):** Initial notifications, short-term reports (within 30 days), periodic reports (at least annually)
5. **Other Requirements (§5.5):** Maintenance information availability

---

## Compliance Assessment Structure (§6)

Four pillars of compliance assessment:
1. **Audit of SMS (§6.1):** Documentation audit of SMS processes
2. **Assessment of Test Environments (§6.2):** Virtual, track, real-world testing assessment
3. **Assessment of Safety Case (§6.3):** Content completeness/robustness, testing activities, confirmatory testing
4. **Post-Deployment Safety Assessment (§6.4):** Review of post-deployment reports

---

## Validation Multi-Pillar Approach (§34–39)

**Fact:** Four validation pillars:
1. **Virtual testing** — simulation toolchains, wide scenario coverage
2. **Track testing** — closed-access testing ground
3. **Real-world testing** — public roads
4. **Audit and assessment** — SMS and safety case audit

Each pillar has strengths and limitations; combination is required. See [[Validation]] and [[VMAD]].

---

## AI-Based ADS — Critical Limitation

**Fact (§41n):** "The requirements in this Regulation are written with the expectation that ADS software does not include the use of online in-vehicle learning that self-modifies system behaviour."

*Interpretation:* This is a significant constraint for AI-first ADS developers (e.g., [[Wayve]]). The GTR does not accommodate continuous in-vehicle learning. Systems using end-to-end neural networks that update in-field may not be covered by this framework.

---

## Procedural History (Confirmed)

| Event | Session/Date | Document |
|---|---|---|
| Framework Document adopted | 178th WP.29 | ECE/TRANS/WP.29/2019/34/Rev.2 |
| NATM first version adopted | 184th WP.29 (June 2021) | ECE/TRANS/WP.29/1159 |
| NATM second version | GRVA 12th session (Jan 2022) | ECE/TRANS/WP29/GRVA/2022/2 |
| FRAV/VMAD Integrated Document | June 2024 WP.29 | ECE/TRANS/WP.29/2024/39 |
| Regulatory approach for ADS adopted; IWG on ADS established | 191st WP.29 (Nov 2023) | WP.29-191-30/Rev.1; report ECE/TRANS/WP.29/1175 |
| AC.3 authorization for new UN GTR | 192nd WP.29 (March 2024) | ECE/TRANS/WP.29/AC.3/62; report ECE/TRANS/WP.29/1177 |
| IWG on ADS formally established | 192nd WP.29 (March 2024) | ECE/TRANS/WP.29/2024/38 |
| Framework Document amended | 192nd WP.29 | ECE/TRANS/WP.29/2024/33 |
| GTR recommended | GRVA 24th session | This document |
| GTR submitted for AC.3 vote | WP.29 199th session (June 2026) | ECE/TRANS/WP.29/2026/139 |

---

## IWG on ADS Leadership

**Fact:** Sponsored and led by: **Canada, China, European Commission, Japan, United Kingdom, United States of America**

Secretariat supported by: **AAPC** (American Automotive Policy Council), **OICA**, **JASIC** (Japan Automobile Standards Internationalization Center), **SAE International**

Ambassadors between IWG and GRVA Workshops: **Australia** and **Netherlands**

---

## Other Related IWGs Mentioned in Document

- [[AVC]] — Automated Vehicle Categorisation (IWG)
- [[EDR-DSSAD]] — Event Data Recorders / Data Storage for Automated Driving
- [[FADS]] — Regulation Fitness for Automated Driving Systems (task force)
- **GRVA ADS Workshops** — parallel process for administrative provisions

---

## Referenced Standards

| Standard | Organisation | Scope |
|---|---|---|
| ISO/SAE 21434:2021 | ISO/SAE | Cybersecurity engineering |
| ISO/PAS 22736:2021 | ISO/SAE | ADS taxonomy (basis for definitions) |
| ISO 26262:2018 | ISO | Functional safety |
| ISO 21448:2022 | ISO | SOTIF |
| ISO 9001 | ISO | Quality management |
| ISO 31000 | ISO | Risk management |
| ISO PAS 8800:2024 | ISO | Safety and artificial intelligence |
| ISO/TS 5083:2025 | ISO | Safety for ADS — design, V&V |
| IATF 16949 | IATF | Automotive quality management |
| ASAM OpenSCENARIO DSL V2.1.0 | ASAM | Scenario description |
| ASAM OpenDRIVE V1.8.1 | ASAM | Road network description |
| ASAM OpenODD V1.0 | ASAM | ODD description |
| SAE J3016 | SAE | Driving automation taxonomy |
| IEEE 2846:2022 | IEEE | Safety model assumptions |

---

## DSSAD — Annex 6 Summary

**Fact:** Every ADS vehicle must be equipped with a DSSAD (§4.3.1). Annex 6 specifies:
- Time-stamped events: activation, deactivation, ODD exit, fallback start, MRC achieved, collision, emergency manoeuvre, EDR trigger, remote intervention, failure
- Time-series data around triggering events: ±7 seconds window (vehicle acceleration, speed, steering demand, object distances and velocities, visual images)
- Data format: open standard (JSON, CSV, XML) except sensor data
- Accessibility: even without main power; even after impact

See [[DSSAD]] (concept) and [[DSSAD]] (working group) for full notes.

---

## Annex 1 — Reportable Occurrences

Three reporting types:
1. **Notification** (immediate): Critical occurrences only
2. **Short-term report** (within 30 days): Critical + significant occurrences (ODD exit, MRC failure, DDT requirement breach, unreasonable risk)
3. **Periodic report** (≥ annually): All occurrence categories

---

## Open Questions

- Was this GTR formally adopted by AC.3 vote at WP.29 199th session? [VERIFY — this document is the proposal; vote outcome not in this document]
- What provisions remain in [square brackets] and need GRVA 25th session confirmation?
- How do contracting parties implement this GTR domestically (particularly US/NHTSA)?
- What is the parallel UN Regulation text document number? (Likely ECE/TRANS/WP.29/2026/140 or similar)
- How does the "no online in-vehicle learning" clause affect AI-native ADS developers?
