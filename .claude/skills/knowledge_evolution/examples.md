# Knowledge Evolution Examples

## Example 1 — Upgrade Vault to Ontology v1.1

User prompt:

```text
Upgrade the Vault to Ontology v1.1.
Generate a migration plan first.
Do not modify files until I approve.
```

Expected behavior:

- Read `Governance/KNOWLEDGE_ONTOLOGY.md`.
- Inspect the requested scope.
- Detect legacy metadata, entity types, relationship vocabulary, naming, and folder issues.
- Generate a migration plan.
- Stop for approval.

## Example 2 — Normalize Evidence Metadata

User prompt:

```text
Normalize evidence metadata for all active regulation notes.
```

Expected behavior:

- Inspect `01 Regulations/`.
- Identify notes missing `knowledge_type`, `evidence_level`, `confidence`, or review metadata.
- Determine which fields can be safely populated from existing note content.
- Recommend fields that cannot be safely populated.
- Produce a migration plan before changes.

## Example 3 — Normalize Relationship Vocabulary

User prompt:

```text
Normalize relationship vocabulary in R171.
```

Expected behavior:

- Inspect R171 and Governance relationship vocabulary.
- Find legacy terms such as `requires` or broad `related`.
- Convert only approved, evidence-supported structural relationships.
- Route uncertain relationship changes to recommendations.

## Example 4 — Normalize Review Artifacts

User prompt:

```text
Normalize review artifacts to the current Governance ontology.
```

Expected behavior:

- Inspect `11 Review/`.
- Identify review files with `review_dashboard`, `review_backlog`, `review_item`, `test_report`, or missing `type`.
- Plan migration to `type: review_artifact` while preserving subtype in `review_type`.
- Apply only after approval.

## Example 5 — Prepare Vault for New Governance Version

User prompt:

```text
Prepare the Vault for the new Governance version.
Detect legacy structures only.
```

Expected behavior:

- Read latest Governance documents.
- Inspect entire Vault or requested scope.
- Produce a migration plan and recommendations.
- Do not edit knowledge notes.

## Example 6 — Detect Legacy Structures Without Modifying Knowledge

User prompt:

```text
Find ontology drift in Organizations.
Do not modify the Vault.
```

Expected behavior:

- Inspect `07 Organizations/`.
- Report unsupported types, missing metadata, weak sources, aliases, and folder issues.
- Do not apply migration.

