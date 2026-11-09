---
name: wyvern-chat-audit-world-sync
description: >-
  Automates the forensic audit of Wyvern Chat Logs (0..N messages, active summaries,
  and party state), detects relationship pacing drift (insta-love, instant devotion),
  character trait/species hallucinations, and extracts new emergent lore, syncing
  clean fixes back to Wyvern World, Lexicon, and active chat summaries via Web API.
---

# Wyvern Chat Audit & World Sync

## Overview
This skill provides an automated pipeline to extract, inspect, and reconcile long-running Wyvern simulation chat logs (`chat_log_*`). It identifies narrative drift, character trait hallucinations (e.g. eye/hair color, wrong species), premature romantic escalation ("insta-love"), and extracts newly emerged world-building facts (locations, factions, events) to keep the World Lexicon, World Characters, and active Chat Summaries 100% canon-compliant.

## Dependencies
- `scripts/sync_from_wyvern_web.py` (provides `get_auth_token` via Chrome IndexedDB refresh token extraction)
- Python 3.10+ (Standard Library `urllib`, `json`, `argparse`, `re`)
- Playwright / Chromium (optional, for DOM and DevTools integrity inspection)

## Quick Start

### 1. Fetch complete chat log (with auto-pagination):
```bash
python .agents/skills/wyvern-chat-audit-world-sync/scripts/chat_audit_sync.py fetch --chat-id chat_log_EG2dpGaMQ4DaEd4g287pE --output scratch/chat_export.json
```

### 2. Audit messages and summaries for drift & hallucinations:
```bash
python .agents/skills/wyvern-chat-audit-world-sync/scripts/chat_audit_sync.py audit --input scratch/chat_export.json --output scratch/audit_report.json
```

### 3. Sanitize chat summaries live on Wyvern:
```bash
python .agents/skills/wyvern-chat-audit-world-sync/scripts/chat_audit_sync.py sanitize-summaries --chat-id chat_log_EG2dpGaMQ4DaEd4g287pE
```

### 4. Sync emergent lore to World Lexicon:
```bash
python .agents/skills/wyvern-chat-audit-world-sync/scripts/chat_audit_sync.py sync-world --world-id _YpX47fNraQFw2dD7TdycJ --lore-file scratch/new_lore_proposals.json
```

## Utility Scripts (`scripts/chat_audit_sync.py`)

The CLI script implements four core subcommands:
- `fetch`: Connects to `https://app.wyvern.chat/api/new/chat-logs/{id}/messages` and paginates through all turns (0..N), dumping the full JSON payload (metadata + full messages array + summaries) to disk.
- `audit`: Scans messages and active summaries against canonical characters for:
  - Premature romantic / mate bond triggers (`caccia`, `compagno eterno`, `innamorato`, etc.).
  - Anatomical / locomotion drift (e.g. demihumans or lamia walking on non-existent legs).
  - Species or team name confusion (e.g. athlete team name confused for biological race).
  - Emergent locations, factions, and events.
- `sanitize-summaries`: Replaces contaminated summary sentences in the live chat log using `PUT /api/new/chat-logs/{id}` without deleting user history.
- `sync-world`: Deploys verified emergent lore entries to `POST /api/worlds/lexicon` with standard Svartúlfr hygiene flags (`whole_words_only: true`, `scan_persona: true`, `is_global: true`, zero em-dash).

## Workflow

### 1. Ingestion & Pagination
Always query `/api/new/chat-logs/{chat_id}/messages?page={N}&limit=100` iteratively until `hasMore` is false. Storing the consolidated array locally ensures zero token wastage and enables lightning-fast regex scanning.

### 2. Summary Contamination Check
Wyvern's automated scene summaries are injected back into the LLM context. If a summary captures an hallucination, the LLM will perpetuate it for hundreds of messages. Purging contaminated phrases in the summary array directly via `PUT /api/new/chat-logs/{id}` breaks the hallucination feedback loop immediately.

### 3. Two-Tier Pacing Enforcement
To prevent "insta-love" from returning:
- **Tier 1 (Character-Level):** Inject a `BEHAVIOR & PACING DISCIPLINE` block into `final_instructions` (or `post_history_instructions`) of the character card.
- **Tier 2 (World-Level):** Inject `<relationship_pacing_gate>` into `base_instructions` and `system_prompt_override` of the World, Assistant (Game Master), and Prompt Assembly.

## Common Mistakes
1. **Confusing Athletic / Team Names with Species:**
   - *Mistake:* Assuming a player on the "SUCC Bulls" is a Minotauro solely because of the team name, or vice-versa assuming a minotaur must be a werewolf because of an omonymous family name.
   - *Remedy:* Always verify the creator's canonical character definition (e.g., iorveths / SUCC-U-VERSE lore) before asserting traits.
2. **Deleting Summaries Instead of Patching:**
   - *Mistake:* Wiping the `summaries` array completely, which causes the AI to lose all high-level narrative continuity.
   - *Remedy:* Perform targeted surgical text replacements on the contaminated summary sentences while preserving timeline metadata.
3. **Using Em-Dashes in Injected Lexicon/Rules:**
   - *Mistake:* Writing `—` in generated lore or instructions, violating Repository Rule 03.
   - *Remedy:* Automatically sanitize all outgoing text with `.replace('—', ', ').replace('–', ', ')`.
