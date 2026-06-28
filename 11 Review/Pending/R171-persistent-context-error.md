---
type: review_item
review_status: resolved
tags: [diagnostic, copilot, chat-history, R171, DSSAD, context-poisoning]
related: [R171]
created: 2026-06-28
last_updated: 2026-06-28
---

# Diagnostic: R171 Persistent DSSAD Error

Root cause identified and confirmed. The issue is **not** in `01 Regulations/R171.md`, **not** in the Obsidian vault vector index, and **not** in any knowledge note. The issue is the **poisoned conversation history** inside the old Copilot chat session.

---

## 1. Current Correct R171.md Frontmatter

File modified: **2026-06-28 09:31:49**

```yaml
type: regulation
status: active
tags: [regulation, DCAS, driver-control-assistance, SAE-L2, ADAS, driver-monitoring]
related: [DCAS, GRVA, ADAS TF, Driver Monitoring, Driver Availability, DDT, R79, R130,
         R131, R152, R156, New UN Regulation on ADS, Assisted Driving, ADAS, Risk Mitigation Function]
source: "E/ECE/TRANS/505/Rev.3/Add.170 (authentic text: ECE/TRANS/WP.29/2024/37)"
last_updated: 2026-06-28
entry_into_force: 2024-09-22
knowledge_type: official_fact
evidence_level: official
```

Title: `# UN Regulation No. 171 — Driver Control Assistance Systems (DCAS)`

**The file is correct. Zero DSSAD content. Zero stale aliases.**

---

## 2. Stale Statements Found

### What Copilot said (in the OLD conversation, at 14:13:01 on 2026-06-28)

```
**From YAML frontmatter:**
| Field     | Value                                                                 |
| Full name | Regulation No. 171 — Data Storage System for Automated Driving       |
| Tags      | regulation, r171, dssad, data-storage                                |
| Aliases   | Regulation 171 · UN R171 · Regulation No. 171 · DSSAD Regulation    |
```

None of these fields exist in the current `01 Regulations/R171.md`. This is hallucinated/stale content originating from conversation history.

---

## 3. Exact File Locations of Stale Content

### Files with stale R171=DSSAD content

| File | R171 mentions | Contains DSSAD=R171 | Type | Modified |
|---|---|---|---|---|
| `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md` | **157** | Yes — extensively | Copilot chat history | 2026-06-28 14:14:56 |

### Files with correct DSSAD references (not stale)

| File | Contains | Correct? |
|---|---|---|
| `01 Regulations/R171.md` | DCAS only | ✓ |
| `04 Working Groups/DSSAD.md` | DSSAD WG (correct concept) | ✓ |
| `05 Concepts/DSSAD.md` | DSSAD concept (correct) | ✓ |
| `03 GRVA/GRVA.md` | DSSAD WG in org tree (correct) | ✓ |
| `00 Home/Home.md` | Links to [[DSSAD]] (correct) | ✓ |
| `11 Review/Pending/R171-copilot-context-mismatch.md` | Quotes stale content for diagnostic purposes | ✓ contextually correct |
| `copilot/copilot-conversations/R171_Regulation_Overview@20260628_141513.md` | DCAS — fully correct | ✓ |

---

## 4. Timeline Reconstruction

```
2026-06-27 19:33   LLM_Wiki conversation STARTED
                   → Initial vault setup: R171 hallucinated as DSSAD
                   → 157 R171+DSSAD mentions written into conversation

2026-06-28 09:31   01 Regulations/R171.md UPDATED to DCAS
                   → Correct content: DCAS, entry into force 2024-09-22

2026-06-28 14:12   User asks "explain R171" in OLD conversation
                   → Copilot returns: "R171 = DSSAD"  ← wrong
                   → Context: [Notes: 01 Regulations/R171.md]  ← injected correctly
                   → But: 157 DSSAD references in chat history OVERRIDE the note

2026-06-28 14:13   User tries "@R171 / use ONLY the note"
                   → Copilot returns: DSSAD tags, aliases  ← still wrong
                   → Note content injected; chat history still wins

2026-06-28 14:14   Old conversation file last modified (stale responses saved)

2026-06-28 14:15   User starts FRESH conversation: R171_Regulation_Overview
                   → Copilot returns: DCAS, §5, entry into force  ← CORRECT
                   → No poisoned history → note read correctly
```

---

## 5. Root Cause

### Primary: Poisoned conversation history in the old chat session

The old conversation file (`LLM_Wiki项目结构搭建@20260627_193324.md`) contains **157 R171 mentions**, the vast majority asserting R171 = DSSAD. This file was created during the initial vault setup on 2026-06-27, when an early Copilot session hallucinated R171 as a DSSAD regulation.

Copilot is configured with `contextTurns: 15`, meaning the last 15 message pairs are included as conversation history in every new query. For a long-running conversation that accumulated 157 R171+DSSAD references:

1. User sends `@R171` → Copilot correctly injects `01 Regulations/R171.md` content (DCAS)
2. Copilot also includes recent conversation history turns → those turns contain dense DSSAD references
3. The LLM receives conflicting signals: note says DCAS, history says DSSAD (many times)
4. **History wins** — the volume of DSSAD references in the conversation history overrides the injected note content

This is **conversation context poisoning**: the AI's own prior incorrect answers are fed back as context, reinforcing the error.

### Confirmed by contrast

When the user opened a **new conversation** (`R171_Regulation_Overview@20260628_141513.md`) at 14:15:13 — just 2 minutes later, same R171.md file, same vault — Copilot immediately returned the correct DCAS content. Zero configuration change. The only difference: no poisoned history.

### Secondary: Vector store stale index

The IndexedDB vector store also contains DSSAD-flavoured R171 embeddings from before the note update. This is a secondary issue — it matters for vault-wide semantic search (`@vault`) but not for direct note injection (`@R171`). The conversation history is the dominant cause.

---

## 6. Copilot Settings Relevant to This Issue

```
contextTurns:                15   ← last 15 turns injected into every query
autoAddActiveContentToContext: true  ← active note content auto-added
qaExclusions:                "copilot"  ← should exclude copilot/ from vector index
maxSourceChunks:             30   ← up to 30 vector chunks per query
defaultSaveFolder:           "copilot/copilot-conversations"  ← saved to vault
```

**The `qaExclusions: "copilot"` setting** should prevent the conversation file from being indexed into the vector store going forward, but it does not affect live conversation context injection.

---

## 7. Recommended Actions

### Action 1 — Stop using the old conversation for R171 queries *(immediate)*

Do not ask R171 questions inside `LLM_Wiki项目结构搭建@20260627_193324.md`. This conversation's history is permanently poisoned with 157 DSSAD references. Starting a fresh conversation is the correct workaround — as already proven at 14:15:13.

### Action 2 — Archive or delete the old conversation file *(recommended)*

The file `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md` contains:
- Factually incorrect regulatory content (R171 = DSSAD is wrong)
- 157 R171+DSSAD contamination points
- No knowledge value (all real knowledge is in vault Markdown notes)

Options:
- **Move to `99 Archive/`** — preserves the session history but removes it from the active copilot conversations folder
- **Delete** — cleanest; the file has no knowledge value
- **Keep but do not continue** — acceptable, but the file will continue to pollute any future questions asked inside it

### Action 3 — Force vault re-index *(recommended, secondary)*

In Obsidian, run from the command palette:
> `Copilot: Clear vault index and rebuild`

This rebuilds the vector store from scratch, this time correctly excluding `copilot/` per `qaExclusions`. This resolves the secondary issue (stale DSSAD embeddings in the vector store).

### Action 4 — Verify the new conversation is correct *(already confirmed)*

`copilot/copilot-conversations/R171_Regulation_Overview@20260628_141513.md` (started 14:15:13) already shows DCAS content correctly. This is the reference for how R171 should behave in a clean context.

---

## 8. Summary

| Question | Answer |
|---|---|
| Is stale content in `01 Regulations/R171.md`? | **No** — file updated 09:31, content is DCAS and correct |
| Is stale content in any knowledge note? | **No** |
| Where is the stale content? | Only in `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md` |
| What is the mechanism? | **Conversation history poisoning** — 157 DSSAD references in the old chat override injected note content |
| Is this a vector store / cache issue? | Secondarily yes, but not the primary cause |
| Does Copilot work correctly in a fresh chat? | **Yes** — proven at 14:15:13 |
| Primary fix? | Stop using the old conversation; archive or delete it |
| Secondary fix? | Force vault re-index to clear stale vector embeddings |

---

## Status

- [x] Root cause identified — conversation history poisoning confirmed
- [ ] Archive or delete `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md`
- [ ] Force vault re-index (Copilot command palette → "Clear vault index and rebuild")
- [x] New clean conversation `R171_Regulation_Overview@20260628_141513.md` already works correctly
