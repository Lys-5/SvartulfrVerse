# Technical Analysis Report: Local Scenarios Investigation (15 Lorebooks & Persona IDs)

**Explorer Agent**: Explorer 1 (Local Scenarios Explorer)  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_1`  
**Date**: 2026-10-20  
**Target Milestone**: 15 Lorebooks Suite & "Offer a persona to play as" Integration across all 7 Character Scenarios  

---

## Executive Summary

A comprehensive, read-only inspection was performed across all 7 local Character Scenario JSON files in `FINAL/scenarios/` and `FINAL/`:
1. `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json` (ID: `char_scenario_nLC84wrHdrbB6P3DEhwKb`)
2. `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` (ID: `char_scenario_CKgwq246DyCj1NNTBV9rt`)
3. `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json` (ID: `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`)
4. `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json` (ID: `char_scenario_88N1eQXqkbydKX9q9XQzp`)
5. `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json` (ID: `char_scenario_eqtRNnDpKbxDp7dmJmq6E`)
6. `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json` (ID: `char_scenario_rrUCdBPH6WTNyBnQkMAKR`)
7. `FINAL/Svartulfr_Master_Scenario.json` (ID: `char_scenario_1DC43ggb6mB8YLJDJKrU4`)

### Key Discoveries:
1. **Lorebook Gap**: The 6 thematic scenario files in `FINAL/scenarios/` currently connect to only the **6 core lorebooks** (`Lore I`, `Lore II`, `Lore III`, `Location`, `NPC Primary`, `NPC Secondary`). All **9 realism lorebooks** (`A0` to `A7`) are completely absent. In contrast, `FINAL/Svartulfr_Master_Scenario.json` already contains all 15 IDs, but in an unordered sequence relative to the canonical standard.
2. **Persona ID Storage**: `linked_persona_ids` is located strictly at the **greeting object level** (`greeting.linked_persona_ids`), as an array of persona ID strings. It is NOT located inside the nested `messages` array.
3. **Current Persona State**: In all 6 thematic scenario files, `linked_persona_ids` is already present in every greeting object, initialized to an empty array `[]`.
4. **Master Scenario POV Mapping**: `FINAL/Svartulfr_Master_Scenario.json` contains exactly **29 greetings**:
   - **16 Shared/Neutral greetings**: Currently `linked_persona_ids: []`. Must be assigned both twins: `["persona_1786335754946", "1792155173728"]`.
   - **7 `[FemPOV]` greetings**: Already have `["persona_1786335754946"]`. Must be preserved.
   - **6 `[MalePOV]` greetings**: Already have `["1792155173728"]`. Must be preserved.
5. **Persona ID Identifiers**:
   - **Alyssa**: `"persona_1786335754946"` (retains `"persona_"` prefix).
   - **Jasper**: `"1792155173728"` (numeric string without prefix).

---

## 1. Unified 15 Lorebook Suite Specification

The unified suite of 15 Lorebooks must be applied across all 7 scenarios in the following canonical sequence:

| # | Lorebook ID | Name / Title | Category |
|---|---|---|---|
| 1 | `_gwwCxCfQ6PQaLEjAQVpJL` | Svartúlfr - Lorebook I | World Lore, Houses, Runes |
| 2 | `_HfG7TeV6MJyj6bxMwxkpt` | Svartúlfr - Lorebook II | Economy, Contracts, DDM Voidspace |
| 3 | `_9zWTGqYJNJ4BCDMj8gfcD` | Svartúlfr - Lorebook III | SUCC Campus, Frats, Underworld |
| 4 | `_EjXxkmPVhpCXg8xABpFkK` | Svartúlfr - Location | World Locations |
| 5 | `_Uht3Ckz44JBDrPnUHq7LV` | Svartúlfr - NPC Secondary | Secondary & Tertiary NPCs |
| 6 | `_zwEqgEEzh12X6gHVmMKKC` | Svartúlfr - NPC Primary | Primary NPCs & Intimacy Profiles |
| 7 | `_GV1KyHVY1RMbCnWgLkzDG` | A0 Behavioral Realism | Realism Suite |
| 8 | `_GbWJbkhgLzWexMHrjyUUc` | A1 Physics | Realism Suite |
| 9 | `_FaVcHfmrqcaJq8pa3WmRw` | A2 Social Realism | Realism Suite |
| 10 | `_BbrRgrcdGPMLEbBU2b6xk` | A3 Medical Realism | Realism Suite |
| 11 | `_gchmML4Q478zdFjhXf8rN` | A4 Cultural Realism | Realism Suite |
| 12 | `_brNyzEdhzNAyxK8xC8hhm` | A5 Sex Position | Realism Suite |
| 13 | `_YtKLMTwyMxNf1DNYqBx1t` | A5.5 Scene Tone | Realism Suite |
| 14 | `_b9HgpUXtAW8VmTy82BPDV` | A6 World Realism | Realism Suite |
| 15 | `_c8bEm1bWphwqFBXWRPrV8` | A7 Queer Realism | Realism Suite |

### Canonical Array Definition:
```json
"lorebook_ids": [
  "_gwwCxCfQ6PQaLEjAQVpJL",
  "_HfG7TeV6MJyj6bxMwxkpt",
  "_9zWTGqYJNJ4BCDMj8gfcD",
  "_EjXxkmPVhpCXg8xABpFkK",
  "_Uht3Ckz44JBDrPnUHq7LV",
  "_zwEqgEEzh12X6gHVmMKKC",
  "_GV1KyHVY1RMbCnWgLkzDG",
  "_GbWJbkhgLzWexMHrjyUUc",
  "_FaVcHfmrqcaJq8pa3WmRw",
  "_BbrRgrcdGPMLEbBU2b6xk",
  "_gchmML4Q478zdFjhXf8rN",
  "_brNyzEdhzNAyxK8xC8hhm",
  "_YtKLMTwyMxNf1DNYqBx1t",
  "_b9HgpUXtAW8VmTy82BPDV",
  "_c8bEm1bWphwqFBXWRPrV8"
]
```

### Current Status per File:
- `Svartulfr_Scenario_Camp_Mystic.json`: Currently has 6 IDs. Missing items 7 to 15 (all 9 realism LBs).
- `Svartulfr_Scenario_SUCC_Route_Alyssa.json`: Currently has 6 IDs. Missing items 7 to 15.
- `Svartulfr_Scenario_SUCC_Route_Jasper.json`: Currently has 6 IDs. Missing items 7 to 15.
- `Svartulfr_Scenario_Villa_Douglas.json`: Currently has 6 IDs. Missing items 7 to 15.
- `Svartulfr_Scenario_DMHA_Dungeons.json`: Currently has 6 IDs. Missing items 7 to 15.
- `Svartulfr_Scenario_Underworld_Sindacato.json`: Currently has 6 IDs. Missing items 7 to 15.
- `Svartulfr_Master_Scenario.json`: Contains all 15 IDs, but in non-canonical order (`_GbWJ...` first). Must be reordered to match the canonical 1-to-15 standard.

---

## 2. Greetings and Messages Schema Analysis

### Greeting Object Schema:
Every greeting inside `data.greetings` adheres to the following JSON structure:

```json
{
  "id": "scene-unique-id",
  "name": "01. Scene Title",
  "description": "Contextual timeline and location description",
  "speaker_slot": "slot_key",
  "content": "Opening text matching the first message",
  "linked_persona_ids": [
    "persona_1786335754946",
    "1792155173728"
  ],
  "messages": [
    {
      "id": "msg-unique-id-1",
      "speaker_slot": "slot_key",
      "content": "Narrative or spoken dialogue conforming to formatting rules."
    }
  ]
}
```

### Critical Schema Findings:
1. **Persona Storage Location**: `linked_persona_ids` is an attribute of the **greeting object**, NOT of individual `messages`. Setting `linked_persona_ids` on the greeting defines which personas the Wyvern UI offers to the player in the "Offer a persona to play as" dropdown before launching the chat.
2. **Nested `linked_personas` in Master Scenario**:
   In `FINAL/Svartulfr_Master_Scenario.json`, each greeting also contains a cached `linked_personas` array of full objects:
   ```json
   {
     "persona_id": "persona_1786335754946",
     "name": "Alyssa",
     "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public",
     "title": "The White Moon",
     "comment": "Seven Hills Pack Princess & Dominant Omega Healer"
   }
   ```
   ```json
   {
     "persona_id": "1792155173728",
     "name": "Jasper",
     "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public",
     "title": "Jasper Svartr Douglas Bloodmoon",
     "comment": "MalePOV Twin Protagonist — Technomancer & Cyber-Mage at SUCC"
   }
   ```
   In the 6 files in `FINAL/scenarios/`, `linked_personas` does NOT exist (only `linked_persona_ids` is present). Wyvern API populates `linked_personas` dynamically from `linked_persona_ids` upon retrieval. For local consistency in `Svartulfr_Master_Scenario.json`, updating both `linked_persona_ids` and the cached `linked_personas` objects ensures 100% data fidelity.

---

## 3. Comprehensive Master Scenario Greetings Catalog & Classification

The Master Scenario (`FINAL/Svartulfr_Master_Scenario.json`) contains 29 greetings. Here is the exhaustive classification and verification of each greeting:

| # | Greeting ID | Scene Name / Title | Initial Speaker Slot | POV Classification | Current `linked_persona_ids` | Target `linked_persona_ids` |
|---|---|---|---|---|---|---|
| 0 | `opening` | 01. Estate a Villa Douglas: Serata Call of Duty in Famiglia | `eldest_brother` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 1 | `scene-camp-mystic-arrival` | 02. Estate a Camp Mystic: Benvenuti al Lago | `twin` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 2 | `scene-alyssa-story-1-1` | 03. [FemPOV] Cap. 1 (Parte 1): Primo Giorno di College - Partenza da Villa Douglas | `father` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |
| 3 | `scene-jasper-1` | 04. [MalePOV] Cap. 1 (Jasper): Rombo sul Viale e Addii da Villa Douglas | `father` | **[MalePOV]** | `['1792155173728']` | `['1792155173728']` (Preserve) |
| 4 | `scene-alyssa-story-1-2` | 05. Cap. 1 (Parte 2): Arrivo al Griffin Clocktower sul Campus SUCC | `twin` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 5 | `scene-succ-move-in-day` | 06. SUCC Campus: Move-in Day ai Wyrm Dormitories | `twin` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 6 | `greeting_ch27_jasper_russ_dorm` | 07. [MalePOV] Dormitori Wyrm Hall: Stanza 304 con Russ | `male_roommate` | **[MalePOV]** | `['1792155173728']` | `['1792155173728']` (Preserve) |
| 7 | `scene-alyssa-story-2-1` | 08. [FemPOV] Cap. 2: Stage Formativo HSK - Il Colloquio con Zeera (Aetheris Clinic) | `twin` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |
| 8 | `scene-alyssa-story-3-1` | 09. [FemPOV] Cap. 3 (Parte 1): Impatto sul Campo dei Bulls - Lo Scontro con Jared | `quarterback` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |
| 9 | `scene-alyssa-story-3-2` | 10. [MalePOV] Cap. 3 (Parte 2): Tunnel e Spogliatoi del Bulls Stadium post-allenamento | `quarterback` | **[MalePOV]** | `['1792155173728']` | `['1792155173728']` (Preserve) |
| 10 | `scene-succ-open-third-person` | 11. SUCC Open Campus: Lunar Quad in Pieno Semestre (3a Persona) | `friend` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 11 | `scene-succ-open-second-person` | 12. SUCC Open Campus: Lunar Quad in Pieno Semestre (2a Persona) | `twin` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 12 | `scene-alyssa-story-4-1` | 13. [FemPOV] Cap. 4: Basso Distorto al Sidewinders - Primo Incontro con Mac | `crush` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |
| 13 | `scene-guild-1` | 14. Gilda DMHA (Cap. 1): Ingresso al Desk DMHA e L'Incarico di Coach D | `twin` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 14 | `scene-guild-2` | 15. Gilda DMHA (Cap. 2): Discesa nel Rift Sotterraneo (Hive Apex Rift) | `eldest_brother` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 15 | `greeting_ch29_malachia_roman_kolya_gym` | 16. Palestra SUCC: Pesi e Tappeti con Malachia, Roman e Kolya | `eldest_brother` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 16 | `scene-alyssa-story-5-1` | 17. [FemPOV] Cap. 5: Overclock Notturno - Il Rave Clandestino di DJ Frequency | `twin` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |
| 17 | `scene-jasper-2` | 18. [MalePOV] Cap. 5 (Jasper): Sul Palco di DJ Frequency al Rave nei Magazzini | `twin` | **[MalePOV]** | `['1792155173728']` | `['1792155173728']` (Preserve) |
| 18 | `greeting_ch28_jasper_neon_purr_verve` | 19. [MalePOV] Soundclash al Verve: DJ Frequency contro Neon Purr | `uncle` | **[MalePOV]** | `['1792155173728']` | `['1792155173728']` (Preserve) |
| 19 | `scene-solarton-full-moon-festival` | 20. Solarton: Festival della Luna Piena in Town Square | `brother` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 20 | `scene-alyssa-story-6-1` | 21. [FemPOV] Cap. 6: Halloween dei BRO - La Festa di Beta Rho Omega | `quarterback` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |
| 21 | `scene-jasper-3` | 22. [MalePOV] Cap. 6 (Jasper): Pattuglia Notturna e Dragon Glass Katana al Riverbank | `twin` | **[MalePOV]** | `['1792155173728']` | `['1792155173728']` (Preserve) |
| 22 | `scene-alyssa-story-7-1` | 23. Cap. 7 (Parte 1): Pausa d'Autunno on the Road - Partenza da The Verve con Zio Logan | `uncle` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 23 | `scene-alyssa-story-7-2` | 24. Cap. 7 (Parte 2): Sosta Notturna al Neptune Diner sulla Pacific Coast Highway | `uncle` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 24 | `scene-alyssa-story-8-1` | 25. Cap. 8 (Parte 1): Solstizio d'Inverno - La Grande Veglia di Yule con Wulfnic | `maternal_grandfather` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 25 | `scene-alyssa-story-8-2` | 26. Cap. 8 (Parte 2): La Veglia Notturna sotto l'Albero Sacro con i Firstborn | `maternal_grandfather` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 26 | `scene-alyssa-story-9-1` | 27. Cap. 9: Reclute sotto Scorta - Visita Tattica di Erik e Kaladin al Campus SUCC | `father` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 27 | `scene-alyssa-story-10-1` | 28. Cap. 10: Fine del Primo Anno - Il Bivio in Cucina con Erik a Villa Douglas | `father` | **Shared/Neutral** | `[]` | `['persona_1786335754946', '1792155173728']` |
| 28 | `scene-alyssa-story-11-1` | 29. [FemPOV] Cap. 11: Fumo di Gomma, Birra e Cloro - Il Branco dei Nomads con Marek | `twin` | **[FemPOV]** | `['persona_1786335754946']` | `['persona_1786335754946']` (Preserve) |

### Summary Statistics:
- **Total Greetings**: 29
- **Shared / Neutral Greetings**: 16 (IDs: 0, 1, 4, 5, 10, 11, 13, 14, 15, 19, 22, 23, 24, 25, 26, 27)
- **`[FemPOV]` Greetings (Alyssa)**: 7 (IDs: 2, 7, 8, 12, 16, 20, 28)
- **`[MalePOV]` Greetings (Jasper)**: 6 (IDs: 3, 6, 9, 17, 18, 21)

---

## 4. Exact Modifications Required per Scenario File

### File 1: `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json`
- **Scenario ID**: `char_scenario_nLC84wrHdrbB6P3DEhwKb`
- **Scenario Type**: Dual Scenario (Jasper & Alyssa)
- **Target `lorebook_ids`**:
  Replace existing 6 IDs with the full canonical 15 IDs array:
  ```json
  "lorebook_ids": [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_Uht3Ckz44JBDrPnUHq7LV",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_GV1KyHVY1RMbCnWgLkzDG",
    "_GbWJbkhgLzWexMHrjyUUc",
    "_FaVcHfmrqcaJq8pa3WmRw",
    "_BbrRgrcdGPMLEbBU2b6xk",
    "_gchmML4Q478zdFjhXf8rN",
    "_brNyzEdhzNAyxK8xC8hhm",
    "_YtKLMTwyMxNf1DNYqBx1t",
    "_b9HgpUXtAW8VmTy82BPDV",
    "_c8bEm1bWphwqFBXWRPrV8"
  ]
  ```
- **Target `linked_persona_ids`**:
  In all 4 greetings (`scene-camp-mystic-shuttle`, `scene-camp-mystic-cabins`, `scene-camp-mystic-docks`, `scene-camp-mystic-campfire`), change:
  ```json
  "linked_persona_ids": []
  ```
  to:
  ```json
  "linked_persona_ids": [
    "persona_1786335754946",
    "1792155173728"
  ]
  ```

---

### File 2: `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`
- **Scenario ID**: `char_scenario_CKgwq246DyCj1NNTBV9rt`
- **Scenario Type**: Single Route (Alyssa)
- **Target `lorebook_ids`**:
  Replace existing 6 IDs with the full canonical 15 IDs array.
- **Target `linked_persona_ids`**:
  In all 6 greetings (`scene-alyssa-greek-row`, `scene-alyssa-labs`, `scene-alyssa-library-corner`, `scene-alyssa-ice-rink`, `scene-alyssa-bulls-tunnel`, `scene-alyssa-sidewinders`), change:
  ```json
  "linked_persona_ids": []
  ```
  to:
  ```json
  "linked_persona_ids": [
    "persona_1786335754946"
  ]
  ```

---

### File 3: `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`
- **Scenario ID**: `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`
- **Scenario Type**: Single Route (Jasper)
- **Target `lorebook_ids`**:
  Replace existing 6 IDs with the full canonical 15 IDs array.
- **Target `linked_persona_ids`**:
  In all 5 greetings (`scene-jasper-wyrm-304`, `scene-jasper-roof-hack`, `scene-jasper-quad-tension`, `scene-jasper-warehouse-rave`, `scene-jasper-bro-halloween`), change:
  ```json
  "linked_persona_ids": []
  ```
  to:
  ```json
  "linked_persona_ids": [
    "1792155173728"
  ]
  ```

---

### File 4: `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json`
- **Scenario ID**: `char_scenario_88N1eQXqkbydKX9q9XQzp`
- **Scenario Type**: Dual Scenario (Jasper & Alyssa)
- **Target `lorebook_ids`**:
  Replace existing 6 IDs with the full canonical 15 IDs array.
- **Target `linked_persona_ids`**:
  In all 5 greetings (`scene-villa-living-room`, `scene-villa-erik-study`, `scene-villa-verve-lounge`, `scene-villa-yule-vigil`, `scene-villa-kitchen-dawn`), change:
  ```json
  "linked_persona_ids": []
  ```
  to:
  ```json
  "linked_persona_ids": [
    "persona_1786335754946",
    "1792155173728"
  ]
  ```

---

### File 5: `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json`
- **Scenario ID**: `char_scenario_eqtRNnDpKbxDp7dmJmq6E`
- **Scenario Type**: Dual Scenario (Jasper & Alyssa)
- **Target `lorebook_ids`**:
  Replace existing 6 IDs with the full canonical 15 IDs array.
- **Target `linked_persona_ids`**:
  In all 4 greetings (`scene-dmha-briefing`, `scene-dmha-floor-10`, `scene-dmha-incursion-nomads`, `scene-dmha-horns-debrief`), change:
  ```json
  "linked_persona_ids": []
  ```
  to:
  ```json
  "linked_persona_ids": [
    "persona_1786335754946",
    "1792155173728"
  ]
  ```

---

### File 6: `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json`
- **Scenario ID**: `char_scenario_rrUCdBPH6WTNyBnQkMAKR`
- **Scenario Type**: Dual Scenario (Jasper & Alyssa)
- **Target `lorebook_ids`**:
  Replace existing 6 IDs with the full canonical 15 IDs array.
- **Target `linked_persona_ids`**:
  In all 4 greetings (`scene-underworld-summit`, `scene-underworld-penthouse`, `scene-underworld-harbor-ambush`, `scene-underworld-sinclair-lab`), change:
  ```json
  "linked_persona_ids": []
  ```
  to:
  ```json
  "linked_persona_ids": [
    "persona_1786335754946",
    "1792155173728"
  ]
  ```

---

### File 7: `FINAL/Svartulfr_Master_Scenario.json`
- **Scenario ID**: `char_scenario_1DC43ggb6mB8YLJDJKrU4`
- **Scenario Type**: Master Scenario (Choral Dual + Dedicated POV Greetings)
- **Target `lorebook_ids`**:
  Reorder existing 15 IDs to match the canonical 1-to-15 sequence.
- **Target `linked_persona_ids` & `linked_personas`**:
  1. For the **16 Shared/Neutral Greetings** (indices 0, 1, 4, 5, 10, 11, 13, 14, 15, 19, 22, 23, 24, 25, 26, 27):
     - Update `linked_persona_ids`:
       ```json
       "linked_persona_ids": [
         "persona_1786335754946",
         "1792155173728"
       ]
       ```
     - Update `linked_personas`:
       ```json
       "linked_personas": [
         {
           "persona_id": "persona_1786335754946",
           "name": "Alyssa",
           "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public",
           "title": "The White Moon",
           "comment": "Seven Hills Pack Princess & Dominant Omega Healer"
         },
         {
           "persona_id": "1792155173728",
           "name": "Jasper",
           "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public",
           "title": "Jasper Svartr Douglas Bloodmoon",
           "comment": "MalePOV Twin Protagonist — Technomancer & Cyber-Mage at SUCC"
         }
       ]
       ```
  2. For the **7 `[FemPOV]` Greetings** (indices 2, 7, 8, 12, 16, 20, 28):
     - Preserve existing `linked_persona_ids: ["persona_1786335754946"]` and matching `linked_personas` with Alyssa.
  3. For the **6 `[MalePOV]` Greetings** (indices 3, 6, 9, 17, 18, 21):
     - Preserve existing `linked_persona_ids: ["1792155173728"]` and matching `linked_personas` with Jasper.

---

## 5. Verification Protocol for Downstream Workers

To verify modifications locally and prevent regressions:
1. **JSON Syntax & Encoding**: All files must parse without error via `json.load()` using `utf-8`.
2. **Lorebook Length**: Every scenario file must return `len(data["lorebook_ids"]) == 15` and match `canonical_lorebook_ids`.
3. **Persona Selection Completeness**:
   - For Dual Scenarios: `all(set(g["linked_persona_ids"]) == {"persona_1786335754946", "1792155173728"} for g in data["greetings"])` must evaluate to `True`.
   - For Alyssa Single Route: `all(g["linked_persona_ids"] == ["persona_1786335754946"] for g in data["greetings"])` must evaluate to `True`.
   - For Jasper Single Route: `all(g["linked_persona_ids"] == ["1792155173728"] for g in data["greetings"])` must evaluate to `True`.
   - For Master Scenario: Exactly 16 greetings with 2 personas, 7 greetings with Alyssa only, 6 greetings with Jasper only.
4. **Live API Deployment Preparation**:
   - Prior to issuing `PUT /api/character-scenarios/:id`, workers must perform `GET /api/character-scenarios/:id` to retrieve the latest `revision` field and preserve any cloud-assigned metadata.
   - Enforce `visibility: "private"` across all payloads.

---
*Report completed by Explorer 1 (Local Scenarios Explorer).*
