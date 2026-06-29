# ADR-006 Unknown Over Guess

## Status

Accepted

## Context

Regulatory, organizational, and meeting data often arrives incomplete. Filling gaps by inference can create false facts that later become hard to detect.

## Decision

Unknown values must be marked explicitly as `unknown` rather than guessed.

## Rationale

Explicit unknowns preserve integrity and create actionable review or acquisition targets.

## Consequences

- Agents should use `unknown` in metadata when critical fields are missing.
- Missing information should become an open question, backlog item, or acquisition candidate.
- Meeting attendees, decisions, action items, dates, and legal relationships must not be inferred.
- Review should treat unknowns as manageable gaps, not failures of writing style.
