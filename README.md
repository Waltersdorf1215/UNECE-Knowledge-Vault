# UNECE Knowledge OS

> An evidence-driven Knowledge Operating System for UNECE automated driving regulations.

![Status](https://img.shields.io/badge/status-foundation%20ready-2ea44f)
![Vault](https://img.shields.io/badge/vault-Obsidian-7c3aed)
![Automation](https://img.shields.io/badge/automation-Claude%20Code-111827)
![Knowledge](https://img.shields.io/badge/principle-evidence%20first-2563eb)

## Overview

**UNECE Knowledge OS** is a structured knowledge management system built on Obsidian and Claude Code for researching, organizing, validating, and continuously evolving knowledge related to UNECE automated driving regulations.

Unlike a traditional note collection, this project treats regulatory knowledge as a living system:

> Every new question should make the knowledge base permanently better.

The Vault is the primary source of truth. AI assists with acquisition, merge, review, and evolution, but it does not replace evidence.

## Vision

The goal is to build a continuously evolving regulatory knowledge graph covering:

- 📘 UNECE Regulations
- 🏛️ WP.29
- 🚗 GRVA
- 👥 Working Groups
- 🏢 Organizations
- 🧠 Technical Concepts
- 🗂️ Meeting Documents
- 📝 Regulatory Proposals
- 🕒 Timeline Evolution

## Core Principles

| Principle | Meaning |
| --- | --- |
| 🔎 Evidence First | Prefer official sources and traceable evidence. |
| 🗄️ Vault First | Answer from the Vault whenever knowledge already exists. |
| ⚠️ Unknown Is Better Than Incorrect | Mark uncertainty instead of inventing facts. |
| 🧩 Incremental Accumulation | Each task should improve reusable knowledge. |
| 👤 Human-Reviewable Updates | Changes must remain inspectable and reversible. |
| 📈 Continuous Quality Improvement | Review and backlog drive long-term reliability. |

## Architecture

```text
User Question
      |
      v
Search Existing Vault
      |
      +--------------------------+
      |                          |
      v                          v
Knowledge Exists          Missing / Incomplete
      |                          |
      v                          v
Answer User              Acquire Knowledge
                                 |
                                 v
                          Deep Research
                                 |
                                 v
                          Knowledge Merge
                                 |
                                 v
                          Knowledge Review
                                 |
                                 v
                       Updated Knowledge Vault
```

## Repository Structure

```text
UNECE/
├── 00 Home/
├── 01 Regulations/
├── 02 WP29/
├── 03 GRVA/
├── 04 Working Groups/
├── 05 Concepts/
├── 06 OEM/
├── 07 Organizations/
├── 08 Meetings/
├── 09 Proposals/
├── 10 Research Notes/
├── 11 Review/
├── 12 Attachments/
├── 13 Resources/
├── 14 Timeline/
├── Governance/
├── .claude/
│   └── skills/
├── raw/
└── README.md
```

## Claude Skills

| Skill | Purpose | Output |
| --- | --- | --- |
| 🔍 Acquire Knowledge | Search the Vault, detect missing knowledge, and acquire only what is needed. | New or updated knowledge notes. |
| 🔀 Knowledge Merge | Integrate acquired knowledge while preserving manually curated content. | Clean merged knowledge. |
| ✅ Knowledge Review | Evaluate completeness, evidence, relationships, timelines, and gaps. | Review reports, dashboard, backlog. |
| 🧭 Knowledge Evolution | Modernize existing knowledge to match the current Governance layer. | Migration plans and approved structural updates. |

## Knowledge Lifecycle

```text
Question
   ↓
Vault Search
   ↓
Acquire
   ↓
Merge
   ↓
Review
   ↓
Verified Knowledge
   ↓
Future Questions Answered Directly from Vault
```

## Knowledge Model

The Vault organizes knowledge into canonical entity types:

- Regulation
- Concept
- Organization
- Working Group
- Meeting
- Proposal
- Timeline Event
- Evidence

Relationships between these entities form an evolving knowledge graph. Knowledge Views may provide user-oriented navigation and summaries, but canonical facts belong in canonical entity notes.

## Evidence Policy

Knowledge is sourced according to the following priority:

1. UNECE Regulations
2. UNECE Official Documents
3. UNECE Wiki
4. Official Organization Websites
5. Official Meeting Reports
6. Academic Publications
7. Industry Publications
8. LLM Prior Knowledge, used only as a last resort and never as official evidence

## Current Status

**Milestone:** `UNECE-Knowledge-OS-Foundation`

Current capabilities:

- ✅ Structured Vault architecture
- ✅ Governance-based ontology
- ✅ Evidence-based knowledge acquisition
- ✅ Knowledge merge workflow
- ✅ Knowledge quality review
- ✅ Knowledge evolution planning
- ✅ Acceptance testing
- ✅ Git version control

## Roadmap

Upcoming priorities:

- Complete UNECE regulation coverage
- Build Working Group knowledge graph
- Expand organization profiles
- Develop meeting archive
- Track proposal evolution
- Build timeline views
- Improve knowledge analytics

## Versioning

Current foundation tag:

```text
UNECE-Knowledge-OS-Foundation
```

## License

Private research repository.

## Acknowledgements

This project is inspired by:

- Andrej Karpathy's LLM Wiki concept
- Obsidian knowledge management
- Claude Code workflow automation
