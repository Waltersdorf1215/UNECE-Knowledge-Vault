# ADR-004 Meeting Lifecycle

## Status

Accepted

## Context

Meetings produce invitations, agendas, notes, minutes, decisions, actions, and follow-up material over time. A single flat note cannot reliably represent this lifecycle or preserve source boundaries.

## Decision

Meeting records are stored as structured folders under:

```text
08 Meetings/<Organizer>/<Working Group or General>/<YYYY-MM>/<YYYY-MM-DD Meeting Title>/
```

Each source type maps to a specific artifact file, such as `pre-meeting-record.md`, `agenda.md`, `minutes.md`, `decisions.md`, `action-items.md`, `follow-up.md`, and `source-materials.md`.

## Rationale

The structure makes meeting records traceable by organizer, working group, and month. It also prevents invitations, agendas, minutes, and decisions from being confused.

## Consequences

- Invitations create pre-meeting records only.
- Decisions and action items are created only when explicitly sourced.
- Canonical notes are not updated automatically from meeting material.
- Private links and participant details must be handled conservatively.
