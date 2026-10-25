import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

# 1. Update .agents/rules/13_workflow_chat_di_gruppo_stand_alone.md
rule13_path = ROOT / '.agents' / 'rules' / '13_workflow_chat_di_gruppo_stand_alone.md'
with open(rule13_path, 'r', encoding='utf-8', newline='') as f:
    text13 = f.read()

start_tag = '## 3. Registro Ufficiale'
end_tag = '### 3.1 Registro Ufficiale Assistant'

if start_tag in text13 and end_tag in text13:
    pos_start = text13.find(start_tag)
    pos_end = text13.find(end_tag)
    replacement = """## 3. Registro Ufficiale dei Character Scenarios (Wyvern Cloud \u2014 Visibility Private)\r\n\r\nIn seguito alla razionalizzazione operativa (21 Ottobre 2026), il Verse mantiene attivi su Wyvern **esclusivamente i 2 Character Scenarios focalizzati sui due gemelli Douglas-Bloodmoon** (SUCC Collegiate Arcs). Tutti gli altri scenari omnicomprensivi o secondari sono stati dismessi da Wyvern ed archiviati localmente in `FINAL/scenarios/` e `scratch/backup_deleted_scenarios_20261021/`.\r\n\r\n### 3.1 I 2 Character Scenarios Ufficiali Attivi (SUCC Collegiate Arcs)\r\nEntrambi sono configurati con `visibility: \"private\"`, `unavailable_count: 0`, e con la Suite Completa dei **15 Lorebook** (`lorebook_ids` per un totale di 1.173 voci) e Personas offerte (`linked_persona_ids`):\r\n\r\n1. `char_scenario_CKgwq246DyCj1NNTBV9rt` \u2014 **SUCC Collegiate Arc (Alyssa Route)**: 8 slot (`twin` Jasper, `best_friend` Scarlett Rose, `crush` Mackenzie \"Mac\" Sanchez-Rogers, `roommate` Sierra Cruz, `childhood_friend` Finnegan Novak [Demi-Umano Lupo Artico Kemonomimi], `quarterback` Jared Thompson, `friend` Stanley \"Stan\" Davies Jr., `sports_rival` Vincent Campbell).\r\n2. `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` \u2014 **SUCC Collegiate Arc (Jasper Route)**: 8 slot (`twin` Alyssa, `male_roommate` Russell 'Russ' Sinclair, `crush` Scarlett Rose, `ai_companion` Echo, `childhood_friend` Finnegan Novak, `quarterback` Jared Thompson, `friend` Stanley Davies Jr., `sports_rival` Vincent Campbell + The Five Cocketeers).\r\n\r\n### 3.2 Scenari Dismessi ed Archiviati Localmente (Backup Storico)\r\n1. `char_scenario_1DC43ggb6mB8YLJDJKrU4` \u2014 **Master Scenario Omnibus (29 Greetings)**\r\n2. `char_scenario_nLC84wrHdrbB6P3DEhwKb` \u2014 **Camp Mystic (Lake Erie Summer Arc)**\r\n3. `char_scenario_88N1eQXqkbydKX9q9XQzp` \u2014 **Villa Douglas (The Douglas Patriarchs)**\r\n4. `char_scenario_eqtRNnDpKbxDp7dmJmq6E` \u2014 **DMHA Dungeons (Otherworld Incursions)**\r\n5. `char_scenario_rrUCdBPH6WTNyBnQkMAKR` \u2014 **Underworld Sindacato (Los Angeles Syndicate War)**\r\n\r\n"""
    text13 = text13[:pos_start] + replacement + text13[pos_end:]
    with open(rule13_path, 'w', encoding='utf-8', newline='') as f:
        f.write(text13)
    print("Updated rule 13 successfully.")
else:
    print("Could not find tags in rule 13.")

# 2. Update GEMINI.md
gemini_path = ROOT / 'GEMINI.md'
with open(gemini_path, 'r', encoding='utf-8', newline='') as f:
    text_gemini = f.read()

gem_start = 'I 6 Character Scenario Tematici Focalizzati'
gem_end = '2. **Startup Script Lua'

if gem_start in text_gemini and gem_end in text_gemini:
    pos_start = text_gemini.find(gem_start)
    pos_end = text_gemini.find(gem_end)
    bullet_start = text_gemini.rfind('-', 0, pos_start)
    replacement = """- **I 2 Character Scenarios Ufficiali Attivi (Deploy Ufficiale Wyvern API - Visibilit\u00e0 Private):**\r\n\r\n      In seguito alla razionalizzazione (21 Ottobre 2026), sono mantenuti attivi esclusivamente i 2 archi universitari dei gemelli, collegati alla Suite Completa dei 15 Lorebook Standalone (`lorebook_ids`) e Personas offerte (`linked_persona_ids`):\r\n\r\n      1. `char_scenario_CKgwq246DyCj1NNTBV9rt` - **SUCC Collegiate Arc (Alyssa Route)**: 8 slot (twin Jasper, Scarlett Rose, Mac, Sierra Cruz, Finn Novak [Arctic Wolf demi-human], Jared Thompson, Stan Davies Jr., Vincent Campbell).\r\n\r\n      2. `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` - **SUCC Collegiate Arc (Jasper Route)**: 8 slot (twin Alyssa, Russ Sinclair, Scarlett Rose [cotta segreta di Jasper], drone Echo, Finn Novak, Jared Thompson, Stan Davies Jr., Vincent Campbell + Five Cocketeers via pool).\r\n\r\n      *(Gli scenari Omnibus Master `char_scenario_1DC43ggb6mB8YLJDJKrU4`, Camp Mystic `char_scenario_nLC84wrHdrbB6P3DEhwKb`, Villa Douglas `char_scenario_88N1eQXqkbydKX9q9XQzp`, DMHA `char_scenario_eqtRNnDpKbxDp7dmJmq6E` e Underworld `char_scenario_rrUCdBPH6WTNyBnQkMAKR` sono stati dismessi da Wyvern ed archiviati localmente).*\\r\n\r\n"""
    # Fix the trailing literal \\r\n if needed
    replacement = replacement.replace('\\r\n\r\n', '\r\n\r\n')
    text_gemini = text_gemini[:bullet_start] + replacement + text_gemini[pos_end:]
    with open(gemini_path, 'w', encoding='utf-8', newline='') as f:
        f.write(text_gemini)
    print("Updated GEMINI.md successfully.")
else:
    print("Could not find tags in GEMINI.md.")
