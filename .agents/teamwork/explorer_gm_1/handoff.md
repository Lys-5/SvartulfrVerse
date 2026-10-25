# Handoff Report — Explorer GM 1 (Assistant Architecture & Wyvern API)

## 1. Observation
1. **Wyvern API Endpoints Tested:**
   - Command `inspect_endpoints.py` tested standard assistant paths:
     - `GET https://app.wyvern.chat/api/assistants` -> HTTP 404 (`{"message":"Route GET:/assistants not found","error":"Not Found","statusCode":404}`).
     - `GET https://app.wyvern.chat/api/mine/assistants` -> HTTP 404.
     - `GET https://app.wyvern.chat/api/characters?type=assistant` -> HTTP 404.
     - `GET https://app.wyvern.chat/api/characters/mine` -> HTTP 200, but inspection revealed no assistant records.
2. **Authoritative API Endpoint & Internal Entity Model:**
   - Next.js frontend chunk `/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js` (lines 157392–158000) revealed module `91650`:
     `create: e => r.hi.post("".concat(s.BC,"/simple-assistant-config"), e)`
     `update: (e, t) => r.hi.put("".concat(s.BC,"/simple-assistant-config/").concat(e), t)`
     `getNarratorPresets: () => r.hi.get("".concat(s.BC,"/simple-assistant-config/narrator-presets")).then(e=>e.presets)`
   - Command `test_post_validation.py` executed `POST https://app.wyvern.chat/api/simple-assistant-config` with `{}` and received HTTP 500 containing the raw backend MikroORM entity validation dump:
     ```text
     Value for SimpleAssistantConfig.title is required, 'undefined' found
     entity: SimpleAssistantConfig {
       created_at: ISODate('2026-10-20T17:35:56.828Z'),
       updated_at: ISODate('2026-10-20T17:35:56.828Z'),
       _id: 'simple_assistant_Cxz6xA2b8DPHfKh8BGBq7',
       kind: 'sidechat',
       visibility: 'private',
       rating: 'none',
       status: 'approved',
       tags: [],
       approval_date: null,
       rejection_date: null,
       approval_comment: null,
       rejection_comment: null,
       forked_from: null,
       title: undefined,
       description: undefined,
       system_prompt: undefined,
       final_instructions: undefined,
       avatar: undefined,
       user: UserInfo { ... }
     }
     ```
3. **Frontend Form & Creation Workflow:**
   - Chunk `/_next/static/chunks/54866-5b1f01a517163780.js` (pos 183875) confirmed:
     `Y = () => ({ title: "", description: "", system_prompt: "", final_instructions: "", avatar: "", visibility: "private", rating: "none", tags: [] })`
     `kind`: `"narrator"` (for Narrator / Game Master) or `"sidechat"` (for side assistant).
4. **Narrator Presets:**
   - `GET https://app.wyvern.chat/api/simple-assistant-config/narrator-presets` returned 4 built-in presets: `preset:storyteller`, `preset:screenwriter`, `preset:game-master`, `preset:erotica-writer`.
   - The `preset:game-master` preset explicitly embeds player agency, thought privacy, and multi-NPC voice discipline (`Name: "..."`).
5. **Lorebook Attachments Architecture:**
   - The MikroORM schema for `SimpleAssistantConfig` contains no `lorebook_ids` field.
   - Lorebook binding is decoupled: Character Scenarios bind lorebooks via `lorebook_ids: [...]`, Standalone Characters bind lorebooks via `lorebooks: [...]`, and Chat sessions attach lorebooks dynamically.
6. **Existing Payloads in Repository:**
   - Search across `FINAL/`, `scratch/`, `scripts/`, `ARCHIVIO/` confirmed zero assistant JSON payloads or scripts currently exist in the repository.

## 2. Logic Chain
1. *From Observation 1 & 2:* Since generic assistant endpoints return 404, and module `91650` calls `/simple-assistant-config`, the only valid REST endpoint for standalone assistants on Wyvern is `https://app.wyvern.chat/api/simple-assistant-config`.
2. *From Observation 2 & 3:* The backend entity model and frontend form definitions prove that an assistant payload requires `title` (string), `description` (string), `system_prompt` (string), `final_instructions` (string), `avatar` (URL), `kind` (`"narrator"`), `visibility` (`"private"`), `rating` (`"explicit"`), and `tags` (string array).
3. *From Observation 4 & Repository Rules (`GEMINI.md`, `CanonDecisions.md`):* The Assistant must be created with `kind: "narrator"` to act as the full Game Master / Narrator in Wyvern chat, incorporating the D20 + S.P.E.C.I.A.L. engine (`STR, PER, END, CHA, INT, AGI, LCK`), the isolated diegetic test block `> [TEST: ...]`, and the Italian Sandwich formatting invariants.
4. *From Observation 5:* Since `SimpleAssistantConfig` does not store `lorebook_ids`, lorebooks are maintained at the scenario/character/session layer. The 6 Svartúlfr Lorebooks (`_gwwCxCfQ6PQaLEjAQVpJL`, `_HfG7TeV6MJyj6bxMwxkpt`, `_9zWTGqYJNJ4BCDMj8gfcD`, `_EjXxkmPVhpCXg8xABpFkK`, `_zwEqgEEzh12X6gHVmMKKC`, `_Uht3Ckz44JBDrPnUHq7LV`) are linked through the deployed Character Scenarios and user chat settings, activated by the custom Prompt Assembly's XML templates (`<npc>`, `<location>`, `<item>`, `<lore_entry>`, `<special_stats>`).
5. *From Observation 6:* A new payload file `FINAL/assistants/Svartulfr_Game_Master_Assistant.json` and deployment script must be created in Milestone 2.

## 3. Caveats
- While `SimpleAssistantConfig` accepts custom tags, tags do not affect prompt injection mechanics; they only serve UI search/filtering in `/mine > ASSISTANT`.
- Creating the assistant via API with `visibility: "private"` makes it immediately usable in the creator's chat sessions without waiting for public community moderation approval.

## 4. Conclusion
Standalone Assistants on Wyvern are `SimpleAssistantConfig` entities managed via `https://app.wyvern.chat/api/simple-assistant-config`. To deploy "Svartúlfr — Game Master & World Engine", the implementer in Milestone 2 must:
1. Issue a `POST https://app.wyvern.chat/api/simple-assistant-config` request with `kind: "narrator"`, `visibility: "private"`, `rating: "explicit"`, and the complete system prompt and final instructions.
2. The payload schema is fully mapped and documented in `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_1\analysis.md`.
3. The 6 Lorebooks are tied via Character Scenarios and the Prompt Assembly XML templates rather than a field on the assistant table.

## 5. Verification Method
1. **API Endpoint Verification:**
   Run:
   `python -c "import urllib.request, json, pathlib; t = pathlib.Path('scratch/wyvern_token.txt').read_text().strip(); req = urllib.request.Request('https://app.wyvern.chat/api/simple-assistant-config', headers={'Authorization': 'Bearer ' + t, 'User-Agent': 'Mozilla/5.0'}); print(urllib.request.urlopen(req).status)"`
   Expected Result: HTTP 200 OK.
2. **Narrator Preset Inspection:**
   Run `python e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_1\print_gm_preset.py` to inspect the official `preset:game-master` prompt structure.
3. **Inspect Comprehensive Findings:**
   Inspect `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_1\analysis.md`.
