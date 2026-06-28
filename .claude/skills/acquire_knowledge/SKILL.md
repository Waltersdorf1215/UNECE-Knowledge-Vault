# Skill: Acquire Knowledge

**Version:** 1.0.0
**Category:** Acquire + Merge
**Depends on:** `deep-research` skill (external), `knowledge-merge` skill (internal)

---

## Purpose

`acquire_knowledge` is the **primary knowledge acquisition workflow** for the UNECE Knowledge OS. It orchestrates the complete pipeline from user question → vault search → web research (if needed) → note creation/update → answer.

It does not replace the `deep-research` skill. It decides **when** to invoke it, and what to do with the results.

> **Guiding principle:** Every acquisition permanently improves the Vault. Future questions about the same topic should be answered from the Vault rather than repeating web research.

---

## When to Invoke This Skill

Use this skill whenever the user asks:
- What is [UNECE entity / concept / regulation / working group]?
- Explain [topic] in the context of UNECE / WP.29 / GRVA / automated driving
- What happened at [session]?
- Who submitted [document]?
- What is the status of [regulation]?
- Any question where the answer might live in or should be added to the Vault

Do **not** use this skill for:
- Pure web searches with no UNECE relevance
- Tasks that are already fully answered by an existing `active` vault note
- Tasks handled by `knowledge-merge` (merging pre-analyzed evidence) or `deep-research` alone

---

## Workflow: 10 Steps

---

### Step 1 — Search the Vault

**Before touching the web, search the vault.**

Check the following locations in order:
1. `01 Regulations/` — for regulation queries
2. `04 Working Groups/` — for IWG / TF / body queries
3. `05 Concepts/` — for technical / regulatory concept queries
4. `07 Organizations/` — for org queries
5. `02 WP29/` and `03 GRVA/` — for session / meeting queries
6. `08 Meetings/`, `09 Proposals/` — for proposal and meeting queries
7. `10 Research Notes/` — for prior research
8. `14 Timeline/` — for historical event queries

Search by:
- Note title (exact match)
- Aliases in YAML frontmatter
- Wiki links mentioning the entity name
- Tags

**Determine the vault state before proceeding:**

| State | Condition | Next step |
|---|---|---|
| `exists_complete` | Note exists, `status: active`, all key sections populated | Step 2 |
| `exists_incomplete` | Note exists but `status: placeholder` or `draft`, or key sections missing | Step 3 |
| `missing` | No note found anywhere in vault | Step 3 |

**Never assume the vault state. Always check.**

---

### Step 2 — Answer from Vault (Complete Knowledge)

If the vault state is `exists_complete`:

- Answer the user's question directly from vault content
- Cite the relevant vault note(s) as source
- Do **not** invoke `deep-research`
- Do **not** perform any web search
- State clearly: "This answer is based on existing vault knowledge."

If there are minor gaps (e.g., one missing field, one unverified date), note them as open questions but still answer from vault.

---

### Step 3 — Invoke Deep Research (Missing or Incomplete)

If the vault state is `missing` or `exists_incomplete`:

Invoke the `deep-research` skill with a targeted query.

**Query construction rules:**
- Be specific: include the entity name, the UNECE context, and what is missing
- Include disambiguation context when needed (e.g., "EME in UNECE vehicle regulations, not electromagnetic emissions")
- Request: definition, regulatory status, official documents, related entities, timeline

**Example query:**
```
What is EME in the context of UNECE WP.29 and vehicle regulations?
Find: (1) full name and definition, (2) regulatory status and relevant documents,
(3) relationship to GRVA/DCAS/ADS, (4) official sources only — UNECE wiki,
official regulations, working group documents.
```

Proceed to Step 4 after `deep-research` returns results.

---

### Step 4 — Apply Research Priority

When evaluating sources returned by `deep-research`, apply this priority hierarchy strictly:

| Priority | Source Type | Trust Level |
|---|---|---|
| 1 | Official UNECE regulations (ECE/TRANS/WP.29/…) | Authoritative — cite as Fact |
| 2 | UNECE wiki (wiki.unece.org) | High — cite as Fact with verification |
| 3 | Official organization websites (OICA, CLEPA, ISO, SAE) | High — cite as Structural/Fact |
| 4 | Official UNECE meeting reports | High — cite as Fact |
| 5 | Official UNECE working documents (INF / WP series) | Medium-High — cite as Fact with source |
| 6 | Published standards (ISO, SAE, IEEE) | Medium — cite with standard number |
| 7 | Academic papers | Medium — label as *Interpretation:* if synthesized |
| 8 | Industry publications (OICA papers, ACEA news) | Low-Medium — label appropriately |
| 9 | LLM prior knowledge (last resort) | Low — label `[UNVERIFIED — LLM knowledge]` |

**Hard rules:**
- Model prior knowledge must **never** overwrite content sourced from official documents
- Any fact without a citable source must be labeled `[VERIFY]` or `[UNVERIFIED]`
- If `deep-research` returns no reliable sources, explicitly state the gap rather than fabricating content

---

### Step 5 — Create or Update Vault Notes

After research, update the Vault:

**If note exists (incomplete):**
- Open the existing note
- Read its full content before writing anything
- Append or merge new knowledge into the appropriate sections
- Do not overwrite manually written content unless it is factually wrong and a better source exists
- Upgrade `status` from `placeholder` → `draft` or `draft` → `active` as content warrants

**If note is missing:**
- Select the appropriate template from `.claude/skills/acquire_knowledge/templates/`
- Create the note in the correct folder per SCHEMA.md folder mapping
- Fill all available fields; leave unavailable fields as `source_pending` or `[VERIFY]`

**Note types and folders:**

| Type | Folder | Template |
|---|---|---|
| Regulation | `01 Regulations/` | `templates/regulation.md` |
| Working Group / IWG / TF | `04 Working Groups/` | `templates/working_group.md` |
| Concept | `05 Concepts/` | `templates/concept.md` |
| Organization | `07 Organizations/` | (use `templates/working_group.md` adapted) |
| Meeting / Session | `02 WP29/`, `03 GRVA/`, `08 Meetings/` | `templates/meeting.md` |
| Entity (generic) | Appropriate folder | `templates/entity.md` |

**Epistemic labeling — always applied:**
- Sourced official fact → `**Fact (source, §X.Y):**`
- Derived / interpreted → `*Interpretation:*`
- Personal analysis → `*Insight:*` (Research Notes only)
- Unverified → `[VERIFY]`
- LLM knowledge only → `[UNVERIFIED — LLM knowledge]`

---

### Step 6 — Preserve Existing Knowledge

When updating an existing note:

- **Append** new sections; do not delete existing ones
- **Merge** if the same topic is covered — combine, don't duplicate
- If a sourced fact contradicts existing content: add the new fact with citation, flag the conflict with `[CONFLICT — verify]`, do not silently overwrite
- The `created` YAML field is **never** changed
- Always update `last_updated` to today's date on any touched note

---

### Step 7 — Update Relationships

After creating or updating a note:

1. **Add wiki links** in the note body to all related entities
2. **Update related notes** — add a backlink from at least one existing note to the new/updated note
3. **Check RELATIONSHIPS.md** — if a new relationship *type* (verb) has been used that doesn't exist yet, add it
4. **Update `related` YAML field** to mirror all wiki links in the note body

**Forbidden:**
- Creating relationships by conceptual similarity alone (see `RELATIONSHIPS.md §0.6`)
- Stating that Entity A "is a companion of" / "is a prerequisite of" Entity B without explicit evidence
- Any Class 4 (Interpretive) relationship in an entity note — those go to `10 Research Notes/` or `11 Review/Pending/`

---

### Step 8 — Attach Evidence

For every new fact added to the vault, record:

```yaml
# In YAML (for the note as a whole):
source: "ECE/TRANS/WP.29/2026/139"
knowledge_type: official_fact | structural_relationship | interpretation | personal_insight
evidence_level: official | derived | personal

# Inline (for specific claims):
**Fact (ECE/TRANS/WP.29/2026/139, §2.1, explicit, high):** "[quote]"
```

If a source cannot be named: write `[VERIFY — source needed]` and do not present as fact.

---

### Step 9 — Knowledge Gap Detection

After creating or updating the note, scan it for these gap types:

| Gap Type | Check |
|---|---|
| Missing Overview | Is there a Summary section with ≥2 sourced sentences? |
| Missing Definitions | For concepts/regulations: is there a formal definition with source? |
| Missing Relationships | Does the note have ≥3 outgoing wiki links? |
| Missing Timeline | For regulations/WGs: is there a regulatory history or milestone table? |
| Missing References | Does the source field have a real document number? |
| Missing OEM context | For regulations: are implementing OEMs noted? |
| Missing Open Questions | Is there an Open Questions section? |

For each gap found:
- Either fill it immediately (if research provides the answer)
- Or add a `[VERIFY]` item in the **Open Questions** section of the note
- And add the gap to `ROADMAP.md` if it requires a separate research session

---

### Step 10 — Answer the User

Deliver the final answer structured as follows:

```
## Answer

[Direct answer to the user's question — concise, accurate]

## Sources Used

| Source | Type | Note |
|---|---|---|
| [document or vault note] | [vault / official / web] | [confidence] |

## Vault State After This Acquisition

- Notes created: [list]
- Notes updated: [list]
- Relationships added: [list]
- Knowledge gaps remaining: [list]

## Remaining Uncertainties

- [Any [VERIFY] items that couldn't be resolved]
```

Clearly distinguish:
- **Existing vault knowledge** (was already there)
- **Newly acquired knowledge** (added this session)
- **Assumptions** (labeled as such)
- **Remaining uncertainties** (labeled `[VERIFY]`)

---

## Constraints

- Never modify `CLAUDE.md`, `SCHEMA.md`, `KNOWLEDGE_RULES.md`, `RELATIONSHIPS.md`, or `IMPORT_PIPELINE.md` unless explicitly asked
- Never delete existing vault notes
- Never rename files without user confirmation
- Never present inferred relationships as official facts
- Never skip Step 1 (vault search) — even for obscure queries
- Never rely on LLM prior knowledge when official sources are available or findable

---

## Integration with Other Skills

| Skill | Role | Called by Acquire Knowledge? |
|---|---|---|
| `deep-research` | Web research harness | Yes — in Step 3 when vault is incomplete |
| `knowledge-merge` | Writes pre-analyzed evidence to vault | No — separate skill for batch imports |
| `UNECE_Space_Seeder` | Crawls UNECE wiki for page hierarchy | No — run separately before acquisition |

---

## Output

After every execution, update `CHANGELOG.md` with:

```markdown
## Acquisition — YYYY-MM-DD | [Topic]

**Question:** [User's original question]
**Vault state before:** [exists_complete | exists_incomplete | missing]
**Deep Research invoked:** [yes / no]

### Notes Created
- [path] — [entity type]

### Notes Updated
- [path] — [what changed]

### Relationships Added
- [Entity A] → [relationship] → [Entity B]

### Knowledge Gaps Remaining
- [gap] — [what evidence is needed]
```
