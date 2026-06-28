# Prompt: Classify Knowledge

**Parameters to fill before use:**
- `{{STATEMENT}}` — the exact statement to be classified
- `{{SOURCE_DOCUMENT}}` — the document this statement came from
- `{{SOURCE_SECTION}}` — the section or paragraph (or "not identified")

---

## Prompt Text

```
You are a knowledge classification assistant for the UNECE Knowledge OS.

Apply the Inference Drift Test from KNOWLEDGE_RULES.md to the following statement:

Statement: "{{STATEMENT}}"
Source document: {{SOURCE_DOCUMENT}}
Source section: {{SOURCE_SECTION}}

Answer each question in sequence:

Question 1: Is this statement explicitly written in {{SOURCE_DOCUMENT}} §{{SOURCE_SECTION}}?
- If YES: classify as OFFICIAL FACT. Provide the exact quote.
- If NO: continue to Question 2.

Question 2: Is this statement derived by combining {{SOURCE_DOCUMENT}} with 
one or more other documents or by logical inference?
- If YES: classify as INTERPRETATION. State what inference was made.
- If NO: continue to Question 3.

Question 3: Is this statement a structural relationship 
(e.g., "GRVA reports to WP.29") stated in the document's process description?
- If YES: classify as STRUCTURAL RELATIONSHIP. Cite where stated.
- If NO: continue to Question 4.

Question 4: Is this statement the author's own analysis or hypothesis?
- If YES: classify as PERSONAL INSIGHT. Note it belongs in Research Notes only.
- If UNSURE: classify as [VERIFY]. Do not merge until source is confirmed.

Output format:
Classification: [OFFICIAL FACT | STRUCTURAL RELATIONSHIP | INTERPRETATION | PERSONAL INSIGHT | VERIFY]
Reason: [one sentence]
Suggested label: [exact label text to prepend in the note, or "cite source inline"]
Safe to merge into: [regulation note | concept note | research note | not yet]
```

---

## Notes

- Run this prompt for any statement you are uncertain about before writing it into the graph
- The output gives you the exact label to prepend in the note
- "Safe to merge into: not yet" means flag with `[VERIFY]` and do not merge until confirmed
