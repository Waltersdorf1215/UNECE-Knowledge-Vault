UNECE Knowledge OS

An evidence-driven Knowledge Operating System for UNECE automated driving regulations.

⸻

Overview

UNECE Knowledge OS is a structured knowledge management system built on Obsidian and Claude Code for researching, organizing, validating and continuously evolving knowledge related to UNECE automated driving regulations.

Unlike a traditional note collection, this project treats regulatory knowledge as a living system.

Every new question should make the knowledge base permanently better.

⸻

Vision

The goal is to build a continuously evolving regulatory knowledge graph covering:

* UNECE Regulations
* WP.29
* GRVA
* Working Groups
* Organizations
* Technical Concepts
* Meeting Documents
* Regulatory Proposals
* Timeline Evolution

The Vault serves as the primary source of truth.

AI assists in acquiring, validating and maintaining knowledge rather than replacing it.

⸻

Core Principles

* Evidence First
* Vault First
* Unknown is better than incorrect
* Incremental knowledge accumulation
* Human-reviewable updates
* Continuous quality improvement

⸻

Architecture

                User Question
                       │
                       ▼
              Search Existing Vault
                       │
         ┌─────────────┴─────────────┐
         │                           │
      Knowledge Exists        Missing / Incomplete
         │                           │
         ▼                           ▼
     Answer User            Acquire Knowledge
                                     │
                                     ▼
                              Deep Research
                                     │
                                     ▼
                              Knowledge Merge
                                     │
                                     ▼
                             Knowledge Review
                                     │
                                     ▼
                            Updated Knowledge Vault

⸻

Repository Structure

00 Home/
01 Regulations/
02 WP29/
03 GRVA/
04 Working Groups/
05 Concepts/
06 OEM/
07 Organizations/
08 Meetings/
09 Proposals/
10 Research Notes/
11 Review/
12 Attachments/
13 Resources/
14 Timeline/
.claude/
    skills/
raw/
README.md

⸻

Claude Skills

Current workflow is powered by three core Claude Code Skills.

Acquire Knowledge

Responsible for:

* Searching the Vault
* Detecting missing knowledge
* Invoking Deep Research when necessary
* Creating or updating Markdown notes

⸻

Knowledge Merge

Responsible for:

* Integrating newly acquired knowledge
* Preserving manually curated content
* Updating relationships
* Maintaining consistency

⸻

Knowledge Review

Responsible for:

* Reviewing knowledge quality
* Detecting missing sections
* Evaluating evidence coverage
* Producing review reports
* Maintaining dashboard and backlog

⸻

Knowledge Lifecycle

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

⸻

Knowledge Model

The Vault currently organizes knowledge into several major entity types.

* Regulation
* Concept
* Organization
* Working Group
* Meeting
* Proposal
* Timeline Event
* Evidence

Relationships between these entities form an evolving knowledge graph.

⸻

Evidence Policy

Knowledge is always sourced according to the following priority:

1. UNECE Regulations
2. UNECE Official Documents
3. UNECE Wiki
4. Official Organization Websites
5. Official Meeting Reports
6. Academic Publications
7. Industry Publications
8. LLM Prior Knowledge (last resort only)

⸻

Current Status

Current milestone:

UNECE Knowledge OS Foundation

Current capabilities:

* Structured Vault architecture
* Evidence-based knowledge acquisition
* Automated knowledge merge
* Knowledge quality review
* Acceptance testing
* Git version control

⸻

Roadmap

Upcoming priorities include:

* Complete UNECE regulation coverage
* Working Group knowledge graph
* Organization profiles
* Meeting archive
* Proposal evolution tracking
* Timeline engine
* Knowledge analytics

⸻

Versioning

Current Tag:

UNECE-Knowledge-OS-Foundation

⸻

License

Private research repository.

⸻

Acknowledgements

This project is inspired by:

* Andrej Karpathy’s LLM Wiki concept
* Obsidian knowledge management
* Claude Code workflow automation

while extending these ideas into an evidence-driven regulatory Knowledge Operating System.
