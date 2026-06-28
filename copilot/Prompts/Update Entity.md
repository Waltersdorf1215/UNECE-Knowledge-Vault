# Prompt: Update Entity

**Parameters to fill before use:**
- `{{NOTE_PATH}}` — vault path to the note to update, e.g., `01 Regulations/R157.md`
- `{{NEW_INFORMATION}}` — brief description of what new information is available
- `{{SOURCE_DOCUMENT}}` — document number or name providing the new information
- `{{SECTION}}` — section of the source document, e.g., `§4.1.2` (or "unknown")

---

## Prompt Text

```
You are maintaining the UNECE Knowledge OS Obsidian vault.

Before starting, read CLAUDE.md and KNOWLEDGE_RULES.md (Rule Zero).

Task: Update the note at {{NOTE_PATH}} with the following new information:
- New information: {{NEW_INFORMATION}}
- Source document: {{SOURCE_DOCUMENT}}
- Source section: {{SECTION}}

Rules:
1. Read the existing note before making any change.
2. Do not overwrite existing content — append or extend.
3. Classify the new information before merging:
   - Explicitly stated in {{SOURCE_DOCUMENT}} §{{SECTION}} → Official Fact with citation
   - Derived by combining multiple documents → *Interpretation:* label required
   - Your own analysis → Research Note only, not in this note
4. Update `last_updated` in the YAML frontmatter.
5. If the new information introduces new entity relationships, add wiki links.
6. If `status` is `placeholder` or `draft` and the note now has sourced content, 
   upgrade status to `draft` or `active` as appropriate.

Report: what section was updated, what was added, what label was applied.
```
