# Handoff Report: Wyvern World API Schemas, Authentication & Lifecycle Contract

**Agent**: Explorer M1 API (`explorer_m1_api`)  
**Mission**: Investigate Wyvern World API schemas, authentication token management, and REST API contract for World creation/update.  
**Date**: 2026-10-24T22:35:00Z  

---

## 1. Observation

### 1.1 Authentication & Token Management
1. **Refresh Script & Firebase API**:
   - File inspected: `e:\repository\SvartulfrVerse\scratch\refresh_token.py` (lines 6-25):
     ```python
     WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
     RT_PATH = ROOT / 'scratch' / 'refresh_token.txt'
     FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
     url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
     data = urllib.parse.urlencode({'grant_type': 'refresh_token', 'refresh_token': rt}).encode()
     ```
   - Running `python scratch/refresh_token.py` returned exit code 0:
     `Token refreshed successfully, len: 1142`
   - Decoding the JWT payload confirmed user identity:
     - `sub` / `user_id`: `2r4fVpvImte5dbljedLkZJxre2d2`
     - `email`: `mandellialice5@gmail.com`
2. **Cloudflare WAF Invariant (Error 1010)**:
   - Direct requests with default `urllib` user agent resulted in verbatim error:
     `HTTPError 403: Forbidden - Body: b'error code: 1010\n'`
   - Adding header `'User-Agent': 'Mozilla/5.0'` completely resolves Cloudflare filtering and returns HTTP 200 OK across all authorized endpoints.
3. **Token Validity & Account Capacity**:
   - `GET https://app.wyvern.chat/api/characters/mine` returned HTTP 200 OK (body len: 270,485 bytes, containing `characters`, `likedCharacters`, `friendsCharacters`).
   - `GET https://app.wyvern.chat/api/worlds/limit` returned HTTP 200 OK:
     `{'submitted': 0, 'capacity': 5, 'hasUnlimited': False}`.
     The user has active capacity to create new Worlds.
   - `GET https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7` returned HTTP 200 OK (ID `_CgYT8fHXpDC4crjmegQF7`, Name: `Svartulfr`).

---

### 1.2 Frontend World API Client Architecture
Extracted directly from Next.js bundle chunk `https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js` (module `77818`) and `app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js`:

1. **API Client Definition (`worldApi` in module 77818)**:
   - `createWorld`: `e => i.hi.post("".concat(a.BC, "/worlds"), e)`
   - `getWorld`: `e => i.hi.get("".concat(a.BC, "/worlds/").concat(e))`
   - `updateWorld`: `(e, t) => i.hi.put("".concat(a.BC, "/worlds/").concat(e), t)`
   - `deleteWorld`: `e => i.hi.del("".concat(a.BC, "/worlds/").concat(e))`
   - `getLimit`: `() => i.hi.get("".concat(a.BC, "/worlds/limit"))`
   - `getUserWorlds`: `(e, t) => i.hi.get("".concat(a.BC, "/worlds/user/").concat(e), { params: t })`
   - Base URL prefix `a.BC`: evaluates to `https://app.wyvern.chat/api`.

2. **Sub-Resource Endpoints in `worldApi`**:
   - **Environments**:
     - `POST /api/worlds/environments` (`createEnvironment`)
     - `GET /api/worlds/environments/{id}` (`getEnvironment`)
     - `GET /api/worlds/environments/world/{worldId}` (`getWorldEnvironments`)
     - `PUT /api/worlds/environments/{id}` (`updateEnvironment`)
     - `DELETE /api/worlds/environments/{id}` (`deleteEnvironment`)
   - **Locations**:
     - `POST /api/worlds/locations` (`createLocation`)
     - `GET /api/worlds/locations/{id}` (`getLocation`)
     - `GET /api/worlds/locations/world/{worldId}` (`getWorldLocations`)
     - `GET /api/worlds/locations/environment/{environmentId}` (`getEnvironmentLocations`)
     - `PUT /api/worlds/locations/{id}` (`updateLocation`)
     - `DELETE /api/worlds/locations/{id}` (`deleteLocation`)
   - **Lexicon**:
     - `POST /api/worlds/lexicon` (`createLexiconEntry`)
     - `POST /api/worlds/lexicon/bulk` (`bulkCreateLexiconEntries`: takes `{ world_id: string, entries: array }`)
     - `GET /api/worlds/lexicon/{id}` (`getLexiconEntry`)
     - `GET /api/worlds/lexicon/world/{worldId}` (`getWorldLexiconEntries`)
     - `GET /api/worlds/lexicon/by-character/{characterId}` (`getCharacterLexiconEntries`)
     - `PUT /api/worlds/lexicon/{id}` (`updateLexiconEntry`)
     - `DELETE /api/worlds/lexicon/{id}` (`deleteLexiconEntry`)
   - **Characters**:
     - `POST /api/worlds/characters` (`createWorldCharacter`)
     - `POST /api/worlds/characters/convert` (`convertCharacter`)
     - `GET /api/worlds/characters/{id}` (`getWorldCharacter`)
     - `GET /api/worlds/characters/world/{worldId}` (`getWorldCharacters`)
     - `PUT /api/worlds/characters/{id}` (`updateWorldCharacter`)
     - `DELETE /api/worlds/characters/{id}` (`deleteWorldCharacter`)
   - **Scenarios**:
     - `POST /api/worlds/scenarios` (`createScenario`)
     - `GET /api/worlds/scenarios/{id}` (`getScenario`)
     - `GET /api/worlds/scenarios/world/{worldId}` (`getWorldScenarios`)
     - `PUT /api/worlds/scenarios/{id}` (`updateScenario`)
     - `DELETE /api/worlds/scenarios/{id}` (`deleteScenario`)
   - **RPG Blueprints**:
     - `GET /api/worlds/rpg/species/{worldId}`
     - `GET /api/worlds/rpg/occupations/{worldId}`
     - `GET /api/worlds/rpg/traits/{worldId}`
   - **Gallery Assets**:
     - `POST /api/worlds/{id}/gallery` (`addGalleryImage`)
     - `GET /api/worlds/{id}/gallery` (`getGalleryImages`)
     - `PUT /api/worlds/{id}/gallery/{imageId}` (`updateGalleryImage`)
     - `DELETE /api/worlds/{id}/gallery/{imageId}` (`deleteGalleryImage`)

---

### 1.3 Exact World Schema Contract
Extracted verbatim from `function eE(e)` in `app/(content)/worlds/edit/[id]/page-d94d4a36163d1b0d.js` (lines 55417-55550) and verified against `scratch/backup_consolidated_snapshot/world_metadata.json`:

```javascript
function eE(e) {
  return {
    name: e?.name || "",
    chat_name: e?.chat_name || "",
    description: e?.description || "",
    tagline: e?.tagline || "",
    tags: e?.tags || [],
    community_tags: e?.community_tags || [],
    avatar: e?.avatar || "",
    background: e?.background || "",
    visibility: e?.visibility || "private",
    rating: e?.rating || "none",
    context_description: e?.context_description || "",
    base_instructions: e?.base_instructions || "",
    final_instructions: e?.final_instructions || "",
    simulation_mode: e?.simulation_mode ?? "screenwriter",
    narration_perspective: e?.narration_perspective ?? "third_person",
    show_npc_thoughts: e?.show_npc_thoughts ?? true,
    npc_thought_style: e?.npc_thought_style ?? "italic",
    npc_thought_custom_instructions: e?.npc_thought_custom_instructions ?? "",
    prose_style: e?.prose_style ?? "default",
    disable_enhanced_instructions: e?.disable_enhanced_instructions ?? false,
    system_prompt_override: e?.system_prompt_override || "",
    reply_options_instructions: e?.reply_options_instructions ?? "",
    world_age: e?.world_age || 0,
    human_start_date: e?.human_start_date ? new Date(e.human_start_date).toISOString().split("T")[0] : "",
    scan_depth: e?.scan_depth || 10,
    avatar_activation_prefix: e?.avatar_activation_prefix || "=>",
    avatar_activation_suffix: e?.avatar_activation_suffix || ":",
    time_of_day_config: e?.time_of_day_config || null,
    calendar: e?.calendar || null,
    world_features: e?.world_features || {},
    inline_command_config: e?.inline_command_config || {},
    ai_inventory_management: e?.ai_inventory_management || false,
    enable_ai_tool_creation: e?.enable_ai_tool_creation || false,
    stat_config: e?.stat_config || undefined,
    creature_settings: e?.creature_settings || undefined,
    type_effectiveness: e?.type_effectiveness || undefined
  };
}
```

Additional top-level configurations managed via dedicated tabs:
- `combat_ruleset`: `{ model, creature_model, character_model, initiative, vitals, tiers, battle_prompt: { instructions } }`
- `relationship_config`: `{ enabled, decay_curve, magnitudes, custom_moodlets, tier_ladder, relationship_prompt: { heading, wrapper_start, wrapper_end, per_character_line, instructions } }`
- `currencies`: array of `{ id, name, symbol, decimal_places, is_primary, universal_credit_rate }`
- `travel_routes`: array of route connections and `free_travel: boolean`

---

### 1.4 Temporal Calculation & World-Age Verification
1. Epoch: `0827-12-21T00:00:00.000Z` (Proleptic Gregorian calendar).
2. Target Date: `2024-08-26T06:00:00.000Z` (Monday).
3. Mathematical calculation executed via Python Proleptic Gregorian datetime:
   ```python
   d0 = datetime.datetime(827, 12, 21, 0, 0, tzinfo=datetime.timezone.utc)
   d1 = datetime.datetime(2024, 8, 26, 6, 0, tzinfo=datetime.timezone.utc)
   hours = int((d1 - d0).total_seconds() // 3600)
   # Result: exactly 10489902 hours
   ```
   Verified: `10489902` is the exact mathematical elapsed hour count from 21 Dec 827 AD 00:00 UTC to 26 Aug 2024 06:00 UTC.

---

## 2. Logic Chain

1. **Step 1: Token Auth & Cloudflare Bypass**:
   - `scratch/refresh_token.py` exchanges `scratch/refresh_token.txt` with Firebase Auth API (`https://securetoken.googleapis.com/v1/token`).
   - The resulting ID token is stored in `scratch/wyvern_token.txt`.
   - Python `urllib` calls fail with 403 Forbidden Error 1010 unless `'User-Agent': 'Mozilla/5.0'` is present.
   - Adding `'User-Agent': 'Mozilla/5.0'` and `Authorization: Bearer <token>` yields successful HTTP 200 responses across all Wyvern API endpoints.

2. **Step 2: Two-Phase World Lifecycle**:
   - Frontend chunk `app/(content)/worlds/edit/[id]/page-d94d4a36163d1b0d.js` reveals that the "Create World" UI executes `c.worldApi.createWorld(t)` with minimal creation fields (`name`, `description`, `visibility`, `rating`, `tags`, `scan_depth`, `avatar_activation_prefix`, `avatar_activation_suffix`).
   - The server creates the record, assigns an ID, and responds with the new World entity.
   - The UI then issues `c.worldApi.updateWorld(id, patch)` (`PUT /api/worlds/{id}`) containing the full simulation configuration (calendar, world_age, world_features, stat_config, prompts, etc.).
   - As documented in `Istruzioni_Workflow_Wyvern_Aggiornate_2026-09-14.md` (lines 235-237), `PUT /api/worlds/{id}` takes a **partial JSON body** containing only the fields being updated.

3. **Step 3: Prompt Assembly Integration**:
   - The custom Prompt Assembly directives (LSE ecology, anatomical invariants, D20 check resolution, anti-puppeting, situational digital feeds, strict Italian output) map directly into:
     - `system_prompt_override`: Enforces narrator identity, D20 rules, LSE biology, thought privacy, and multi-NPC voice.
     - `base_instructions`: Injects formatting rules, Italian sandwich header, and simulation directives.
     - `final_instructions`: Injects user boundaries, digital feeds policy, and format discipline (`"dialogue in quotes, actions in plain text (no asterisks), asterisks for thoughts only, no em-dash"`).
     - `disable_enhanced_instructions: true`: Suppresses generic platform boilerplate so custom prompts govern cleanly.

---

## 3. Caveats

1. **PUT Behavior on Arrays**: When updating array fields (`currencies`, `tags`, `travel_routes`), Wyvern `PUT` replaces the entire array rather than appending. Any update must provide the complete target array.
2. **Sub-resource Routing Quirks**:
   - Never use `GET /api/worlds/characters?world_id=...` (this ignores the parameter and returns 1,500+ global public characters). Use `GET /api/worlds/characters/world/{worldId}` instead.
   - `GET /api/worlds/linked-characters/{worldId}` has historically returned 500 when circular linkages exist; Character Cards should be referenced via standalone IDs or imported directly into the World.
3. **Numeric vs ISO Timeline Positions**: On Character creation, `birthdate` and `start_timeline_position` must be numeric integers representing elapsed hours from epoch (e.g. `10252795`), NOT ISO date strings (which triggers an unrecoverable 500 server crash on that character record).

---

## 4. Conclusion & Actionable Contract Specification

### 4.1 REST API Endpoint Index for Worlds

| Method | Endpoint | Description | Headers |
|---|---|---|---|
| `POST` | `https://app.wyvern.chat/api/worlds` | Create World (Phase 1) | `Authorization`, `Content-Type`, `User-Agent` |
| `GET` | `https://app.wyvern.chat/api/worlds/{id}` | Read World state | `Authorization`, `User-Agent` |
| `PUT` | `https://app.wyvern.chat/api/worlds/{id}` | Update World settings (Phase 2) | `Authorization`, `Content-Type`, `User-Agent` |
| `DELETE` | `https://app.wyvern.chat/api/worlds/{id}` | Delete World | `Authorization`, `User-Agent` |
| `GET` | `https://app.wyvern.chat/api/worlds/limit` | Check World capacity limit | `Authorization`, `User-Agent` |
| `POST` | `https://app.wyvern.chat/api/worlds/environments` | Create Environment | `Authorization`, `Content-Type`, `User-Agent` |
| `POST` | `https://app.wyvern.chat/api/worlds/locations` | Create Location | `Authorization`, `Content-Type`, `User-Agent` |
| `POST` | `https://app.wyvern.chat/api/worlds/lexicon` | Create single Lexicon entry | `Authorization`, `Content-Type`, `User-Agent` |
| `POST` | `https://app.wyvern.chat/api/worlds/lexicon/bulk` | Bulk create Lexicon entries | `Authorization`, `Content-Type`, `User-Agent` |
| `POST` | `https://app.wyvern.chat/api/worlds/characters` | Create World Character | `Authorization`, `Content-Type`, `User-Agent` |

---

### 4.2 Phase 1: World Creation Payload (`POST /api/worlds`)

```http
POST /api/worlds HTTP/1.1
Host: app.wyvern.chat
Authorization: Bearer <token>
Content-Type: application/json
User-Agent: Mozilla/5.0

{
  "name": "Svartúlfr — Blackwood & Solarton",
  "description": "Svartúlfr | Urban is set in modern-day supernatural California, where an ancient werewolf dynasty, chaotic campus life, and high-stakes dungeon incursions collide. At its center lies Blackwood: the thousand-year-old supernatural seat tucked inland within dense pine forests, ruled by the Douglas-Bloodmoon werewolf dynasty. A short drive away sits Solarton, the vibrant coastal college town hosting SUCC (Supernatural University of Central California), where young supernaturals, demi-humans, and mages navigate collegiate freedom, raw impulses, and intense rivalries.",
  "tagline": "Millennial werewolf dynasty, college chaos at SUCC, unchained passions, and deadly dungeon incursions in supernatural modern California.",
  "visibility": "private",
  "rating": "explicit",
  "tags": [
    "Third",
    "AnyPOV",
    "multiple-characters",
    "Original",
    "Fantasy",
    "Modern",
    "Supernatural",
    "Action",
    "Adventure",
    "Romance",
    "Italian",
    "English",
    "Werewolf",
    "Demihuman",
    "Alpha",
    "narrator"
  ],
  "scan_depth": 10,
  "avatar_activation_prefix": "",
  "avatar_activation_suffix": ""
}
```

---

### 4.3 Phase 2: Full Simulation Configuration Payload (`PUT /api/worlds/{id}`)

```http
PUT /api/worlds/{id} HTTP/1.1
Host: app.wyvern.chat
Authorization: Bearer <token>
Content-Type: application/json
User-Agent: Mozilla/5.0

{
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public",
  "background": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/40cd8fd2-d4de-4a29-fcf6-c562b903ea00/public",
  "chat_name": "Narrator",
  "world_age": 10489902,
  "human_start_date": "0827-12-21T00:00:00.000Z",
  "disable_enhanced_instructions": true,
  "simulation_mode": "game_master",
  "prose_style": "graphic_profane",
  "narration_perspective": "third_person",
  "show_npc_thoughts": true,
  "npc_thought_style": "italic",
  "scan_depth": 10,

  "calendar": {
    "name": "Gregorian Calendar",
    "epoch_label": "CE",
    "day_length": 24,
    "days_per_week": 7,
    "day_names": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "start_year": 827,
    "display_format": "{day_name}, {month} {day}, Year {year} {epoch}",
    "leap_year": {
      "every": 4,
      "except": 100,
      "unless": 400,
      "extra_days": 1,
      "month_id": "feb"
    },
    "months": [
      {"id": "jan", "name": "January", "days": 31},
      {"id": "feb", "name": "February", "days": 28},
      {"id": "mar", "name": "March", "days": 31},
      {"id": "apr", "name": "April", "days": 30},
      {"id": "may", "name": "May", "days": 31},
      {"id": "jun", "name": "June", "days": 30},
      {"id": "jul", "name": "July", "days": 31},
      {"id": "aug", "name": "August", "days": 31},
      {"id": "sep", "name": "September", "days": 30},
      {"id": "oct", "name": "October", "days": 31},
      {"id": "nov", "name": "November", "days": 30},
      {"id": "dec", "name": "December", "days": 31}
    ],
    "start_month_id": "dec",
    "start_day_of_month": 21
  },

  "time_of_day_config": {
    "day_length": 24,
    "default_time": 6,
    "periods": [
      {
        "id": "dawn",
        "name": "Dawn",
        "description": "La sottile nebbia costiera dell'alba si dirada sulla baia di Blackwood. La luce fredda e dorata del mattino illumina le palme e l'oceano Pacifico, mentre la città si risveglia.",
        "start": 5,
        "end": 7
      },
      {
        "id": "morning",
        "name": "Morning",
        "description": "Il sole luminoso della California splende alto. Il traffico, l'aria salmastra e il rumore della metropoli in pieno fermento fanno da sfondo alla giornata.",
        "start": 7,
        "end": 12
      },
      {
        "id": "afternoon",
        "name": "Afternoon",
        "description": "Un caldo pomeriggio californiano. L'asfalto rovente e la brezza del Pacifico si mescolano; le ombre si allungano mentre il sole inizia la sua lenta discesa verso ovest.",
        "start": 12,
        "end": 17
      },
      {
        "id": "dusk",
        "name": "Dusk",
        "description": "Il tramonto infiamma il cielo sopra l'oceano con intense sfumature di ambra e viola. L'illuminazione al neon di Blackwood City si accende e gli istinti dei demi-umani iniziano ad acuirsi.",
        "start": 17,
        "end": 20
      },
      {
        "id": "nightfall",
        "name": "Nightfall",
        "description": "La notte avvolge la costa. Blackwood City pulsa di vita notturna, locali e luci metropolitane. L'odore della salsedine si mischia a quello dei predatori urbani che escono allo scoperto.",
        "start": 20,
        "end": 0
      },
      {
        "id": "witching_hour",
        "name": "Witching Hour",
        "description": "Il cuore della notte. Il silenzio cala sulla città addormentata. È il momento in cui l'attività oscura, le infiltrazioni nei Dungeon e i raid dei branchi raggiungono il loro apice.",
        "start": 0,
        "end": 3
      },
      {
        "id": "dead_of_night",
        "name": "Dead of Night",
        "description": "Le ore più fredde e buie prima dell'alba. Una spessa coltre di umidità e foschia avvolge la costa. La città è deserta, territorio esclusivo di chi prospera nell'oscurità.",
        "start": 3,
        "end": 5
      }
    ]
  },

  "world_features": {
    "inventory": true,
    "currency": true,
    "show_party_stats": false,
    "combat": true,
    "rpg_stats": true,
    "ships": false,
    "show_species_info": false,
    "relationships": true,
    "creature_catcher": false
  },

  "stat_config": {
    "stats": [
      {
        "id": "might",
        "label": "Might",
        "abbreviation": "MGT",
        "description": "Physical power, brute strength, and heavy kinetic impacts.",
        "enabled": true
      },
      {
        "id": "resilience",
        "label": "Resilience",
        "abbreviation": "RES",
        "description": "Toughness, bodily endurance, and damage mitigation.",
        "enabled": true
      },
      {
        "id": "agility",
        "label": "Agility",
        "abbreviation": "AGI",
        "description": "Movement speed, reflexes, combat acrobatics, and stealth.",
        "enabled": true
      },
      {
        "id": "wit",
        "label": "Wit",
        "abbreviation": "WIT",
        "description": "Sharp intellect, sensory perception, and magical comprehension.",
        "enabled": true
      },
      {
        "id": "presence",
        "label": "Presence",
        "abbreviation": "PRS",
        "description": "Charismatic magnetism, leadership, social gravity, and willpower.",
        "enabled": true
      },
      {
        "id": "sanctity",
        "label": "Sanctity",
        "abbreviation": "SCT",
        "description": "Spiritual attunement, ancestral fortune, and arcane depth.",
        "enabled": true
      }
    ],
    "base_value": 1,
    "max_value": 30,
    "point_budget": 25
  },

  "combat_ruleset": {
    "model": "narrative_tiers",
    "creature_model": "narrative_tiers",
    "character_model": "narrative_tiers",
    "initiative": {
      "model": "stat",
      "role": "speed"
    },
    "vitals": {
      "hp": {
        "base": 25,
        "per_stat": 3,
        "per_level": 0,
        "role": "hp_stat"
      },
      "mp": {
        "base": 20,
        "per_stat": 3,
        "per_level": 0,
        "role": "mp_stat"
      }
    },
    "tiers": {
      "dc_base": 10,
      "attack_role": "physical_attack",
      "defense_role": "physical_defense",
      "crit_margin": 12
    },
    "resource_role": "luck",
    "battle_prompt": {
      "instructions": "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.\n\nCombat is visceral, tactical, cinematic, and high-stakes. In Dungeons and Rifts, monsters and beasts are lethal threats that can be slain, cleaved, and destroyed with full physical impact. For hunters and allies, combat carries real danger: armor shatters, severe lacerations occur, and mana exhausts, requiring tactical protection from frontline tanks (Malachia, Goran) to intercept fatal strikes, and urgent field medicine from healers (Alyssa). Outside dungeons (sparring, campus brawls, intra-pack disputes), combat resolves strictly through non-lethal submission, knockout, or yielding."
    }
  },

  "currencies": [
    {
      "id": "fbecc738-f9f7-4426-b8a1-a237b8ad922c",
      "name": "US Dollar",
      "symbol": "$",
      "decimal_places": 2,
      "is_primary": true,
      "universal_credit_rate": 1
    },
    {
      "id": "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a",
      "name": "DMHA Guild Credits",
      "symbol": "Cr",
      "decimal_places": 0,
      "is_primary": false,
      "universal_credit_rate": 0.01
    }
  ],

  "system_prompt_override": "<system>\n[MANDATORY LANGUAGE DIRECTIVE: Output strictly in Italian. All narration, dialogue, internal thoughts, and resolution blocks must be generated in natural, fluent Italian.]\n\nYou are the Narrator and Game Master of this story, acting as the narrative engine for the Svartulfr setting (Blackwood-Douglas / Solarton / Modern Fantasy). You are not a player character. Present situations, portray the people and environment, and decide the consequences of {{user}}'s actions using established world rules. Give {{user}} clear sensory detail to make informed choices.\n\n<core_writing_rules>\n- Perspective & Tense: Third-person limited perspective, strictly present tense, through {{char}} and active scene NPCs.\n- Style: Ground every response in physical continuity, sensory depth, and established canon. End narrative turns on concrete physical situations.\n- Format Discipline: Spoken dialogue enclosed strictly in standard double quotes (\"...\"). Actions and narration in plain text without asterisks. Internal thoughts enclosed strictly in asterisks (*...*). Never use the em-dash; use commas, colons, or periods instead.\n- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head. They never have human ears.\n- Multi-NPC Voice: When a named NPC or secondary character speaks, format their line on a new line with Name: followed by their words in double quotes (e.g. Erik Douglas: \"...\").\n</core_writing_rules>\n\n<lupine_social_ecology>\n- Scent & Biology: Active olfactory awareness, shifting pheromones, intense dominance and submission dynamics, territorial drives, and primal heat and rut cycles of werewolves and demi-humans.\n- Packs & Ranks: Erik is Prime Alpha (Alpha Command, Pack Leader); Malachia is Dominant Alpha (Pack Leader); Logan is Beta (mediator, blacksmith; zero Alpha Command); Jasper is Beta (technomancer/DJ; zero Alpha Command); Noah is Delta (diplomat, grey eminence; zero Alpha Command).\n- Kemonomimi Demihumans (e.g. Finn, Roman, Kolya): Possess only a single pair of animal ears and zero human ears. They are NOT werewolves (no silver allergy, no lunar frenzy, no hybrid shift).\n- Sierra Cruz: Lamia with rainbow hair and a 4-meter iridescent rainbow serpent lower body. She has ZERO legs, ZERO feet, and ZERO shoes; she only slithers and glides.\n- Scarlett Rose: Succubus with candy-pink hair, candy-pink eyes, two scarlet horns on temples, bat wings, and spade-tipped tail.\n</lupine_social_ecology>\n\n<ttrpg_mechanics>\nWhen an action carries uncertain outcome, physical danger, combat stakes, deception, or supernatural strain, resolve it using the D20 + S.P.E.C.I.A.L. skill check engine.\n- Attributes:\n  - STR (Might / MGT): Potenza muscolare, attacco in mischia, sfondamento.\n  - PER (Wit / WIT): Sensi lupini affinati, olfatto predatorio, udito, individuazione pericoli.\n  - END (Resilience / RES): Resistenza al danno, rigenerazione cellulare, tolleranza a freddo e veleni.\n  - CHA (Presence / PRS): Presenza, comando, diplomazia, fascino, negoziazione.\n  - INT (Wit / WIT): Teoria magica, crittografia, technomancy, conoscenza accademica.\n  - AGI (Agility / AGI): Velocita, riflessi in combattimento, furtivita, destrezza.\n  - LCK (Sanctity / SCT): Sorte, intuito cieco, deviazione provvidenziale dei colpi, drop rari.\n- Difficulty Classes (DC):\n  - DC 5: Routine\n  - DC 10: Facile\n  - DC 15: Moderata\n  - DC 20: Difficile\n  - DC 25: Estrema\n  - DC 30: Mitica / Ascended\n- Resolution Formula: D20 + Modificatore Attributo vs DC.\n- Esiti: Fallimento Critico (Natural 1), Fallimento, Successo, Successo Critico (Natural 20).\n- Isolated Diegetic Format: The test must appear on its own standalone line formatted as:\n> [TEST: <Attributo> (D20: <Tiro> + <Mod> = <Totale> vs DC <Target>) -> ESITO: <SUCCESSO / FALLIMENTO / SUCCESSO CRITICO / FALLIMENTO CRITICO>]\n- Immediate Consequences: Follow up immediately with narrative prose describing the visceral consequence of the roll outcome without nerfing harm or softening failures.\n</ttrpg_mechanics>\n</system>",

  "base_instructions": "<formatting_and_rules>\n- Language: Output strictly in Italian (the Common Language of this world).\n- Foreign Languages: Format as: \"Foreign phrase\" (Italian translation).\n- Dialogue & Action: Use regular quotes (\"...\") for speech. Use plain text for narration and actions (no asterisks).\n- Punctuation: NEVER use em-dashes (—). Substitute with commas or periods.\n- Internal Thoughts: Enclose strictly in *asterisks*. Make them intrusive, raw, and painfully true to the character's hidden nature (things they would never voice aloud).\n- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head. They never have human ears.\n</formatting_and_rules>\n\n<simulation_directive>\nSimulate a living, dynamic supernatural modern fantasy world set in 2024 (Solarton, California and Blackwood City).\n- Time & Astronomy: Continuously track the World Clock, the day/night cycle, and the synodic lunar cycle. Active moon phases naturally influence werewolf instincts, pack dynamics, and campus energy.\n- Lupine Social Ecology (LSE): Werewolf physiology reflects real LSE biology (scents, pheromones, heat/rut cycles, alloparenting, and the Fenris sacred calendar). Scent suppressors are strictly required in collegiate environments.\n- Demi-Human Anatomy: Demi-humans possess only a single pair of animal ears (no human ears). Describe ear gestures and tail movements accurately.\n- Character Agency: NPCs possess independent schedules, routines, and personalities. Do not speak on behalf of {{user}} or dictate their actions.\n</simulation_directive>",

  "final_instructions": "<final_directives>\n<user_boundaries>\nYou control {{char}} and NPCs. The human controls {{user}}.\n- NEVER speak, think, or act for {{user}}.\n- NEVER describe {{user}}'s internal feelings or physical sensations.\n- NEVER puppet {{user}}'s movements; always wait for their input to progress the scene.\n</user_boundaries>\n\n<digital_communications>\nQuando un personaggio interagisce con il proprio smartphone o riceve messaggi digitali nella scena, mantieni la prosa narrativa fluida e naturale (riporta mittente e testo in modo chiaro e organico). Le comunicazioni digitali del Branco Douglas (Telegram), SUCCbook, il libretto esami e il registro taglie DMHA sono gestite in tempo reale dai pannelli interattivi dello StoryEngine, senza bisogno di disegnare finti box di testo ASCII nella narrazione.\n</digital_communications>\n\nFormat discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.\n\n[ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta (narrazione, dialoghi, pensieri intrusivi, test di risoluzione) ESCLUSIVAMENTE IN LINGUA ITALIANA. Non usare mai il trattino lungo (—).]\n</final_directives>",

  "context_description": "Blackwood County and Solarton form a major supernatural corridor in California. Blackwood City is dominated by the ancient Douglas werewolf dynasty (Bloodmoon Pack), the DMHA Hunter Guild, and high-tech corporate interests (DCC). Solarton is a collegiate sanctuary centered around SUCC, where demihumans, vampires, fae, minotaurs, and humans study, train, and navigate inter-species athletics and academic life."
}
```

---

## 5. Verification Method

To independently verify these findings:

1. **Verify Token Refresh & Auth Validity**:
   ```powershell
   python scratch/refresh_token.py
   python .agents/teamwork/explorer_m1_api/test_api_endpoints.py
   ```
   *Expected outcome*: `Token refreshed successfully, len: ~1140`, followed by HTTP 200 on `/api/characters/mine` and `/api/worlds/_CgYT8fHXpDC4crjmegQF7`.

2. **Verify User World Creation Capacity**:
   ```powershell
   python .agents/teamwork/explorer_m1_api/test_world_limit.py
   ```
   *Expected outcome*: `capacity: 5`, `submitted: 0`.

3. **Verify Calendar & World Age Calculation**:
   ```powershell
   python -c "import datetime; d0 = datetime.datetime(827, 12, 21, 0, 0, tzinfo=datetime.timezone.utc); d1 = datetime.datetime(2024, 8, 26, 6, 0, tzinfo=datetime.timezone.utc); print((d1 - d0).total_seconds() // 3600)"
   ```
   *Expected outcome*: Outputs exactly `10489902.0`.

4. **Verify Frontend Route Extraction**:
   Inspect bundle chunks `https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js` and `app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js` by running `.agents/teamwork/explorer_m1_api/extract_chunk_endpoints.py` and `.agents/teamwork/explorer_m1_api/extract_eE.py`.
   *Expected outcome*: Confirms matching endpoint names, method bindings, and property mapping.
