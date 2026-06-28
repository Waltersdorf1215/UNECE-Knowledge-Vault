---
type: meta
status: active
tags: [archive]
last_updated: 2026-06-27
created: 2026-06-27
---

# Archive

This folder stores deprecated notes, superseded drafts, and historical versions that are no longer part of the active knowledge graph.

## Rules

- Notes are moved here when they are **superseded** by a more authoritative note or a merger
- Notes are moved here when the entity they describe is **dissolved, superseded, or no longer relevant**
- Notes are **never deleted** — the archive preserves history
- Archived notes should have `status: archived` in their YAML frontmatter
- Add a comment at the top of the note explaining why it was archived and what replaced it

## How to Archive

1. Update the note's YAML: `status: archived`
2. Add a comment block at the top: `> Archived YYYY-MM-DD. Superseded by [[replacement note]].`
3. Move the file here
4. Remove outgoing wiki links from the archived note (to prevent graph pollution)
5. Update the canonical note to note the archive in its **History** section if relevant

## Current Contents

*Empty — no notes archived yet.*
