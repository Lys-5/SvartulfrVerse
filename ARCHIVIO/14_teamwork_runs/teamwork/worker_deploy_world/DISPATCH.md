## 2026-10-24T22:35:32Z
You are a Worker implementing the deployment of the new Svartúlfr Lightweight World on Wyvern Web API.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\worker_deploy_world\
Your original request is at: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
The orchestrator dispatch instructions are at: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_9\DISPATCH.md
The synthesized specification is at: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_9\SPECIFICATION.md
Detailed technical reports to consult:
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_api\handoff.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_locations\handoff.md
- e:\repository\SvartulfrVerse\.agents\teamwork\spec_miner_m1_simulation\handoff.md

Domain skills available:
- e:\repository\SvartulfrVerse\.agents\skills\wyvern-ttrpg-master-deployer\SKILL.md
- e:\repository\SvartulfrVerse\.agents\skills\wyvern-card-lorebook-sync\SKILL.md

Exclusive write ownership:
- scripts/deploy_new_world.py
- scratch/world_new_deployed.json
- scratch/verify_deployed_world.py
- e:\repository\SvartulfrVerse\.agents\teamwork\worker_deploy_world\*

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Core Tasks:
1. Token & API Setup:
   - Refresh token using `python scratch/refresh_token.py`.
   - Read token from `scratch/wyvern_token.txt`.
   - Always include header `'User-Agent': 'Mozilla/5.0'` to avoid Cloudflare 1010 blocks.
2. Build `scripts/deploy_new_world.py`:
   - R1 (World Core): Create the new World via `POST https://app.wyvern.chat/api/worlds` with name "Svartúlfr — Blackwood & Solarton", visibility "private", rating "explicit", tags. Capture the generated `world_id`.
   - R2 (Simulation Engine & Prompts): Update the world via `PUT https://app.wyvern.chat/api/worlds/{id}`:
     * `world_age: 10489902` (Mon Aug 26, 2024, 06:00:00 UTC)
     * Gregorian calendar from epoch `0827-12-21T00:00:00.000Z`
     * Prompt Assembly: `assistant_id: "simple_assistant_xRfBnV7wq48QppqbPPpTM"`, `prompt_assembly_id: "pha_kWkWUAfTJTF9q72c2bC98"`, system prompt override, base instructions, final instructions with format discipline (dialogue in quotes, actions in plain text, thoughts in asterisks, no em-dash, Italian sandwich), `disable_enhanced_instructions: true`.
     * Simulation: `stat_config` with 6 JED+ attributes (MGT, RES, AGI, WIT, PRS, SCT; base 1, budget 25), `combat_ruleset` (`narrative_tiers`), currencies (`$`, `Cr`), `relationship_config` (10 moodlets, 14 tiers), anti-bloat flags (`show_party_stats: false`, `show_species_info: false`, `ships: false`, `creature_catcher: false`), and `linked_characters` (8 active cards from `/characters/mine`).
   - R3 (7 Environments & 188 Locations):
     * Create the 7 canonical Environments via `POST /api/worlds/environments`:
       1. California Coast (Root)
       2. SUCC campus (Parent: California Coast)
       3. Solarton (Parent: California Coast)
       4. Blackwood (Parent: California Coast)
       5. Seven Hills (Parent: Blackwood)
       6. DMHA HQ & Guild District (Parent: California Coast)
       7. Voidspace/Otherworld (Parent: California Coast)
       Store environment ID map.
     * Ingest all 188 canonical Locations via `POST /api/worlds/locations`:
       Source data from `exports/Svartulfr_Export.json` or `scratch/backup_consolidated_snapshot/world_locations.json` (excluding the 8 deprecated Digitalis entries).
       Map parent-child hierarchy properly (roots first, then depth 1, 2, 3, 4) updating parent IDs to new IDs as created, and setting appropriate environment IDs.
       Ensure 'The Verve' at 808 Neon Ave (`_hfm1W4nYnXfQEqcNGwNxr`) is wired as secret bar behind Logan's Custom Garage with its 3 item lexicon IDs.
       Include ambient text and included_lexicon_entries.
   - R4 (Mirrored Lexicon):
     * Bulk create or ingest lexicon entries into the World with anti-bloat flags (`selective: true`, `secondary_keys`, `ignored_characters`, `ignored_personas`, `scan_persona: true`, `whole_words_only: true`, `enableEntryHighlighting: true`). Ensure frontend Zod parity (`entries == lexicon`).
   - Save complete snapshot of deployed world to `scratch/world_new_deployed.json`.
3. Build and execute `scratch/verify_deployed_world.py`:
   - Issue GET requests on `/api/worlds/{id}`, `/api/worlds/environments/world/{id}`, `/api/worlds/locations/world/{id}`, `/api/worlds/lexicon/world/{id}`.
   - Confirm HTTP 200 on all, verify 7 environments, 188 locations, 0 orphans, correct world age and simulation features.
4. Document all results, world ID, verification outputs, and API logs in:
   `e:\repository\SvartulfrVerse\.agents\teamwork\worker_deploy_world\handoff.md`

Update progress.md in your directory as you execute.
Send a completion message via send_message when done.
