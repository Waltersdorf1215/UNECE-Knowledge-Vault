# ADR-002 Knowledge Views

## Status

Accepted

## Context

Users often ask questions that span many entities, such as DCAS timelines, ADS evolution, or organization participation. These are perspectives over canonical knowledge, not new facts.

## Decision

Knowledge Views are presentation and query artifacts. They aggregate and navigate canonical knowledge without introducing new facts.

## Rationale

Views make the Vault usable for exploration while preserving canonical storage by entity.

## Consequences

- Views should link to canonical notes.
- Views may include generated timelines, summaries, tables, diagrams, and Dataview-style queries.
- Views are excluded from canonical ontology compliance scoring.
- Views may be regenerated when canonical knowledge changes.
