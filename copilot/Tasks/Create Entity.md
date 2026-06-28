# Task: Create Entity

**Type:** One-off task
**Output:** One new note in the appropriate vault folder

---

## Instructions for Claude

You are creating a new entity note in the UNECE Knowledge OS.

Before creating anything:
1. Search the vault to confirm no note already exists for this entity
2. If a note exists under a different name, update it and add an alias — do not create a duplicate
3. Read the appropriate template from `11 Templates/`

### Step 1 — Identify Entity Type and Folder

| Entity Type | Folder | Template |
|---|---|---|
| Regulation | `01 Regulations/` | `Regulation Template.md` |
| Working Group | `04 Working Groups/` | `Working Group Template.md` |
| Meeting | `02 WP29/`, `03 GRVA/`, or `08 Meetings/` | `Meeting Template.md` |
| Proposal | `09 Proposals/` | `Proposal Template.md` |
| Concept | `05 Concepts/` | `Technical Concept Template.md` |
| OEM | `06 OEM/` | `OEM Template.md` |
| Organization | `07 Organizations/` | `Organization Template.md` |
| Research Note | `10 Research Notes/` | `Research Note Template.md` |

### Step 2 — Fill YAML Frontmatter

Required fields:
```yaml
type:
status: placeholder
tags: []
related: []
source: ""
last_updated: YYYY-MM-DD
created: YYYY-MM-DD
knowledge_type: official_fact | structural_relationship | interpretation | personal_insight
evidence_level: official | derived | personal
```

### Step 3 — Write Content

- Only include content that can be classified (Official Fact / Structural Relationship / Interpretation)
- Label interpretations `*Interpretation:*`
- Leave unknown fields as `source_pending` or `[VERIFY]`
- Add at least three wiki links to related notes

### Step 4 — Link Back

Add a link to the new note from at least one existing related note. Orphan notes are not permitted.

### Step 5 — Report

State: note created, folder, wiki links added, any backlinks updated.

---

## Definition of Done

- [ ] No duplicate exists in the vault
- [ ] Correct folder and template used
- [ ] YAML complete with all required fields
- [ ] Minimum three outgoing wiki links
- [ ] At least one existing note links back to the new note
- [ ] All content classified and labeled appropriately
