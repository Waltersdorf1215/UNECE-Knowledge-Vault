---
type: research_note
status: active
tags: [reading-note, ADS, GTR, WP29, 2026, ECE-TRANS-WP29-2026-139]
related: [ADS UN GTR, GRVA 24th Session, WP29 199th Session, ADS IWG, VMAD, FRAV, DSSAD, ADS, DDT, ODD, MRC, Safety Case, Safety Management System, Behavioural Competency, OEDR, ISMR, ADS Fallback Response, ADSF-1 and ADSF-2, Validation, AVC, FADS, Wayve, OICA]
source: "ECE/TRANS/WP.29/2026/139"
last_updated: 2026-06-27
created: 2026-06-27
question: "What does the actual ADS UN GTR text (ECE/TRANS/WP.29/2026/139) contain, and what are its key regulatory implications?"
---

# 2026-06 ADS GTR Reading Note

## Document

**ECE/TRANS/WP.29/2026/139** — Proposal for a new United Nations Global Technical Regulation on Automated Driving Systems (ADS)
- Submitted to: **WP.29 199th session, Geneva, 23–26 June 2026**
- Agenda Item: **14.1.1** (AC.3 consideration and vote on draft UN GTRs)
- Submitted by: **GRVA**
- Recommended by: **GRVA at its 24th session**
- 87 pages, 6 sections, 6 annexes

---

## Key Observations

### 1. This is the ADS UN GTR Proposal — Not Yet a Confirmed Adoption
The document is the **proposal submitted to WP.29 199th session** for AC.3 vote. It does not confirm the outcome of that vote. The companion document ECE/TRANS/WP.29/2026/142 contains the Article 6 report justifying the GTR. Vote outcome must be found in the official session report.

### 2. ADSF-1 / ADSF-2 is the Core Structural Distinction
The GTR's most important structural innovation is distinguishing ADS features that require a human fallback user (**ADSF-1**) from those that do not (**ADSF-2**). This replaces the loose "Level 3 vs Level 4" framing with a function-specific classification. This matters enormously for regulatory coverage and OEM product design.

### 3. MRC Replaces MRM in the GTR Vocabulary
The GTR uses **MRC (Mitigated Risk Condition)** for the end-state, and **ADS Fallback Response** for the process. This differs from R157 and SAE J3016's "MRM" terminology. The existing vault notes using "MRM" should note this distinction.

### 4. AI-Based ADS is Explicitly Excluded from Online Learning
**Paragraph 41(n)** states the regulation does not cover "online in-vehicle learning that self-modifies system behaviour." This is a critical constraint for AI-native ADS developers. Systems like Wayve's end-to-end model that update continuously may not be certifiable under this framework as written.

### 5. Multi-Pillar Validation is Formalized
The four-pillar approach (virtual, track, real-world, audit) is now the established validation framework. No single pillar is sufficient. Virtual testing requires a formal credibility framework for simulation toolchains.

### 6. Safety Case + SMS = The Compliance Architecture
The GTR's compliance model is entirely based on a **Safety Case** (manufacturer's structured evidence) audited under a **Safety Management System** (SMS). This is different from prescriptive pass/fail tests. The authority audits the manufacturer's processes and evidence, not just the vehicle.

### 7. Simultaneous GTR and UN Regulation Development
**Paragraph 87** notes this is "the first simultaneous development of a UN GTR and corresponding UN Regulation for shared safety goals." The parallel 1958 Agreement UN Regulation text is not in this document; its document number needs to be verified.

### 8. Massive Standards Stack Referenced
The GTR references an impressive stack: ISO 26262, ISO 21448, ISO/SAE 21434, ISO 9001, ISO 31000, ISO PAS 8800 (AI safety), ISO/TS 5083:2025, IATF 16949, ASAM OpenSCENARIO, ASAM OpenDRIVE, ASAM OpenODD, SAE J3016, IEEE 2846. National standards from China, UK, Germany, Japan, and US also listed.

### 9. DSSAD Data Requirements are Concrete
Annex 6 provides specific data element requirements: ±7 second time-series window, open format (JSON/CSV/XML), accessibility requirements. This is implementable and auditable.

### 10. Post-Deployment is Institutionalized
The ISMR (In-Service Monitoring and Reporting) requirements are detailed and mandatory. Short-term reports within 30 days; periodic reports at least annually. Manufacturers must demonstrate monitoring capability before deployment.

### 11. Text Contains Square Brackets
Some provisions are in [square brackets] requiring GRVA 25th session reconfirmation. This means the text submitted to WP.29 199th is not fully finalized.

---

## IWG on ADS Leadership — Confirmed

**Leadership sponsors:** Canada, China, European Commission, Japan, United Kingdom, United States
**Secretariat:** AAPC, OICA, JASIC, SAE International
**Ambassadors (ADS-GRVA liaison):** Australia, Netherlands

---

## Key Document References Found in This Document

| Reference | Description |
|---|---|
| ECE/TRANS/WP.29/2026/139 | This GTR proposal |
| ECE/TRANS/WP.29/2026/142 | Companion Article 6 report |
| ECE/TRANS/WP.29/GRVA/2026/2 | GRVA formal basis document |
| WP.29-198-07 | Informal document (basis) |
| ECE/TRANS/WP.29/2024/39 | FRAV/VMAD Integrated Document (June 2024) — primary technical basis |
| ECE/TRANS/WP.29/2024/38 | IWG on ADS establishment document |
| ECE/TRANS/WP.29/2024/33 | Framework Document amendment (incorporating IWG establishment) |
| ECE/TRANS/WP.29/AC.3/62 | AC.3 authorization for GTR |
| ECE/TRANS/WP.29/1175 | Report of 191st WP.29 session |
| ECE/TRANS/WP.29/1177 | Report of 192nd WP.29 session |
| ECE/TRANS/WP.29/1159 | NATM first version (184th WP.29, June 2021) |
| ECE/TRANS/WP29/GRVA/2022/2 | NATM second version |
| ECE/TRANS/WP.29/2019/34/Rev.2 | Framework Document on Automated Vehicles |
| ECE/TRANS/WP.29/2022/57 | NATM guidelines |

---

## Unresolved Questions

1. **Was the GTR adopted by AC.3 at WP.29 199th session?** — The document is the proposal; the vote outcome is in the session report (not in this document).
2. **What is the parallel UN Regulation document number?** (1958 Agreement) — Not in this document; likely submitted as a separate document.
3. **What provisions are in [square brackets]?** — Appears throughout the DSSAD Annex 6 specifically; requires GRVA 25th session reconfirmation.
4. **How does NHTSA respond to this GTR?** — US is a co-sponsor of the IWG but FMVSS transposition is needed domestically.
5. **How do Chinese OEMs align?** — China is a co-sponsor; GB/T national standards listed suggest China-specific context.
6. **What does "regulation fitness" analysis from FADS show about R79, R157, R171 gaps?**
7. **How does the AVC categorisation framework map to the ADSF-1/ADSF-2 distinction?**

---

## Follow-Up Documents to Find

1. **ECE/TRANS/WP.29/2026/142** — Companion Article 6 report (cost-benefit, technical justification)
2. **ECE/TRANS/WP.29/2024/39** — FRAV/VMAD Integrated Document (full technical basis)
3. **WP.29 199th session report** — Actual adoption/vote outcomes
4. The **parallel 1958 Agreement UN Regulation** text document (not identified yet)
5. **GRVA 25th session report** — Resolution of square bracket provisions
6. **AVC Task Force outputs** — Categorisation framework document
7. **FADS Task Force outputs** — Regulation fitness analysis

---

## Future Research Ideas

1. **AI Regulation Boundary Study:** What does the "no online in-vehicle learning" clause mean in practice for AI-native ADS? Can a model be validated before deployment and then frozen? What about over-the-air model updates under R156?

2. **ADSF-1 vs ADSF-2 OEM Mapping:** Which products from [[BMW]], [[Mercedes-Benz]], [[Wayve]], [[Mobileye]], [[NIO]], [[Xpeng]] are ADSF-1 vs ADSF-2?

3. **Type Approval Pathway Analysis:** For the EU: how does the new ADS UN Regulation get incorporated into EU 2018/858? What are the competent authority implications for [[RDW]], [[BASt]], [[TÜV]]?

4. **DSSAD Implementation:** What does Annex 6 mean for OEM data architectures? Is on-board or off-board DSSAD preferred? Privacy implications under GDPR?

5. **R157 Alignment:** How does the ADSF-1/ADSF-2 framework map to R157's ALKS? Is ALKS an ADSF-1 feature by definition?

6. **China Implementation:** The GB/T standards listed suggest China has parallel national standards. How does the GTR relate to China's GB standards on ADS?
