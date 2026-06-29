# ADR-001 Canonical Knowledge

## Status

Accepted

## Context

The Vault must support long-term regulatory research. Regulatory facts can become unreliable if copied into many notes, summaries, dashboards, or meeting records.

## Decision

Canonical regulatory facts must live in the appropriate canonical knowledge entity note. Other artifacts may link, summarize, review, or propose updates, but they must not become competing sources of truth.

## Rationale

A single canonical location preserves evidence traceability, reduces conflicts, and makes future updates manageable.

## Consequences

- Cross-entity answers should be generated from canonical notes.
- Meeting artifacts and review reports may identify update candidates but should not silently update canonical facts.
- Knowledge Merge is required when new evidence should become canonical.
