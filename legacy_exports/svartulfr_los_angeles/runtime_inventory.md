# Runtime Asset Discovery — Svartúlfr Los Angeles

**Discovery Date:** 2026-06-09
**Phase:** 15.1 — Legacy Bot Import & Repository Registration
**Scope:** Runtime asset analysis — no content modified

---

## 1. Existing Runtime Logic

### 1.1 Engine Layer (En_Core.js)

**File:** `core/En_Core.js`
**Lines:** ~1,034
**Status:** ACTIVE — Full engine pipeline

| System | Description | Status |
|---|---|---|
| **World Routing** | Multiverse dimension detection via `dimensionAliases` (modern, underworld, pack, cyber, fantasy, wasteland, regency) | ACTIVE |
| **POV Override Interceptor** | `Object.defineProperty` on `context.character.personality` to block C_Alyssa injection when C_Alyssa is the POV | ACTIVE |
| **Lorebook Compilation** | `compile()` function — deep-copies dynamicLore entries, preserves legacy + canonical schema fields | ACTIVE |
| **Runtime State** | `context.variables` management — scn_location, scn_time_of_day, scn_weather, scn_tension | ACTIVE |
| **Multiverse Gatekeeper** | Dimension detection from chat context, transition term detection, L1 active tracking | ACTIVE |
| **Atmospheric Backdrop** | Weather pools (sunny, rain, extreme, wind, night) with random triggers at message intervals | ACTIVE |
| **Vitals Mechanics** | Heart rate, temperature tracking with keyword-triggered changes and random ticks | ACTIVE |
| **Narrative Engines** | Safe zone turns, user stress streak, travel/fatigue protocol, care escalation | ACTIVE |
| **Diegetic UI Hints** | Per-dimension UI templates (cyber, modern, pack, fantasy) — comms, logs, alerts, social, whisper | ACTIVE |
| **Media/Social Engine** | Gossip, broadcast, intoxication mechanics triggered by chat content | ACTIVE |
| **Output Standardization** | HUD footer with affection, comfort, arousal, energy, HR, temperature | ACTIVE |
| **User Settings Parser** | Parses [LANGUAGE:], [NSFW_GATE:], [DARK_THEMES:], [PROSE_STYLE:] from context | ACTIVE |
| **Static Directives Injection** | POV prohibition, GM contract, anti-omniscience, prose standards, NSFW gate, dark themes | ACTIVE |
| **Session Checkpoint** | OOC summary every 25 messages | ACTIVE |

**Known Technical Debt (documented in En_Core.js):**
- DEBT-001: Legacy runtime variable names (mv_active_l1, mv_prev_l1)
- DEBT-002: POV Override identity parsing constrained until ADR_008
- DEBT-003: World-specific lore in En_Core (Douglas Estate, Solarton, Bloodmoon, Ambrosia)
- DEBT-004: WORLD_REGISTRY / Runtime Taxonomy Divergence
- DEBT-005: Lorebook Runtime Schema Divergence (dual-field: legacy + canonical)

### 1.2 Experience Layer (Ex_LosAngeles.js)

**File:** `bots/ensemble/Ex_LosAngeles.js`
**Lines:** ~261
**Status:** ACTIVE — Experience-specific lorebook pipeline

| System | Description | Status |
|---|---|---|
| **POV Override** | Sets `mv_pov_override = "C_Alyssa"` in context.variables | ACTIVE |
| **dynamicLore Pipeline** | Initializes empty dynamicLore array, runs through compile/priority/select pipeline | ACTIVE |
| **Shared Engine Pattern** | Replicates En_Core.js pipeline (compile, pP, priority buckets, selection) | ACTIVE |

**Observation:** Ex_LosAngeles.js contains a standalone copy of the engine pipeline rather than importing En_Core.js. This is consistent with JanitorAI's isolated execution model.

### 1.3 World Layer (W_Contemporary.js)

**File:** `worlds/contemporary/W_Contemporary.js`
**Lines:** ~626
**Status:** ACTIVE — LA scenario lorebook

| System | Description | Status |
|---|---|---|
| **14 Triggerable Entries** | Location, domain, event, lineage, NPC, and multi-presence lore entries | ACTIVE |
| **Tag-Based Chaining** | Entries trigger via `andAnyTags` (scenario_losangeles_active, etc.) | ACTIVE |
| **Keyword Matching** | Standard keyword + regex matching on normalized chat window | ACTIVE |
| **User Relation Mode** | Sets `mv_user_relation_mode = "relative"` | ACTIVE |
| **Twin Profile** | Sets `mv_canon_twin_profile = "char_Alyssa"` | ACTIVE |

### 1.4 Character Layer (C_*.js)

**Files:** C_Erik.js, C_Jasper.js, C_Logan.js, C_Malachia.js, C_Noah.js, C_Wulfnic.js
**Status:** ACTIVE — World-aware character micro-engines

**Shared Pattern (all character scripts):**
- `C_ENTRIES` array with world-filtered entries
- Key matching against chat window (last 5 messages)
- Limit of 8 entries max per activation
- World-aware filtering via `context.variables.mv_active_l1`

**World Coverage (C_Erik.js, C_Jasper.js):**

| World ID | C_Erik.js | C_Jasper.js |
|---|---|---|
| modern | YES | YES |
| pack | YES | YES |
| cyber | YES | YES |
| jarn (fantasy) | YES | YES |
| djfrequency | YES | YES |
| underworld | YES | N/A |

### 1.5 Behavior Layer

**relationship_engine.js:**
| System | Description | Status |
|---|---|---|
| Trust State | 0-100 scale with 4 tiers (Low/Cautious/Friendly/Deep) | ACTIVE |
| Relationship State | 7-state machine (stranger/acquaintance/friend/close friend/partner/mate/enemy/family) | ACTIVE |
| Attraction Modifier | svart_attraction variable injection | ACTIVE |
| Family Dynamic | svart_family_dynamic variable injection | ACTIVE |

**state_engine.js:**
| System | Description | Status |
|---|---|---|
| Emotion State | fear/anger/protectiveness/affection | ACTIVE |
| Scenario State | school/workplace/home/mission/combat | ACTIVE |
| Pack Status | alpha/omega/outsider | ACTIVE |
| Current Role | svart_current_role variable injection | ACTIVE |

**Note:** state_engine.js has a bug — `inject` variable is used without initialization (line 14: `inject += ...` should be `var inject = "\n\n[BEHAVIOR - STATE ENGINE]";` first).

---

## 2. Lorebook Architecture

### 2.1 Layer Structure

| Layer | File(s) | JanitorAI Label | Purpose |
|---|---|---|---|
| L0 (Engine) | En_Core.js | Core Engine | NSFW gate, behavioral guidelines |
| L1 (Core) | En_Core.js (embedded) | Core Mechanics | World routing, POV, state |
| L2 (World) | W_Contemporary.js | Scenario & Domain | LA-specific locations, events, NPCs |
| L3 (Character) | C_*.js | Character Profiles | Per-character identity, world-aware variants |

### 2.2 Activation Order (JanitorAI Runtime)

```
1. En_Core.js (L0/L1) — Always first
2. W_Contemporary.js (L2) — Scenario/domain context
3. C_*.js (L3) — Highest insertion priority per character
```

### 2.3 Lorebook Entry Schema

**Dual-field system (DEBT-005):**

| Legacy Field | Canonical Field | Status |
|---|---|---|
| keywords | key | Both populated |
| layer | category | Both populated |
| text | content | Both populated |
| priority | priority | Same value |
| world | world | Same value (array) |
| — | uid | Canonical only |
| — | keysecondary | Canonical only |
| — | related | Canonical only |
| — | tags | Canonical only |
| — | comment | Canonical only |
| — | disable | Canonical only |
| — | order | Canonical only |

Runtime uses legacy fields; canonical fields coexist for future migration.

### 2.4 Trigger Mechanism

All lorebook scripts use the same pipeline:
1. **compile()** — Deep-copies dynamicLore entries
2. **Keyword Match** — Tests normalized chat window against entry keywords
3. **Priority Sort** — Buckets by priority (1-5), processes 5→1
4. **Selection Limit** — APPLY_LIMIT caps total activated entries (default: 8)
5. **Tag Chaining** — Secondary pass for tag-triggered entries
6. **Injection** — Appends personality/scenario text to `context.character`

---

## 3. Reusable Components

### 3.1 Engine Pipeline (compile/pP/selection)

**Location:** En_Core.js (lines 827-1034), replicated in Ex_LosAngeles.js (lines 83-261)
**Reusability:** HIGH — Standard pattern across all SvartúlfrVerse lorebook scripts
**Components:**
- `compile(src)` — Entry deep-copy with keyword/shift preservation
- `pP(e, aTS)` — Priority evaluation function (requires, requireAll, requireAny, block, tags, probability)
- `hasTerm(txt, t)` — Normalized text matching with partial support
- `isAO(e)` — Always-on entry detection
- Bucket-based priority selection with APPLY_LIMIT

### 3.2 Character Micro-Engine Pattern

**Location:** C_Erik.js, C_Jasper.js (and presumably C_Logan.js, C_Malachia.js, C_Noah.js, C_Wulfnic.js)
**Reusability:** HIGH — Standard pattern for all character scripts
**Components:**
- `C_ENTRIES[]` array with keys/world/text fields
- World filtering via `mv_active_l1`
- Key matching against chat window
- 8-entry activation limit

### 3.3 POV Override System

**Location:** En_Core.js (lines 164-196), Ex_LosAngeles.js (lines 76-78)
**Reusability:** MEDIUM — Pattern reusable for other ensemble bots with POV overrides
**Components:**
- `mv_pov_override` variable setting (experience layer)
- `Object.defineProperty` interceptor (engine layer)
- Name-based blocking logic

### 3.4 Vitals & Atmosphere System

**Location:** En_Core.js
**Reusability:** MEDIUM — Useful for immersive scenarios but tightly coupled to En_Core
**Components:**
- Heart rate / temperature tracking
- Keyword-triggered vital changes
- Random tick variations
- Weather pools with probability triggers

### 3.5 Diegetic UI System

**Location:** En_Core.js (lines 653-714)
**Reusability:** HIGH — Per-dimension UI templates reusable across world-specific bots
**Components:**
- `DIEGETIC_UI_BY_L1` — Per-dimension UI hint templates
- Trigger categories: LOG/SCROLL, COMMS, ALERT, SOCIAL, WHISPER

### 3.6 Behavior Engines

**Location:** relationship_engine.js, state_engine.js
**Reusability:** HIGH — Generic behavior systems usable by any bot
**Components:**
- Trust state machine (0-100)
- Relationship state machine (7 states)
- Emotion state machine (4 states)
- Scenario state machine (4 states)
- Pack status (3 states)

---

## 4. Obsolete Components

### 4.1 Confirmed Obsolete

| Component | Location | Reason |
|---|---|---|
| **EX_LosAngeles.md "Alternate Universes" section** | Lines 283-306 | References external bots (Werewolf Pack, Cyberpunk, Warlord's Merchant) that are not part of this experience; cross-linking content with no runtime function |
| **C_Jasper.js Jarn name "Jorund"** | C_Jasper.js line 20 | Jarn-Gildi name variant not referenced in export; world-specific variant for a scenario not active in the LA export |
| **C_Erik.js Jarn name "Eirikr"** | C_Erik.js line 20 | Same as above |

### 4.2 Potentially Obsolete (requires runtime validation)

| Component | Location | Reason |
|---|---|---|
| **DEBT-003 world references** | En_Core.js | Hard-coded references to Solarton, Bloodmoon, Ambrosia in engine core — should be in World files |
| **WORLD_REGISTRY** | En_Core.js (lines 327-396) | Documentation-only registry; runtime uses legacy `dimensionAliases`. Registry duplicates data without runtime effect |
| **State engine `inject` initialization bug** | state_engine.js line 14 | `inject` variable used without `var inject = ...` declaration. May work due to hoisting in non-strict mode but is technically broken |
| **C_*.js underworld entries** | C_Erik.js, C_Jasper.js | Underworld (Ballantine, Ambrosia, Sinners) entries exist in character scripts but are not referenced by the LA export scenario |

### 4.3 Legacy-Only (no canonical counterpart)

| Component | Location | Notes |
|---|---|---|
| **Advanced Prompt (JanitorAI-specific)** | original_export.md lines 776-791 | `<PLUGIN>`, `<GOOGLESEARCH>`, `<NPCNEEDS>`, `<VIOLENCETORTURE>`, `<AAUTOPLOT>`, `<SLICEOFLIFE>`, `<BETTERSPICE>` — JanitorAI-specific tags with no repository equivalent |
| **SoundCloud integration** | original_export.md / Ex_LosAngeles.md | JanitorAI-specific soundtrack feature; no runtime script counterpart |
| **JanitorAI visibility settings** | original_export.md | Public/private, show definition, allow proxies — platform-specific metadata |
| **JanitorAI tags** | original_export.md | 👨 Male, 🧑‍🎨 OC, 👭 Multiple, etc. — JanitorAI-specific emoji tags |

---

## 5. Runtime Execution Context

**Platform:** JanitorAI
**Scripting Model:** Isolated per-lorebook execution
**Execution Order:** L0 → L1 → L2 → L3 (engine → core → world → character)
**Shared State:** `context.character`, `context.variables`, `context.chat` (platform-provided)
**No Inter-Script Communication:** Each lorebook script runs independently; communication via `context.variables` only
**ES5 Only:** No ES6+ syntax permitted

---

## 6. Summary

| Category | Count | Notes |
|---|---|---|
| **Active Engine Systems** | 14 | In En_Core.js |
| **Lorebook Entries (export)** | 12 | In original_export.json |
| **Lorebook Entries (source)** | 14 | In W_Contemporary.js |
| **Character Scripts** | 6 | All with world-aware micro-engines |
| **Behavior Scripts** | 2 | Relationship + State engines |
| **Reusable Component Patterns** | 6 | Pipeline, micro-engine, POV, vitals, diegetic UI, behavior |
| **Obsolete Components** | 3 confirmed | Cross-world links, Jarn names |
| **Potentially Obsolete** | 4 | World debt, registry, state bug, underworld entries |
| **Legacy-Only Components** | 4 | Platform-specific features |

---

*Generated by Phase 15.1 — Legacy Bot Import & Repository Registration*
*Analysis only — no content modified*
