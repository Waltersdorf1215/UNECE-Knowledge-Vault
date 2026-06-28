# Knowledge Review Scoring

Knowledge Review scores knowledge quality only. It never scores writing style.

## Total Score

The final score is out of 100 points:

| Dimension | Points |
|---|---:|
| Completeness | 25 |
| Evidence Quality | 25 |
| Relationship Coverage | 15 |
| Timeline Coverage | 10 |
| Cross References | 10 |
| Verification Status | 15 |
| **Total** | **100** |

## 1. Completeness — 25 Points

Evaluate whether the note has the expected sections for its type and whether those sections contain substantive content.

| Score | Meaning |
|---:|---|
| 22-25 | All expected sections present and meaningfully populated |
| 16-21 | Most sections present; one or two sections weak or incomplete |
| 8-15 | Several expected sections missing or placeholder-only |
| 0-7 | Note is mostly empty, fragmentary, or structurally incomplete |

Missing expected sections are Knowledge Gaps.

## 2. Evidence Quality — 25 Points

Evaluate whether factual claims are supported by visible evidence in the Vault.

| Score | Meaning |
|---:|---|
| 22-25 | Facts have clear source fields and inline citations where needed |
| 16-21 | Primary source is present, but some claims lack inline traceability |
| 8-15 | Evidence is uneven; many claims are only generally sourced |
| 0-7 | Most factual claims lack visible support |

Official evidence has highest value:

- UNECE Regulation
- UNECE Wiki
- Official Meeting Report
- Official Working Document
- Official Organization Website
- Other Official Evidence

Do not award evidence points for unsupported model knowledge.

## 3. Relationship Coverage — 15 Points

Evaluate the quality and completeness of relationships.

| Score | Meaning |
|---:|---|
| 13-15 | Strong outgoing links, relevant related YAML, and evidence-aware relationships |
| 9-12 | Good relationship coverage with minor missing links |
| 4-8 | Sparse links or mismatch between body links and YAML `related` |
| 0-3 | Isolated note or relationships mostly unsupported |

Suggested relationships without evidence should improve the backlog, not the score.

## 4. Timeline Coverage — 10 Points

Evaluate whether key milestones are captured.

| Score | Meaning |
|---:|---|
| 9-10 | Major historical milestones documented with dates and sources |
| 6-8 | Timeline exists but is incomplete |
| 3-5 | Only one or two milestones present |
| 0-2 | No meaningful timeline coverage where one is expected |

For regulations, check adoption, entry into force, amendments, revision history, and WP.29/GRVA milestones.

## 5. Cross References — 10 Points

Evaluate whether the note participates in the knowledge graph.

| Score | Meaning |
|---:|---|
| 9-10 | Links connect across regulations, concepts, groups, organizations, and timeline context |
| 6-8 | Links exist but are concentrated in one category |
| 3-5 | Few outgoing links or weak graph context |
| 0-2 | No meaningful cross references |

Cross references should be relevant and evidence-aware. Do not reward link stuffing.

## 6. Verification Status — 15 Points

Evaluate how much unresolved uncertainty remains.

| Score | Meaning |
|---:|---|
| 13-15 | Few or no `[VERIFY]`, `source_pending`, or unsupported claims |
| 9-12 | Some verification items remain but are clearly marked |
| 4-8 | Many unresolved verification items or vague unsupported claims |
| 0-3 | Verification status is unclear or high-risk |

Mark unsupported factual statements as `Needs Verification`. Do not infer sources.

## Status Mapping

Use these labels in review reports:

| Label | Meaning |
|---|---|
| `OK` | Quality is sufficient for the current scope |
| `Warning` | Usable, but improvement recommended |
| `Missing` | Required knowledge is absent |
| `Needs Verification` | Claim, relationship, or date lacks evidence |
| `Conflict` | Vault content appears contradictory |

## Score Interpretation

| Score | Meaning |
|---:|---|
| 90-100 | Strong, trustworthy, well-connected knowledge |
| 75-89 | Good knowledge with manageable gaps |
| 60-74 | Useful but incomplete; needs targeted improvement |
| 40-59 | Weak or uneven; requires follow-up acquisition or merge work |
| 0-39 | Not reliable enough for authoritative use |

## Hard Penalties

Apply these caps when relevant:

- If a note has no source field and no inline evidence, maximum score is 60.
- If a note contains major unsupported legal or regulatory dependency claims, maximum score is 65.
- If a note has unresolved contradictions in core facts, maximum score is 70.
- If a note is a placeholder, maximum score is 45.
- If a note appears to duplicate another canonical note without clarification, maximum score is 75.

## Scoring Discipline

- Do not score writing style.
- Do not reward confident prose without evidence.
- Do not penalize a concise note if it contains the needed sourced knowledge.
- Do not fill gaps while scoring.
- Do not browse for missing information.
