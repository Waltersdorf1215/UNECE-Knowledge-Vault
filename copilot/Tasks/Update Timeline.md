# Task: Update Timeline

**Type:** One-off task
**Output:** Updated milestone entry in one or more `14 Timeline/` notes

---

## Instructions for Claude

You are adding one or more new milestones to the UNECE timeline layer.

### Step 1 — Identify the Correct Timeline File

| Timeline | When to Update |
|---|---|
| `14 Timeline/ADS Timeline.md` | Any milestone in the history of ADS regulation (WP.29, GRVA, IWG decisions) |
| `14 Timeline/GRVA Timeline.md` | Any GRVA session outcome or GRVA-level decision |
| `14 Timeline/WP29 Timeline.md` | Any WP.29 session outcome or WP.29-level adoption |
| `14 Timeline/R157 Timeline.md` | Any milestone specific to UN Regulation 157 (ALKS) |
| `14 Timeline/R171 Timeline.md` | Any milestone specific to UN Regulation 171 (DCAS) |

### Step 2 — Format the New Entry

Add to the **Known Milestones** table in chronological order:

```markdown
| YYYY-MM-DD | Event description | Document reference | Source |
```

Rules:
- Date must be specific (year-month or year-month-day). Do not use "TBD" for past events.
- Event must be stated as an **Official Fact** — only add confirmed milestones
- Document reference: use official document number if known (e.g., `ECE/TRANS/WP.29/2026/139`)
- Source: cite where you found this (document number or section)

For future/unconfirmed milestones, add to the **Pending Milestones** table with `[VERIFY]`.

### Step 3 — Epistemic Check

Before adding any entry:
- Is this milestone explicitly stated in a named source? → Add to Known Milestones with citation
- Is this milestone inferred or expected? → Add to Pending Milestones with `[VERIFY]`
- Is this my own prediction? → Do not add to timelines; write in a Research Note instead

### Step 4 — Update last_updated

Set `last_updated` in the YAML frontmatter to today's date.

---

## Definition of Done

- [ ] Milestone added to the correct timeline file
- [ ] Entry includes date, description, document reference, and source
- [ ] Fact/pending distinction correct
- [ ] `last_updated` field updated
