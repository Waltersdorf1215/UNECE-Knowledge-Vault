---
type: meta
status: active
tags: [ontology, schema, knowledge-graph, mermaid]
related: [SCHEMA, KNOWLEDGE_RULES, CLAUDE, Home]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# ONTOLOGY — UNECE Automated Driving Knowledge OS

Concise visual model of the knowledge graph. Every future Claude session should load this file to understand the entity types and relationships in this vault before taking any action.

---

## Entity Hierarchy

```mermaid
graph TD
    KB[Knowledge Base]

    KB --> REG[Regulation]
    KB --> WG[Working Group]
    KB --> MTG[Meeting]
    KB --> PROP[Proposal]
    KB --> CON[Concept]
    KB --> OEM[OEM]
    KB --> ORG[Organization]
    KB --> RN[Research Note]
    KB --> PI[Personal Insight]

    REG:::entity
    WG:::entity
    MTG:::entity
    PROP:::entity
    CON:::entity
    OEM:::entity
    ORG:::entity
    RN:::working
    PI:::working

    classDef entity fill:#2d4a6e,stroke:#5b8dd9,color:#e8f0fe
    classDef working fill:#3d3d2e,stroke:#a89a5b,color:#f5f0d8
```

---

## Core Entity Relationships

```mermaid
graph LR
    ORG[Organization]
    WG[Working Group]
    MTG[Meeting]
    PROP[Proposal]
    REG[Regulation]
    CON[Concept]
    OEM[OEM]

    ORG -->|hosts| MTG
    ORG -->|supervises| WG
    ORG -->|submits| PROP
    WG -->|reports to| ORG
    WG -->|creates| PROP
    WG -->|develops| REG
    MTG -->|considers| PROP
    MTG -->|advances| REG
    PROP -->|modifies| REG
    PROP -->|discussed at| MTG
    REG -->|defines| CON
    REG -->|requires| CON
    REG -->|complements| REG
    CON -->|is component of| CON
    CON -->|precedes| CON
    OEM -->|implements| REG
    OEM -->|submits| PROP
    OEM -->|member of| ORG
```

---

## Regulatory Process Flow

```mermaid
flowchart LR
    subgraph UNECE Process
        ORG[Organization\ncontracting party / observer]
        WG[Working Group\nIWG / TF]
        MTG[Meeting\nGRVA / WP.29 session]
        PROP[Proposal\nINF / WP document]
        REG[Regulation\nUN Reg / UN GTR]
    end

    ORG -->|establishes mandate for| WG
    WG -->|drafts| PROP
    PROP -->|submitted to| MTG
    MTG -->|adopts or defers| PROP
    PROP -->|amends| REG
    REG -->|type approval via| ORG
```

---

## Concept Dependency Graph (Core Concepts)

```mermaid
graph LR
    ADS[ADS\nAutomated Driving System]
    ADAS[ADAS]
    ODD[ODD\nOperational Design Domain]
    DDT[DDT\nDynamic Driving Task]
    MRM[MRM\nMinimal Risk Maneuver]
    TD[Transition Demand]
    DM[Driver Monitoring]
    DA[Driver Availability]
    DSSAD[DSSAD]
    EDR[Event Data Recorder]
    FS[Functional Safety]
    SOTIF[SOTIF]
    CYB[Cybersecurity]
    SWU[Software Update]

    ADS -->|operates within| ODD
    ADS -->|performs| DDT
    ADS -->|executes| MRM
    ADAS -->|assists with| DDT
    DDT -->|transitions via| TD
    TD -->|triggers if unresponded| MRM
    DM -->|assesses| DA
    DA -->|required for| TD
    DSSAD -->|records| DDT
    EDR -->|subset of| DSSAD
    FS -->|complements| SOTIF
    CYB -->|interacts with| FS
    SWU -->|vector for| CYB
```

---

## Regulation Landscape

```mermaid
graph TD
    subgraph Active Regulations
        R79[R79\nSteering / ACSF]
        R155[R155\nCybersecurity]
        R156[R156\nSoftware Updates]
        R157[R157\nALKS — SAE L3]
        R171[R171\nDCAS — SAE L2]
    end

    subgraph In Development
        GTR[ADS UN GTR\nSAE L3+]
    end

    R155 <-->|companion| R156
    R79 -->|underpins steering in| R157
    R157 -->|preceded| GTR
    R171 -->|DCAS feeds into| GTR
```

---

## Working Group Map

```mermaid
graph TD
    WP29[WP.29]
    GRVA[GRVA]
    ADSI[ADS IWG]
    VMAD[VMAD]
    FRAV[FRAV]
    DSSAD_WG[DSSAD WG]
    EDRDSSAD[EDR-DSSAD]
    DCAS_WG[DCAS WG]
    ADASTF[ADAS TF]

    WP29 -->|subsidiary| GRVA
    GRVA -->|mandate| ADSI
    GRVA -->|mandate| DCAS_WG
    GRVA -->|mandate| ADASTF
    ADSI -->|sub-group| VMAD
    ADSI -->|sub-group| FRAV
    ADSI -->|sub-group| DSSAD_WG
    DSSAD_WG -->|joint with| EDRDSSAD

    ADSI -->|develops| GTR[ADS UN GTR]
    DCAS_WG -->|developed| R171[R171]
    ADASTF -->|supports| R171
```

---

## Knowledge Lifecycle State Machine

```mermaid
stateDiagram-v2
    [*] --> placeholder : note created from template
    placeholder --> draft : first substantive content added
    draft --> active : content is current and reliable
    active --> draft : new information arrives, update needed
    active --> archived : entity superseded or dissolved
    draft --> archived : note abandoned or merged
    archived --> [*]
```

---

## Entity Type Quick Reference

| Entity | Folder | Key Relationships | Status Values |
|---|---|---|---|
| `regulation` | `01 Regulations/` | defines Concept, developed by WG, implemented by OEM | placeholder → draft → active → archived |
| `working_group` | `04 Working Groups/` | creates Proposal, develops Regulation, reports to Org | placeholder → draft → active → dissolved |
| `meeting` | `02 WP29/` `03 GRVA/` `08 Meetings/` | considers Proposal, advances Regulation, hosted by Org | placeholder → draft → active → archived |
| `proposal` | `09 Proposals/` | modifies Regulation, submitted by Org, discussed at Meeting | placeholder → draft → active → adopted / rejected / deferred |
| `concept` | `05 Concepts/` | defined by Regulation, component of Concept | placeholder → draft → active → archived |
| `oem` | `06 OEM/` | implements Regulation, submits Proposal, member of Org | placeholder → draft → active → archived |
| `organization` | `07 Organizations/` | hosts Meeting, supervises WG, submits Proposal | placeholder → draft → active → archived |
| `research_note` | `10 Research Notes/` | analyzes Regulation, references Concept | draft → active → resolved → archived |
| `personal_insight` | `10 Research Notes/` | concerns Regulation, builds on Research Note | draft → active → archived |
