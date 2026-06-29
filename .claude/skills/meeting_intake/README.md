# Meeting Intake Skill

Meeting Intake processes meeting material into structured UNECE Knowledge OS meeting folders.

It stays practical:

```text
meeting material -> meeting folder -> meeting records -> knowledge-gap-analysis.md -> merge-suggestions.md
```

It never updates canonical knowledge notes automatically.

## Folder Structure

```text
08 Meetings/
└── <Organizer>/
    └── <Working Group or General>/
        └── <YYYY-MM>/
            └── <YYYY-MM-DD Meeting Title>/
                ├── pre-meeting-record.md
                ├── agenda.md
                ├── meeting-notes.md
                ├── minutes.md
                ├── source-materials.md
                ├── knowledge-gap-analysis.md
                └── merge-suggestions.md
```

Do not create extra files such as `knowledge-extraction.md`, `timeline-events.md`, `review-report.md`, `decisions.md`, or `action-items.md` unless explicitly requested.

## Source Routing

| Source type | Files to create or update |
| --- | --- |
| `invitation` | `pre-meeting-record.md`, `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md` |
| `agenda` | `agenda.md`, `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md` |
| `meeting_note` | `meeting-notes.md`, `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md` |
| `minutes` | `minutes.md`, `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md` |
| `presentation` | `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md`, plus another record only if justified |
| `follow_up_email` | `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md`, plus another record only if justified |
| `attachment` | `source-materials.md`, `knowledge-gap-analysis.md`, `merge-suggestions.md` |
| `unknown` | Conservative source inventory, gap analysis, and merge suggestions marked `Needs Review` |

## Knowledge Gap Analysis

`knowledge-gap-analysis.md` identifies knowledge mentioned in meeting material that is missing or incomplete in the Vault.

Rules:

- Search the Vault before listing missing items.
- Missing entities route to Acquire Knowledge recommendations.
- Existing but incomplete notes go under incomplete existing notes.
- Do not create canonical notes automatically.

## Merge Suggestions

`merge-suggestions.md` identifies existing canonical notes that may need updates because of the meeting material.

Rules:

- Do not apply merges automatically.
- Do not update canonical notes.
- Each suggestion needs target note, proposed update, reason, source evidence, confidence, and risk.
- Low-confidence suggestions are marked `Needs Review`.

## Privacy

Meeting material may include Teams links, private email addresses, attendee names, or non-public agenda content.

Rules:

- Do not expose Teams links in public summaries.
- Avoid private emails unless necessary.
- Mark non-public meeting artifacts `sensitive: true`.
- Prefer summaries over raw invitation text.
- Warn before committing sensitive meeting material to GitHub.

## Governance

Meeting Intake follows:

- `Governance/MEETING_KNOWLEDGE_MODEL.md`
- `Governance/KNOWLEDGE_EXTRACTION_SPEC.md`
- `Governance/KNOWLEDGE_ONTOLOGY.md`

## Test Prompt

```text
Use Meeting Intake for the EME SDV/AVS/AI first meeting summary.
Create or update meeting-notes.md, source-materials.md, knowledge-gap-analysis.md, and merge-suggestions.md.
Do not update E-Mobility Europe.md, R171.md, ADS UN GTR.md, or GRVA.md.
Only suggest canonical updates in merge-suggestions.md.
```
