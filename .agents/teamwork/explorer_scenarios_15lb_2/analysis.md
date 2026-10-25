# Detailed Technical Analysis: Live Wyvern API Scenarios & 15 Lorebooks Integration

## Executive Summary
This report documents the live state of all 7 Character Scenarios in the Svartúlfr Verse on Wyvern, the authentication token lifecycle, API communication requirements (including Cloudflare headers), the exact structure of `linked_persona_ids` on greetings, and the complete payload blueprint for PUT updates.

---

## 1. Inventory of Character Scenarios

All 7 scenario IDs have been located, cross-referenced across `GEMINI.md`, `CHANGELOG.md`, `FINAL/scenarios/`, and confirmed active on the live Wyvern API:

| # | Scenario Name | Scenario ID | Local File | Scenario Mode | Current Live Rev | Local File Rev |
|---|---------------|-------------|------------|---------------|------------------|----------------|
| 1 | Master Scenario | `char_scenario_1DC43ggb6mB8YLJDJKrU4` | `FINAL/Svartulfr_Master_Scenario.json` | Master (Dual + POV) | **27** | 26 |
| 2 | Villa Douglas | `char_scenario_88N1eQXqkbydKX9q9XQzp` | `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json` | Dual | **1** | None (null) |
| 3 | Camp Mystic | `char_scenario_nLC84wrHdrbB6P3DEhwKb` | `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json` | Dual | **1** | None (null) |
| 4 | DMHA Dungeons | `char_scenario_eqtRNnDpKbxDp7dmJmq6E` | `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json` | Dual | **1** | None (null) |
| 5 | Underworld Sindacato | `char_scenario_rrUCdBPH6WTNyBnQkMAKR` | `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json` | Dual | **1** | None (null) |
| 6 | SUCC Route Alyssa | `char_scenario_CKgwq246DyCj1NNTBV9rt` | `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` | Single (Alyssa) | **1** | None (null) |
| 7 | SUCC Route Jasper | `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` | `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json` | Single (Jasper) | **1** | None (null) |

---

## 2. Token & API Communication Verification

### Token Status & Refresh
- Initial inspection of `scratch/wyvern_token.txt` showed an existing JWT token with only ~318 seconds (~5.3 minutes) before expiration.
- Running `python scratch/refresh_token.py` successfully contacted Firebase Auth via `securetoken.googleapis.com` using the refresh token in `scratch/refresh_token.txt`.
- The token in `scratch/wyvern_token.txt` is now updated with an expiration timestamp yielding **3600 seconds (~1 hour)** of active validity.

### Cloudflare Header Guardrail
- Direct HTTP requests without browser headers trigger `HTTP 403 Forbidden` with Cloudflare `error code: 1010`.
- All requests (GET and PUT) **must** include:
  ```python
  headers = {
      'Authorization': f'Bearer {token}',
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
  }
  ```

---

## 3. Live API GET Audit Findings

Each scenario was queried via `GET https://app.wyvern.chat/api/character-scenarios/:id`. All 7 responded with `HTTP 200 OK`.

### A. Lorebook IDs Parity
- **Master Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`)**:
  - Already contains **15 lorebook IDs** live in the cloud:
    `['_GbWJbkhgLzWexMHrjyUUc', '_brNyzEdhzNAyxK8xC8hhm', '_YtKLMTwyMxNf1DNYqBx1t', '_gwwCxCfQ6PQaLEjAQVpJL', '_HfG7TeV6MJyj6bxMwxkpt', '_9zWTGqYJNJ4BCDMj8gfcD', '_EjXxkmPVhpCXg8xABpFkK', '_Uht3Ckz44JBDrPnUHq7LV', '_zwEqgEEzh12X6gHVmMKKC', '_FaVcHfmrqcaJq8pa3WmRw', '_b9HgpUXtAW8VmTy82BPDV', '_gchmML4Q478zdFjhXf8rN', '_BbrRgrcdGPMLEbBU2b6xk', '_GV1KyHVY1RMbCnWgLkzDG', '_c8bEm1bWphwqFBXWRPrV8']`
- **The 6 Thematic Scenarios**:
  - Currently contain only **6 standalone lorebook IDs**:
    `['_gwwCxCfQ6PQaLEjAQVpJL', '_HfG7TeV6MJyj6bxMwxkpt', '_9zWTGqYJNJ4BCDMj8gfcD', '_EjXxkmPVhpCXg8xABpFkK', '_zwEqgEEzh12X6gHVmMKKC', '_Uht3Ckz44JBDrPnUHq7LV']`
  - Need addition of the **9 realism lorebooks**:
    `_GV1KyHVY1RMbCnWgLkzDG` (A0 Behavioral Realism), `_GbWJbkhgLzWexMHrjyUUc` (A1 Physics), `_FaVcHfmrqcaJq8pa3WmRw` (A2 Social Realism), `_BbrRgrcdGPMLEbBU2b6xk` (A3 Medical Realism), `_gchmML4Q478zdFjhXf8rN` (A4 Cultural Realism), `_brNyzEdhzNAyxK8xC8hhm` (A5 Sex Position), `_YtKLMTwyMxNf1DNYqBx1t` (A5.5 Scene Tone), `_b9HgpUXtAW8VmTy82BPDV` (A6 World Realism), `_c8bEm1bWphwqFBXWRPrV8` (A7 Queer Realism).

### B. Greeting Representation & `linked_persona_ids` Structure
- On each greeting object:
  - `linked_persona_ids`: JSON array of persona ID strings. Example: `["persona_1786335754946", "1792155173728"]`.
  - `linked_personas`: Read-only server-hydrated array returned by GET requests containing objects with keys: `persona_id`, `name`, `avatar`, `title`, `comment`.
- In the 6 thematic scenarios:
  - All greetings currently have `linked_persona_ids: []`.
- In the Master Scenario:
  - Greetings currently have partial assignments (7 FemPOV greetings have `['persona_1786335754946']`, 6 MalePOV greetings have `['1792155173728']`, while 16 neutral/shared greetings have `[]`).
  - Requirement R2 mandates setting the 16 neutral greetings to `['persona_1786335754946', '1792155173728']`.

### Persona Identification Metadata
- **Alyssa Douglas**: ID = `persona_1786335754946`
  - Name: "Alyssa"
  - Avatar: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public`
  - Title: "The White Moon"
  - Comment: "Seven Hills Pack Princess & Dominant Omega Healer"
- **Jasper Douglas**: ID = `1792155173728`
  - Name: "Jasper"
  - Avatar: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public`
  - Title: "Jasper Svartr Douglas Bloodmoon"
  - Comment: "MalePOV Twin Protagonist — Technomancer & Cyber-Mage at SUCC"

---

## 4. Persona Assignment Mapping Rules

| Scenario | Mode | Greetings Count | Greeting Indexes & Rules | Target `linked_persona_ids` |
|---|---|---|---|---|
| **Villa Douglas** | Dual | 5 | All 5 greetings (0 to 4) | `["persona_1786335754946", "1792155173728"]` |
| **Camp Mystic** | Dual | 4 | All 4 greetings (0 to 3) | `["persona_1786335754946", "1792155173728"]` |
| **DMHA Dungeons** | Dual | 4 | All 4 greetings (0 to 3) | `["persona_1786335754946", "1792155173728"]` |
| **Underworld Sindacato** | Dual | 4 | All 4 greetings (0 to 3) | `["persona_1786335754946", "1792155173728"]` |
| **SUCC Route Alyssa** | Single | 6 | All 6 greetings (0 to 5) | `["persona_1786335754946"]` |
| **SUCC Route Jasper** | Single | 5 | All 5 greetings (0 to 4) | `["1792155173728"]` |
| **Master Scenario** | Master | 29 | **7 FemPOV** (2, 7, 8, 12, 16, 20, 28) | `["persona_1786335754946"]` |
| | | | **6 MalePOV** (3, 6, 9, 17, 18, 21) | `["1792155173728"]` |
| | | | **16 Shared/Neutral** (0, 1, 4, 5, 10, 11, 13, 14, 15, 19, 22, 23, 24, 25, 26, 27) | `["persona_1786335754946", "1792155173728"]` |

---

## 5. Blueprint for PUT Update Payload

To update each scenario via `PUT https://app.wyvern.chat/api/character-scenarios/:id`:

### Request Specifications
- Method: `PUT`
- URL: `https://app.wyvern.chat/api/character-scenarios/{scenario_id}`
- Headers:
  ```python
  {
      "Authorization": f"Bearer {token}",
      "Content-Type": "application/json",
      "Accept": "application/json",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
  }
  ```

### Payload Schema
```json
{
  "name": "<string>",
  "display_description": "<string>",
  "avatar": "<string url>",
  "tags": ["<string>", ...],
  "visibility": "private",
  "rating": "explicit",
  "revision": <integer matching fresh GET>,
  "scenario": "<string>",
  "startup_script": "<string>",
  "slots": [
    {
      "key": "<string>",
      "label": "<string>",
      "pool": ["<character_id>", ...],
      "unavailable_count": 0
    }
  ],
  "greetings": [
    {
      "id": "<string>",
      "name": "<string>",
      "description": "<string>",
      "speaker_slot": "<string>",
      "content": "<string>",
      "messages": [
        {
          "role": "<string>",
          "content": "<string>"
        }
      ],
      "linked_persona_ids": ["<persona_id_string>", ...]
    }
  ],
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
  ],
  "gallery": [],
  "linked_world_id": ""
}
```

### Critical Implementation Safeguards
1. **Fetch Fresh Revision:** Immediately before issuing PUT, call `GET /api/character-scenarios/:id` to extract the current revision integer. Inject this exact integer into the payload's `revision` key to prevent `HTTP 409 Conflict`.
2. **Pacing Delay:** Wyvern API applies rate limits. Maintain a 2.5-second pacing delay between successive PUT calls.
3. **Local File Sync:** Following each successful PUT, synchronize the updated `lorebook_ids`, `linked_persona_ids`, and the new incremented `revision` (from response or `revision + 1`) into the local JSON files:
   - `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json`
   - `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json`
   - `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`
   - `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`
   - `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json`
   - `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json`
   - `FINAL/Svartulfr_Master_Scenario.json`
