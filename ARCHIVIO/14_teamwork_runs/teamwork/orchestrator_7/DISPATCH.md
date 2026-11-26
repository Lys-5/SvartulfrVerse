## 2026-10-21T15:58:50Z
You are the Project Orchestrator (orchestrator_7).
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_7
Read your mission from: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md

Your mission is:
Execute Lorebook NPC Full JED+ Restoration, Layout Homogenization (310 entries), Official DCC Avatar Placeholder, House Emblem Lorebook Cover, and Live Wyvern API Deployment.

Requirements to satisfy:
1. R1: In `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`), convert the 6 core characters (Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie) from `lore/concept` to `type: "npc"`, `selective: false` with complete JED+ text from `FINAL/<name>_card.json` (including vehicles, intimacy, RPG stats/traits), proper `ignored_characters` array containing their respective card IDs, custom_avatar_regex, lines_parsed: 1, npc_info, original avatar URL, and token_budget: 7500. In `FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`), convert Edric Douglas to `type: "npc"`, `selective: false` with complete JED+ text from `FINAL/Edric_Douglas_card.json`, avatar, regex, `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]`, and token_budget: 5000.
2. R2: Inspect and normalize all 99 entries of Primary and 211 entries of Secondary to standard JED+ 4-block layout (plus thematic closure). Encapsulate irregular entries (Bruce, Campus Staff Rat, Adrian) into standard JED+ with bracket header, BACKSTORY, VOICE & BEHAVIOR. Standardize uppercase headers (`BACKSTORY:`, `FAMILY & PACK:` or `CLAN AND COMPANY:`, `VOICE & BEHAVIOR:`).
3. R3: Update all entries in Primary and Secondary lacking a custom avatar portrait to the official DCC placeholder: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`. Ensure 100% of the 310 entries have a valid HTTPS avatar URL.
4. R4: Strictly enforce formatting discipline across all 310 entries: 0 em-dashes, dialog in double quotes, narration in plain text (no markdown asterisks), no orphan `{{age}}` macros, no umbrella `BROAD_KEYS` on NPC keys, and `exclude_from_recursion: true` on all NPC entries.
5. R5: Set the official House Svartúlfr emblem (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public`) as the `photoURL` cover for both Lorebooks. Synchronize updated JSON files from `FINAL/` to `lorebooks/optimized/`. Deploy live via `PUT /api/lorebooks/:id` sending compact payload (`lexicon` and top-level metadata, excluding duplicate `entries` array). Validate live via authenticated GET calls and Chrome DevTools inspection.
