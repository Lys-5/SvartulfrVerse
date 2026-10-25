## 2026-10-21T16:10:35Z
You are Worker R7-1 (Implementation & Deployment Specialist).
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\worker_r7_1
Read ORIGINAL_REQUEST.md from: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
Read PROJECT.md from: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_7\PROJECT.md
Review GEMINI.md at: e:\repository\SvartulfrVerse\GEMINI.md
Review survey findings:
- Explorer R7-1: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r7_1\analysis.md and handoff.md
- Explorer R7-2: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r7_2\analysis.md and handoff.md (contains exact JED+ replacement texts for Bruce, Campus Staff Rat, Adrian)
- Explorer R7-3: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r7_3\analysis.md and handoff.md (contains avatar lists, cover URLs, API mechanics)

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Write ownership:
You exclusively own:
- `FINAL/Svartulfr_NPC_Primary.json`
- `FINAL/Svartulfr_NPC_Secondary.json`
- `lorebooks/optimized/Svartulfr_NPC_Primary.json`
- `lorebooks/optimized/Svartulfr_NPC_Secondary.json`
- `CHANGELOG.md`
- Scratch scripts in `scratch/`

Your objective:
Execute Milestone 1 (R1, R2, R3, R4, R5):
1. R1: Full JED+ restoration for 7 core characters (Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie in Primary; Edric in Secondary) as `type: "npc"`, `selective: false`, full JED+ texts from `FINAL/<name>_card.json`, card avatars, multiline regex `(?:^|\n)\s*(?:Nome Completo|Nome|Nickname)\s*:`, `lines_parsed: 1`, structured `npc_info`, confirm `ignored_characters`, set Primary token_budget to 7500, Secondary token_budget to 5000.
2. R2: Homogenize layout:
   - Encapsulate Bruce (`NQd7n3QacMcK-TzowQ2LE`), Campus Staff Rat (`oov5UWuVhZ3RGgoxMkaTS`), and Adrian (`Og7V6v67guXXAaP0_PsTM`) into standard JED+ using the exact texts formulated in `explorer_r7_2\analysis.md`.
   - Normalize `VOICE AND BEHAVIOR:` to `VOICE & BEHAVIOR:`.
   - Ensure all 310 entries have standard bracket start `[...]`.
3. R3: Update all 200 fallback entries (42 in Primary, 158 in Secondary) currently using `6f8b7c78...` to official DCC placeholder: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`. Preserve all 110 custom portrait entries. Ensure 100% of 310 entries have valid HTTPS avatars.
4. R4: Strictly enforce formatting discipline: 0 em-dashes (`\u2014`), standard double quotes for dialogue, plain text actions (no markdown asterisks), 0 `{{age}}`, 0 umbrella `BROAD_KEYS` on trigger keys. Inject `exclude_from_recursion: true` on all 310 entries.
5. R5:
   - Set House Svartúlfr emblem `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public` as `photoURL` cover on both Primary and Secondary lorebooks.
   - Apply updates to both `entries` and `lexicon` in local JSONs to preserve 1:1 internal consistency.
   - Synchronize updated files from `FINAL/` into `lorebooks/optimized/`.
   - Deploy live to Wyvern API via `PUT /api/lorebooks/:id` with compact payload (`lexicon` + top-level metadata, excluding duplicate `entries`), using Bearer token from `scratch/wyvern_token.txt` (running `scratch/refresh_token.py` if needed), with 2.5-second pacing delay.
   - Verify deployment with live GET calls (status 200, entry count retention, token budget, photoURL).
   - Update `CHANGELOG.md` with comprehensive release documentation.
