# Development Workflow

This document describes repeatable engineering workflows for maintaining UNECE Knowledge OS.

## Adding a Regulation

1. Search the Vault for the regulation number, aliases, and related concepts.
2. If missing, use Acquire Knowledge with official evidence.
3. Create or update the canonical note under `01 Regulations/`.
4. Record evidence, source documents, relationships, and timeline facts.
5. Use Knowledge Merge for integration.
6. Run Knowledge Review on the regulation note.
7. Update backlog if gaps remain.
8. Commit the change with a focused message.

## Receiving a Meeting Invitation

1. Use Meeting Intake.
2. Classify source as `invitation`.
3. Create or update the meeting folder:

```text
08 Meetings/<Organizer>/<Working Group or General>/<YYYY-MM>/<YYYY-MM-DD Meeting Title>/
```

4. Create `pre-meeting-record.md`.
5. Create or update `source-materials.md`.
6. Do not create minutes, decisions, or action items unless explicitly present.
7. Mark private links and attendee details as sensitive.
8. Do not update canonical notes.

## Importing Meeting Minutes

1. Use Meeting Intake.
2. Match the minutes to an existing meeting folder.
3. If match confidence is medium or low, ask before merging.
4. Create or update `minutes.md`.
5. Extract discussion, decisions, action items, follow-up, regulatory impact, and open questions.
6. Create `decisions.md` or `action-items.md` only if explicit source text supports them.
7. Identify canonical update candidates.
8. Invoke Knowledge Merge only if the user approves canonical updates.

## Running Knowledge Review

1. Determine scope: note, folder, domain, or entire Vault.
2. Read relevant Governance and skill instructions.
3. Review completeness, evidence, relationships, timelines, duplicates, and verification status.
4. Do not research.
5. Do not modify canonical notes unless separately instructed.
6. Generate or update review artifacts in `11 Review/`.
7. Update dashboard and backlog when requested.

## Running Knowledge Evolution

1. Read current Governance, especially `Governance/KNOWLEDGE_ONTOLOGY.md`.
2. Inspect target notes or folders.
3. Detect structural drift only.
4. Generate a migration plan before modifying files.
5. Apply migration only after approval.
6. Preserve meaning and manually authored content.
7. Generate an evolution report after migration.

## Committing Changes

1. Run `git status`.
2. Review modified and untracked files.
3. Exclude secrets, cache files, private local state, and unintended binaries.
4. Stage intended files only.
5. Review staged files.
6. Commit with a focused message.
7. Push only when requested or when the workflow requires it.

## Creating a Release

1. Confirm the Vault is clean or intentionally staged.
2. Run relevant acceptance checks or reviews.
3. Update project state or session summary if needed.
4. Commit all release-relevant changes.
5. Create an annotated tag using a stable release name.
6. Push commits and tags after confirming remote status.
7. Record release notes or milestone summary.
