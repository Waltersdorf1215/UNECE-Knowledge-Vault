---
type: meta
status: active
tags: [review, queue, evidence-gate, relationships]
related: [RELATIONSHIPS, SCHEMA, CLAUDE, IMPORT_PIPELINE, KNOWLEDGE_RULES]
source: ""
last_updated: 2026-06-27
created: 2026-06-27
---

# Review Queue — Evidence-Pending Relationships

This folder holds relationships, claims, and knowledge items that could not be merged into the knowledge graph due to insufficient evidence. Every item here is waiting for either:
- A source document that confirms the relationship (→ upgrade to Approved)
- A decision to reject the relationship as unsupported (→ move to Rejected)

---

## Subfolders

| Folder | Purpose |
|---|---|
| `Pending/` | Relationships awaiting evidence or human decision |
| `Approved/` | Relationships that have been confirmed and merged into entity notes |
| `Rejected/` | Relationships confirmed as unsupported — preserved for audit trail |

---

## When Claude Creates a Pending Review Item

Claude routes a relationship to `Pending/` whenever:

1. `evidence_strength = inferred` or `unsupported` — no source document found
2. `confidence = low` or `needs_review` — source is uncertain or ambiguous
3. The relationship class is **Conceptual** (Class 3) or **Interpretive** (Class 4)
4. Two regulations are connected in a way that implies legal dependency without a direct citation
5. Pattern completion was detected — "A relates to B because it's similar to how C relates to D"
6. The Evidence Gate (IMPORT_PIPELINE.md Stage 7.2) blocked the merge

**Claude must not wait for the user to notice the problem.** When a blocked relationship is found, a review item is created immediately and the user is notified.

---

## Review Item Format

Each review item in `Pending/` follows this structure:

```yaml
---
type: review_item
review_status: pending
entities: [Entity A, Entity B]
proposed_relationship: "[relationship type]"
evidence_strength: inferred | unsupported
confidence: low | needs_review
created: YYYY-MM-DD
source_of_concern: ""   # where this relationship appeared and why it was flagged
---
```

Body must include:
- **Unsupported claims** — exact statements that were blocked
- **Why unsafe** — what makes the claim potentially incorrect
- **Safer wording** — how to describe the relationship without overstating the evidence
- **Evidence needed** — what specific document, section, or source would confirm the relationship
- **Resolution options** — what actions can be taken

---

## How to Approve a Review Item

1. Find the source document that explicitly states the relationship
2. Record: document number, section, evidence quote
3. Update the review item: set `review_status: approved`, add citation fields
4. Move the file to `Approved/`
5. Update the entity notes with the now-confirmed relationship, with full citation
6. Add an entry to `CHANGELOG.md`

---

## How to Reject a Review Item

1. Confirm no source supports the relationship
2. Update the review item: set `review_status: rejected`, note the reason
3. Move the file to `Rejected/`
4. **Do not delete.** Rejected items preserve audit history — future Claude sessions must not re-propose the same unsupported relationship

---

## Rejected Items as Permanent Guard Rails

Rejected review items serve a specific protective function: they prevent the same inference from re-entering the graph in future sessions.

When starting a new session, Claude should check `Rejected/` for any relationship that resembles one being proposed. If a match is found, the relationship must not be proposed again unless new source evidence has been found.

---

## Current Review Queue

| File | Entities | Status | Created |
|---|---|---|---|
| `Pending/R157-R171-evidence-review.md` | R157, R171 | pending | 2026-06-27 |
