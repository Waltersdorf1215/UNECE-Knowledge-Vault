# CHANGELOG — UNECE Knowledge OS

Chronological history of every knowledge import and vault operation.
Newest entries first.

---

## Acquisition + Merge + Review — 2026-06-28 | GDPR implications of R171

**Question:** What are the GDPR implications of R171?
**Vault state before:** `exists_incomplete` — R171 contained driver monitoring and in-service monitoring facts but no GDPR/data-protection section
**Deep Research invoked:** Yes — missing section acquired from official GDPR text only

### Scores
- Before GDPR section: **84 / 100**
- After GDPR section: **88 / 100**

### Notes Updated
- `01 Regulations/R171.md` — added `GDPR / Data Protection Implications` section covering personal data risk, lawful basis, minimisation, privacy by design/default, DPIA relevance, retention, access/security, and reporting proportionality.

### Review Artifacts Updated
- `11 Review/R171 Review.md`
- `11 Review/Knowledge Backlog.md`

### Sources Used
- `01 Regulations/R171.md` / `E/ECE/TRANS/505/Rev.3/Add.170`
- Regulation (EU) 2016/679, official EUR-Lex text

### Knowledge Gaps Remaining
- [VERIFY] Concrete retention periods and reporting schemas for R171 in-service monitoring data.
- [VERIFY] Anonymisation/pseudonymisation expectations from type approval authorities or implementation guidance.

---

## Acquisition + Review — 2026-06-28 | Driver Availability in UNECE DCAS

**Question:** What is Driver Availability in UNECE DCAS?
**Vault state before:** `exists_incomplete` — `05 Concepts/Driver Availability.md` existed but was `draft` with `source_pending`
**Deep Research invoked:** No — existing Vault evidence from R171 was sufficient for DCAS scope

### Answer
In UNECE DCAS, Driver Availability is the working concept for whether the driver remains engaged and able to supervise and intervene while DCAS assists with longitudinal and lateral control. R171 does not define a standalone term called "driver availability"; it defines driver disengagement and requires driver monitoring, warning escalation, and Risk Mitigation Function activation if the driver remains unavailable.

### Notes Updated
- `05 Concepts/Driver Availability.md` — upgraded to active; added R171-sourced DCAS meaning, driver disengagement basis, warning escalation, RMF fallback, evidence, references, and open questions

### Review Artifacts Created or Updated
- `11 Review/Driver Availability Review.md`
- `11 Review/Dashboard.md`
- `11 Review/Knowledge Backlog.md`

### Knowledge Score
- Driver Availability: **88 / 100**

### Knowledge Gaps Remaining
- [VERIFY] R157 driver availability / transition demand requirements need official source extraction.
- [VERIFY] ADSF-1 vs ADSF-2 fallback-user availability needs ADS regulation review.
- [VERIFY] EU DMS/DDAW interaction with DCAS driver monitoring needs EU source processing.

---

## Review — 2026-06-28 | EME answered from Vault and reviewed

**Question:** What is EME in the context of UNECE?
**Vault state before:** `exists_complete` — canonical note found at `07 Organizations/E-Mobility Europe.md`
**Deep Research invoked:** No

### Answer
EME = **E-Mobility Europe** in the current UNECE/GRVA Vault context. It is documented as a European e-mobility industry association participating in GRVA/ADAS Task Force work on DCAS and R171 amendment development.

### Review Artifacts Created
- `11 Review/E-Mobility Europe Review.md`
- `11 Review/Dashboard.md`
- `11 Review/Knowledge Backlog.md`

### Notes Updated
- None. No knowledge notes were modified.

### Knowledge Gaps Remaining
- Add precise references for EME organization facts and membership claims.
- Confirm and backlink EME participation from ADAS TF, NIO, and Xpeng after evidence capture.
- Determine whether EME participates in GRVA sub-groups beyond ADAS TF.

---

## Acquisition — 2026-06-28 | E-Mobility Europe (EME) — What is EME in UNECE GRVA?

**Question:** What is EME in the context of UNECE GRVA?
**Vault state before:** MISSING — no EME note existed
**Deep Research invoked:** Yes (workflow launched; source document retrieved directly via WebFetch)
**Primary source:** ADAS-45-07 (EME) Inputs Next Steps.pdf — TF-ADAS 45th session, 2026-03-03

### Answer
EME = **E-Mobility Europe** — European trade association representing the e-mobility ecosystem (70+ members). Founded February 3, 2025 as the evolution of AVERE. Secretary General: Chris Heron. Participates in UNECE GRVA ADAS Task Force, submitting DCAS Phase 3 and Phase 4 proposals.

### Notes Created
- `07 Organizations/E-Mobility Europe.md` — organization profile, UNECE engagement, R171 phase overview

### Notes Updated
- `03 GRVA/GRVA 24th Session.md` — added confirmed Phase 3 (02 series) endorsement fact
- `14 Timeline/R171 Timeline.md` — added GRVA 24th Phase 3 milestone and ADAS 45th session entry

### Attachments Saved
- `12 Attachments/UNECE/ADAS-45-07-EME-Inputs-Next-Steps.pdf`

### Relationships Added
- E-Mobility Europe → `participates_in` → ADAS TF (Class 2, explicit from doc)
- E-Mobility Europe → `contributes_to` → R171 development (Class 2, explicit from doc)
- GRVA 24th Session → `endorses` → R171 02 series Phase 3 (Class 1, explicit: ADAS-45-07 p.2)
- NIO, Xpeng → `member_of` → E-Mobility Europe (Class 1, from emobilityeurope.org)

### New Knowledge Discovered
- R171 development phases (Phase 1–4) with amendment series mapping (from ADAS-45-07)
- wHOR (Withholding HOR) and SIM (System-Initiated Manoeuvre) as new acronyms in R171 Phase 2–4
- GRVA 24th session confirmed to have endorsed R171 02 series (Phase 3)
- Phase 4 (03 series) planned to address non-rule-based algorithm systems (AI-based DCAS)

### Knowledge Gaps Remaining
- [VERIFY] Official document number for R171 02 series endorsed at GRVA 24th
- [VERIFY] What was AVERE's role before EME was founded?
- [VERIFY] Phase 4 (03 series) formal mandate and timeline

---

## Import — 2026-06-28 | E/ECE/TRANS/505/Rev.3/Add.170 (UN Regulation No. 171)

**Imported Document**
- `12 Attachments/UNECE/R171e.pdf` — UN Regulation No. 171 (DCAS), original version
- Authentic text: ECE/TRANS/WP.29/2024/37
- Entry into force: 22 September 2024 | Published: 13 December 2024
- Pages: 80

**Updated Notes**
- `01 Regulations/R171.md` — fully sourced rewrite: official definitions, SAE L2 classification, explicit prerequisite regulations (R79, R130, R131, R152, R156), driver monitoring escalation sequence (HOR/EOR/DCA timings), RMF requirement, multi-pillar validation, in-service monitoring, R157 absence confirmed; status upgraded to `active`
- `14 Timeline/R171 Timeline.md` — entry into force date confirmed: 2024-09-22; status upgraded to `active`
- `05 Concepts/DCAS.md` — official §2.1 definition, SAE L2 confirmation, ADS distinction (Introduction §5), feature types, R79 dependency
- `05 Concepts/Driver Monitoring.md` — full HOR/EOR/DCA escalation sequence from §5.5.4.2.6 with exact timing thresholds; motoric vs visual disengagement definitions; status upgraded to `active`
- `01 Regulations/R156.md` — added confirmed explicit cross-reference from R171 §10.3
- `01 Regulations/R79.md` — added confirmed cross-references from R171 §5.1.5 and §5.3.7.3.1
- `11 Review/Pending/R157-R171-evidence-review.md` — status updated to `partially_resolved`; R171 confirmed to contain no R157 cross-reference

**Created Notes**
- `05 Concepts/Risk Mitigation Function.md` — new concept; RMF defined in R79 04-series, cross-referenced in R171 §5.3.7.3.1; comparison table with MRM and MRC

**Relationships Merged (Class 1 — Official, from R171 text)**
- R171 → `requires` → R79 (Corrective Steering Function, §5.1.5)
- R171 → `requires` → R130 (LDWS, §5.1.5)
- R171 → `requires` → R131 (AEBS heavy, §5.1.5)
- R171 → `requires` → R152 (AEBS light, §5.1.5)
- R171 → `requires` → R156 (Software Updates, §10.3)
- R171 → `defines` → Driver disengagement (§2.6)
- R171 → `defines` → System Boundaries (§2.5)
- R171 → `references` → R79 04-series (RMF requirement, §5.3.7.3.1)

**Review Items Updated**
- `R157-R171-evidence-review.md` — partially resolved: R171 text confirms no R157 cross-reference; recommend move to Rejected/

**Claims Rejected (Evidence Gate)**
- "R171 is the data-recording companion of R157" — R171 contains no mention of R157; rejected
- "R171 derives from R157" — no evidence in R171 text; rejected
- "R155 is a prerequisite for R171" — R171 §10.3 requires R156 only; R155 not mentioned; rejected for R171 specifically

**Remaining Evidence Gaps**
- R157 full text not ingested — cannot confirm whether R157 references R171 (add to ROADMAP High Priority)
- R171 adoption WP.29 session date not in document — only entry into force (2024-09-22) confirmed
- Supplement 2 (ADAS-37-02 DOCX) content unread — requires DOCX parser
- EU mandatory applicability timeline for R171 not confirmed

---

## Import — 2026-06-27 | ECE/TRANS/WP.29/2026/139

**Imported Documents**
- ECE/TRANS/WP.29/2026/139 — Proposal for a new UN GTR on Automated Driving Systems (87 pages)
- Source: `12 Attachments/UNECE/ECE-TRANS-WP.29-2026-139e.pdf`

**Updated Notes**
- `01 Regulations/ADS UN GTR.md` — Full sourced content: official definitions, requirements structure, procedural history, IWG leadership, standards references, DSSAD Annex 6 summary
- `03 GRVA/GRVA 24th Session.md` — Confirmed recommendation fact; document number ECE/TRANS/WP.29/GRVA/2026/2
- `02 WP29/WP29 199th Session.md` — Confirmed dates (June 23–26, 2026), Agenda Item 14.1.1, document number
- `04 Working Groups/ADS IWG.md` — Leadership (Canada/China/EC/Japan/UK/US), secretariat (AAPC/OICA/JASIC/SAE), ambassadors (Australia/Netherlands)
- `04 Working Groups/VMAD.md` — NATM deliverables confirmed, multi-pillar mandate, FRAV/VMAD Integrated Document
- `04 Working Groups/FRAV.md` — FRAV/VMAD Integrated Document (ECE/TRANS/WP.29/2024/39) confirmed as technical basis
- `04 Working Groups/DSSAD.md` — Annex 6 data requirements (time-stamped events, ±7s time-series window)
- `05 Concepts/Automated Driving System.md` — Official §2.1 definition; ADSF-1/ADSF-2 types; online learning exclusion
- `05 Concepts/DDT.md` — Official §2.3 definition with three subcategories
- `05 Concepts/ODD.md` — Official §2.12 definition; ODD exit defined
- `05 Concepts/MRM.md` — Clarified MRM (R157/SAE) vs. MRC (GTR) terminology distinction
- `05 Concepts/Validation.md` — Four-pillar approach confirmed; NATM history
- `05 Concepts/DSSAD.md` — Official §2.11 definition; full Annex 6 data element tables

**Created Notes**
- `05 Concepts/MRC.md` — Mitigated Risk Condition (official §2.20)
- `05 Concepts/Safety Case.md` — §2.31 + §5.3
- `05 Concepts/Safety Management System.md` — §2.27 + §5.1
- `05 Concepts/Behavioural Competency.md` — §2.22 + Annex 5
- `05 Concepts/OEDR.md` — Object and Event Detection and Response
- `05 Concepts/ISMR.md` — In-Service Monitoring and Reporting §5.1.8 + §5.4
- `05 Concepts/ADS Fallback Response.md` — §2.15
- `05 Concepts/ADSF-1 and ADSF-2.md` — §2.6.1–2.6.2
- `04 Working Groups/AVC.md` — Automated Vehicle Categorisation
- `04 Working Groups/FADS.md` — Regulation Fitness for ADS
- `10 Research Notes/2026-06 ADS GTR Reading.md`

**New Relationships**
- `GRVA 24th Session` → recommends → `ADS UN GTR`
- `WP29 199th Session` → considers (AC.3 vote) → `ADS UN GTR`
- `ADS IWG` → sponsored by → Canada, China, EC, Japan, UK, US
- `ADS UN GTR` → defines → MRC, ADSF-1/ADSF-2, Safety Case, SMS, Behavioural Competency, OEDR, ISMR, ADS Fallback Response
- `ADS UN GTR` → based on → FRAV/VMAD Integrated Document (ECE/TRANS/WP.29/2024/39)
- `AVC` + `FADS` → reports to → `ADS IWG`

**Open Questions**
- Was the GTR formally adopted by AC.3 at WP.29 199th? (vote outcome not in source document)
- What is the parallel 1958 Agreement UN Regulation document number?
- Which provisions are in [square brackets] requiring GRVA 25th reconfirmation?
- How does §41(n) "no online in-vehicle learning" affect AI-native ADS developers?

**Follow-up Documents**
- ECE/TRANS/WP.29/2026/142 (companion Article 6 report)
- ECE/TRANS/WP.29/2024/39 (FRAV/VMAD Integrated Document — primary technical basis)
- WP.29 199th session official report (vote outcome)
- Parallel 1958 Agreement UN Regulation text

---

## Import — 2026-06-27 | Initial Knowledge Framework Import

**Imported Documents**
- Research synthesis: UNECE 2026 ADAS/ADS regulatory framework (no source document)
- Vault structure, rules, schema, and ontology designed

**Created Notes**
- `CLAUDE.md`, `KNOWLEDGE_RULES.md`, `SCHEMA.md`, `ONTOLOGY.md`, `RELATIONSHIPS.md`, `IMPORT_PIPELINE.md`
- `00 Home/Home.md`
- All regulation placeholders: R79, R155, R156, R157, R171, ADS UN GTR
- All working group placeholders: ADS IWG, VMAD, FRAV, DSSAD, DCAS, ADAS TF, EDR-DSSAD
- All concept placeholders: ADS, ADAS, ODD, DDT, MRM, Driver Monitoring, Driver Availability, etc.
- All OEM placeholders: NIO, BMW, Mercedes-Benz, VW, Tesla, Wayve, Mobileye, Xpeng
- All organization placeholders: UNECE, WP.29, GRVA, OICA, CLEPA, EC, RDW, BASt, TÜV
- All 8 templates in `11 Templates/`
- `10 Research Notes/UNECE 2026 ADAS ADS Regulatory Framework.md`

**New Relationships**
- Full vault relationship structure per ONTOLOGY.md and RELATIONSHIPS.md

**Open Questions**
- All entity notes in `placeholder` status — require source document ingestion to become `active`

---

## Vault Initialization — 2026-06-27

**Created**
- Vault structure: folders `00 Home` through `13 Resources`
- All root meta documents
- Initial placeholder notes for all major UNECE entities

**Version:** Knowledge OS v1.0 initialization
