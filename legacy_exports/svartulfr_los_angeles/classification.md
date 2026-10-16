# Repository Classification — Svartúlfr Los Angeles

**Classification Date:** 2026-06-09
**Phase:** 15.1 — Legacy Bot Import & Repository Registration
**Scope:** Classification only — no content modified

---

## 1. Bot Archetype

**Classification:** ENSEMBLE

**Rationale:**
- Multiple NPCs driven simultaneously (Malachia, Noah, Jasper, Wulfnic, Erik, Logan)
- Experience-focused: the family dynamic is the product
- POV Slot assigned to {{user}} (player-defined character)
- Player Avatar exists outside the NPC cast (Alyssa persona available as fallback)
- Directory convention: `bots/ensemble/`

---

## 2. Primary Character

**Classification:** ENSEMBLE — No single primary NPC

**NPC Cast (in order of narrative prominence):**

| NPC | Role | Export Presence | Repository Source |
|---|---|---|---|
| Malachia Douglas-Bloodmoon | PMC Director, eldest shield | Full personality + 3 dialogue examples | C_Malachia.md / .js |
| Noah Douglas-Bloodmoon | Corporate lawyer, velvet glove | Full personality + 3 dialogue examples | C_Noah.md / .js |
| Jasper Douglas-Bloodmoon | Twin brother, DJ, rebel | Full personality + 3 dialogue examples | C_Jasper.md / .js |
| Wulfnic Bloodmoon | Retired mob patriarch | Full personality + 3 dialogue examples | C_Wulfnic.md / .js |
| Erik Douglas | CEO father, tyrant | Full personality + 3 dialogue examples | C_Erik.md / .js |
| Logan Douglas | Cool uncle, mechanic | Full personality + 3 dialogue examples | C_Logan.md / .js |

**Player POV Slot:**
- {{user}} — youngest Douglas-Bloodmoon heir (age 19, human, player-defined gender/appearance/personality)
- Fallback POV: Alyssa Douglas-Bloodmoon (via `alyssa_avatar.md` persona, loaded when {{user}} is not playing the twin)

---

## 3. World Association

**Primary World:** Contemporary → Urban Fantasy (base: Contemporary)

**World Taxonomy Mapping:**

| Taxonomy Level | Classification | Notes |
|---|---|---|
| Genre | Contemporary | Modern realistic setting |
| World | Contemporary (base) | Los Angeles, Beverly Hills |
| Overlay | Urban Fantasy (latent) | Export is human-only; repository source files contain werewolf/pack/cyber/fantasy variants |

**World Identifier (runtime):** `modern` (legacy) → `contemporary` (canonical)

**Key Locations:**
- Douglas Estate (Beverly Hills compound)
- LA University / UCLA campus
- The Verve (Logan's bar)
- Beverly Hills Luxury Cafe
- LA Luxury Mall

**Repository World File:** `worlds/contemporary/W_Contemporary.md` / `.js`

---

## 4. Faction Association

**Primary Factions:**

| Faction | Type | Role in Export |
|---|---|---|
| Douglas Commerce Company (DCC) | Corporate entity | Erik's company; finance/logistics power base |
| Bloodmoon Associates | Legacy enforcement network | Old-world dynasty enforcement |
| Vanguard PMC | Private military company | Malachia's security force; family protection |

**Faction Hierarchy:**
```
Douglas Commerce Company (DCC)
├── Erik Douglas — CEO / Patriarch
├── Vanguard PMC — Malachia (Director)
├── Legal Division — Noah (Corporate Lawyer)
├── IT / Cybersecurity — Jasper (Security Specialist)
└── Bloodmoon Associates (legacy enforcement)
    └── Wulfnic Bloodmoon — Retired Patriarch
```

---

## 5. Timeline Association

**Era:** Contemporary 2020s
**Setting:** Modern Realistic Slice-of-Life
**Timeline Anchor:** Post-Nixara (mother died in childbirth ~19 years before present)

**Key Timeline Events (from export):**
- Nixara Bloodmoon died giving birth to the twins (Jasper + Alyssa) — ~19 years ago
- Erik escalated security to draconian levels after Nixara's death
- Present: {{user}} (age 19) balances university life under family surveillance
- Rogue-mercenary pressure near estate (ambient threat)

---

## 6. Canon Status

**Classification:** CANON — Published Production Bot

**Canon Layer:** L3 (Experience Layer)

**Justification:**
- Published on JanitorAI as a public bot
- Creator: @Alyssa_5
- Character ID: 4bf8b24c-7128-46e7-871f-0829c89feec8
- Part of the SvartúlfrVerse cross-world ecosystem
- Referenced by other bots (DJ Frequency, Werewolf Pack, Cyberpunk, Warlord's Merchant)

**Canon Constraints (from export):**
- No White Moon in this scenario
- No pack rank in this scenario
- No Twin Link in this scenario
- Strictly human (Douglas-Bloodmoon line)
- Biometric smartwatch IF female (conditional)

---

## 7. Repository Ownership Domain

**Authority:** Experience Authority (Ex_)

**Ownership Chain:**
```
SvartúlfrVerse (Repository)
└── bots/ensemble/
    └── Ex_LosAngeles.md / .js  ← Experience Authority
        ├── core/En_Core.js  ← Engine Authority
        ├── characters/C_*.md / .js  ← Character Authority (per NPC)
        ├── worlds/contemporary/W_Contemporary.md / .js  ← World Authority
        ├── scripts/relationship_engine.js  ← Behavior Authority
        ├── scripts/state_engine.js  ← Behavior Authority
        └── personas/alyssa_avatar.md  ← Persona Layer (POV fallback)
```

**Cross-Authority Dependencies:**

| Authority | Component | Dependency Type |
|---|---|---|
| Experience (Ex_) | Ex_LosAngeles | Owns scenario framing, session structure, POV override |
| Engine (En_) | En_Core | Owns runtime orchestration, world routing, output formatting |
| Character (C_) | C_Erik, C_Jasper, C_Logan, C_Malachia, C_Noah, C_Wulfnic | Owns identity, appearance, traits, preferences |
| World (W_) | W_Contemporary | Owns world facts, locations, culture, organizations |
| Behavior (B1) | relationship_engine, state_engine | Owns runtime logic, state transitions |
| Persona | alyssa_avatar | Owns player avatar template (NOT loaded as C_ lorebook) |

---

## 8. POV Override Status

**Active POV Override:** `C_Alyssa` (set in Ex_LosAngeles.js)

**Override Mechanism:**
```
Experience decides (Ex_LosAngeles.js: mv_pov_override = "C_Alyssa")
↓
Engine enforces (En_Core.js: POV_OVERRIDE_INTERCEPTOR)
↓
Character remains passive (C_Alyssa.js loads only if {{user}} is not playing the twin)
```

**POV Rules:**
- {{user}} is the youngest Douglas-Bloodmoon heir by default
- If {{user}} plays the twin (Alyssa), no C_Alyssa.js is loaded
- If {{user}} does NOT play the twin, Alyssa.js loads as NPC
- Player characteristics are fully customizable (gender, appearance, personality, pronouns)

---

## 9. Cross-World References

The export references the following alternate universe bots:

| Bot | World | Status (in export) |
|---|---|---|
| SvartúlfrVerse \| DJ Frequency | Modern (alternate) | COMING SOON |
| SvartúlfrVerse \| Werewolf Pack | Urban Fantasy | LINKED |
| SvartúlfrVerse \| Cyberpunk | Cyber | LINKED |
| SvartúlfrVerse \| Warlord's Merchant | High Fantasy / Norse Mythic | LINKED |

These represent the same characters across different world overlays within the SvartúlfrVerse multiverse.

---

## 10. Classification Summary

| Field | Value |
|---|---|
| **Bot Archetype** | ENSEMBLE |
| **Primary Character** | ENSEMBLE (6 NPCs, no single primary) |
| **Player POV** | {{user}} (youngest heir) / Alyssa (fallback) |
| **World** | Contemporary (base) |
| **World Overlay** | Urban Fantasy (latent in source; human-only in export) |
| **Faction** | Douglas Commerce Company / Bloodmoon Associates / Vanguard PMC |
| **Timeline** | Contemporary 2020s, ~19 years post-Nixara |
| **Canon Status** | CANON — Published Production Bot |
| **Canon Layer** | L3 (Experience) |
| **Repository Domain** | Experience Authority (Ex_) |
| **POV Override** | C_Alyssa (active) |
| **Repository Path** | bots/ensemble/Ex_LosAngeles.* |

---

*Generated by Phase 15.1 — Legacy Bot Import & Repository Registration*
*Classification only — no content modified*
