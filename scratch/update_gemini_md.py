with open('GEMINI.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 320: insert 15 Lorebook suite after line 321
sec7_addition = "  - **Suite Unificata a 15 Lorebook per Character Scenarios:** A tutti i 7 Character Scenarios è assegnata stabilmente la suite completa e ordinata dei 15 Lorebook (i 6 Lorebook Svartúlfr più i 9 Lorebook della serie Realism: `A0 Behavioral Realism`, `A1 Physics`, `A2 Social Realism`, `A3 Medical Realism`, `A4 Cultural Realism`, `A5 Sex Position`, `A5.5 Scene Tone`, `A6 World Realism`, `A7 Queer Realism`), unificando 1.173 voci di lore e realismo narrativo.\n\n"
lines.insert(322, sec7_addition)

# Line 1052 (now shifted by 1):
for i in range(1040, 1070):
    if 'Le aperture `[FemPOV]` collegano la Persona di **Alyssa**' in lines[i]:
        lines[i] = '     - Le aperture `[FemPOV]` e la rotta `SUCC Route Alyssa` collegano la Persona di **Alyssa** (`["persona_1786335754946"]`), le aperture `[MalePOV]` e la rotta `SUCC Route Jasper` collegano la Persona di **Jasper** (`["1792155173728"]`), mentre le aperture Dual (*Villa Douglas*, *Camp Mystic*, *DMHA Dungeons*, *Underworld Sindacato* e i greeting condivisi del Master Scenario) offrono contemporaneamente entrambe le Persona (`["persona_1786335754946", "1792155173728"]`) permettendo al giocatore di scegliere direttamente il protagonista al lancio.\n'
        print('Updated line', i)
        break

# Line 1096:
for i in range(1090, 1110):
    if 'Oltre al Master Scenario Omnibus originario' in lines[i]:
        lines[i] = '     Oltre al Master Scenario Omnibus originario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`), il Verse dispone di 6 storyline tematiche autonome, ciascuna dotata di party snello, greeting contestuali, collegamento alla Suite Completa dei 15 Lorebook Standalone (`lorebook_ids`) e Personas offerte (`linked_persona_ids`):\n'
        print('Updated line', i)
        break

# Line 1124 & 1126:
for i in range(1120, 1140):
    if '4. **I 6 Lorebook Collegati & I 4 Prompt Overrides:**' in lines[i]:
        lines[i] = '4. **La Suite Unificata a 15 Lorebook & I 4 Prompt Overrides:**\n'
        lines[i+2] = '   - Ogni Character Scenario collega stabilmente la suite completa dei 15 Lorebook ufficiali (`Lorebook I`, `Lorebook II`, `Lorebook III`, `Location`, `NPC Secondary`, `NPC Primary`, `A0 Behavioral Realism`, `A1 Physics`, `A2 Social Realism`, `A3 Medical Realism`, `A4 Cultural Realism`, `A5 Sex Position`, `A5.5 Scene Tone`, `A6 World Realism`, `A7 Queer Realism`).\n'
        print('Updated lines', i, i+2)
        break

with open('GEMINI.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("GEMINI.md successfully updated!")
