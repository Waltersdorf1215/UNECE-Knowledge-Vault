# Example: Merge R171 Evidence

Use the **Knowledge Merge Skill**.

---

## Input

Evidence folder: `15 Evidence/R171/`

Load all JSON files present in that folder. Expected files may include:

- `evidence.json` — extracted facts with source citations
- `entities.json` — entity list (R171, DCAS, Driver Monitoring, ADAS TF, etc.)
- `relationships.json` — relationship triples with evidence metadata
- `timeline.json` — dated milestones for R171
- `open_questions.json` — unresolved items

If any file is missing, proceed with what is available and note the gap in the changelog.

---

## Instructions

1. **Load the OS rules first.** Read `CLAUDE.md`, `KNOWLEDGE_RULES.md`, `SCHEMA.md`, `RELATIONSHIPS.md`, and `IMPORT_PIPELINE.md` before touching any note.

2. **Do not browse the web.** Do not fetch URLs. Do not read from wiki.unece.org. All evidence must come from the input folder or files already in this vault.

3. **Do not infer unsupported relationships.** In particular:
   - Do not assert that R171 is a "companion" or "predecessor" of R157 unless the evidence JSON explicitly cites a source for this
   - Do not assert that R155 or R156 are prerequisites for R171 unless explicitly evidenced
   - Route any R171 ↔ R157 relationship claim to `11 Review/Pending/` (see existing review item `11 Review/Pending/R157-R171-evidence-review.md`)

4. **Update existing notes first.** Check these notes before creating anything new:
   - `01 Regulations/R171.md`
   - `04 Working Groups/DCAS.md`
   - `04 Working Groups/ADAS TF.md`
   - `05 Concepts/DCAS.md`
   - `05 Concepts/Driver Monitoring.md`
   - `05 Concepts/Driver Availability.md`
   - `14 Timeline/R171 Timeline.md`

5. **Apply the Evidence Gate to every claim.** If a fact from the evidence JSON cannot be traced to a named document and section, do not merge it — route it to `11 Review/Pending/` with a note explaining what source is needed.

6. **Use inline citations.** Every merged fact must follow the format:
   `**Fact (document, §X.Y, explicit, high):** "[quote or paraphrase]"`

7. **Label interpretations.** Any claim that is a logical conclusion rather than a direct quote must be prefixed: `*Interpretation:*`

8. **Route low-confidence items to Review Queue.** Create review items in `11 Review/Pending/` for:
   - Relationships between R171 and other regulations without explicit citation
   - Supplement 2 changes that cannot be confirmed from the local ADAS-37-02 file
   - Date claims that are approximate or inferred

9. **Update the R171 timeline.** Add confirmed milestones to `14 Timeline/R171 Timeline.md`. Use `[VERIFY]` for dates that are uncertain.

10. **Generate a changelog.** Append a merge entry to `CHANGELOG.md` listing all files updated, created, and all review items created.

---

## Expected Output

After execution, report:

- Which R171-related notes were updated
- Any new notes created
- Which relationships were merged (with evidence class)
- Which claims were routed to Review Queue and why
- Remaining evidence gaps (e.g., "R171 original adoption date — source needed")
