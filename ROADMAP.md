---
type: meta
status: active
tags: [roadmap, planning, knowledge-acquisition]
related: [CHANGELOG, IMPORT_PIPELINE, REVIEW_PIPELINE, Home]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# ROADMAP — Future Knowledge Acquisition

Tracks planned knowledge imports, research priorities, and vault development goals.

---

## High Priority

Documents and knowledge areas needed to unlock the most value in the current regulatory cycle.

### Regulations and Frameworks

- [ ] **New UN Regulation on ADS (1958 Agreement)** — Parallel instrument to the GTR. Document number unknown; find companion to ECE/TRANS/WP.29/2026/139. Key: regulation number, scope, adoption status.
- [ ] **R157 — ALKS (current amendment series)** — Ingest the full R157 text including the speed limit extension amendments (01/02 series). Clarify ODD parameters, MRC requirements, and relationship to ADSF-1 definition.
- [ ] **R171 — DCAS (Supplement 2)** — Read local file `raw/ADAS-37-02`. Extract Supplement 2 changes to R171. Key: what does Supplement 2 modify vs. original R171?
- [ ] **GRVA 24th Session official report** — Find ECE/TRANS/WP.29/GRVA/24/Report or equivalent. Verify outcomes, document numbers, agenda items.
- [ ] **WP.29 199th Session official report** — Find ECE/TRANS/WP.29/1xxx (199th session report). Verify: Was the ADS UN GTR formally adopted by AC.3?

### Working Group Documents

- [ ] **ECE/TRANS/WP.29/2024/39** — FRAV/VMAD Integrated Document (June 2024). This is the primary technical basis for the ADS UN GTR. Critical for understanding VMAD multi-pillar methodology and FRAV functional requirements.
- [ ] **ECE/TRANS/WP.29/2026/142** — Companion Article 6 report for the ADS UN GTR. Contains cost-benefit analysis and full technical justification.
- [ ] **VMAD latest outputs** — Any VMAD session documents from 2025–2026 on validation methodology, scenario databases, simulation toolchain credibility.
- [ ] **FRAV functional requirements document** — The standalone FRAV deliverable before merger with VMAD.

### Concepts (Pending Source)

- [ ] **DCAS** — Read R171 original version text. Confirm scope, speed range, DMS requirements, ODD.
- [ ] **DSSAD Annex 6** — Already ingested from GTR; cross-check against any standalone DSSAD instrument.
- [ ] **Safety Case** — Ingest any GRVA guidance on safety case methodology beyond GTR §5.3.

---

## Medium Priority

Important for completeness but not immediately blocking.

### EU Regulatory Context

- [ ] **R(EU) 2021:1341 — DMS** — Read local file `raw/R(EU) 2021:1341 DMS.pdf`. EU mandate for Driver Monitoring Systems. Align with R171 DMS requirements.
- [ ] **R(EU) 2021:646 — ELKS** — Read local file `raw/R(EU) 2021:646 ELKS.pdf`. Emergency Lane Keeping System. Relate to R79 ACSF.
- [ ] **R(EU) 2021:1958 — ISA** — Read local file `raw/R(EU) 2021:1958 ISA.pdf`. Intelligent Speed Assistance. Link to ADAS regulatory landscape.
- [ ] **R(EU) 2023:2590 — DDAW** — Read local file `raw/R(EU) 2023:2590 DDAW.pdf`. Driver Drowsiness and Attention Warning. Link to Driver Monitoring.

### Additional GRVA Sessions

- [ ] **GRVA 25th Session** — Update placeholder. Key: resolution of [square brackets] in ADS UN GTR text.
- [ ] **GRVA 23rd Session** — Immediate predecessor to GRVA 24th. What was the state of ADS GTR one session before recommendation?
- [ ] **GRVA 18th Session** — Key session: adopted ToR for IWG on ADS, discussed regulatory approach.

### OEM Engagement

- [ ] **Mercedes-Benz Drive Pilot** — First R157 ALKS type approval. Update `06 OEM/Mercedes-Benz.md` with approval details.
- [ ] **Wayve regulatory position** — How does Wayve's end-to-end model interact with the GTR's "no online learning" clause (§41n)?
- [ ] **Chinese OEM ADS strategy** — NIO, Xpeng: GB/T national standard alignment vs. GTR adoption pathway.

### Standards

- [ ] **ISO PAS 8800:2024** — Safety and artificial intelligence. Referenced in ADS UN GTR. Critical for AI-based ADS regulatory analysis.
- [ ] **ISO/TS 5083:2025** — Safety for automated driving systems. Also referenced in GTR.
- [ ] **SAE J3016** — Driving automation taxonomy. The definitional basis for ADS levels. Summarize relevant sections.

---

## Low Priority

Useful background; not required for near-term analysis.

- [ ] **NATM first version** — ECE/TRANS/WP.29/1159. Historical context for VMAD methodology.
- [ ] **Framework Document on Automated Vehicles** — ECE/TRANS/WP.29/2019/34/Rev.2. The 2019 foundational document that set the WP.29 ADS agenda.
- [ ] **WP.29-191-30/Rev.1** — Regulatory approach proposal for ADS (November 2023). Historical record of IWG establishment decision.
- [ ] **AVC Task Force outputs** — Automated Vehicle Categorisation taxonomy document.
- [ ] **FADS Task Force outputs** — Regulation Fitness analysis for existing UN Regulations.
- [ ] **R79 current amendment series** — Confirm ACSF categories A–E and relationship to ADS steering requirements.
- [ ] **R155 / R156 amendments** — Any post-2021 amendments to the cybersecurity and software update regulations.

---

## Vault Development

Non-document tasks for vault improvement.

- [ ] **Install poppler** — `brew install poppler` to enable direct PDF reading without pypdf workaround
- [ ] **Run REVIEW_PIPELINE** — First full monthly review. Check for orphans, broken links, inconsistent metadata.
- [ ] **Resolve duplicate GRVA notes** — `07 Organizations/GRVA.md` vs `03 GRVA/GRVA.md`
- [ ] **Resolve duplicate WP.29 notes** — `07 Organizations/WP.29.md` vs `02 WP29/WP29.md`
- [ ] **Add 14 Timeline entries** — Populate `ADS Timeline.md` and `GRVA Timeline.md` with the confirmed milestones from ECE/TRANS/WP.29/2026/139 procedural history
- [ ] **Add Source Registry entries** — Populate `13 Resources/Source Registry.md` with sources used so far
- [ ] **Update Home.md** — Link to Dashboard and Today pages

---

## Completed

Items that have been ingested or resolved.

- [x] **ADS UN GTR** — ECE/TRANS/WP.29/2026/139 — ingested 2026-06-27 — 87 pages, full knowledge graph update
- [x] **GRVA 24th Session** — Confirmed facts from GTR cover page
- [x] **WP.29 199th Session** — Confirmed dates, agenda item 14.1.1
- [x] **VMAD** — Confirmed NATM deliverables, multi-pillar framework
- [x] **FRAV** — Confirmed FRAV/VMAD Integrated Document basis
- [x] **DSSAD** — Confirmed Annex 6 data requirements from GTR
- [x] **Safety Case** — Defined from GTR §2.31 and §5.3
- [x] **Safety Management System** — Defined from GTR §2.27 and §5.1
- [x] **Behavioural Competency** — Defined from GTR §2.22 and Annex 5
- [x] **ADSF-1 / ADSF-2** — Defined from GTR §2.6.1–2.6.2
- [x] **MRC** — Defined from GTR §2.20; distinguished from MRM
- [x] **ISMR** — Defined from GTR §5.1.8 and §5.4
- [x] **Vault structure** — Folders, templates, meta documents created
