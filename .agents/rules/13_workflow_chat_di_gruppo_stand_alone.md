# Regola 13 — Standard Operativo "Character Scenarios" & Architettura Unificata Svartúlfr

Con la dismissione definitiva della modalità World di Wyvern (`_CgYT8fHXpDC4crjmegQF7`), l'intero progetto **SvartúlfrVerse** adotta ufficialmente la modalità **Character Scenarios** (`https://wiki.wyvern.chat/en/Features/Character-Scenarios`, endpoint `/api/character-scenarios`).

---

## 1. Architettura dello Scenario Unificato (`char_scenario_1DC43ggb6mB8YLJDJKrU4`)

1. **Scenario Unico Multi-Greeting (Cronache dei Gemelli Douglas-Bloodmoon):**
   - Tutte le aperture narrative (dalla serata domestica a *Call of Duty* a Villa Douglas e le vacanze estive a *Camp Mystic*, lungo l'intero primo anno accademico alla SUCC, i rave di DJ Frequency, le spedizioni della Gilda DMHA e la veglia di Yule con Wulfnic) sono raccolte come **Greetings ordinate** all'interno di un unico grande Character Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`).
2. **Gestione Dual-Protagonist (Alyssa & Jasper) tramite Slot `twin` e Personas Proposte:**
   - **Personas Proposte (`linked_persona_ids`):**
     - **Alyssa** (`persona_1786335754946`) per le aperture `[FemPOV]` e condivise;
     - **Jasper** (`1792155173728`, ID interno `user_persona_bGDFCEtKDzVmgbCmHJWEW`) per le aperture `[MalePOV]` e condivise;
     - **Echo** (`1791389790053`) disponibile come Persona alternativa tecnomanziale.
     - **Requisito Obbligatorio `can_fork: true`:** Qualsiasi Persona collegata a uno Scenario in `linked_persona_ids` deve avere tassativamente `can_fork: true` per essere accettata da Wyvern (in caso contrario l'API restituisce `HTTP 400: Only your own forkable personas can be offered`).
   - **Pool dello Slot `twin` (`key: "twin"`, `label: "Twin"`):**
     - Il pool dello slot `twin` contiene **sia la Character Card di Jasper** (`_t4J9aQNJM36cUKAP4wB4U`) **sia la Character Card di Alyssa** (`_6exg3yPfe2eCDK4hTftkh`), entrambe con `weight: 100`.
     - Quando il giocatore avvia una chat usando la Persona di Alyssa, assegna Jasper allo slot `twin`; quando gioca con la Persona di Jasper, assegna la Card di Alyssa allo slot `twin`.
   - **Taggatura POV delle Greetings:**
     - Le aperture specifiche per il punto di vista di Alyssa portano il prefisso **`[FemPOV]`** nel titolo/descrizione e suggeriscono la Persona di Alyssa.
     - Le aperture specifiche per il punto di vista di Jasper portano il prefisso **`[MalePOV]`** nel titolo/descrizione e suggeriscono la Persona di Jasper.
     - Le aperture giocabili indifferentemente da entrambi i gemelli collegano entrambe le Personas (`Alyssa` e `Jasper`) e usano `{{user}}` + `{{scenarioChar "twin"}}`.

---

## 2. Configurazione degli Slot (`slots`): Disciplina dei Ruoli (Non Nomi di Persona)

Negli Scenari Wyvern, gli slot non devono mai usare i nomi propri dei personaggi come chiavi o etichette: **si utilizzano esclusivamente i ruoli relazionali o funzionali** (es. `boss` per Zeera, `quarterback` per Jared, `crush` per Mac).

### I 13 Slot Ufficiali del Master Scenario Svartúlfr
1. `maternal_grandfather` (Label: "Maternal Grandfather") $\rightarrow$ **Wulfnic Báleygr Bloodmoon** (`_HEQQbbRFwKdG8QE2Fh1z1`)
2. `paternal_grandfather` (Label: "Paternal Grandfather") $\rightarrow$ **Magnus Douglas III** (`_dJ7nRMQEbcUgdWG96MqLz`)
3. `paternal_grandmother` (Label: "Paternal Grandmother") $\rightarrow$ **Elizabeth Duskwood** (`_zBD6rWUkJBAjLfXnja4xh`)
4. `father` (Label: "Father") $\rightarrow$ **Erik Ulfr Douglas** (`_QPea6g4Q1QfeYCVHCLMPR`)
5. `twin` (Label: "Twin") $\rightarrow$ Pool bilanciato: **Jasper Svartr Douglas Bloodmoon** (`_t4J9aQNJM36cUKAP4wB4U`) + **Alyssa Hvit Douglas Bloodmoon** (`_6exg3yPfe2eCDK4hTftkh`)
6. `brother` (Label: "Brother") $\rightarrow$ **Noah Loki Douglas Bloodmoon** (`_zFLUjV8aVxQRAfQxGcAcY`)
7. `eldest_brother` (Label: "Eldest Brother") $\rightarrow$ **Malachia Björn Douglas Bloodmoon** (`_RDfz7XzTpM23LpPALVXHM`)
8. `uncle` (Label: "Uncle") $\rightarrow$ **Logan Járn Douglas** (`_T8Ywcr9FEqNf9JxbK6eHP`)
9. `cousin` (Label: "Cousin") $\rightarrow$ **Edric Douglas** (`_TbRM3EdxDjHFgqztTbCpL`)
10. `boss` (Label: "Boss") $\rightarrow$ **Zeera Darkfire** (`_3tMk6cRAFewRnKMkdJ4XU`)
11. `quarterback` (Label: "Quarterback") $\rightarrow$ **Jared Thompson** (`_xJVPtBLL3dxy69RLKL9X9`)
12. `crush` (Label: "Crush") $\rightarrow$ **Mackenzie "Mac" Sanchez-Rogers** (`_zn24784jfcchQ7EwCyAnm`)
13. `major` (Label: "Major") $\rightarrow$ **Major Kaladin Blackwolf Nargathon** (`_EnRGd1jfbjTTGmz4EFJdd`)

*Nota di compatibilità per Card Esterne:* Personaggi pubblicati da altri autori sul portale pubblico (come **Marek**, Blue Oni del Team Ukiyo di Kakihara) non possono essere inseriti nei pool degli slot se l'API Wyvern riserva gli slot ai soli personaggi di proprietà (`/mine`). Nelle scene in cui compaiono co-protagonisti esterni (es. Cap. 11 al Club House Nomads), il ruolo di `speaker_slot` viene assegnato a `twin` (Jasper o Alyssa a vegliare sulla scena) o `boss`, mantenendo il testo dialogico di Marek intatto nella narrazione.
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
