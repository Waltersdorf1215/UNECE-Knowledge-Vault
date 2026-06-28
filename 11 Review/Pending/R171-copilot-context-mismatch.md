---
type: review_item
review_status: pending
tags: [diagnostic, copilot, cache, R171, DSSAD, context-mismatch]
related: [R171]
created: 2026-06-28
last_updated: 2026-06-28
---

# Diagnostic: R171 Copilot Context Mismatch

Obsidian Copilot's `@R171 Current` context returns stale metadata describing R171 as DSSAD (Data Storage System for Automated Driving). The actual `01 Regulations/R171.md` is correct and contains DCAS content.

---

## 1. Actual Current R171.md Frontmatter

```yaml
type: regulation
status: active
tags: [regulation, DCAS, driver-control-assistance, SAE-L2, ADAS, driver-monitoring]
related: [DCAS, GRVA, ADAS TF, Driver Monitoring, Driver Availability, DDT, R79, R130,
         R131, R152, R156, New UN Regulation on ADS, Assisted Driving, ADAS, Risk Mitigation Function]
source: "E/ECE/TRANS/505/Rev.3/Add.170 (authentic text: ECE/TRANS/WP.29/2024/37)"
last_updated: 2026-06-28
regulation_number: "171"
entry_into_force: 2024-09-22
knowledge_type: official_fact
evidence_level: official
```

Heading: `# UN Regulation No. 171 — Driver Control Assistance Systems (DCAS)`

**The source file is correct.** The mismatch is not in `01 Regulations/R171.md`.

---

## 2. Stale Copilot Context Observed

Copilot is returning content such as:

```
full-name: Regulation No. 171 — Data Storage System for Automated Driving
tags: [regulation, r171, dssad, data-storage]
aliases: ["DSSAD Regulation", "UN R171", "Regulation 171"]
# R171 — Data Storage System for Automated Driving (DSSAD)
```

This content never appeared in `01 Regulations/R171.md`. It was fabricated during an early Copilot setup conversation and saved into conversation history.

---

## 3. Files Containing Stale R171/DSSAD Content

### Confirmed Source — Single File

| File | Lines | R171 mentions | Status |
|---|---|---|---|
| `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md` | 6,562 | **149** | Stale — should be excluded |

**Key stale lines in this file (confirmed by grep):**

| Line | Content |
|---|---|
| 274 | `\| [[R171]] \| DSSAD \| Active \|` |
| 957 | `full-name: Data Storage System for Automated Driving` |
| 1347 | `full-name: Regulation No. 171 — Data Storage System for Automated Driving` |
| 1349 | `tags: [regulation, r171, dssad, data]` |
| 1353 | `# R171 — Data Storage System for Automated Driving (DSSAD)` |
| 3270 | `full-name: Regulation No. 171 — Data Storage System for Automated Driving` |
| 3278–3284 | `tags: [dssad, data-storage]`, `aliases: ["DSSAD Regulation"]` |
| 3287 | `# R171 — Data Storage System for Automated Driving (DSSAD)` |
| 5941 | `R171 的全称是 Regulation No. 171 — Data Storage System for Automated Driving（DSSAD）` |
| 5984 | `R171 (DSSAD) ← R157 要求的数据记录配套` |
| 6160 | `## R171 — Data Storage System for Automated Driving (DSSAD)` |
| 6282 | `R157 强制要求 ALKS 车辆配备符合 R171 的 DSSAD` |
| 6482 | `Tags: regulation, r171, dssad, data-storage` |
| 6483 | `Aliases: Regulation 171, UN R171, DSSAD Regulation` |

### Other Files — DSSAD/data-storage strings present but NOT stale R171 content

These files contain "DSSAD" or "data-storage" as correct references to the DSSAD working group and concept — they are not misidentifying R171:

| File | Content | Correct? |
|---|---|---|
| `05 Concepts/DSSAD.md` | DSSAD concept note | ✓ Correct |
| `04 Working Groups/DSSAD.md` | DSSAD working group note | ✓ Correct |
| `03 GRVA/GRVA.md` | GRVA organizational tree mentioning DSSAD | ✓ Correct |
| `00 Home/Home.md` | Navigation links to [[DSSAD]] | ✓ Correct |
| `CHANGELOG.md`, `IMPORT_PIPELINE.md`, etc. | Examples of rejected "R171 is companion of R157" claim | ✓ Correct — these are guard-rail references |

---

## 4. Plugin Cache Analysis

### Copilot data.json settings (`.obsidian/plugins/copilot/data.json`)

| Setting | Value | Relevance |
|---|---|---|
| `indexVaultToVectorStore` | `"ON MODE SWITCH"` | Index is built when switching to Copilot mode |
| `enableIndexSync` | `true` | Index sync is enabled |
| `qaExclusions` | `"copilot"` | **Should** exclude `copilot/` folder from indexing |
| `qaInclusions` | `""` (all) | No inclusion filter |
| `embeddingModelKey` | `"text-embedding-3-small\|openai"` | Embedding model for vector search |
| `maxSourceChunks` | `30` | Up to 30 chunks retrieved per query |
| `autoAddActiveContentToContext` | `true` | Active note auto-added to context |

### Vector Store Location

The Copilot plugin stores its vector index in **Obsidian's IndexedDB** (not in the vault folder):

```
~/Library/Application Support/obsidian/IndexedDB/
    app_obsidian.md_0.indexeddb.leveldb/
        000005.ldb    ← Vector embeddings stored here
        000004.log    ← Write-ahead log
```

Inspection of the LevelDB `.ldb` file confirms it contains string references to both `R171` and `DSSAD`, indicating the stale conversation **was indexed** into the vector store.

---

## 5. Root Cause

### Primary cause: Stale conversation file indexed into vector store before or despite exclusion

The conversation file `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md` was created on **2026-06-27** during the initial vault setup. At that time, an early Copilot session incorrectly invented R171 = DSSAD content (a hallucination — R171 is DCAS; DSSAD is a separate data storage regulation).

This file (6,562 lines, 149 R171 mentions) was indexed into the Obsidian Copilot vector store. The vector index now contains dense DSSAD-flavoured embeddings associated with "R171".

### Why `qaExclusions: "copilot"` did not prevent this

Two possible failure modes:

**A. Timing:** The conversation file was indexed before `qaExclusions: "copilot"` was configured. The exclusion prevents future indexing but does not retroactively purge existing vectors from IndexedDB.

**B. The `@R171 Current` feature uses vector search alongside direct note injection.** When `@R171` is invoked, Copilot may:
1. Inject the current `01 Regulations/R171.md` content (correct)
2. Also retrieve top-N semantically similar chunks from the vector store — and the conversation file's 149 R171+DSSAD chunks score highest due to sheer repetition, polluting the context window alongside the correct note content

### Why the actual vault notes are not the source

- `01 Regulations/R171.md` — correct, no DSSAD content
- No other knowledge note in `01 Regulations/`, `05 Concepts/`, `04 Working Groups/` contains "R171 = DSSAD"
- The stale alias/tag metadata (`DSSAD Regulation`, `data-storage`) appears **only** in the conversation file

---

## 6. Recommended Cleanup Steps

### Step 1 — Force re-index without the stale conversation file *(primary fix)*

In Obsidian, with Copilot plugin:
1. Open Copilot settings → **QA Exclusions**
2. Confirm `copilot` is listed (it is: `"qaExclusions": "copilot"`)
3. Run **"Force re-index vault"** from the Copilot command palette
   - Command: `Copilot: Clear vault index and rebuild`
   - This clears the IndexedDB LevelDB and rebuilds from scratch, respecting current exclusions
   - The `copilot/` folder will be excluded on rebuild, removing all stale conversation embeddings

**Expected result:** After re-index, `@R171` context will only retrieve chunks from `01 Regulations/R171.md` and related DCAS notes.

### Step 2 — (Optional) Archive or delete the stale conversation file

The file `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md` contains historically incorrect regulatory content (R171 = DSSAD is factually wrong). It is a saved conversation, not a knowledge note.

Options:
- **Archive**: Move to `99 Archive/` to preserve history without polluting future indexes
- **Delete**: Remove the file entirely (it has no knowledge value — the correct R171 knowledge is now in `01 Regulations/R171.md`)
- **Leave in place**: The exclusion (`qaExclusions: "copilot"`) should prevent it from being re-indexed after Step 1

### Step 3 — Verify after re-index

After running the rebuild, test:
1. Open a new Copilot chat
2. Type `@R171` or `@R171 Current`
3. Confirm context shows: `UN Regulation No. 171 — Driver Control Assistance Systems (DCAS)`
4. Confirm no DSSAD aliases or tags appear

---

## 7. Summary Table

| Question | Answer |
|---|---|
| Is stale content in `01 Regulations/R171.md`? | **No** — file is correct |
| Is stale content in any knowledge note? | **No** — only in the conversation file |
| Where exactly is the stale content? | `copilot/copilot-conversations/LLM_Wiki项目结构搭建@20260627_193324.md`, 149 R171 mentions |
| Is it in the plugin cache (IndexedDB)? | **Yes** — LevelDB contains R171+DSSAD strings |
| Is `qaExclusions: copilot` set? | Yes — but did not retroactively purge existing vectors |
| Fix required in vault Markdown? | **None** — knowledge notes are correct |
| Fix required in plugin? | **Yes** — force re-index vault from Copilot command palette |

---

## Status

- [ ] Step 1: Force re-index vault (Copilot command palette → "Clear vault index and rebuild")
- [ ] Step 2: Decide fate of stale conversation file
- [ ] Step 3: Verify `@R171` context after re-index
