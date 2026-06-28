# Acquire Knowledge — Skill README

## What This Skill Does

`acquire_knowledge` is the **front door to the UNECE Knowledge OS**. Use it whenever you want to learn about a UNECE-related topic, understand a regulation, or expand what the vault knows.

It does three things in sequence:
1. **Checks the vault first** — if the answer exists and is complete, it uses it directly
2. **Researches the web** — only when the vault is incomplete or missing, using `deep-research`
3. **Writes the answer back to the vault** — so future questions are answered faster

---

## When to Use It

**Use this skill for questions like:**
- "What is [regulation / working group / concept]?"
- "Explain [topic] in the UNECE context"
- "What happened at [session]?"
- "What is the status of [regulation]?"
- "Who is responsible for [topic]?"

**Do not use this skill for:**
- Importing a specific PDF document → use `IMPORT_PIPELINE.md`
- Batch-merging analyzed evidence → use `knowledge-merge` skill
- Crawling the UNECE wiki for document links → use `UNECE_Space_Seeder`
- Pure web browsing without a UNECE question → use `deep-research` directly

---

## How It Differs from Deep Research

| | `acquire_knowledge` | `deep-research` |
|---|---|---|
| **Purpose** | Orchestrates the full acquisition pipeline | Performs web search and synthesis only |
| **Vault interaction** | Reads and writes the vault | Does not touch the vault |
| **When it calls deep-research** | Only when vault is incomplete | Always |
| **Output** | Updated vault notes + answer | Research report only |
| **Primary source** | Vault, then web | Web |

`deep-research` is a tool inside `acquire_knowledge`. The acquisition skill decides when to use it.

---

## Research Priority Order

When multiple sources are available, always prefer:

1. Official UNECE regulations (ECE/TRANS/…)
2. UNECE wiki (wiki.unece.org)
3. Official organization websites (OICA, CLEPA, ISO, SAE)
4. Official meeting reports
5. Official working documents (INF / WP series)
6. Published standards (ISO, SAE, IEEE)
7. Academic papers
8. Industry publications
9. LLM prior knowledge ← last resort only; must be labeled `[UNVERIFIED]`

---

## The Vault Is Always Primary

The Vault is the long-term memory of this Knowledge OS. Every acquisition is designed to make the Vault permanently more complete. The goal is that every question is asked once — and then answered from the Vault forever after.

---

## Skill Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow specification (10 steps) |
| `README.md` | This file — quick reference |
| `examples.md` | 10+ worked example questions |
| `templates/entity.md` | Generic entity template |
| `templates/regulation.md` | Regulation note template |
| `templates/concept.md` | Concept note template |
| `templates/meeting.md` | Meeting / session note template |
| `templates/working_group.md` | Working group / IWG / TF note template |
