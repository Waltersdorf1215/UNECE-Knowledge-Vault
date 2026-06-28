# Workflows — Long-Running Standard Operating Procedures

This folder stores multi-step standard operating procedures (SOPs) for Claude Code.

## What Belongs Here

A **Workflow** is an ordered sequence of operations that span multiple tasks, prompts, and decisions. Each workflow file:

- Defines a complete end-to-end operation (import, review, evolution)
- References Tasks and Prompts from sibling folders rather than duplicating them
- References the authoritative process documents in the vault root (`IMPORT_PIPELINE.md`, `REVIEW_PIPELINE.md`)
- Specifies decision points, checkpoints, and output criteria

Workflows are **not single tasks** — those live in `Tasks/`. Workflows are **not prompt templates** — those live in `Prompts/`.

## Relationship to Vault Process Documents

The vault's root-level process documents are the authoritative definitions:
- `IMPORT_PIPELINE.md` — canonical import SOP (9 stages)
- `REVIEW_PIPELINE.md` — canonical monthly review (10 stages)

Workflow files in this folder are **executable companions** to those documents — they translate the process into specific Claude instructions, checklists, and decision trees.

## Current Workflows

| File | Purpose | Vault Reference |
|---|---|---|
| `Import Pipeline.md` | Full document import from PDF to graph update | `IMPORT_PIPELINE.md` |
| `Review Pipeline.md` | Monthly knowledge quality review | `REVIEW_PIPELINE.md` |
| `Knowledge Evolution Pipeline.md` | Multi-session regulatory development tracking | — |

## Naming Convention

`[Name] Pipeline.md`

Examples: `Import Pipeline.md`, `Review Pipeline.md`, `Session Coverage Pipeline.md`
