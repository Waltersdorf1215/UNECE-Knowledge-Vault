# AI Workflow Library — UNECE Knowledge OS

This directory is the reusable AI workflow library for Claude Code operating inside this Obsidian vault.

---

## Purpose

The UNECE Knowledge OS is maintained by Claude Code. Over time, the same types of tasks recur — importing a regulation, updating a timeline, reviewing the graph for drift. This library stores those tasks as reusable, versionable, executable units so that:

- Every operation has a documented, consistent procedure
- New Claude sessions can bootstrap quickly without re-deriving workflows
- Improvements to one workflow benefit all future runs

**This library does not replace `IMPORT_PIPELINE.md` or `REVIEW_PIPELINE.md`.** Those are the authoritative process definitions. This library provides Claude-executable instructions that reference them.

---

## Directory Structure

```
copilot/
├── README.md               ← This file — library index
├── Tasks/                  ← One-off engineering tasks
│   ├── README.md
│   ├── Import Document.md
│   ├── Create Entity.md
│   ├── Update Timeline.md
│   ├── Fix Inference Drift.md
│   └── Run Monthly Review.md
├── Prompts/                ← Reusable parametric prompt templates
│   ├── README.md
│   ├── Ingest Document.md
│   ├── Update Entity.md
│   ├── Create Regulation Note.md
│   ├── Create Concept Note.md
│   └── Classify Knowledge.md
└── Workflows/              ← Multi-step standard operating procedures
    ├── README.md
    ├── Import Pipeline.md
    ├── Review Pipeline.md
    └── Knowledge Evolution Pipeline.md
```

The `copilot-conversations/` and `copilot-custom-prompts/` directories are managed by the Obsidian Copilot plugin and are separate from this library.

---

## Folder Roles

| Folder | Contents | When to Use |
|---|---|---|
| `Tasks/` | Concrete, fully-specified one-off instructions | "Import this specific PDF" / "Fix the R155 note" / "Run the monthly review" |
| `Prompts/` | Parametric templates with `{{placeholders}}` | When you need a consistent prompt pattern but fill in specifics each time |
| `Workflows/` | Multi-step SOPs that sequence multiple tasks | Long-running operations that span multiple sessions or involve many files |

---

## Naming Conventions

### Tasks
- Verb + Object: `Import Document.md`, `Update Timeline.md`, `Fix Inference Drift.md`
- One task = one file
- Each task file is self-contained and can be copy-pasted directly into a Claude session

### Prompts
- Action + Target: `Ingest Document.md`, `Create Concept Note.md`
- Use `{{PARAMETER}}` syntax for values that change per use
- Parameters listed at the top of each prompt file

### Workflows
- `[Name] Pipeline.md` for end-to-end procedures
- Each workflow references Tasks and Prompts rather than duplicating them
- Version tracked in the YAML frontmatter

---

## Recommended Workflow Order

For a typical knowledge import session:

```
1. Read: IMPORT_PIPELINE.md          ← understand the process
2. Run: Workflows/Import Pipeline.md  ← execute the full import
3. Use: Prompts/Ingest Document.md   ← for each document
4. Use: Prompts/Classify Knowledge.md ← before merging each statement
5. Use: Tasks/Update Timeline.md     ← after import complete
6. Run: Workflows/Review Pipeline.md ← monthly or post-batch
```

For a maintenance session:

```
1. Read: REVIEW_PIPELINE.md                ← understand the review
2. Run: Workflows/Review Pipeline.md       ← execute the review
3. Use: Tasks/Fix Inference Drift.md       ← act on Inference Drift Report
4. Use: Tasks/Run Monthly Review.md        ← generate the review summary
```

---

## How Claude Should Use This Library

1. **At session start:** Check if a Task or Workflow exists for the intended operation before deriving a new procedure from scratch.
2. **Before importing a document:** Load `Workflows/Import Pipeline.md` and follow it step by step.
3. **When creating a new entity:** Use the relevant Prompt template from `Prompts/`.
4. **When classifying a statement:** Use `Prompts/Classify Knowledge.md` before writing anything into the graph.
5. **After any batch operation:** Update `CHANGELOG.md` and check `ROADMAP.md`.
6. **Monthly:** Run `Workflows/Review Pipeline.md`.

---

## Adding New Workflows

When a new recurring task pattern is identified:
1. Determine the type: Task (one-off), Prompt (parametric), or Workflow (multi-step)
2. Create the file in the appropriate folder
3. Add it to this index
4. Note it in `CHANGELOG.md` as a vault improvement
