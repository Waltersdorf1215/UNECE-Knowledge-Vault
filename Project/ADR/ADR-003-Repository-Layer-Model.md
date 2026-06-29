# ADR-003 Repository Layer Model

## Status

Accepted

## Context

The repository contains different artifact classes: knowledge notes, governance documents, skills, project files, and future views. Treating every Markdown file as a knowledge entity creates noisy compliance results and unclear responsibilities.

## Decision

The repository is organized into architectural layers: Knowledge, Governance, Automation, Project, and Knowledge Views.

## Rationale

Layer separation allows tools and agents to apply the right rules to the right files. Governance documents define policy, skills implement workflows, project documents support maintainers, and only canonical knowledge is scored as domain knowledge.

## Consequences

- Agents must determine repository layer before applying ontology rules.
- Automation and Project files are not canonical knowledge.
- Governance may be validated separately.
- Knowledge Review and Knowledge Evolution should operate on the Knowledge Layer by default.
