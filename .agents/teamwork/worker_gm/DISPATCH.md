# DISPATCH — Worker GM (Implementation & Deployment)
Role: teamwork_preview_worker
Target: Assemble and deploy Svartúlfr Game Master Assistant and Master TTRPG Prompt Assembly on Wyvern Chat Web API.

## 2026-10-20T17:41:34Z
Sender: 6c88066a-eba8-41aa-adf7-8e00569a9154
Priority: MESSAGE_PRIORITY_HIGH
Content:
You are Worker GM (Implementation & Deployment Specialist).
Working Directory: e:\repository\SvartulfrVerse\.agents\teamwork\worker_gm
Authoritative Request: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (section "## Follow-up — 2026-10-20T17:19:55Z").
Project Scope: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_3\PROJECT.md.
Explorer Handoffs:
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_1\handoff.md (and analysis.md)
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_2\handoff.md (and analysis.md)
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_3\handoff.md (and analysis.md)

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

EXCLUSIVE WRITE OWNERSHIP:
You own and may create/modify:
- FINAL/assistants/Svartulfr_Game_Master_Assistant.json
- FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json
- scratch/deploy_gm_assistant.py
- scratch/deploy_prompt_assembly.py
- CHANGELOG.md

OBJECTIVES:
1. Construct and Deploy Assistant:
   - Assemble `FINAL/assistants/Svartulfr_Game_Master_Assistant.json` for "Svartúlfr — Game Master & World Engine":
     - Title: "Svartúlfr — Game Master & World Engine"
     - Description: "Official AI Game Master & World Engine for Svartúlfr Verse with D20 + S.P.E.C.I.A.L. dice mechanics and immersive narrative direction."
     - Kind: "narrator"
     - Visibility: "private"
     - Rating: "explicit"
     - Avatar: "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"
     - Tags: ["svartulfr", "game-master", "world-engine", "special", "d20", "ttrpg"]
     - System prompt & Final instructions: Adhering strictly to Svartúlfr canon rules (Italian Sandwich language enforcement, third-person present tense, anti-puppeting of {{user}}, thought privacy, multi-NPC dialogue format Nome: "..."). Zero em-dashes ('—')!
     - D20 + S.P.E.C.I.A.L. resolution format: Isolated diegetic block `> [TEST: ...]`.
   - Deploy payload via `POST https://app.wyvern.chat/api/simple-assistant-config` using Bearer token from `scratch/wyvern_token.txt`.
   - Verify HTTP 200/201 and record returned assistant id.

2. Construct and Deploy Custom Prompt Assembly:
   - Assemble `FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json` for "Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)":
     - Follow the complete validated schema extracted by Explorer GM 2 (in `explorer_gm_2\analysis.md` section 8).
     - Main Prompt Template with standard Handlebars macros.
     - Lore Templates formatted with XML `<npc>`, `<location>`, `<item>`, `<lore_entry>` and `<special_stats>{{rpg_stats}}</special_stats>`.
     - Floating Prompt Template injected at Depth 4% (`floating_depth_percent: 4`) with HTTP role `User` (`floating_role: "user"`) containing active anti-drift directives.
     - Director's Whisper template configured for OOC instructions.
     - Final Instructions post-history with HTTP role `User` enforcing formatting, situational digital feeds (`【 LIVE FEED 】`, `❤️Pack-Family❤️`), and strict Italian output. Zero em-dashes ('—')!
   - Deploy payload via `POST https://app.wyvern.chat/api/prompt-assembly` using Bearer token.
   - Verify HTTP 200/201 and record returned prompt assembly `pha_...` id.

3. Update CHANGELOG.md:
   - Document both new deployments, their generated IDs, schemas, and verification results.

4. Produce Handoff Report:
   - Write comprehensive report to `e:\repository\SvartulfrVerse\.agents\teamwork\worker_gm\handoff.md` with Observation, Logic Chain, Caveats, Conclusion, and Verification Method.
   - Send completion message to parent orchestrator via `send_message`.
