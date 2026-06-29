# Meeting Intake Examples

## 1. Outlook Invitation

Prompt:

```text
Use Meeting Intake for this E-Mobility Europe WG SDV/AVS/AI Outlook invitation.
This source is only an invitation.
```

Expected folder:

```text
08 Meetings/EME/WG SDV-AVS-AI/2026-06/2026-06-29 EME WG SDV-AVS-AI Initial Meeting/
```

Expected outputs:

```text
pre-meeting-record.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Do not create `minutes.md` or `meeting-notes.md`. Do not invent decisions, actions, or outcomes.

## 2. Agenda Intake

Prompt:

```text
Use Meeting Intake for this agenda.
Extract agenda items and identify missing Vault context.
```

Expected outputs:

```text
agenda.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Agenda items are planned topics, not decisions.

## 3. Meeting Summary

Prompt:

```text
Use Meeting Intake for the EME SDV/AVS/AI first meeting summary.
Do not update canonical notes.
```

Expected outputs:

```text
meeting-notes.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

If the summary contains clear decisions or actions, capture them inside `meeting-notes.md`. Canonical updates should appear only in `merge-suggestions.md`.

Do not update:

- `07 Organizations/E-Mobility Europe.md`
- `01 Regulations/R171.md`
- `01 Regulations/ADS UN GTR.md`
- `03 GRVA/GRVA.md`

## 4. Official Minutes

Prompt:

```text
Use Meeting Intake for these official minutes.
Extract discussion, decisions, actions, knowledge gaps, and merge suggestions.
```

Expected outputs:

```text
minutes.md
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Decisions and actions may be captured inside `minutes.md` only when explicitly supported.

## 5. Follow-Up Email

Prompt:

```text
Use Meeting Intake for this follow-up email.
Identify new information, changed timing, attachments, action candidates, and possible merge suggestions.
```

Expected outputs:

```text
source-materials.md
knowledge-gap-analysis.md
merge-suggestions.md
```

Update `meeting-notes.md`, `agenda.md`, or `minutes.md` only if the follow-up clearly functions as one of those artifacts.

## 6. Knowledge Gap Output

Prompt:

```text
From this meeting material, identify what the Vault does not yet know.
```

Expected behavior:

- Search the Vault before listing missing items.
- Existing canonical notes are not listed as missing.
- Incomplete existing notes are listed separately.
- Missing items become Acquire Knowledge recommendations.
- Priority is `High`, `Medium`, `Low`, or `Needs Review`.

## 7. Merge Suggestion Output

Prompt:

```text
From this meeting material, suggest what existing canonical notes may need updates.
Do not apply the updates.
```

Expected behavior:

- Suggest updates only in `merge-suggestions.md`.
- Include target note, proposed update, reason, source evidence, confidence, and risk.
- Use `Needs Review` for low-confidence suggestions.
