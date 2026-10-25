with open('GEMINI.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = '     - Usare `{{scenarioChar "slot_key"}}` per riferirsi agli altri slot, `{{char}}` per il mittente del messaggio corrente e `{{user}}` per il giocatore.\n2. **Startup Script Lua'

replacement = '''     - Usare `{{scenarioChar "slot_key"}}` per riferirsi agli altri slot, `{{char}}` per il mittente del messaggio corrente e `{{user}}` per il giocatore.
   - **I 6 Character Scenario Tematici Focalizzati (Deploy Ufficiale Wyvern API - Visibilità Private):**
     Oltre al Master Scenario Omnibus originario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`), il Verse dispone di 6 storyline tematiche autonome, ciascuna dotata di party snello, greeting contestuali e collegamento a tutti i 6 Lorebook Standalone:
     1. `char_scenario_nLC84wrHdrbB6P3DEhwKb` - **Camp Mystic (Lake Erie Summer Arc)**: 8 slot (twin, cousin Edric 13yo, supervisore dinamico via Lua [Marcus Dean Vale per ragazzi / Celeste Amara Nadir per ragazze], direttrice Mara Voss, 4 slot pool camper del lago).
     2. `char_scenario_CKgwq246DyCj1NNTBV9rt` - **SUCC Collegiate Arc (Alyssa Route)**: 8 slot (twin Jasper, Scarlett Rose, Mac, Sierra Cruz, Finn Novak [Arctic Wolf demi-human], Jared Thompson, Stan Davies Jr., Vincent Campbell).
     3. `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` - **SUCC Collegiate Arc (Jasper Route)**: 8 slot (twin Alyssa, Russ Sinclair, Scarlett Rose [cotta segreta di Jasper], drone Echo, Finn Novak, Jared Thompson, Stan Davies Jr., Vincent Campbell + Five Cocketeers via pool).
     4. `char_scenario_88N1eQXqkbydKX9q9XQzp` - **Villa Douglas (The Douglas Patriarchs)**: 7 slot maschili completi con card (Erik, Malachia, Jasper, Noah, Wulfnic, Logan, Edric).
     5. `char_scenario_eqtRNnDpKbxDp7dmJmq6E` - **DMHA Dungeons (Otherworld Incursions)**: 9 slot (Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team, con le ambientazioni originali di Kakihara).
     6. `char_scenario_rrUCdBPH6WTNyBnQkMAKR` - **Underworld Sindacato (Los Angeles Syndicate War)**: 6 slot (Contractor indipendente: Rory Ballantine & Sully Jones vs Jean-Luc Virtuoso [Umano Telepate], Alicia, Arthur Sinclair + Ilya/Vasile).
2. **Startup Script Lua'''

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open('GEMINI.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Successfully updated GEMINI.md!')
else:
    print('Target not found!')
