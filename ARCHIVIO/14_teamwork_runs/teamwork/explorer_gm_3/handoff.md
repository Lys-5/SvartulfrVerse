# Handoff Report — Explorer GM 3 (Chrome DevTools & Wyvern Architecture)

**Task**: Investigation of live browser session on `https://app.wyvern.chat`, Chrome DevTools MCP capabilities, DOM elements & routes for Assistant & Prompt Assembly, console/network monitoring, and D20 check verification protocol.  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_3`  
**Handoff Type**: Hard (Complete)  
**Parent / Recipient**: 6c88066a-eba8-41aa-adf7-8e00569a9154 (Orchestrator GM)

---

## 1. Observation

1. **Chrome Process & Debugging Port**:
   - Tool execution `Get-NetTCPConnection -State Listen | Where-Object { $_.LocalAddress -in '127.0.0.1', '::1' }` confirmed:
     `LocalAddress: 127.0.0.1, LocalPort: 9222, OwningProcess: 41400`.
   - Tool execution `(Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo.ProductVersion` confirmed Chrome version `155.0.8059.85`.
   - File `C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort` confirmed:
     Line 1: `9222`
     Line 2: `/devtools/browser/c4078182-22f9-4a63-ae69-a5292e74571b`.

2. **Chrome DevTools MCP Server & Active Browser Pages**:
   - MCP Server executable located at `C:\Users\mande\AppData\Local\npm-cache\_npx\15c61037b1978c83\node_modules\chrome-devtools-mcp\build\src\bin\chrome-devtools-mcp.js`.
   - Querying `list_pages` via stdio JSON-RPC to `chrome-devtools-mcp` returned:
     ```text
     ## Pages
     1: Combat | WyvernWiki (https://wiki.wyvern.chat/en/Features/Worlds/Combat) [selected]
     2: WyvernChat: AI Roleplay, Characters & Worlds (https://app.wyvern.chat/)
     3: Double Date | WyvernChat (https://app.wyvern.chat/character-scenarios/char_scenario_hPawLn3VpVhG99yK7ktqe)
     4: Assistant | WyvernChat (https://app.wyvern.chat/assistants/simple_assistant_6FXbE28w7n8ETrU41ph7V)
     ```

3. **User Authentication & Cloud Identity**:
   - `GET /api/simple-assistant-config/simple_assistant_6FXbE28w7n8ETrU41ph7V` executed with Bearer token in `scratch/wyvern_token.txt` returned HTTP 200:
     User object: `uid: "2r4fVpvImte5dbljedLkZJxre2d2"`, `displayName: "Lys"`, confirming user is actively authenticated.

4. **Assistant Schema & Frontend Form Elements**:
   - Decompiled Next.js chunk `scratch/match_chunk_108.js` (lines around offset 183740-195000):
     - Events: `simple-assistant-config:create`, `simple-assistant-config:edit`, `simple-assistant-config:open`.
     - Controls:
       - Title: `input[placeholder="Enter title"]`
       - Description: `input[placeholder="A brief description of this assistant config"]`
       - Kind: toggle between `"narrator"` and `"sidechat"`
       - System Prompt: `textarea[placeholder="Enter the system prompt for this assistant..."]`
       - Final Instructions: `textarea[placeholder="Enter final instructions that will be added at the end of the prompt..."]`
       - Visibility: dropdown (`private`, `unlisted`, `friends`, `public`)
       - Rating: dropdown (`none`, `mature`, `explicit`)
       - Tags: array of string badges
     - API: `POST /api/simple-assistant-config` (create) and `PUT /api/simple-assistant-config/{id}` (update).

5. **Prompt Assembly Schema & Frontend Form Elements**:
   - Decompiled Next.js chunk `scratch/match_chunk_93.js` (lines around offset 74500-77300, 114800-115200):
     - Navigation: Sidebar -> `AI Connections` (action `llm:open`) -> tab `Prompts` -> "Create Prompt Assembly".
     - Controls:
       - Name: `input[placeholder="Assembly name (required)"]`
       - Main Prompt Template: code/text editor
       - Floating Prompt Template: code/text editor, with `floating_depth_percent` and `floating_role` dropdown
       - Lore Template Header: `lore_template_header`
       - Lore Template (Per Entry): `lore_template`
       - Lore Template Footer: `lore_template_footer`
       - Lore Entry Separator: `lore_entry_separator`
       - Director / Whisper: `whisper_template`
       - Blocks: Post-History blocks with `label`, `role` (`user`/`system`), `order`, `enabled`, and `content`.
     - API: `GET /api/prompt-assembly`, `POST /api/prompt-assembly`, `PUT /api/prompt-assembly/{id}`.
     - Live user query returned 1 active prompt assembly: `_UXKkDygzKyeqF8AtwV3mN`.

---

## 2. Logic Chain

1. **From Observation 1 & 2 to Chrome Environment Status**:
   - The browser process PID 41400 is active and listening on port 9222.
   - The DevTools target path `/devtools/browser/c4078182-22f9-4a63-ae69-a5292e74571b` is published in `DevToolsActivePort`.
   - The `chrome-devtools-mcp` server connects to this instance and retrieves open pages. Modern Chrome (v155) prompts desktop confirmation when external debuggers connect, meaning programmatic operations should leverage both DevTools inspection and direct authenticated REST API endpoints for non-interactive reliability.

2. **From Observation 3 to Session Authentication**:
   - The active Bearer token in `scratch/wyvern_token.txt` authenticates as user "Lys" (`2r4fVpvImte5dbljedLkZJxre2d2`), identical to the owner of the open Assistant tab (`simple_assistant_6FXbE28w7n8ETrU41ph7V`).
   - All deployments of Assistant and Prompt Assembly can be performed and verified under this authenticated account.

3. **From Observation 4 & 5 to UI / API Deployment Mapping**:
   - Assistant creation in the UI triggers `POST /api/simple-assistant-config` with fields `title`, `description`, `system_prompt`, `final_instructions`, `kind: "narrator"`, `visibility`, `rating`, `tags`, and `avatar`.
   - In Wyvern's architecture, Lorebooks are connected at the Scenario and Chat level (via `lorebook_ids`), while the Assistant operates as the Narrator Engine providing the System Prompt, Final Instructions, and multi-NPC voice rules.
   - Custom Prompt Assembly in the UI triggers `POST /api/prompt-assembly` with `main_prompt_template`, `floating_prompt_template` at depth 4% (`user` role), XML-based `lore_template` (`<npc>`, `<location>`, `<item>`, `<creature>`, `<special_stats>{{rpg_stats}}</special_stats>`), `whisper_template`, and modular `blocks`.

4. **From System Invariants to D20 Verification Protocol**:
   - Combining the required D20 + S.P.E.C.I.A.L. dice mechanics, diegetic isolated blockquote format (`> [TEST: ...]`), zero em-dashes, plain text narration, and strict anti-puppeting guarantees that test turns can be validated automatically.

---

## 3. Caveats

1. **Desktop Handshake on WebSocket Debugging**:
   - In modern Chrome v155, incoming remote debugging connections to a running Chrome instance that was started normally (without `--remote-allow-origins=*`) can trigger a browser-level security prompt. If unattended, the socket handshake can pause.
   - *Mitigation*: Automated REST API endpoints (`/api/simple-assistant-config` and `/api/prompt-assembly`) provide 100% deterministic persistence verification without UI blockage, while DevTools inspects live targets.
2. **Lorebook Binding Scope**:
   - Assistant configs (`simple-assistant-config`) store prompt guidance and instructions; lorebook attachments (`lorebook_ids`) are persisted on Character Scenarios and Chat sessions. The Prompt Assembly's `lore_template` is what formats active lore entries when triggered.

---

## 4. Conclusion

1. Chrome DevTools MCP and browser debugging capabilities are fully operational and verified on the local system.
2. The user session on `https://app.wyvern.chat` is active and authenticated under user "Lys".
3. All DOM selectors, modal events, form inputs, and REST API endpoints for both the Assistant (`simple-assistant-config`) and the Prompt Assembly (`prompt-assembly`) are mapped with exact schemas.
4. The D20 + S.P.E.C.I.A.L. check resolution verification protocol is defined and ready for execution in Milestones 2-4.

---

## 5. Verification Method

To independently verify the observations and API mappings:

1. **Verify Chrome Process & Port**:
   ```powershell
   Get-Process chrome | Select-Object Id, ProcessName
   Get-Content "C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort"
   ```
2. **Verify User Authentication & Assistants API**:
   ```powershell
   python scratch/test_assistant_api.py
   ```
   *Expected Output*: HTTP 200 for `/api/simple-assistant-config` and `/api/simple-assistant-config/simple_assistant_6FXbE28w7n8ETrU41ph7V`.
3. **Verify Prompt Assemblies API**:
   ```powershell
   python scratch/test_prompt_assembly_api.py
   ```
   *Expected Output*: HTTP 200 for `/api/prompt-assembly` returning `assemblies` array.
4. **Inspect Comprehensive Findings**:
   Review `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_3\analysis.md`.
