# Technical Analysis Report: Lorebook Primary Restoration & 6 NPC Profiles

**Author**: Explorer R6-3  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3`  
**Target Milestone**: Survey & Discovery for R4 (Lorebook Primary & 6 NPC Profiles Restoration)  
**Date**: 2026-10-21  

---

## 1. Executive Summary

This investigation analyzed `FINAL/Svartulfr_NPC_Primary.json`, the live Wyvern Web API endpoint for Lorebook Primary (`_zwEqgEEzh12X6gHVmMKKC`), the 6 source character cards in `FINAL/`, and the persona anti-duplicate architecture.

### Key Discoveries:
1. **Entry Identity Key**: In `FINAL/Svartulfr_NPC_Primary.json`, individual entries are keyed by `entry_id` (not `id`). Both top-level `entries` and `lexicon` exist and are identical (`len = 99`). On the live Wyvern API, entries are returned under the key `lexicon` (`len = 99`).
2. **Current Degradation**: In `FINAL/Svartulfr_NPC_Primary.json`, the 6 target entries currently contain short stubs (761 to 1,385 characters), with `type: "lore/concept"`, missing avatars or missing regex/UI splitting metadata.
3. **Full JED+ Cards Available**: All 6 full character cards exist in `FINAL/`:
   - `Scarlett_Rose_card.json` (4,777 chars)
   - `Sierra_Cruz_card.json` (5,117 chars)
   - `Russ_card.json` (5,505 chars)
   - `Stan_Davies_Jr_card.json` (8,008 chars)
   - `Jared_Thompson_card.json` (8,696 chars)
   - `Alyssa_Douglas_Bloodmoon_card.json` (16,957 chars)
   All descriptions exceed 2,000 characters, have zero em-dashes, zero action asterisks, zero illegal macros, and conform strictly to JED+ standards.
4. **Jasper Reference Model**: Jasper Svartr Douglas Bloodmoon (`entry_id: "Vcj4h2TL4Usola2A4OOl6"`, index 60) utilizes `selective: true`, `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`, `key_logic: "AND_ANY"`, and `type: "lore/concept"`.
5. **Alyssa Persona Protection**: Alyssa (`entry_id: "alyssa_world_dossier_2b54a223"`, index 98) currently has an empty avatar (`avatar: ""`). To mirror Jasper's protection and prevent persona collision when playing as Alyssa, her record must retain `selective: true`, `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`, `key_logic: "AND_ANY"`, `type: "lore/concept"`, while updating her avatar to the valid Cloudflare asset (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public`) and injecting the full 16,957-character JED+ description.
6. **5 Other Targets as Full NPCs**: Scarlett, Sierra, Russ, Stan, and Jared must be configured with `type: "npc"`, `selective: false`, `secondary_keys: []`, multiline `avatar_activation_regex`, `lines_parsed: 1`, valid Cloudflare/Janitor avatars, structured `npc_info` blocks, and their full JED+ descriptions.

---

## 2. Inventory of Target Entries in `Svartulfr_NPC_Primary.json`

| Index | Target Name | Entry ID | Current Type | Current Content Len | Current Avatar | Target Type | Target Content Len | Target Avatar Source |
|---|---|---|---|---|---|---|---|---|
| **17** | Scarlett Rose | `4NzXF4_0hYxmN7Idltzpw` | `lore/concept` | 761 chars | `6f8b7c78...` (placeholder) | `npc` | 4,777 chars | `c8bdfad3...` (card) |
| **18** | Sierra Cruz | `ijy8vrlphNv19-p-gbYuY` | `lore/concept` | 813 chars | `6f8b7c78...` (placeholder) | `npc` | 5,117 chars | `c8bdfad3...` (card) |
| **24** | Russell 'Russ' Sinclair | `YCxAqNoShpefVvk0_Pc7i` | `lore/concept` | 1,385 chars | `None` | `npc` | 5,505 chars | `9yrobVTbiGDRLHlS6GtIz.webp` (card) |
| **41** | Stanley Davies Jr. | `ekdQjq63xP7HtNuaPQJQE` | `lore/concept` | 779 chars | `b7c9c7d1...` | `npc` | 8,008 chars | `b7c9c7d1...` (card) |
| **60** | Jasper Svartr Douglas Bloodmoon *(Ref)* | `Vcj4h2TL4Usola2A4OOl6` | `lore/concept` | 874 chars | `343ac305...` | `lore/concept` *(Protected)* | 874 chars | `343ac305...` (unchanged) |
| **62** | Jared Thompson | `RM6rcwv8MlY1XWaCTQp0M` | `lore/concept` | 793 chars | `b7476db0...` | `npc` | 8,696 chars | `b7476db0...` (card) |
| **98** | Alyssa Hvit Douglas Bloodmoon | `alyssa_world_dossier_2b54a223` | `lore/concept` | 902 chars | `""` (Empty string) | `lore/concept` *(Protected)* | 16,957 chars | `ba5a7fed...` (card) |

---

## 3. Investigation of Jasper Persona Anti-Duplicate Architecture

### 3.1 Verbatim Record of Jasper (`Vcj4h2TL4Usola2A4OOl6`)
Located at index 60 of `FINAL/Svartulfr_NPC_Primary.json`:
```json
{
  "entry_id": "Vcj4h2TL4Usola2A4OOl6",
  "keys": [
    "Jasper Douglas",
    "Jasper Svartr",
    "Jasper Douglas-Bloodmoon"
  ],
  "secondary_keys": [
    "Dossier",
    "Scheda",
    "Archivio",
    "Database",
    "Profilo"
  ],
  "regex_patterns": [],
  "content": "[NAME: Jasper Svartr Douglas Bloodmoon; ...]",
  "extensions": {},
  "enabled": true,
  "case_sensitive": false,
  "insertion_order": 10,
  "name": "Jasper Svartr Douglas Bloodmoon",
  "priority": 1,
  "comment": "",
  "constant": false,
  "position": "before_char",
  "scan_persona": false,
  "whole_words_only": true,
  "key_logic": "AND_ANY",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public",
  "type": "lore/concept",
  "selective": true
}
```

### 3.2 Architectural Analysis: Why Selective AND_ANY Prevents Duplication
1. **The Problem**: In Wyvern, when a user plays a Persona (e.g. Jasper or Alyssa), the persona prompt is injected as the player character (`{{user}}`). If the Lorebook contains an active NPC entry matching the name (`"Jasper"` or `"Alyssa"`) with `selective: false`, the lorebook entry triggers on almost every turn where the character speaks or is addressed. This causes the LLM to hallucinate a separate third-person NPC in the scene simultaneously with the player persona.
2. **The Mechanism**: By designating `type: "lore/concept"` with `selective: true`, `key_logic: "AND_ANY"`, and `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`:
   - Normal chat dialogue mentioning "Jasper" or "Alyssa" does NOT activate the lorebook entry.
   - The entry activates ONLY if an explicit technical inquiry occurs (e.g. "Dossier Jasper", "Archivio Alyssa", "Scheda Alyssa").
   - This prevents dual-instance hallucination while preserving encyclopedic lore accessibility.

---

## 4. Alyssa's Record Specification (Mirroring Jasper)

To mirror Jasper's exact anti-duplicate protection while upgrading her content to the full JED+ description and fixing the empty avatar:

### Alyssa Target Configuration (`alyssa_world_dossier_2b54a223`)
- **Index**: 98
- **Entry ID**: `"alyssa_world_dossier_2b54a223"`
- **Name**: `"Alyssa Hvit Douglas Bloodmoon"`
- **Type**: `"lore/concept"` (Preserves non-NPC status so it does not parse as a speaker slot)
- **Selective**: `true`
- **Secondary Keys**: `["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`
- **Key Logic**: `"AND_ANY"`
- **Keys**: `["Alyssa Douglas", "Alyssa Hvit", "Alyssa Douglas-Bloodmoon", "White Moon Alyssa"]`
- **Position**: `"before_char"`
- **Constant**: `false`
- **Avatar**: `"https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public"`
  *(Source: `FINAL/Alyssa_Douglas_Bloodmoon_card.json`, replacing invalid `""`)*
- **Content**: Full JED+ description from `FINAL/Alyssa_Douglas_Bloodmoon_card.json` (**16,957 characters**).

---

## 5. Specification for the 5 NPC Entries

Each of the 5 NPC entries must follow the mandatory Wyvern NPC metadata standard specified in GEMINI.md section 7:
1. `type: "npc"`
2. `selective: false`
3. `secondary_keys: []`
4. `custom_avatar_regex: true`
5. `lines_parsed: 1`
6. `avatar_activation_regex`: multiline expression matching start of line or newline, character names/aliases, followed by optional spaces and colon: `(?:^|\n)\s*(?:...)\s*:`
7. `npc_info`: structured object with `first_name`, `last_name`, `nicknames`, `titles`.
8. Full JED+ description (> 2,000 characters) extracted from source cards.

### 5.1 Scarlett Rose (`4NzXF4_0hYxmN7Idltzpw`, Index 17)
```json
{
  "entry_id": "4NzXF4_0hYxmN7Idltzpw",
  "name": "Scarlett Rose",
  "type": "npc",
  "selective": false,
  "secondary_keys": [],
  "keys": ["Scarlett Rose", "Scarlett"],
  "key_logic": "AND_ANY",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public",
  "custom_avatar_regex": true,
  "avatar_activation_regex": "(?:^|\\n)\\s*(?:Scarlett\\ Rose|Scarlett)\\s*:",
  "lines_parsed": 1,
  "npc_info": {
    "first_name": "Scarlett",
    "last_name": "Rose",
    "nicknames": ["Scarlett"],
    "titles": []
  },
  "content": "<4,777 chars from FINAL/Scarlett_Rose_card.json>"
}
```

### 5.2 Sierra Cruz (`ijy8vrlphNv19-p-gbYuY`, Index 18)
```json
{
  "entry_id": "ijy8vrlphNv19-p-gbYuY",
  "name": "Sierra Cruz",
  "type": "npc",
  "selective": false,
  "secondary_keys": [],
  "keys": ["Sierra Cruz", "Sierra"],
  "key_logic": "AND_ANY",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public",
  "custom_avatar_regex": true,
  "avatar_activation_regex": "(?:^|\\n)\\s*(?:Sierra\\ Cruz|Sierra)\\s*:",
  "lines_parsed": 1,
  "npc_info": {
    "first_name": "Sierra",
    "last_name": "Cruz",
    "nicknames": ["Sierra"],
    "titles": []
  },
  "content": "<5,117 chars from FINAL/Sierra_Cruz_card.json>"
}
```

### 5.3 Russell 'Russ' Sinclair (`YCxAqNoShpefVvk0_Pc7i`, Index 24)
```json
{
  "entry_id": "YCxAqNoShpefVvk0_Pc7i",
  "name": "Russell 'Russ' Sinclair",
  "type": "npc",
  "selective": false,
  "secondary_keys": [],
  "keys": ["Russell 'Russ' Sinclair", "Russell Sinclair", "Russ Sinclair", "Russ"],
  "key_logic": "AND_ANY",
  "avatar": "https://ella.janitorai.com/bot-avatars/9yrobVTbiGDRLHlS6GtIz.webp",
  "custom_avatar_regex": true,
  "avatar_activation_regex": "(?:^|\\n)\\s*(?:Russell\\ Sinclair|Russ\\ Sinclair|Russell\\ 'Russ'|Russell|Russ)\\s*:",
  "lines_parsed": 1,
  "npc_info": {
    "first_name": "Russell",
    "last_name": "Sinclair",
    "nicknames": ["Russ"],
    "titles": []
  },
  "content": "<5,505 chars from FINAL/Russ_card.json>"
}
```

### 5.4 Stanley Davies Jr. (`ekdQjq63xP7HtNuaPQJQE`, Index 41)
```json
{
  "entry_id": "ekdQjq63xP7HtNuaPQJQE",
  "name": "Stanley Davies Jr.",
  "type": "npc",
  "selective": false,
  "secondary_keys": [],
  "keys": ["Stanley Davies Jr.", "Stan Davies", "Stan"],
  "key_logic": "AND_ANY",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7c9c7d1-51e6-4441-82e3-c6ab5f537500/public",
  "custom_avatar_regex": true,
  "avatar_activation_regex": "(?:^|\\n)\\s*(?:Stanley\\ Davies\\ Jr\\.|Stanley\\ Davies|Stan\\ Davies|Stan)\\s*:",
  "lines_parsed": 1,
  "npc_info": {
    "first_name": "Stanley",
    "last_name": "Davies Jr.",
    "nicknames": ["Stan"],
    "titles": []
  },
  "content": "<8,008 chars from FINAL/Stan_Davies_Jr_card.json>"
}
```

### 5.5 Jared Thompson (`RM6rcwv8MlY1XWaCTQp0M`, Index 62)
```json
{
  "entry_id": "RM6rcwv8MlY1XWaCTQp0M",
  "name": "Jared Thompson",
  "type": "npc",
  "selective": false,
  "secondary_keys": [],
  "keys": ["Jared Thompson", "J-Man", "Jared"],
  "key_logic": "AND_ANY",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7476db0-8dae-4450-8c84-3408b375c000/public",
  "custom_avatar_regex": true,
  "avatar_activation_regex": "(?:^|\\n)\\s*(?:Jared\\ Thompson|J-Man|Jared)\\s*:",
  "lines_parsed": 1,
  "npc_info": {
    "first_name": "Jared",
    "last_name": "Thompson",
    "nicknames": ["J-Man", "The Golden Bull"],
    "titles": []
  },
  "content": "<8,696 chars from FINAL/Jared_Thompson_card.json>"
}
```

---

## 6. Live Wyvern API Status & Deployment Protocol

### 6.1 GET Verification
- Endpoint: `GET https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC`
- Verification Status: **HTTP 200 OK**
- Schema: Contains top-level property `lexicon` (99 items).
- Notice on Cloudflare: Requests require explicit header `'User-Agent': 'AuditorBot/1.0'` (or standard browser UA) to prevent Cloudflare error code 1010.

### 6.2 PUT Deployment Requirements for Implementation
When Worker deploys the updated lorebook:
1. Update `entries` AND `lexicon` in `FINAL/Svartulfr_NPC_Primary.json` so both arrays remain identical (99 entries).
2. Transmit `PUT https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` with JSON payload:
   ```python
   {
       "name": data.get("name"),
       "description": data.get("description"),
       "visibility": "private",
       "rating": "explicit",
       "scan_depth": data.get("scan_depth", 5),
       "token_budget": data.get("token_budget", 5000),
       "recursive_scanning": data.get("recursive_scanning", True),
       "lexicon": entries
   }
   ```
3. Verify HTTP 200 return code and confirm that all 99 entries persist in `lexicon`.
