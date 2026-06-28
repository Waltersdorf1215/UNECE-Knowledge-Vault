# Prompts — Reusable Parametric Prompt Templates

This folder stores reusable prompt templates for Claude Code.

## What Belongs Here

A **Prompt** is a parametric template with `{{PLACEHOLDERS}}` for values that change per use. Each prompt file:

- Contains a complete, copy-paste-ready instruction block
- Uses `{{PARAMETER}}` syntax to mark fields to fill in before use
- Lists all required parameters at the top
- Is designed to be used repeatedly across different documents or entities

Prompts are **not single-use tasks** — those live in `Tasks/`. Prompts are **not multi-step SOPs** — those live in `Workflows/`.

## Current Prompts

| File | Purpose |
|---|---|
| `Ingest Document.md` | Template for importing any new document into the knowledge graph |
| `Update Entity.md` | Template for updating an existing note with new information |
| `Create Regulation Note.md` | Template for creating a new regulation note |
| `Create Concept Note.md` | Template for creating a new concept note |
| `Classify Knowledge.md` | Template for classifying a statement before merging it |

## How to Use a Prompt

1. Open the prompt file
2. Replace all `{{PARAMETER}}` occurrences with actual values
3. Copy the complete text
4. Paste into a new Claude Code session or message

## Naming Convention

`Action + Target.md`

Examples: `Ingest Document.md`, `Create Concept Note.md`, `Update Timeline Entry.md`
