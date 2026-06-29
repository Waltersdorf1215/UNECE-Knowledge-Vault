---
name: meeting_intake
description: Process meeting invitations, agendas, notes, summaries, minutes, presentations, and follow-ups into structured UNECE Knowledge OS meeting folders with source materials, knowledge gap analysis, and merge suggestions; use for Outlook invites, agenda intake, meeting summaries, official minutes, and meeting-derived acquisition or merge recommendations.
---

# Skill: Meeting Intake

**Version:** 1.2.0
**Category:** Meeting Lifecycle + Knowledge Suggestions
**Governance:** `Governance/MEETING_KNOWLEDGE_MODEL.md`, `Governance/KNOWLEDGE_EXTRACTION_SPEC.md`, `Governance/KNOWLEDGE_ONTOLOGY.md`
**Coordinates with:** `acquire_knowledge`, `knowledge-merge`, `knowledge_review`, `knowledge_evolution`

---

## Purpose

`meeting_intake` turns meeting material into a structured meeting folder and practical next-step knowledge suggestions.

Core flow:

```text
Meeting material
  |
  v
Meeting folder
  |
  v
Meeting records
  |
  v
knowledge-gap-analysis.md
  |
  v
merge-suggestions.md
```

Meeting Intake remains the single Skill for processing invitations, agendas, meeting notes, meeting summaries, minutes, presentations, and follow-up material.

It does **not** update canonical knowledge notes automatically.

---

## When to Invoke This Skill

Use this skill when the user provides or references:

- Outlook meeting invitations
- Meeting invitations
- Agenda emails
- Meeting decks or presentations
- Attached PDFs
- User meeting notes
- Meeting summaries
- Official minutes
- Follow-up emails
- Working group or task force meeting material

Example prompts:

- "把这个会议放进 vault"
- "帮我整理这个 EME meeting"
- "为这个 GRVA 会议建一个 meeting folder"
- "根据这个 agenda 生成会前背景"
- "根据会议纪要生成 merge suggestions"
- "从这个 meeting summary 找出 Vault 还缺什么"

---

## When NOT to Use This Skill

Do **not** use this skill for:

- General regulatory research without a meeting context
- Creating regulation notes directly
- Updating ontology or governance
- Bulk importing official regulation PDFs
- Speculative meeting summaries without source material
- Applying merge suggestions to canonical notes

Use:

- `acquire_knowledge` for missing canonical entities
- `knowledge-merge` for approved canonical updates
- `knowledge_review` for quality review
- `knowledge_evolution` for approved schema migration

---

## Operating Rules

1. The Vault remains the source of truth.
2. Meeting folders are lifecycle containers.
3. Meeting artifacts should link to canonical entities, not duplicate them.
4. Search the Vault before declaring knowledge missing.
5. Do not list an entity as missing if a canonical note already exists.
6. If an entity exists but lacks context, list it under incomplete existing notes.
7. Never update canonical notes automatically.
8. Missing entities route to Acquire Knowledge recommendations.
9. Existing entity updates route to Knowledge Merge suggestions.
10. Preserve uncertainty with `unknown`, `Needs Review`, or low confidence.
11. Invitations do not generate fake minutes, decisions, or action items.
12. Agenda items are not decisions.
13. Meeting summaries do not overwrite canonical knowledge.
14. Private or sensitive meeting content must be handled conservatively.

---

## Required Folder Structure

All meeting records use:

```text
08 Meetings/
└── <Organizer>/
    └── <Working Group or General>/
        └── <YYYY-MM>/
            └── <YYYY-MM-DD Meeting Title>/
                ├── pre-meeting-record.md
                ├── agenda.md
                ├── meeting-notes.md
                ├── minutes.md
                ├── source-materials.md
                ├── knowledge-gap-analysis.md
                └── merge-suggestions.md
```

Do not add extra files such as `knowledge-extraction.md`, `timeline-events.md`, `review-report.md`, `decisions.md`, or `action-items.md` unless explicitly requested.

Create only files supported by the input type, except `source-materials.md`, `knowledge-gap-analysis.md`, and `merge-suggestions.md`, which should be updated whenever meeting material is processed.

---

## Folder Naming Rules

### Organizer

Use the meeting organizer as the first folder level.

Examples:

- `08 Meetings/EME/`
- `08 Meetings/UNECE/`
- `08 Meetings/OICA/`
- `08 Meetings/CLEPA/`
- `08 Meetings/Euro NCAP/`
- `08 Meetings/NIO/`

If unclear, use:

```text
08 Meetings/Unknown Organizer/
```

Do not guess the organizer.

### Working Group

Use the relevant working group, task force, or internal group when available.

Examples:

- `08 Meetings/EME/WG SDV-AVS-AI/`
- `08 Meetings/UNECE/GRVA/`
- `08 Meetings/UNECE/WP29/`
- `08 Meetings/UNECE/ADAS TF/`
- `08 Meetings/UNECE/VMAD/`

If no identifiable working group exists, use:

```text
General/
```

Do not invent a working group from the topic.

### Meeting Month

Use the scheduled meeting date:

```text
YYYY-MM
```

If unknown, use:

```text
Unknown Date/
```

### Meeting Folder

Use:

```text
YYYY-MM-DD Meeting Title
```

If exact day is unknown:

```text
YYYY-MM Unknown Day Meeting Title
```

---

## Source Classification

Classify input before updating files.

Allowed source types:

- `invitation`
- `agenda`
- `meeting_note`
- `minutes`
- `presentation`
- `follow_up_email`
- `attachment`
- `unknown`

If source type is uncertain, use `unknown` and mark outputs as `Needs Review`.

---

## Artifact Routing

### Invitation

Create or update only:

```text
pre-meeting-record.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Do not create `minutes.md` or `meeting-notes.md` unless explicitly provided. Do not invent decisions, action items, or minutes.

### Agenda

Create or update:

```text
agenda.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Agenda items are not decisions.

### Meeting Note or User Summary

Create or update:

```text
meeting-notes.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

If the summary contains clear decisions or actions, capture them inside `meeting-notes.md`. Do not create canonical updates automatically.

### Official Minutes

Create or update:

```text
minutes.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Extract discussion, decisions, and actions into `minutes.md`. Do not update canonical notes unless the user explicitly invokes Knowledge Merge.

### Presentation, Attachment, or Follow-Up Email

Create or update:

```text
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Also update `agenda.md`, `meeting-notes.md`, or `minutes.md` only if the source clearly functions as that artifact type.

---

## Knowledge Gap Analysis

`knowledge-gap-analysis.md` answers:

> What does this meeting reveal that the Vault does not yet know?

Required sections:

- `# Knowledge Gap Analysis`
- `## Summary`
- `## Missing Organizations`
- `## Missing Working Groups`
- `## Missing Regulations`
- `## Missing Concepts`
- `## Missing Initiatives / Projects`
- `## Missing Proposals or Documents`
- `## Incomplete Existing Notes`
- `## Recommended Acquire Actions`
- `## Priority`
- `## Evidence`

Rules:

- Search the Vault before listing an item as missing.
- Do not list an entity as missing if a canonical note already exists.
- If the entity exists but lacks important context, list it under `Incomplete Existing Notes`.
- Do not create missing canonical notes automatically.
- Recommend Acquire Knowledge for missing or incomplete items.
- Preserve uncertainty.

Priority levels:

- `High`
- `Medium`
- `Low`
- `Needs Review`

---

## Merge Suggestions

`merge-suggestions.md` answers:

> What existing knowledge might need to be updated because of this meeting?

Required sections:

- `# Merge Suggestions`
- `## Summary`
- `## Candidate Updates`
- `## Regulation Updates`
- `## Organization Updates`
- `## Working Group Updates`
- `## Concept Updates`
- `## Meeting / Timeline Updates`
- `## Suggested Merge Actions`
- `## Items Requiring Review`
- `## Evidence`

Each suggestion must include:

- Target note
- Proposed update
- Reason
- Source evidence
- Confidence
- Risk

Confidence levels:

- `High`
- `Medium`
- `Low`
- `Needs Review`

Risk levels:

- `Low`
- `Medium`
- `High`

Rules:

- Do not apply the merge automatically.
- Do not update canonical notes.
- Only suggest possible updates.
- If confidence is low, mark as `Needs Review`.

---

## Source Materials

Update `source-materials.md` every time new meeting material is processed.

Track:

- Source type
- File name
- Original source if available
- Received date
- Privacy / sensitivity
- Reliability
- Notes

Do not expose private Teams links in public summaries.

---

## Matching Logic

When a new input arrives, match it to an existing meeting folder using:

1. Exact meeting date
2. Organizer
3. Working group
4. Meeting title similarity
5. Calendar subject
6. Source sender
7. Meeting time

If confidence is high, update the existing folder.

If confidence is medium or low, list candidate folders and ask before merging.

Never merge unrelated meeting materials.

---

## Privacy

Meeting materials may contain private information.

Rules:

- Do not expose Teams links in public summaries.
- Do not include private email addresses unless necessary.
- Mark files as `sensitive: true` when meeting material is non-public.
- Prefer summaries over raw invitation text.
- Warn before committing sensitive meeting material to GitHub.

---

## Templates

Use bundled templates:

- `templates/pre-meeting-record.md`
- `templates/agenda.md`
- `templates/meeting-notes.md`
- `templates/minutes.md`
- `templates/source-materials.md`
- `templates/knowledge-gap-analysis.md`
- `templates/merge-suggestions.md`
