# Dispatch for Explorer Scenarios 2
Role: Character & Roster Explorer (Camp Mystic, SUCC Routes, Villa Douglas)
Working Directory: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_2

## 2026-10-20T17:09:53Z
From: 6f2f7fce-1035-4880-af5b-6087c18617c4 (orchestrator_2)
Message:
You are Explorer 2 (Character Roster & Lore Explorer) for the Svartúlfr Verse character scenarios milestone.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_2

MANDATORY FIRST STEP: Read the authoritative requirements in:
e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (specifically the latest Follow-up — 2026-10-20T17:04:21Z).
Also consult e:\repository\SvartulfrVerse\GEMINI.md and .agents/rules/ for canonical rules.

Tasks to investigate:
1. Map character IDs, card paths, and canonical data across the repository for:
   - Scenario 1: `Svartulfr_Scenario_Camp_Mystic.json`:
     * 8 slots: twin (Jasper/Alyssa), cousin (Edric 13yo), supervisor (Marcus Vale / Celeste Nadir), director (Mara Voss), cabin_mate_1, cabin_mate_2, camper_peer_1, camper_peer_2.
     * Find card IDs or references for Marcus Vale, Celeste Nadir, Mara Voss, Edric, and peers.
     * Find Lake Erie shuttle arrival details from `_L3143TCBCzH7QPwUVKE6p` or local cards/lore.
     * Identify Lua startup_script logic for dynamically adjusting supervisor and cabin mates based on persona gender/name.
   - Scenario 2: `Svartulfr_Scenario_SUCC_Route_Alyssa.json`:
     * 8 slots: twin (Jasper), best_friend (Scarlett Rose), crush (Mackenzie "Mac" Sanchez-Rogers), roommate (Sierra Cruz), childhood_friend (Finnegan Novak, confirm Arctic Wolf demi-human), quarterback (Jared Thompson), friend (Stanley Davies Jr.), sports_rival (Vincent Campbell, Bears captain).
     * Verify exact card IDs and surnames.
   - Scenario 3: `Svartulfr_Scenario_SUCC_Route_Jasper.json`:
     * 8 slots: twin (Alyssa), male_roommate (Russell 'Russ' Sinclair - verify Sinclair surname), crush (Scarlett Rose - verify Rose surname), ai_companion (Echo), childhood_friend (Finnegan Novak - verify Arctic Wolf demi-human), quarterback (Jared Thompson), friend (Stanley Davies Jr.), sports_rival (Vincent Campbell).
     * Find Cocketeers pool/NPC references (Dean, Eric, Javier Reyes, Raymond).
   - Scenario 4: `Svartulfr_Scenario_Villa_Douglas.json`:
     * Exactly 7 canonical male Douglas/Bloodmoon characters with standalone cards: father Erik, eldest_brother Malachia, tech_brother Jasper, politician_brother Noah, maternal_grandfather Wulfnic, uncle Logan, cousin Edric.
     * Confirm their exact standalone card IDs / character IDs.
2. Confirm formatting invariants:
   - Zero em-dashes ('—') in all text (use commas or periods).
   - Dialogue strictly in double quotes, narration in plain text (no asterisks).

Output requirements:
Write a comprehensive report to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_2\handoff.md with all character IDs, slot mappings, card paths, and greeting lore points.
When finished, send a message to orchestrator_2 (parent) via send_message with your status and report path.
