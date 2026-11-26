# Comprehensive Investigation Report: Chrome DevTools Session, Wyvern DOM & API Architecture, and D20 Check Verification Protocol

**Author**: Explorer GM 3 (Chrome DevTools Session Explorer)  
**Date**: 2026-10-20T17:38:00Z  
**Target Environment**: `https://app.wyvern.chat` & Local Chrome DevTools Instance  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_3`  
**Reference Directives**: `ORIGINAL_REQUEST.md` (§ Follow-up 2026-10-20T17:19:55Z), `PROJECT.md` (orchestrator_3), `GEMINI.md`

---

## Executive Summary

This investigation analyzed the live browser session on `https://app.wyvern.chat`, inspected the Chrome DevTools debugging capabilities, decompiled the relevant Next.js frontend bundles for Assistant (`simple-assistant-config`) and Prompt Assembly (`prompt-assembly`), mapped the exact DOM selectors and API persistence mechanisms, and formulated the end-to-end verification protocol for the live D20 + S.P.E.C.I.A.L. check resolution engine.

Key discoveries:
1. **Live Browser Environment**: Chrome process PID 41400 is running on Windows with `DevToolsActivePort` listening on `127.0.0.1:9222`. Active tabs in the live session were queried directly via DevTools:
   - Page 1: `Combat | WyvernWiki (https://wiki.wyvern.chat/en/Features/Worlds/Combat)`
   - Page 2: `WyvernChat: AI Roleplay, Characters & Worlds (https://app.wyvern.chat/)`
   - Page 3: `Double Date | WyvernChat (https://app.wyvern.chat/character-scenarios/char_scenario_hPawLn3VpVhG99yK7ktqe)`
   - Page 4: `Assistant | WyvernChat (https://app.wyvern.chat/assistants/simple_assistant_6FXbE28w7n8ETrU41ph7V)`
2. **User Authentication**: Authenticated as user **Lys** (`uid: "2r4fVpvImte5dbljedLkZJxre2d2"`), verified via `scratch/wyvern_token.txt` with live HTTP 200 API responses.
3. **Assistant Architecture (`simple-assistant-config`)**:
   - Backend API: `POST /api/simple-assistant-config` (create), `PUT /api/simple-assistant-config/{id}` (update), `GET /api/simple-assistant-config/{id}` (fetch).
   - Route: `/mine?tab=assistants` and `/assistants/{id}`.
   - Core Fields: `title`, `description`, `system_prompt`, `final_instructions`, `avatar`, `rating` (`none`/`mature`/`explicit`), `visibility` (`private`/`unlisted`/`friends`/`public`), `tags` (array), `kind` (`narrator` vs `sidechat`).
4. **Prompt Assembly Architecture (`prompt-assembly`)**:
   - Backend API: `POST /api/prompt-assembly` (create), `PUT /api/prompt-assembly/{id}` (update), `GET /api/prompt-assembly` (list), `GET /api/prompt-assembly/{id}` (fetch).
   - UI Access: `AI Connections` (sidebar `llm:open`) -> `Prompts` -> "Create Prompt Assembly" / "Edit Prompt Assembly".
   - Core Schema: `name`, `main_prompt_template`, `main_prompt_sections`, `floating_prompt_template`, `floating_depth_percent` (4), `floating_role` (`user`), `lore_template_header`, `lore_template`, `lore_template_footer`, `lore_entry_separator`, `whisper_template`, `blocks` (Final Instructions blocks array with `label`, `role`, `order`, `enabled`, `content`).
5. **D20 + S.P.E.C.I.A.L. Resolution Protocol**: Defined diegetic check output format `> [TEST: ...]` and testing methodology.

---

## 1. Chrome DevTools Environment & Process Status

### 1.1 Process & Network Port Analysis
- **Process**: Google Chrome v155.0.8059.85 (`chrome.exe`, main browser PID 41400).
- **Listening Port**: `127.0.0.1:9222`.
- **DevToolsActivePort**: `C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort`
  - Port: `9222`
  - Browser WebSocket Target Path: `/devtools/browser/c4078182-22f9-4a63-ae69-a5292e74571b`
- **MCP Server Binary**: Installed and verified at:
  `C:\Users\mande\AppData\Local\npm-cache\_npx\15c61037b1978c83\node_modules\chrome-devtools-mcp\build\src\bin\chrome-devtools-mcp.js` (v1.11.0).
- **MCP Client Capabilities**: `chrome-devtools-mcp` connects via stdio JSON-RPC. Direct query via `list_pages` enumerated the user's active browser tabs:
  1. `Combat | WyvernWiki` (`https://wiki.wyvern.chat/en/Features/Worlds/Combat`)
  2. `WyvernChat: AI Roleplay, Characters & Worlds` (`https://app.wyvern.chat/`)
  3. `Double Date | WyvernChat` (`https://app.wyvern.chat/character-scenarios/char_scenario_hPawLn3VpVhG99yK7ktqe`)
  4. `Assistant | WyvernChat` (`https://app.wyvern.chat/assistants/simple_assistant_6FXbE28w7n8ETrU41ph7V`)

### 1.2 Handshake & Security Invariant
In modern Chrome (v144+ / v155), Chrome security prompts a desktop approval dialog when an external WebSocket client initiates debugging unless Chrome was explicitly started with `--remote-debugging-port=9222 --remote-allow-origins=*`. If an external socket disconnects abruptly, Chrome holds the session. Therefore, programmatic verification must support both DevTools socket inspection and direct authenticated REST API verification (`GET /api/simple-assistant-config/{id}` and `GET /api/prompt-assembly/{id}`).

---

## 2. Wyvern Chat Navigation, DOM Selectors & UI Architecture

### 2.1 User Session & Authentication Status
- **Authentication**: User is fully logged in as **Lys** (`uid: "2r4fVpvImte5dbljedLkZJxre2d2"`).
- **Profile Data**:
  - `displayName`: "Lys"
  - `photoURL`: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bd18ce0c-6994-4729-845d-1fb1e759f900/public`
- **Token Validity**: Bearer token in `scratch/wyvern_token.txt` is active, verified with live HTTP 200 responses across `/api/simple-assistant-config`, `/api/prompt-assembly`, `/api/character-scenarios`, and `/api/lorebooks`.

---

### 2.2 Svartúlfr Assistant (`/mine > ASSISTANT` / `simple-assistant-config`)

#### UI Route & Access
- Navigation: Header / Sidebar -> `/mine` (`My Creations & Bookmarks`) -> Tab `Assistants` (`/mine?tab=assistants`).
- Direct entity URL: `https://app.wyvern.chat/assistants/{id}`.
- Event Trigger:
  - Create: `emit("simple-assistant-config:create", { kind: "narrator" })`
  - Edit: `emit("simple-assistant-config:edit", assistant_id)`
  - Browse/List: `emit("simple-assistant-config:open", { kind: "narrator" })`

#### Modal & DOM Selectors
Extracted directly from Next.js bundle `scratch/match_chunk_108.js`:
| Field / Control | DOM Selector / Element | Placeholder / Label | Payload Key |
|---|---|---|---|
| Dialog Container | `div[role="dialog"]` | "Create Assistant" / "Edit Assistant" | - |
| Title Input | `input` | `placeholder="Enter title"` | `title` |
| Description Input | `input` / `textarea` | `placeholder="A brief description of this assistant config"` | `description` |
| Kind Toggle | `button` / radio group | "Assistant" (`sidechat`) / "Narrator" (`narrator`) | `kind` |
| System Prompt | `textarea` | `placeholder="Enter the system prompt for this assistant..."` | `system_prompt` |
| Final Instructions | `textarea` | `placeholder="Enter final instructions that will be added at the end of the prompt..."` | `final_instructions` |
| Avatar Input | Image upload / file input | "Upload avatar" / `avatar` | `avatar` |
| Visibility Select | `select` / dropdown | "Private", "Draft" (`unlisted`), "Friends", "Public" | `visibility` |
| Rating Select | `select` / dropdown | "None (SFW)", "Mature", "Explicit" | `rating` |
| Tags Input | Tag input component | Tags array | `tags` |
| Submit Button | `button[type="submit"]` | "Save" / "Create" | Triggers API |

#### API Request & Response
- **Endpoint**: `POST https://app.wyvern.chat/api/simple-assistant-config` (create) or `PUT https://app.wyvern.chat/api/simple-assistant-config/{id}` (update).
- **Headers**: `Authorization: Bearer <token>`, `Content-Type: application/json`.
- **Payload Schema**:
```json
{
  "title": "Svartúlfr — Game Master & World Engine",
  "description": "Official AI Game Master and World Engine for the Svartúlfr Verse. Integrates D20 + S.P.E.C.I.A.L. checks, multi-NPC dialogue, anti-puppeting, and canon lorebook reasoning.",
  "system_prompt": "...",
  "final_instructions": "...",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
  "kind": "narrator",
  "visibility": "private",
  "rating": "none",
  "tags": ["svartulfr", "game-master", "ttrpg", "special-checks", "narrator"]
}
```
- **Response**: HTTP 200 OK with created assistant object containing `id: "simple_assistant_..."`.

---

### 2.3 Custom TTRPG Prompt Assembly (`AI Connections > Prompts`)

#### UI Route & Access
- Navigation: Left Sidebar -> "AI Connections" (action `llm:open`) -> Tab "Prompts" -> "Link Prompt Assembly".
- Dialog Title: `create === W.kind ? "Create Prompt Assembly" : "Edit Prompt Assembly"`.

#### Modal & DOM Selectors
Extracted directly from Next.js bundle `scratch/match_chunk_93.js`:
| Section / Template | DOM Selector / Control | UI Label / Placeholder | Payload Key |
|---|---|---|---|
| Name Input | `input` | `placeholder="Assembly name (required)"` | `name` |
| Visibility | Dropdown / Select | "Private", "Draft" (`unlisted`), "Friends", "Public" | `visibility` |
| Rating | Dropdown / Select | "None", "Mature", "Explicit" | `rating` |
| Main Prompt Template | Code editor / Textarea | "Main Prompt Template" | `main_prompt_template` |
| Main Sections | Section items list | "Main Prompt Sections" | `main_prompt_sections` |
| Floating Prompt Template | Code editor / Textarea | "Floating Prompt Template" | `floating_prompt_template` |
| Floating Depth | Number input | Depth % (e.g. `4`) | `floating_depth_percent` |
| Floating Role | Dropdown (`user` / `system`) | Role for floating prompt | `floating_role` |
| Lore Template Header | Text input | "Lore Template Header" | `lore_template_header` |
| Lore Template (Per Entry) | Code editor / Textarea | "Lore Template (Per Entry)" | `lore_template` |
| Lore Template Footer | Text input | "Lore Template Footer" | `lore_template_footer` |
| Lore Entry Separator | Text input | "Lore Entry Separator" | `lore_entry_separator` |
| Whisper Template | Textarea | "Director" / "Whisper Template" | `whisper_template` |
| Final Instructions Blocks | Dynamic Block List | Block Title, Role, Enabled toggle, Content | `blocks` |
| Save Button | `button` | "Save" / "Create" | Triggers API |

#### API Request & Response
- **List Existing Assemblies**: `GET https://app.wyvern.chat/api/prompt-assembly`
  - Already verified: Returns current user assemblies (User has 1 assembly `_UXKkDygzKyeqF8AtwV3mN`).
- **Create Assembly**: `POST https://app.wyvern.chat/api/prompt-assembly`
- **Update Assembly**: `PUT https://app.wyvern.chat/api/prompt-assembly/{id}`
- **Get Assembly**: `GET https://app.wyvern.chat/api/prompt-assembly/{id}`
- **Payload Schema**:
```json
{
  "name": "Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)",
  "description": "Master TTRPG Prompt Assembly for Svartúlfr Verse. Integrates S.P.E.C.I.A.L. XML stats, isolated D20 skill check engine, Italian Sandwich language enforcement, floating anti-drift directives at depth 4%, and modular final instruction blocks.",
  "main_prompt_template": "...",
  "main_prompt_sections": [
    {
      "id": "main_prompt",
      "name": "Main Prompt",
      "content": "...",
      "enabled": true,
      "role": "system",
      "order": 0,
      "marker": null
    }
  ],
  "floating_prompt_template": "<active_directives priority=\"high\">\n{{#if characterNote}}\n<character_note>\n{{characterNote}}\n</character_note>\n{{/if}}\n{{#if authorNote}}\n<author_note>\n{{authorNote}}\n</author_note>\n{{/if}}\n{{#if summary}}\n<recent_summary>\n{{summary}}\n</recent_summary>\n{{/if}}\n</active_directives>",
  "floating_depth_percent": 4,
  "floating_role": "user",
  "floating_prompt_sections": [],
  "lore_template_header": "<world_context position=\"{{position}}\" count=\"{{count}}\">",
  "lore_template": "{{#if (eq type \"npc\")}}\n<npc name=\"{{name}}\"{{#if labels}} labels=\"{{labels}}\"{{/if}}>\n{{content}}\n{{#if npc_info}}\n{{npc_info}}\n{{/if}}\n{{#if rpg_stats}}\n<special_stats>{{rpg_stats}}</special_stats>\n{{/if}}\n</npc>\n{{else}}{{#if (eq type \"location\")}}\n<location name=\"{{name}}\">\n{{content}}\n</location>\n{{else}}{{#if (eq type \"item\")}}\n<item name=\"{{name}}\">\n{{content}}\n{{#if item_config}}{{item_config}}{{/if}}\n</item>\n{{else}}{{#if (eq type \"creature\")}}\n<creature name=\"{{name}}\"{{#if labels}} labels=\"{{labels}}\"{{/if}}>\n{{content}}\n{{#if creature_config}}{{creature_config}}{{/if}}\n{{#if rpg_stats}}\n<special_stats>{{rpg_stats}}</special_stats>\n{{/if}}\n</creature>\n{{else}}\n<lore_entry name=\"{{name}}\"{{#if type}} type=\"{{type}}\"{{/if}}>\n{{content}}\n</lore_entry>\n{{/if}}{{/if}}{{/if}}{{/if}}",
  "lore_template_footer": "</world_context>",
  "lore_entry_separator": "\n\n",
  "whisper_template": "<director_whisper>\n(OOC Director Instructions to guide AI narrative output: {{whisper}})\n</director_whisper>",
  "blocks": [
    {
      "block_id": "block_format_discipline",
      "label": "Format Discipline & Language Sandwich",
      "content": "...",
      "enabled": true,
      "order": 0,
      "role": "user"
    },
    {
      "block_id": "block_d20_resolution",
      "label": "D20 + S.P.E.C.I.A.L. Resolution Engine",
      "content": "...",
      "enabled": true,
      "order": 1,
      "role": "user"
    },
    {
      "block_id": "block_anti_puppeting",
      "label": "Strict Anti-Puppeting of User",
      "content": "...",
      "enabled": true,
      "order": 2,
      "role": "user"
    },
    {
      "block_id": "block_digital_feeds",
      "label": "Situational Digital Feeds",
      "content": "...",
      "enabled": true,
      "order": 3,
      "role": "user"
    }
  ],
  "visibility": "private",
  "rating": "none",
  "join_final_instructions": false,
  "start_reply_with": "",
  "show_reply_prefix": false
}
```

---

## 3. Console & Network Monitoring Verification Strategy

### 3.1 Network Monitoring Protocol
When testing or deploying:
1. Issue the HTTP `POST` or `PUT` request with Bearer authorization.
2. Verify HTTP Status code == `200` (or `201`).
3. Capture the returned entity ID (`simple_assistant_...` or `pha_...`).
4. Re-query via `GET /api/simple-assistant-config/{id}` or `GET /api/prompt-assembly/{id}` to verify database retention, schema fidelity, and field integrity.

### 3.2 Console Error Detection
1. Using Chrome DevTools MCP: `list_console_messages` with `types: ["error", "warn"]`.
2. Inspect for React hydration errors, Next.js chunk loading errors, or syntax errors.
3. Zero fatal console exceptions permitted.

---

## 4. Live D20 + S.P.E.C.I.A.L. Check Resolution Verification Protocol

### 4.1 System Invariants
- **Diegetic Tag Format**:
  Must be isolated on its own line in blockquote format:
  ```text
  > [TEST: Stat | Target DC: XX | Roll: d20(X) + Mod(Y) = Total | Outcome: SUCCESS/FAILURE]
  ```
- **Stats Covered**: S.P.E.C.I.A.L. mapped from canonical attributes:
  - `STR` (Strength / MGT)
  - `PER` (Perception / SCT - Scrutiny)
  - `END` (Endurance / RES)
  - `CHA` (Charisma / PRS)
  - `INT` (Intelligence / WIT)
  - `AGI` (Agility / AGI)
  - `LCK` (Luck / SCT resonance)
- **Formatting Discipline**:
  - Dialogue strictly in standard quotes (`"..."`).
  - Actions and narration in plain text (zero asterisks for narration).
  - Asterisks (`*...*`) strictly reserved for internal thoughts.
  - Zero em-dashes (`—`); use commas or periods.
  - Strict anti-puppeting of `{{user}}`: The model must NEVER write thoughts, speech, or involuntary actions for `{{user}}`.
  - Multi-NPC dialogue format: Each speaking character must be formatted with `Nome: "..."` on its own line.
  - Language: Italian Sandwich enforcement: instructions in system prompt / blocks, final narrative prose rendered strictly in Italian.

### 4.2 Test Scenario & Prompt Harness
To verify the live resolution turn:
1. **User Prompt Input**:
   ```text
   Tento di forzare il terminale di sicurezza della DCC per estrarre i log della spedizione nel Voidspace prima che arrivi la ronda degli enforcer.
   ```
2. **Expected GM Response Structure**:
   - Diegetic check calculation:
     ```text
     > [TEST: INT | Target DC: 14 | Roll: d20(11) + INT(4) = 15 | Outcome: SUCCESS]
     ```
   - Narrative resolution in Italian reflecting the check outcome:
     Jasper o l'Assistente descrive il bypass dei firewall, lo scorrimento dei log verdi sul display, e la tensione della ronda senza mai muovere o far parlare `{{user}}`.
   - Clear ending beat leaving initiative to `{{user}}`.

---

## 5. Artifact Index
- `scratch/wyvern_token.txt` — Live Bearer authentication token
- `scratch/pages_list.txt` — Active Chrome DevTools pages snapshot
- `scratch/assistant_modal_form_extracted.js` — Extracted Assistant modal component
- `scratch/prompt_assembly_ui_slice.js` — Extracted Prompt Assembly UI component
- `scratch/assembly_details_dump.txt` — Full prompt assembly reference schemas
- `scratch/test_assistant_api.py` — Assistant API verification test
- `scratch/test_prompt_assembly_api.py` — Prompt Assembly API verification test
- `scratch/test_direct_call.js` — Chrome DevTools MCP connection test script
