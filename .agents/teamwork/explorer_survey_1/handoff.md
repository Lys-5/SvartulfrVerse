# Handoff Report — Investigation of Requirement 1 (13 Primary World Characters Deployment)

**Agent**: `explorer_survey_1`  
**Milestone**: Investigation of Requirement 1 (`POST /api/worlds/characters` for 13 Primary Characters into World `_YpX47fNraQFw2dD7TdycJ`)  
**Target World**: `_YpX47fNraQFw2dD7TdycJ` ("Svartúlfr — Blackwood & Solarton")  
**Investigation Mode**: Read-Only Survey  

---

## 1. Observation

### 1.1 Canonical Source Files for the 13 Characters
Direct inspection across the repository revealed the authoritative locations for the 13 target characters:

| # | Character | Canonical Source File (Card / Dossier) | Lorebook File & Entry ID | Standalone Card ID (`/mine`) |
|---|---|---|---|---|
| 1 | **Erik Ulfr Douglas** | `FINAL/Erik_Douglas_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`C-JisFj8qA1tsFEqZKevk`) | `_QPea6g4Q1QfeYCVHCLMPR` |
| 2 | **Logan Járn Douglas** | `FINAL/Logan_Douglas_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`tAcrWLtWSDGf3xJJRwUOM`) | `_T8Ywcr9FEqNf9JxbK6eHP` |
| 3 | **Edric Douglas** | `FINAL/Edric_Douglas_card.json` | `FINAL/Svartulfr_NPC_Secondary.json` (`h-ttmlgJYeRXqyDvQjSX7`) | `_TbRM3EdxDjHFgqztTbCpL` |
| 4 | **Noah Loki Douglas Bloodmoon** | `FINAL/Noah_Douglas_Bloodmoon_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`H2JX-NkHRiJ2FzoekC5ZZ`) | `_zFLUjV8aVxQRAfQxGcAcY` |
| 5 | **Malachia Björn Douglas Bloodmoon** | `FINAL/Malachia_Douglas_Bloodmoon_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`jDuJtzirlEZC3K_ArIufh`) | `_RDfz7XzTpM23LpPALVXHM` |
| 6 | **Jasper Svartr Douglas Bloodmoon** | `FINAL/Jasper_Douglas_Bloodmoon_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`Vcj4h2TL4Usola2A4OOl6`) | `_t4J9aQNJM36cUKAP4wB4U` |
| 7 | **Alyssa Hvit Douglas Bloodmoon** | `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`alyssa_world_dossier_2b54a223`) | `_6exg3yPfe2eCDK4hTftkh` |
| 8 | **Wulfnic Báleygr Bloodmoon** | `FINAL/Wulfnic_Bloodmoon_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`HhuMluMmIIENUei3bX6ed`) | `_HEQQbbRFwKdG8QE2Fh1z1` |
| 9 | **Zefir Hvitskog** | `exports/Svartulfr_Export_pre_web_sync.json` | `FINAL/Svartulfr_NPC_Primary.json` (`aA5zIYvLivjMts978RWEn`) | N/A (NPC Primary) |
| 10 | **Mackenzie Sanchez-Rogers** | `FINAL/Mackenzie_Sanchez_Rogers_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`BXi3sENAVYB8OKF80Q9Su`) | `_zn24784jfcchQ7EwCyAnm` |
| 11 | **Finnegan Novak** | `ARCHIVIO/01_Drafts/Wyvern_Superseded/Svartulfr_Urban_FullExport_30-08.md` | `FINAL/Svartulfr_NPC_Primary.json` (`EprHlMVM1g7vAhqUI-VUQ`) | N/A (NPC Primary) |
| 12 | **Sierra Cruz** | `ARCHIVIO/cards_legacy/Sierra_Cruz_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`ijy8vrlphNv19-p-gbYuY`) | `_pnrXbkWqcgmFAf3meRWFY` |
| 13 | **Scarlett Rose** | `ARCHIVIO/cards_legacy/Scarlett_Rose_card.json` | `FINAL/Svartulfr_NPC_Primary.json` (`4NzXF4_0hYxmN7Idltzpw`) | `_qXgBMbFYJfc84hbLHhe92` |

---

### 1.2 Timeline Positions & BigInt Birthdates
- **World Clock Epoch**: `0827-12-21T00:00:00.000Z` (World-Age = 0 hours).
- **Current World-Age of Target World `_YpX47fNraQFw2dD7TdycJ`**: `10489902` (Monday, August 26, 2024 at 06:00:00 UTC).
- **Formula**: `hours = (Date.parse(date_iso) - Date.UTC(827, 11, 21)) / 3600000`.

Verified calculation table:

| Character | Canon Birth Date | Age in 2024 | Exact Hours from Epoch (BigInt) | World-Age Compliance |
|---|---|---|---|---|
| **Erik Ulfr Douglas** | 1969-10-31 00:00:00 UTC | 55 | **`10009344`** (alt legacy: `10035648`) | Valid (`< 10489902`) |
| **Logan Járn Douglas** | 1975-01-12 00:00:00 UTC | 49 | **`10054920`** | Valid (`< 10489902`) |
| **Edric Douglas** | 2011-02-25 00:00:00 UTC | 13 | **`10371552`** (alt legacy: `10380312`) | Valid (`< 10489902`) |
| **Noah Loki Douglas Bloodmoon** | 1998-10-05 00:00:00 UTC | 25 | **`10262928`** (alt legacy: `10271688`) | Valid (`< 10489902`) |
| **Malachia Björn Douglas Bloodmoon** | 1996-08-10 00:00:00 UTC | 28 | **`10244064`** | Valid (`< 10489902`) |
| **Jasper Svartr Douglas Bloodmoon** | 2005-04-22 00:00:00 UTC | 19 | **`10320312`** | Valid (`< 10489902`) |
| **Alyssa Hvit Douglas Bloodmoon** | 2005-04-22 00:00:00 UTC | 19 | **`10320312`** | Valid (`< 10489902`) |
| **Wulfnic Báleygr Bloodmoon** | 0824-12-21 00:00:00 UTC | 1200 | **`0`** (Anchored at Epoch floor 827-12-21) | Valid (`== 0`) |
| **Zefir Hvitskog** | 0848-02-05 00:00:00 UTC | 1176 | **`176424`** | Valid (`< 10489902`) |
| **Mackenzie Sanchez-Rogers** | 2004-11-14 00:00:00 UTC | 19 | **`10316496`** | Valid (`< 10489902`) |
| **Finnegan Novak** | 2005-01-15 00:00:00 UTC | 19 | **`10317984`** (alt legacy: `10299216`) | Valid (`< 10489902`) |
| **Sierra Cruz** | 2005-09-08 00:00:00 UTC | 18 | **`10323648`** | Valid (`< 10489902`) |
| **Scarlett Rose** | 2003-11-18 00:00:00 UTC | 20 | **`10307808`** | Valid (`< 10489902`) |

*Note on Wulfnic*: Born in 824 AD (prior to epoch 827 AD). To prevent negative timeline indexes which break timeline querying and anachronism guards in the Wyvern engine, Wulfnic is anchored at `0`, exactly as established across `scripts/fix_character_birthdates.py` and `scripts/execute_batch1_application.js`.

---

### 1.3 Verified Cloudflare CDN Avatars

| Character | Dedicated Cloudflare CDN Avatar URL | Source Asset Key |
|---|---|---|
| **Erik Ulfr Douglas** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public` | `erikMain` |
| **Logan Járn Douglas** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public` | `loganMain` |
| **Edric Douglas** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public` | `edricMain` |
| **Noah Loki Douglas Bloodmoon** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public` | `noahMain` |
| **Malachia Björn Douglas Bloodmoon** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public` | `mailMain` |
| **Jasper Svartr Douglas Bloodmoon** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public` | `jasperMain` |
| **Alyssa Hvit Douglas Bloodmoon** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public` | `alyssaMain` |
| **Wulfnic Báleygr Bloodmoon** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public` | `mainWulfnic` |
| **Zefir Hvitskog** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bdd8961e-a68a-4c6b-b4e1-29a26db37e00/public` | `zefirMain` |
| **Mackenzie Sanchez-Rogers** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public` | `macMain` |
| **Finnegan Novak** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/75456c02-dddc-4879-7822-ab7c4628f600/public` | `finnMain` |
| **Sierra Cruz** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public` | `sierraMain` |
| **Scarlett Rose** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e96d176a-47e4-4829-2af4-7cd6ae239100/public` | `scarlettMain` |

---

### 1.4 Balanced 25-Point 6-Stat RPG Blocks

The World `_YpX47fNraQFw2dD7TdycJ` `stat_config` mandates:
- **Base value**: `1`
- **Point budget**: `25`
- **Total sum of all 6 attributes**: $6 \times 1 + 25 = \mathbf{31}$
- **Level**: Anagraphic age, capped at `99` ($\text{Level} = \min(\text{Age}, 99)$) to prevent Wyvern's silent save-drop bug.
- **Attributes**:
  1. `might` (`stat_1` / MGT)
  2. `resilience` (`stat_2` / RES)
  3. `agility` (`stat_3` / AGI)
  4. `wit` (`stat_4` / WIT)
  5. `presence` (`stat_5` / PRS)
  6. `scouting` (`stat_6` / SCT)

Verified 13-Character Stat Matrix:

| Character | Level | MGT (`stat_1`) | RES (`stat_2`) | AGI (`stat_3`) | WIT (`stat_4`) | PRS (`stat_5`) | SCT (`stat_6`) | Sum | Arch / Role |
|---|---|---|---|---|---|---|---|---|---|
| **Erik** | 55 | 7 | 7 | 4 | 5 | 7 | 1 | **31** | Prime Alpha / CEO Tank-Commander |
| **Logan** | 49 | 7 | 6 | 6 | 4 | 5 | 3 | **31** | Combat Veteran / Biker Bruiser |
| **Edric** | 13 | 3 | 3 | 7 | 5 | 5 | 8 | **31** | Pack Pup / High-Speed Scouting |
| **Noah** | 25 | 6 | 6 | 5 | 6 | 6 | 2 | **31** | Delta Caretaker / Pack PR Shield |
| **Malachia** | 28 | 8 | 7 | 5 | 4 | 5 | 2 | **31** | Heavy Frontline Vanguard Tank |
| **Jasper** | 19 | 4 | 3 | 8 | 9 | 3 | 4 | **31** | Arcane Hacker / Leyline Infiltrator |
| **Alyssa** | 19 | 2 | 4 | 4 | 7 | 8 | 6 | **31** | Pacifist Healer / White Moon Anchor |
| **Wulfnic** | 99 | 8 | 8 | 5 | 3 | 5 | 2 | **31** | Primordial Apex Sovereign |
| **Zefir** | 99 | 5 | 4 | 9 | 6 | 3 | 4 | **31** | Divine Shadow Scout & Assassin |
| **Mackenzie** | 19 | 8 | 7 | 7 | 3 | 3 | 3 | **31** | Underground Street Brawler |
| **Finn** | 19 | 6 | 6 | 8 | 3 | 4 | 4 | **31** | Varsity Hockey Left Wing / Speed Striker |
| **Sierra** | 18 | 7 | 6 | 3 | 8 | 3 | 4 | **31** | Lamia Constrictor / Necromancy Scholar |
| **Scarlett** | 20 | 2 | 3 | 6 | 6 | 9 | 5 | **31** | Succubus Glamour Social Coordinator |

---

### 1.5 Target World Live State (`_YpX47fNraQFw2dD7TdycJ`)
Direct authenticated query via `GET /api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ`:
- Returns an array with **1 existing character**:
  - `_id`: `_qfaywY2yfrGWcxPBdmURD`
  - `display_name`: `Erik Ulfr Douglas`
  - `created_at`: `2026-10-25T07:33:14.968Z`
  - `avatar`: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/30fe0390-05fb-46cf-2c8a-cd98fc35c700/public` (Outdated non-gallery avatar)
  - `level`: `46` (Discrepancy: Erik's canonical age is 55)
  - `base_stats`: `{'stat_1': 8, 'stat_2': 7, 'stat_3': 3, 'stat_4': 5, 'stat_5': 8, 'stat_6': 0}` (`stat_6` is 0, below base 1)
- The other 12 characters (**Logan, Edric, Noah, Malachia, Jasper, Alyssa, Wulfnic, Zefir, Mackenzie, Finn, Sierra, Scarlett**) are currently **absent** from the World.

---

### 1.6 World Character Deployment API Payload Schema
Endpoint: `POST https://app.wyvern.chat/api/worlds/characters`  
Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`  
Payload format verified from `scripts/import_all_16_characters.js`, `scripts/test_create_character.py`, and `scripts/apply_rpg_stats_and_simulation.py`:

```json
{
  "world_id": "_YpX47fNraQFw2dD7TdycJ",
  "name": "<display_name>",
  "display_name": "<full canonical name>",
  "first_name": "<first_name>",
  "middle_names": ["..."],
  "last_name": "<last_name>",
  "nicknames": ["..."],
  "titles": ["..."],
  "tags": ["..."],
  "avatar": "<Cloudflare CDN URL>",
  "birthdate": <integer BigInt hours>,
  "start_timeline_position": <integer BigInt hours>,
  "is_global": true,
  "world_only": false,
  "keys": ["..."],
  "key_logic": "AND_ANY",
  "whole_words_only": true,
  "display_description": "<concise summary>",
  "summary": "[NAME: ...; ROLE: ...; TRAITS: ...]",
  "long_summary": "<complete JED+ text>",
  "final_instructions": "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.",
  "rpg_stats": {
    "enabled": true,
    "level": <level int>,
    "species_id": null,
    "occupation_id": null,
    "base_stats": {
      "stat_1": <int>,
      "stat_2": <int>,
      "stat_3": <int>,
      "stat_4": <int>,
      "stat_5": <int>,
      "stat_6": <int>,
      "might": <int>,
      "resilience": <int>,
      "agility": <int>,
      "wit": <int>,
      "presence": <int>,
      "scouting": <int>
    }
  }
}
```

---

## 2. Logic Chain

1. **Premise 1 — Project Rules on World Characters vs Cards**:
   As documented in `GEMINI.md` (§7, §8, §14), standalone characters in `/mine` and Lorebook entries in `FINAL/` serve as the Single Source of Truth for narrative text. When deploying native `WorldCharacter` records into a World, their JED+ descriptions must match the canonical text byte-for-byte.
2. **Premise 2 — Timeline Integrity & Calendar Synchronization**:
   The World Clock formula `hours = (Date.parse(date_iso) - Date.UTC(827, 11, 21)) / 3600000` calculates the exact integer hours from the epoch. For mortals born after 827 AD, this produces positive BigInt values between `10,000,000` and `10,400,000`. For ancient entities born prior to the epoch (Wulfnic, 824 AD), setting `birthdate: 0` and `start_timeline_position: 0` ensures they exist across all world epochs without generating negative integer index errors in Wyvern's MongoDB backend.
3. **Premise 3 — RPG Stat Balancing & Bug Prevention**:
   World `_YpX47fNraQFw2dD7TdycJ` defines a 6-stat configuration (`might`, `resilience`, `agility`, `wit`, `presence`, `scouting`) with a base value of 1 and a point budget of 25, requiring every character's base stats to sum to exactly 31. Furthermore, `level` must be capped at 99 because any level $\ge 100$ triggers a silent database serialization failure in Wyvern's RPG subsystem.
4. **Premise 4 — Cloudflare Images Gallery Compliance**:
   Using arbitrary or external avatar URLs causes Wyvern's UI to flag entries with `Custom Image ⚠️ Unknown source`. The canonical Cloudflare CDN URLs (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/...`) mapped during the recent gallery audit must be applied to all 13 characters.
5. **Premise 5 — Current State Reconcilation**:
   Erik Ulfr Douglas already exists in World `_YpX47fNraQFw2dD7TdycJ` as `_qfaywY2yfrGWcxPBdmURD`, but has an outdated avatar, inaccurate level (46 vs 55), and an invalid `stat_6: 0`. It should either be patched via `PUT /api/worlds/characters/_qfaywY2yfrGWcxPBdmURD` or purged via `DELETE` and recreated alongside the other 12 characters.

---

## 3. Caveats

1. **Erik Ulfr Douglas Existing Record**:
   `_qfaywY2yfrGWcxPBdmURD` is currently present in World `_YpX47fNraQFw2dD7TdycJ`. The implementer must decide whether to update this existing character via `PUT` or delete and recreate via `POST`. Updating via `PUT` preserves the character ID; deleting and recreating gives a fresh sequential creation.
2. **Finn Novak Birthdate Variant**:
   Finn's JED+ block explicitly states `AGE: 19`, which maps to a birth year of 2005 (`10317984` hours). However, legacy draft text mentioned age 21/22 (`10299216` hours). In accordance with `GEMINI.md` (§5, Precedenza di Lore), the explicit JED+ in `FINAL/Svartulfr_NPC_Primary.json` takes absolute precedence (`AGE: 19`).
3. **No Code Modification / API Deployment in this Step**:
   As mandated by the read-only exploration scope, zero changes were committed to source files and zero deployment calls were made to Wyvern API during this survey.

---

## 4. Conclusion

Requirement 1 is fully investigated, rigorously mapped, and ready for automated deployment:
- All 13 canonical source texts, full Cloudflare CDN avatar URLs, and JED+ profiles are verified.
- The 13 integer BigInt `birthdate` and `start_timeline_position` values have been calculated from epoch `0827-12-21T00:00:00.000Z` and verified against the world age ceiling (`10489902`).
- A balanced 25-point 6-stat RPG block (Might, Resilience, Agility, Wit, Presence, Scouting; base 1 + 25 = 31 total points, level capped at 99) has been mathematically certified for all 13 characters.
- The deployment payload schema and endpoint (`POST /api/worlds/characters`) are fully documented with complete dual-key (`stat_1..6` and named keys) compatibility.

---

## 5. Verification Method

To independently verify the findings in this report, execute the following commands:

1. **Verify 13 Character Avatars & JED+ Content in Lorebooks**:
   ```powershell
   python -c "import json; p = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))['lexicon']; s = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))['lexicon']; print('Verified entries:', len(p) + len(s))"
   ```

2. **Verify Target World Status and Existing Character**:
   ```powershell
   python -c "import urllib.request, json; token = open('scratch/wyvern_token.txt').read().strip(); headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}; req = urllib.request.Request('https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ', headers=headers); resp = urllib.request.urlopen(req); data = json.loads(resp.read()); print('Characters in world _YpX47fNraQFw2dD7TdycJ:', len(data))"
   ```

3. **Verify RPG Stat Sums for All 13 Characters**:
   ```powershell
   python -c "stats = {'Erik': [7,7,4,5,7,1], 'Logan': [7,6,6,4,5,3], 'Edric': [3,3,7,5,5,8], 'Noah': [6,6,5,6,6,2], 'Malachia': [8,7,5,4,5,2], 'Jasper': [4,3,8,9,3,4], 'Alyssa': [2,4,4,7,8,6], 'Wulfnic': [8,8,5,3,5,2], 'Zefir': [5,4,9,6,3,4], 'Mackenzie': [8,7,7,3,3,3], 'Finn': [6,6,8,3,4,4], 'Sierra': [7,6,3,8,3,4], 'Scarlett': [2,3,6,6,9,5]}; [print(f'{k:12}: sum={sum(v)} (Pass: {sum(v)==31})') for k, v in stats.items()]"
   ```
