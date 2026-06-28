# Prompt: Create Concept Note

**Parameters to fill before use:**
- `{{CONCEPT_NAME}}` — e.g., "Behavioural Competency", "MRC", "ISMR"
- `{{DEFINED_IN}}` — primary source document and section, e.g., "ECE/TRANS/WP.29/2026/139, §2.22"
- `{{ALIASES}}` — alternative names or abbreviations (comma-separated, or "none")

---

## Prompt Text

```
You are maintaining the UNECE Knowledge OS Obsidian vault.

Before starting, read CLAUDE.md and KNOWLEDGE_RULES.md (Rule Zero).

Task: Create a new concept note for: {{CONCEPT_NAME}}

Steps:
1. Check the vault: confirm no note already exists for this concept 
   (search by name and aliases).
   If it does, update the existing note instead.
2. Use the template at 11 Templates/Technical Concept Template.md.
3. Fill in the YAML frontmatter:
   - type: concept
   - status: draft (or active if well-sourced)
   - source: "{{DEFINED_IN}}"
   - defined_in: "{{DEFINED_IN}}"
   - aliases: [{{ALIASES}}]
   - knowledge_type: official_fact (if definition is sourced)
   - evidence_level: official
4. Definition section:
   - If the concept has an official definition in a UNECE document, quote it verbatim
     and cite: **Fact ({{DEFINED_IN}}):** "[quote]"
   - If the definition is from SAE J3016 or ISO standards, cite that standard
   - Do not paraphrase in a way that changes the meaning
5. Regulatory Usage section:
   - List which regulations or working groups use or define this concept
   - Only list confirmed relationships (sourced); label inferred ones *Interpretation:*
6. Related Concepts section:
   - Link to at least two related concepts
   - State the relationship type (extends, depends_on, precedes, etc.)
7. Open Questions section:
   - Add at least one [VERIFY] item
8. After creating the note, link to it from at least one existing related note.

Report: file created, definition source, wiki links added, backlinks updated.
```
