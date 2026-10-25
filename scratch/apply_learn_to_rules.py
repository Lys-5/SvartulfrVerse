import os

rule05_path = '.agents/rules/05_precedenza_lore_e_discrepanze.md'
with open(rule05_path, 'r', encoding='utf-8') as f:
    text05 = f.read()

# Update Section 6
old_s6 = """## 6. Invarianti dei Personaggi Crossover e Preferiti Integrati

A seguito del triage delle sorgenti storiche e delle decisioni autorali dell'utente, le seguenti collocazioni sono canoniche e vincolanti per tutte le card e i lorebook:
1. **Finnegan "Finn" Novak:** Amico d'infanzia dei fratelli Douglas (Alyssa, Jasper, Noah). Demi-umano canino (1 solo paio di orecchie), figura di calda normalità al campus.
2. **Russ & The Five Cocketeers:** Russ è il coinquilino di stanza di Jasper Douglas nei dormitori Wyrm Hall alla SUCC.
3. **Roman Blackwood & Kolya:** Atleti del SUCC Wrestling Team; compagni di allenamento pesante e sparring di Malachia Douglas.
4. **Dallas Rhodes:** Werewolf contadino/allevatore a Bakersfield (ricollocato dal Texas). Pragmatico, instancabile lavoratore dei campi con tail-slit sui jeans.
5. **NOVA FARM:** Branco rurale di licantropi a Bakersfield, in netto contrasto di classe con l'élite Douglas dei Seven Hills.
6. **Neon Purr:** DJ felino australiano, rivale musicale e underground principale di Jasper Douglas tra The Verve e rave illegali.
7. **Romeo "Gray" Dean:** Leader/biker della gang rivale dei Nomads di Marek nei collegamenti tra Solarton e Blackwood.
8. **Warchief Thrakgor Deathspine:** Capoguerra bellicoso del Clan Deathspine, spina nel fianco perenne per il consigliere moderatore orco Brak Ironfist.
9. **Morgeth Steeltooth:** Maestro fabbro orco e pari di forgiatura di Ut Berg; si incontrano al The Verve coinvolgendo Logan in lunghe discussioni sui metalli.
10. **Thorvald & Harald Sigurdsson:** Licantropi del Clan Bloodmoon tradizionale, discendenti della traversata di Wulfnic (1022 d.C.); vivono nella foresta profonda del Dead Zone secondo i riti norreni."""

new_s6 = """## 6. Invarianti dei Personaggi Crossover e Preferiti Integrati

A seguito del triage delle sorgenti storiche e delle decisioni autorali dell'utente, le seguenti collocazioni sono canoniche e vincolanti per tutte le card e i lorebook:
1. **Finnegan "Finn" Novak:** Amico d'infanzia leale dei gemelli Douglas (Alyssa, Jasper, Noah). **Demi-Umano Lupo Artico (Kemonomimi)**: corpo umano, singolo paio di orecchie lupine apicali, coda folta bianca, non-shifter, senza secondo genere Alpha/Beta/Omega, ala sinistra del team di hockey dei SUCC Bears. Vietato categoricamente classificarlo come caracal o felino.
2. **Russell 'Russ' Sinclair & The Five Cocketeers:** **Russ Sinclair** (cognome rigorosamente Sinclair, mai Gallagher) è il coinquilino di stanza di Jasper Douglas nei dormitori Wyrm Hall 304 alla SUCC. Chitarrista rock esuberante, membro dei *Five Cocketeers* (con Dean, Eric, Javier Reyes e Raymond).
3. **Scarlett Rose:** Succube, migliore amica e compagna di stanza di Alyssa (suite Theta Iota Theta 3B), confidente emotiva, cotta segreta non corrisposta di Jasper. Cognome rigorosamente Rose (mai Vance).
4. **Roman Blackwood & Kolya:** Atleti del SUCC Wrestling Team; compagni di allenamento pesante e sparring di Malachia Douglas.
5. **Dallas Rhodes:** Werewolf contadino/allevatore a Bakersfield (ricollocato dal Texas). Pragmatico, instancabile lavoratore dei campi con tail-slit sui jeans.
6. **NOVA FARM:** Branco rurale di licantropi a Bakersfield, in netto contrasto di classe con l'élite Douglas dei Seven Hills.
7. **Neon Purr:** DJ felino australiano, rivale musicale e underground principale di Jasper Douglas tra The Verve e rave illegali.
8. **Romeo "Gray" Dean:** Leader/biker della gang rivale dei Nomads di Marek nei collegamenti tra Solarton e Blackwood.
9. **Warchief Thrakgor Deathspine:** Capoguerra bellicoso del Clan Deathspine, spina nel fianco perenne per il consigliere moderatore orco Brak Ironfist.
10. **Morgeth Steeltooth:** Maestro fabbro orco e pari di forgiatura di Ut Berg; si incontrano al The Verve coinvolgendo Logan in lunghe discussioni sui metalli.
11. **Thorvald & Harald Sigurdsson:** Licantropi del Clan Bloodmoon tradizionale, discendenti della traversata di Wulfnic (1022 d.C.); vivono nella foresta profonda del Dead Zone secondo i riti norreni."""

assert old_s6 in text05, "Section 6 not found in text05"
text05 = text05.replace(old_s6, new_s6)

# Append Section 9
section_9 = """

---

## 9. Tabella delle Identità e Invarianti Canoniche Blindate (Prevenzione Regressioni)

| Personaggio / Entità | Ruolo Canonico & Dettagli Chiave | Errore Vietato (Da Evitare) |
|---|---|---|
| **Russell 'Russ' Sinclair** | Coinquilino di Jasper in Wyrm Hall 304, chitarrista rock, Five Cocketeers. | ❌ Gallagher, Vance |
| **Scarlett Rose** | Succube, best friend di Alyssa (Theta Iota Theta 3B), cotta segreta di Jasper. | ❌ Vance, cognomi alternativi |
| **Finnegan "Finn" Novak** | Demi-Umano Lupo Artico (Kemonomimi: 1 paio di orecchie lupine, coda bianca, non-shifter, ala sinistra SUCC Bears). | ❌ Caracal, felino, licantropo LSE |
| **Jean-Luc Virtuoso** | Umano Telepate ("The Maestro", "Pride", 39 anni, boss del cartello Ambrosia e fondatore dei Sinners a Los Angeles). | ❌ Minotauro, brute da mischia |
| **Coach Dullahan** | Contractor #04 in DDM Inc. (Euclidean Division / Voidspace) e Head Coach atletica SUCC. | ❌ Membro della DMHA |
| **DMHA (Dungeon Management & Hunter Authority)** | Gilda governativa per dungeon urbani. Roster: Barrow (demi-umano orso), Team Ukiyo (*Radek, Goran, Kian*), Marek & Ironhorn Nomads. | ❌ Confusione con DDM Inc. / Voidspace |
| **Camp Mystic Supervision** | Mara Evelyn Voss (Direttrice); Marcus Dean Vale (Supervisore Maschile, Werewolf); Celeste Amara Nadir (Supervisore Femminile, Gorgon). | ❌ Mara come supervisore di cabina |
| **Visibilità Character Scenarios** | Impostazione obbligatoria `visibility: "private"` per tutti i deployment di scenari standalone. | ❌ "public", "unlisted" |
"""

if "## 9. Tabella delle Identità e Invarianti Canoniche Blindate" not in text05:
    text05 = text05.rstrip() + section_9

with open(rule05_path, 'w', encoding='utf-8') as f:
    f.write(text05)
print("Updated Rule 05 successfully.")

# Update Rule 13
rule13_path = '.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md'
with open(rule13_path, 'r', encoding='utf-8') as f:
    text13 = f.read()

# In Rule 13, replace Section 3 heading with Section 4, Section 4 with Section 5, and insert Section 3
target_s3 = """## 3. I 6 Lorebook Ufficiali Collegati & I 4 Prompt Overrides"""
new_s3_and_s4 = """## 3. Registro Ufficiale dei 6 Character Scenarios Tematici (Wyvern Cloud — Visibility Private)

Oltre al Master Scenario Omnibus (`char_scenario_1DC43ggb6mB8YLJDJKrU4`), il Verse dispone di 6 Character Scenarios dedicati e focalizzati per specifiche linee narrative, tutti configurati con `visibility: "private"`, `unavailable_count: 0`, e con i 6 Lorebook Standalone collegati (`lorebook_ids`):

1. `char_scenario_nLC84wrHdrbB6P3DEhwKb` — **Camp Mystic (Lake Erie Summer Arc)**: 8 slot (`twin`, `cousin` Edric 13yo, `supervisor` Marcus Dean Vale / Celeste Nadir via Lua, `director` Mara Evelyn Voss, 4 slot pool camper del lago: `cabin_mate_1`, `cabin_mate_2`, `camper_peer_1`, `camper_peer_2`).
2. `char_scenario_CKgwq246DyCj1NNTBV9rt` — **SUCC Collegiate Arc (Alyssa Route)**: 8 slot (`twin` Jasper, `best_friend` Scarlett Rose, `crush` Mackenzie "Mac" Sanchez-Rogers, `roommate` Sierra Cruz, `childhood_friend` Finnegan Novak [Demi-Umano Lupo Artico Kemonomimi], `quarterback` Jared Thompson, `friend` Stanley "Stan" Davies Jr., `sports_rival` Vincent Campbell).
3. `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` — **SUCC Collegiate Arc (Jasper Route)**: 8 slot (`twin` Alyssa, `male_roommate` Russell 'Russ' Sinclair, `crush` Scarlett Rose, `ai_companion` Echo, `childhood_friend` Finnegan Novak, `quarterback` Jared Thompson, `friend` Stanley Davies Jr., `sports_rival` Vincent Campbell + The Five Cocketeers).
4. `char_scenario_88N1eQXqkbydKX9q9XQzp` — **Villa Douglas (The Douglas Patriarchs)**: 7 slot maschili con card (`father` Erik, `eldest_brother` Malachia, `tech_brother` Jasper, `politician_brother` Noah, `maternal_grandfather` Wulfnic, `uncle` Logan, `cousin` Edric).
5. `char_scenario_eqtRNnDpKbxDp7dmJmq6E` — **DMHA Dungeons (Otherworld Incursions)**: 9 slot (`twin_healer` Alyssa, `twin_tech` Jasper, `eldest_brother` Malachia + `demihuman_representative` Barrow, `biker_enforcer` Marek, `raid_leader` Radek, `tank_frontline` Goran, `scout_infiltrator` Kian, `faction_support` DMHA strike team).
6. `char_scenario_rrUCdBPH6WTNyBnQkMAKR` — **Underworld Sindacato (Los Angeles Syndicate War)**: 6 slot (Rory Ballantine & Sully Jones vs Jean-Luc Virtuoso [Umano Telepate], Alicia Virtuoso, Arthur Sinclair + `mercenary_tracker` Ilya Volkov / Vasile Ionescu).

---

## 4. I 6 Lorebook Ufficiali Collegati & I 4 Prompt Overrides"""

if "## 3. Registro Ufficiale dei 6 Character Scenarios Tematici" not in text13:
    assert target_s3 in text13, "Target Section 3 not found in text13"
    text13 = text13.replace(target_s3, new_s3_and_s4)
    # Also update section 4 -> 5
    text13 = text13.replace("## 4. Startup Script Lua (`startup_script`) & Blindatura Anti-Duplicazione", "## 5. Startup Script Lua (`startup_script`) & Blindatura Anti-Duplicazione")

with open(rule13_path, 'w', encoding='utf-8') as f:
    f.write(text13)
print("Updated Rule 13 successfully.")
