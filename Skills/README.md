# Skills Library — UNECE Knowledge OS

Executable skills are standalone programs or scripts that perform a single, well-defined data acquisition or processing task. Skills are not part of the knowledge graph. They produce intermediate data (JSON, CSV) that the Import Pipeline consumes.

---

## Skill Categories

| Category | Purpose |
|---|---|
| `Acquire/` | Crawl, fetch, and index external data sources. No knowledge generation. |
| `Transform/` | Convert intermediate data into Import-Pipeline-ready format. *(reserved)* |
| `Validate/` | Check vault consistency, link integrity, or source freshness. *(reserved)* |

---

## Skill Index

| Skill | Category | Status | Description |
|---|---|---|---|
| `UNECE_Space_Seeder` | Acquire | v1.0.0 | Crawl a UNECE Confluence space, build full page hierarchy, collect metadata and attachments, output `seed.json` |

---

## How Skills Relate to the Import Pipeline

```
External Source
      ↓
[Skill: Acquire/*]          ← discovers, indexes, exports JSON only
      ↓
seed.json / manifest files  ← intermediate representation
      ↓
12 Attachments/Inbox/       ← stage for human review
      ↓
[IMPORT_PIPELINE.md]        ← Phase 1 classification → Phase 2 extraction
      ↓
Knowledge Graph
```

Skills never write to the vault. They only produce structured data for downstream processing.

---

## Running a Skill

Each skill is self-contained. See the skill's own `.md` file for usage.

```bash
cd Skills/Acquire/
python3 unece_space_seeder.py --url "..." --output output/seed.json
```

---

## Skill Design Constraints

All skills must obey these constraints:

1. **No knowledge generation** — skills never produce Markdown notes, summaries, or interpretations
2. **No vault writes** — skills write only to their `output/` directory
3. **No relationship inference** — skills collect structural metadata, never assert regulatory meaning
4. **Idempotent** — running a skill twice on the same input produces the same output
5. **Self-documenting** — each skill has a corresponding `.md` specification file
