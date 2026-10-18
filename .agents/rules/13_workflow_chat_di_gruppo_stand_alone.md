# Regola 13 — Standard Operativo "Character Scenarios" & Architettura Unificata Svartúlfr

Con la dismissione definitiva della modalità World di Wyvern (`_CgYT8fHXpDC4crjmegQF7`), l'intero progetto **SvartúlfrVerse** adotta ufficialmente la modalità **Character Scenarios** (`https://wiki.wyvern.chat/en/Features/Character-Scenarios`, endpoint `/api/character-scenarios`).

---

## 1. Architettura dello Scenario Unificato (`char_scenario_1DC43ggb6mB8YLJDJKrU4`)

1. **Scenario Unico Multi-Greeting (Cronache dei Gemelli Douglas-Bloodmoon):**
   - Tutte le **29 aperture narrative** ordinate cronologicamente (`01.`–`29.`, da giugno 2024 a giugno 2025: dalla serata domestica a *Call of Duty* a Villa Douglas e le vacanze estive a *Camp Mystic*, lungo l'intero primo anno accademico alla SUCC, i rave di DJ Frequency, le spedizioni della Gilda DMHA e la veglia di Yule con Wulfnic) sono raccolte in lingua italiana come **Greetings ordinate** all'interno di un unico grande Character Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`).
2. **Gestione Dual-Protagonist (Alyssa & Jasper) tramite Slot `twin` e Personas Proposte:**
   - **Personas Proposte (`linked_persona_ids`):**
     - **Alyssa** (`["persona_1786335754946"]`) per le aperture `[FemPOV]`;
     - **Jasper** (`["1792155173728"]`, ID interno `user_persona_bGDFCEtKDzVmgbCmHJWEW`) per le aperture `[MalePOV]`;
     - **`[]` (Scelta libera del giocatore)** per le aperture Dual giocabili da entrambi i gemelli;
     - **Echo** (`1791389790053`) disponibile come Persona alternativa tecnomanziale.
     - **Requisito Obbligatorio `can_fork: true`:** Qualsiasi Persona collegata a uno Scenario in `linked_persona_ids` deve avere tassativamente `can_fork: true` per essere accettata da Wyvern (in caso contrario l'API restituisce `HTTP 400: Only your own forkable personas can be offered`).
   - **Pool dello Slot `twin` (`key: "twin"`, `label: "Twin"`):**
     - Il pool dello slot `twin` contiene **sia la Character Card di Jasper** (`_t4J9aQNJM36cUKAP4wB4U`) **sia la Character Card di Alyssa** (`_6exg3yPfe2eCDK4hTftkh`), entrambe con `weight: 100`.
     - Quando il giocatore avvia una chat usando la Persona di Alyssa, assegna Jasper allo slot `twin`; quando gioca con la Persona di Jasper, assegna la Card di Alyssa allo slot `twin`.
   - **Taggatura POV delle Greetings:**
     - Le aperture specifiche per il punto di vista di Alyssa portano il suffisso **`[FemPOV]`** nel titolo e suggeriscono la Persona di Alyssa (`["persona_1786335754946"]`).
     - Le aperture specifiche per il punto di vista di Jasper portano il suffisso **`[MalePOV]`** nel titolo e suggeriscono la Persona di Jasper (`["1792155173728"]`).
     - Le aperture Dual giocabili indifferentemente da entrambi i gemelli lasciano `linked_persona_ids: []` e usano `{{user}}` + `{{scenarioChar "twin"}}`.

---

## 2. Configurazione degli Slot (`slots`): Disciplina dei Ruoli (Non Nomi di Persona)

Negli Scenari Wyvern, gli slot non devono mai usare i nomi propri dei personaggi come chiavi o etichette: **si utilizzano esclusivamente i ruoli relazionali o funzionali** (es. `quarterback` per Jared, `crush` per Mac, `male_roommate` per Russ).

### I 13 Slot Ufficiali del Master Scenario Svartúlfr (14 Card in `/mine`)
1. `maternal_grandfather` (Label: "Maternal Grandfather") $\rightarrow$ **Wulfnic Báleygr Bloodmoon** (`_HEQQbbRFwKdG8QE2Fh1z1`)
2. `father` (Label: "Father") $\rightarrow$ **Erik Ulfr Douglas** (`_QPea6g4Q1QfeYCVHCLMPR`)
3. `twin` (Label: "Twin") $\rightarrow$ Pool bilanciato: **Jasper Svartr Douglas Bloodmoon** (`_t4J9aQNJM36cUKAP4wB4U`) + **Alyssa Hvit Douglas Bloodmoon** (`_6exg3yPfe2eCDK4hTftkh`)
4. `brother` (Label: "Brother") $\rightarrow$ **Noah Loki Douglas Bloodmoon** (`_zFLUjV8aVxQRAfQxGcAcY`)
5. `eldest_brother` (Label: "Eldest Brother") $\rightarrow$ **Malachia Björn Douglas Bloodmoon** (`_RDfz7XzTpM23LpPALVXHM`)
6. `uncle` (Label: "Uncle") $\rightarrow$ **Logan Járn Douglas** (`_T8Ywcr9FEqNf9JxbK6eHP`)
7. `cousin` (Label: "Cousin") $\rightarrow$ **Edric Douglas** (`_TbRM3EdxDjHFgqztTbCpL`)
8. `quarterback` (Label: "Quarterback") $\rightarrow$ **Jared Thompson** (`_xJVPtBLL3dxy69RLKL9X9`)
9. `friend` (Label: "Friend & Roommate") $\rightarrow$ **Stanley "Stan" Davies Jr.** (`_Xd3NhKnRJByMTtdb6PjxJ`)
10. `crush` (Label: "Crush") $\rightarrow$ **Mackenzie "Mac" Sanchez-Rogers** (`_zn24784jfcchQ7EwCyAnm`)
11. `female_roommate` (Label: "Female Roommate") $\rightarrow$ **Sierra Cruz** (`_pnrXbkWqcgmFAf3meRWFY`)
12. `female_friend` (Label: "Female Friend") $\rightarrow$ **Scarlett Rose** (`_qXgBMbFYJfc84hbLHhe92`)
13. `male_roommate` (Label: "Male Roommate") $\rightarrow$ **Russell "Russ" Sinclair** (`_wn6DkCcg3Xqa2Xpx9ttnT`)

*NPC Gestiti tramite Lorebook:* Personaggi come Zeera Darkfire, Elizabeth Duskwood, Magnus Douglas III, Kaladin Nargathon, Marek, Santiago Herrera, Coach D, Roman Blackwood, Kolya Varenkov e Neon Purr operano tramite le rispettive schede `npc` in `NPC Primary` / `NPC Secondary` con attivazione automatica dell'avatar tramite prefisso su nuova riga (`Nome Completo: "..."`).
3. **Regole sulle Macro e sui Messaggi Multi-Mittente (`messages[]`):**
   - Ogni greeting contiene da 1 a 20 oggetti `messages` (`{ id, content, speaker_slot }`).
   - All'interno di `greeting.messages`, i campi root `greeting.content` e `greeting.speaker_slot` **devono coincidere** con `messages[0].content` e `messages[0].speaker_slot`.
   - Non inserire mai il prefisso `"Nome: "` o `"=>Nome:"` dentro `content`: Wyvern antepone automaticamente il `chat_name` del mittente assegnato a `speaker_slot`.
   - Usare `{{scenarioChar "slot_key"}}` per nominare un altro personaggio dello scenario, `{{char}}` per il mittente del messaggio corrente, e `{{user}}` per il giocatore.

---

## 3. I 6 Lorebook Ufficiali Collegati & I 4 Prompt Overrides

1. **Lorebook Collegati (`lorebook_ids`):**
   Ogni Character Scenario collega i 6 Lorebook ufficiali Svartúlfr (`_gwwCxCfQ6PQaLEjAQVpJL` Lorebook I, `_HfG7TeV6MJyj6bxMwxkpt` Lorebook II, `_9zWTGqYJNJ4BCDMj8gfcD` Lorebook III, `_EjXxkmPVhpCXg8xABpFkK` Location, `_zwEqgEEzh12X6gHVmMKKC` NPC Primary, `_Uht3Ckz44JBDrPnUHq7LV` NPC Secondary) più i 3 moduli tecnici (`_GbWJbkhgLzWexMHrjyUUc` A1 Physics, `_brNyzEdhzNAyxK8xC8hhm` A5 Sex Position, `_YtKLMTwyMxNf1DNYqBx1t` A5.5 Scene Tone).
2. **I 4 Prompt Overrides Ufficiali (`FINAL/PROMPT_OVERRIDES_WYVERN.md`):**
   - `System Prompt Override` (con `[MANDATORY LANGUAGE DIRECTIVE]` in apertura e formati digitali in-scene);
   - `Final Instructions Override` (con `<dual_scene_format>`, `<live_feed_mechanic>` e `[ORDINE FINALE ASSOLUTO]` in italiano in chiusura);
   - `Write for Me Prompt Override`;
   - `Improve My Writing Prompt Override`.

---

## 4. Startup Script Lua (`startup_script`) & Blindatura Anti-Duplicazione

Nei Character Scenarios con slot dinamici o protagonisti multipli alternativi (es. lo slot `twin`), Wyvern espone il campo radice `startup_script` (eseguito prima del salvataggio dei messaggi di apertura).

### 1. Pattern Canonico di Risoluzione Slot via Lua
Lo script verifica a runtime l'identità o i pronomi della User Persona attiva ed assegna la card corrispondente a `memory._scenario.assignments["slot_key"]`:

```lua
if memory and memory._scenario and memory._scenario.assignments then
    local p_id = (user and user.persona_id) or (memory._scenario.persona_id) or ''
    local u_name = string.lower((user and user.name) or '')
    local sub = string.lower((user and (user.pronoun_subjective or (user.pronouns and user.pronouns.subjective))) or '')
    local obj = string.lower((user and (user.pronoun_objective or (user.pronouns and user.pronouns.objective))) or '')

    local alyssa_id = '_6exg3yPfe2eCDK4hTftkh'
    local jasper_id = '_t4J9aQNJM36cUKAP4wB4U'

    -- 1. Risoluzione Diretta per Persona Primaria (Jasper vs Alyssa)
    if p_id == '1792155173728' or p_id == 'user_persona_bGDFCEtKDzVmgbCmHJWEW' or string.find(u_name, 'jasper') then
        memory._scenario.assignments['twin'] = alyssa_id
    elseif p_id == 'persona_1786335754946' or p_id == 'user_persona_VnRF2xGeG1C4xByDF9h9R' or string.find(u_name, 'alyssa') then
        memory._scenario.assignments['twin'] = jasper_id

    -- 2. Risoluzione per Persona Terza Custom tramite Pronomi
    elseif sub == 'he' or obj == 'him' or string.find(u_name, 'maschio') or string.find(u_name, 'male') then
        memory._scenario.assignments['twin'] = alyssa_id
    elseif sub == 'she' or obj == 'her' or string.find(u_name, 'femmina') or string.find(u_name, 'female') then
        memory._scenario.assignments['twin'] = jasper_id

    -- 3. Persona Neutra / Non-Binary (they/them, it/its) -> Randomizer 50/50
    else
        math.randomseed(os.time())
        if math.random(1, 2) == 1 then
            memory._scenario.assignments['twin'] = alyssa_id
        else
            memory._scenario.assignments['twin'] = jasper_id
        end
    end
end
```

### 2. Invariante di Soppressione nei Prompt di Scenario
Per evitare che richiami enciclopedici o memorie dei Lorebook collegati generino sdoppiamenti o dialoghi fantasma del gemello non attivo, ogni Scenario deve includere nel campo `scenario`:

```text
[PERSPECTIVE & LOREBOOK SUPPRESSION INVARIANT]:
The active {{user}} and the active assigned {{scenarioChar "twin"}} are the definitive twin protagonists of this story. Any background lorebook entries or encyclopedic dossiers referring to either Alyssa or Jasper serve exclusively as passive world-building reference and must NEVER create duplicate character personas, third-person ghost dialogue, split-personality narration, or alter the active speaker slot of {{scenarioChar "twin"}}.
```

