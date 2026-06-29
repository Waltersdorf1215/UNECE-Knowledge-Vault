# Architecture

## System View

UNECE Knowledge OS is a governed regulatory knowledge repository. Its architecture separates rules, canonical knowledge, automation, project bootstrap context, and presentation views.

```text
Repository
  |
  v
Governance
  |
  v
Ontology
  |
  v
Canonical Knowledge
  |
  v
Knowledge Views
  |
  v
Skills
  |
  v
Obsidian / Claude Code / Future Agents
```

## Repository Layers

The authoritative layer model is defined in `Governance/KNOWLEDGE_ONTOLOGY.md`.

| Layer | Examples | Role |
| --- | --- | --- |
| Knowledge Layer | `01 Regulations/`, `05 Concepts/`, `07 Organizations/`, `08 Meetings/` | Stores canonical domain knowledge and evidence-bearing artifacts. |
| Governance Layer | `Governance/` | Defines rules, ontology, quality policy, and workflow boundaries. |
| Automation Layer | `.claude/skills/`, `Skills/`, `copilot/` | Implements operational procedures for agents. |
| Project Layer | `Project/`, `README.md`, release files | Provides repository management and bootstrap context. |
| Knowledge Views Layer | `15 Views/` | Provides generated or maintained navigation and query views. |

## Information Flow

```text
User question or source material
  |
  v
Vault search
  |
  +--> Sufficient canonical knowledge --> Answer from Vault
  |
  +--> Missing knowledge --> Acquire Knowledge
                              |
                              v
                         Knowledge Merge
                              |
                              v
                         Knowledge Review
                              |
                              v
                         Updated Vault
```

Meeting-specific flow:

```text
Invitation / agenda / minutes / follow-up
  |
  v
Meeting Intake
  |
  v
08 Meetings/<Organizer>/<Working Group>/<YYYY-MM>/<Meeting>/
  |
  +--> Review meeting artifact completeness
  |
  +--> Knowledge Merge only if canonical updates are approved
```

## Skill Interactions

| Skill | Input | Output | Boundary |
| --- | --- | --- | --- |
| Acquire Knowledge | Missing canonical knowledge need | Evidence-backed draft knowledge | Does not review quality as final authority. |
| Knowledge Merge | Acquired or approved evidence | Updated canonical notes | Does not invent facts. |
| Knowledge Review | Existing Vault content | Review reports, dashboard, backlog | Does not research or modify knowledge notes by default. |
| Knowledge Evolution | Governance/schema drift | Migration plans and approved structural updates | Does not acquire new facts. |
| Meeting Intake | Meeting-related source material | Meeting lifecycle folders and artifacts | Does not update canonical notes automatically. |

## Canonical Knowledge Rule

Canonical facts live once, in the proper canonical entity note. Other artifacts may summarize, link, or propose updates, but they must not become competing sources of truth.

Knowledge Views, review reports, meeting artifacts, and project documents are allowed to point at canonical knowledge. They should not duplicate regulatory content unless the duplication is clearly marked as a source excerpt, summary, or review finding.

## Why Duplication Is Avoided

Duplication creates conflicting facts, stale summaries, and unclear evidence trails. The Knowledge OS prioritizes durable retrieval and maintenance over convenience copies. When a user asks a cross-entity question, the answer should be generated from canonical notes or a Knowledge View that links back to canonical notes.
