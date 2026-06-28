---
type: concept
status: active
tags: [concept, SMS, safety-management, ADS, manufacturer-requirements]
related: [ADS UN GTR, Safety Case, Validation, ISMR, ADS, Functional Safety, SOTIF, Cybersecurity]
source: "ECE/TRANS/WP.29/2026/139, §2.27 and §5.1"
last_updated: 2026-06-27
created: 2026-06-27
defined_in: "ECE/TRANS/WP.29/2026/139, §2.27"
aliases: [SMS, Safety Management System]
---

# Safety Management System (SMS)

## Definition

**Fact (ECE/TRANS/WP.29/2026/139, §2.27):**
> "A systematic approach to managing safety that encompasses and integrates organisational, human, and technical factors:
> (a) Human component ensuring the ADS lifecycle is monitored by personnel with appropriate skills, training, and understanding...
> (b) Organisational component procedures and methods that help to manage the identified risks...
> (c) Technical component using appropriate tools and equipment."

---

## Role in the ADS GTR

**Fact (§5.1):** Every ADS manufacturer must establish, implement, and document an SMS. The SMS is both a **compliance requirement** and the **object of audit** under §6.1.

### SMS Components Required (§5.1):

| Component | Description |
|---|---|
| Safety policy (§5.1.2) | Aims, objectives, governance, safety culture |
| Risk management (§5.1.3) | ISO 31000-aligned identification, analysis, treatment |
| Safety assurance (§5.1.4) | Independent audits, supply chain management, change management |
| Safety promotion (§5.1.5) | Continual improvement, training, internal/external communication |
| Design and development (§5.1.6) | Requirements management, V&V, functional safety (ISO 26262), SOTIF (ISO 21448) |
| Production (§5.1.7) | Quality Management System (IATF 16949 or ISO 9001), supply chain |
| Post-deployment (§5.1.8) | [[ISMR]] — In-Service Monitoring and Reporting |

---

## SMS and the Safety Case

The SMS is the organisational framework within which the [[Safety Case]] is developed and maintained. The safety case demonstrates that the SMS has produced an ADS free of unreasonable risk.

---

## SMS Audit (§6.1)

**Fact:** The SMS documentation is audited by competent auditors for compliance with §5.1. The audit covers:
- Safety policy
- Risk management
- Safety assurance
- Safety promotion
- Design and development processes
- Production processes
- Post-deployment (ISMR) processes

---

## Referenced Standards

**Fact (§5.1.2–5.1.6):**
- ISO 21434 (cybersecurity) — referenced for safety policy
- ISO 9001 / IATF 16949 — quality management
- ISO 26262 — functional safety in design/development
- ISO 21448 (SOTIF) — SOTIF management in design/development
- ISO 31000 — risk management
- ISO 9241-210 — human-centred design
- FMEA, FTA, STPA — safety analysis methods mentioned

---

## Key Links

- [[Safety Case]] — the output demonstrating SMS effectiveness
- [[ISMR]] — post-deployment component of SMS
- [[Validation]] — testing activities are managed under the SMS
- [[Functional Safety]] — managed within SMS design/development
- [[SOTIF]] — managed within SMS design/development
- [[Cybersecurity]] — cross-functional with SMS
