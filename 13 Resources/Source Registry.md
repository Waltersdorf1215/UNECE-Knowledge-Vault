---
type: meta
status: active
tags: [sources, registry, authority, reliability]
related: [KNOWLEDGE_RULES, IMPORT_PIPELINE, CHANGELOG]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# Source Registry

Registry of all information source types used in this vault. Reference when assessing the reliability of a factual claim.

---

## Registry

| Source | Authority Level | Reliability | Typical Usage |
|---|---|---|---|
| **UNECE official documents** (ECE/TRANS/WP.29/…) | Highest — primary regulatory text | Authoritative | Regulations, GTRs, meeting reports, formal proposals |
| **GRVA session documents** (ECE/TRANS/WP.29/GRVA/…) | High — official working party text | Authoritative | Working group decisions, regulatory drafts |
| **GRVA informal documents** (GRVA-XX-YYY) | Medium-High — session working papers | High | Technical proposals, position papers, IWG reports |
| **WP.29 informal documents** (WP.29-XXX-YYY) | Medium-High — session working papers | High | Cross-delegation proposals, IWG reports |
| **IWG session documents** (ADS-XX-YYY, FRAV-XX-YYY) | Medium — informal group working papers | Medium-High | Technical development, internal drafts |
| **European Commission** (EU Official Journal, Regulations) | High — binding EU law | Authoritative for EU context | EU implementing acts, GSR mandates, type approval law |
| **OICA / CLEPA submissions** | Medium — industry position | Reliable for industry stance | OEM/supplier positions in WP.29 |
| **ISO / SAE / IEEE / ASAM standards** | High — consensus technical standards | Authoritative for definitions | Technical definitions, safety frameworks, test methods |
| **OEM press releases / technical blogs** | Low-Medium — self-reported | Use as context only | OEM product announcements, stated capability claims |
| **Academic papers** | Medium — peer reviewed | Use for technical background | Research findings, methodology |
| **Automotive media** (ACEA, SAE news, etc.) | Low — secondary reporting | Useful for context | Regulatory news, industry reactions |
| **National government documents** | Medium-High (jurisdiction-specific) | Authoritative within jurisdiction | National transposition, domestic law |

---

## Source Tiers for This Vault

### Tier 1 — Citable as Fact (no qualifier needed)
- ECE/TRANS/WP.29/XXXX/YYY (official UNECE documents)
- ECE/TRANS/WP.29/GRVA/XXXX/YYY (official GRVA documents)
- EU Official Journal implementing acts
- ISO/SAE/IEC published standards

### Tier 2 — Citable with Document Reference
- GRVA informal documents
- WP.29 informal documents
- IWG working documents
- National government publications

### Tier 3 — Context Only (label as *Interpretation:* or *Insight:*)
- Industry association submissions (OICA, CLEPA)
- OEM announcements
- Academic papers
- Media reports

---

## Documents Ingested So Far

| Document Number | Title | Date | Tier |
|---|---|---|---|
| ECE/TRANS/WP.29/2026/139 | ADS UN GTR proposal | 2026-06-27 | 1 |
| raw/ADAS-37-02 | R171 Supplement 2 proposal | Referenced | 1 |
| raw/R(EU) 2021:1341 | EU DMS regulation | Referenced | 1 |
| raw/R(EU) 2021:646 | EU ELKS regulation | Referenced | 1 |
| raw/R(EU) 2021:1958 | EU ISA regulation | Referenced | 1 |
| raw/R(EU) 2023:2590 | EU DDAW regulation | Referenced | 1 |

---

## Adding a New Source

When a new source is ingested:
1. Add a row to the **Documents Ingested So Far** table above
2. Record the document in `CHANGELOG.md`
3. Update `ROADMAP.md` — move item from pending to completed
