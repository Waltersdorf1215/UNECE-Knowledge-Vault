# Prompt: Create Regulation Note

**Parameters to fill before use:**
- `{{REGULATION_NUMBER}}` — e.g., 157, 171, or "ADS UN GTR"
- `{{REGULATION_TITLE}}` — official full title
- `{{REGULATION_SERIES}}` — "UN Regulation" or "UN GTR"
- `{{DOCUMENT_NUMBER}}` — official adoption document, e.g., ECE/TRANS/WP.29/2021/40
- `{{RESPONSIBLE_BODY}}` — e.g., GRVA
- `{{STATUS}}` — placeholder | draft | active

---

## Prompt Text

```
You are maintaining the UNECE Knowledge OS Obsidian vault.

Before starting, read CLAUDE.md and KNOWLEDGE_RULES.md (Rule Zero).

Task: Create a new regulation note for:
- Regulation: {{REGULATION_NUMBER}} — {{REGULATION_TITLE}}
- Series: {{REGULATION_SERIES}}
- Adoption document: {{DOCUMENT_NUMBER}}
- Responsible body: {{RESPONSIBLE_BODY}}

Steps:
1. Check the vault: confirm no note already exists for this regulation.
   If it does, update the existing note instead of creating a new one.
2. Use the template at 11 Templates/Regulation Template.md.
3. Fill in the YAML frontmatter:
   - type: regulation
   - status: {{STATUS}}
   - source: "{{DOCUMENT_NUMBER}}"
   - regulation_number, regulation_series, responsible_body
   - knowledge_type: official_fact
   - evidence_level: official
4. Add a Summary section — one or two sentences, sourced.
5. Add a Scope section — only content explicitly stated in the regulation or its document.
   Label anything inferred as *Interpretation:*
6. Add Key Links section — link to at minimum:
   - The responsible working group
   - Two related concepts (e.g., ODD, DDT, MRC)
   - One related regulation
7. Add an Open Questions section with at least two [VERIFY] items.
8. After creating the note, link to it from at least one existing related note.

Report: file created, wiki links added, backlinks updated.
```
