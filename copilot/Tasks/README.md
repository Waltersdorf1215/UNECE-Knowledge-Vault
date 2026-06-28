# Tasks — One-Off Engineering Tasks

This folder stores concrete, fully-specified task instructions for Claude Code.

## What Belongs Here

A **Task** is a single, bounded operation with a clear start and end state. Each task file:

- Has a specific goal ("import this PDF", "run the monthly review")
- Can be executed by copy-pasting the file contents into a Claude session
- References vault conventions (CLAUDE.md, IMPORT_PIPELINE.md) rather than restating them
- Produces a defined output (updated notes, a report, a changelog entry)

Tasks are **not parametric templates** — those live in `Prompts/`. Tasks are **not multi-step SOPs** — those live in `Workflows/`.

## Current Tasks

| File | Purpose |
|---|---|
| `Import Document.md` | Import a specific PDF or document into the knowledge graph |
| `Create Entity.md` | Create a new entity note from scratch |
| `Update Timeline.md` | Add a milestone to one or more timeline notes |
| `Fix Inference Drift.md` | Act on the Inference Drift Report and correct flagged notes |
| `Run Monthly Review.md` | Execute the monthly knowledge quality review |

## Naming Convention

`Verb + Object.md`

Examples: `Import Document.md`, `Update Entity.md`, `Archive Note.md`, `Merge Duplicates.md`
