# Agent Guide

This is the first document every AI agent should read before working in the UNECE Knowledge OS repository.

## Mission

UNECE Knowledge OS is an evidence-driven regulatory Knowledge Operating System for UNECE automated driving regulation.

The repository is designed for long-term knowledge accumulation, not ordinary note taking. Each useful answer, meeting record, review, or acquisition should make the Vault more reliable, reusable, and maintainable.

## Core Principles

- Canonical Knowledge is the single source of truth.
- Knowledge Views are presentation and query layers only.
- Evidence First.
- Unknown is better than incorrect.
- Never invent regulatory facts.
- Never duplicate canonical knowledge.
- Governance overrides implementation.
- Repository structure is intentional.
- Every change should improve long-term maintainability.

## Repository Philosophy

The repository follows the layer model defined in `Governance/KNOWLEDGE_ONTOLOGY.md`.

| Layer | Responsibility |
| --- | --- |
| Knowledge Layer | Canonical domain knowledge, evidence-bearing notes, meetings, attachments, timelines, and regulatory entities. |
| Governance Layer | Rules, ontology, quality policy, workflow boundaries, and architectural contracts. |
| Automation Layer | Claude Code skills, prompts, scripts, and agent implementation artifacts. |
| Project Layer | Repository management and permanent bootstrap context for agents. |
| Knowledge Views Layer | Generated or maintained exploration surfaces over canonical knowledge. |

Only the Knowledge Layer is scored as canonical ontology-compliant knowledge by default.

## Skills

| Skill | Use when |
| --- | --- |
| Acquire Knowledge | Missing canonical knowledge must be acquired from evidence. |
| Knowledge Merge | Newly acquired or meeting-derived evidence should be integrated into canonical notes. |
| Knowledge Review | Existing Vault content must be checked for completeness, evidence, relationships, timelines, and gaps. |
| Knowledge Evolution | Existing knowledge structure must be modernized to match Governance. |
| Meeting Intake | Meeting invitations, agendas, minutes, follow-ups, and actions must be organized into meeting lifecycle folders. |

Skills are operational procedures. They must obey Governance and must not invent facts or entity types.

## Working Style

Every substantive task should follow this pattern:

```text
Understand
  |
  v
Review existing knowledge
  |
  v
Acquire if needed
  |
  v
Merge
  |
  v
Review
  |
  v
Commit
```

Skip steps only when the user explicitly limits scope, such as "do not research" or "do not modify the Vault."

## What an AI Should Never Do

- Never guess regulations.
- Never invent dates, meeting outcomes, participants, decisions, or evidence.
- Never overwrite manually curated content.
- Never duplicate canonical entities.
- Never bypass Governance.
- Never modify ontology without explicit approval.
- Never treat Automation or Project files as canonical knowledge.
- Never merge meeting-derived claims into canonical notes without evidence and approval.
- Never expose private meeting links, passcodes, or personal attendee information in public summaries.

## Startup Procedure

At the beginning of a new AI session:

1. Read `Project/`.
2. Read `Governance/`.
3. Read `README.md`.
4. Check `git status`.
5. Summarize the current project state before taking action.

If the user request names a Skill, read that Skill's `SKILL.md` before acting.
