# Technical Analysis: Survey of 7 Core Character Cards & Target Lorebook Records

**Date:** 2026-10-21  
**Investigator:** Explorer R7-1 (Core NPC & Card Investigator)  
**Task Scope:** Requirement R1 of Milestone 7 (Full JED+ Restoration for 7 Core Characters & Native Suppression via `ignored_characters`)

---

## 1. Executive Summary

This investigation performed a comprehensive audit and structural verification of the **7 core standalone character cards** located in `FINAL/` and their corresponding target entries within the two NPC Lorebooks:
- `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`, 99 entries)
- `FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`, 211 entries)

### Key Survey Discoveries:
1. **7 Core Standalone Cards (`FINAL/`):**
   - All 7 cards possess rich, full-length canonical descriptions formatted in **JED+ standard** with initial bracket parameter blocks, detailed Backstory, Family & Pack dynamics, Voice & Behavior, situational vignettes, Intimacy Profiles, Signature Vehicles & Assets, and full S.P.E.C.I.A.L. RPG stat/trait blocks.
   - Text hygiene is 100% compliant: **0 em-dashes (`—`)**, **0 residual `{{age}}` macros**, and **0 markdown asterisks** across all 7 card descriptions.
   - The card IDs and exact character counts match specification down to the single character:
     - Erik Ulfr Douglas: `_QPea6g4Q1QfeYCVHCLMPR` (22,775 chars)
     - Malachia Björn Douglas Bloodmoon: `_RDfz7XzTpM23LpPALVXHM` (18,520 chars)
     - Noah Loki Douglas Bloodmoon: `_zFLUjV8aVxQRAfQxGcAcY` (10,398 chars)
     - Logan Járn Douglas: `_T8Ywcr9FEqNf9JxbK6eHP` (13,735 chars)
     - Wulfnic Báleygr Bloodmoon: `_HEQQbbRFwKdG8QE2Fh1z1` (14,530 chars)
     - Mackenzie Sanchez-Rogers: `_zn24784jfcchQ7EwCyAnm` (9,618 chars)
     - Edric Douglas: `_TbRM3EdxDjHFgqztTbCpL` (7,240 chars)
   - Total character volume to be injected across Primary (6 characters) is **89,576 characters**, and for Secondary (Edric) is **7,240 characters**.

2. **Target Lorebook Records:**
   - In both lorebooks, the `entries` and `lexicon` arrays are completely synchronized in length and ID sequence (Primary: 99/99 items; Secondary: 211/211 items).
   - Currently, all 7 target entries are set to `type: "lore/concept"` with truncated placeholder summaries (~800 to 1,200 chars).
   - All 7 target entries **already have their respective standalone Card ID configured in `ignored_characters`**, verifying that native collision suppression was anticipated.
   - None of the 7 entries currently have `custom_avatar_regex`, `avatar_activation_regex`, `lines_parsed`, or `npc_info` populated (all are `null` / missing).
   - Avatar discrepancies exist for 6 of the 7 characters: the lorebook records currently reference older image hashes rather than the high-resolution portraits present on the standalone cards.
   - The token budget of `FINAL/Svartulfr_NPC_Primary.json` is currently `5000` and must be increased to `7500` to prevent prompt truncation when long cards (especially Erik's 22.7k chars and Malachia's 18.5k chars) activate.

---

## 2. Comprehensive Survey of the 7 Standalone Cards

### 2.1 File & Metadata Overview

| Character Name | Source Card File | Standalone Card ID | Description Length | Avatar URL |
|---|---|---|---|---|
| **Erik Ulfr Douglas** | `FINAL/Erik_Douglas_card.json` | `_QPea6g4Q1QfeYCVHCLMPR` | 22,775 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61648731-7c96-454d-95e5-e27aa69d8c00/public` |
| **Malachia Björn Douglas Bloodmoon** | `FINAL/Malachia_Douglas_Bloodmoon_card.json` | `_RDfz7XzTpM23LpPALVXHM` | 18,520 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d77a20fc-49da-4f35-a311-1539ef698d00/public` |
| **Noah Loki Douglas Bloodmoon** | `FINAL/Noah_Douglas_Bloodmoon_card.json` | `_zFLUjV8aVxQRAfQxGcAcY` | 10,398 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/968cc93e-879d-4aab-94b7-3838f94a9e00/public` |
| **Logan Járn Douglas** | `FINAL/Logan_Douglas_card.json` | `_T8Ywcr9FEqNf9JxbK6eHP` | 13,735 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0b5a932b-0a3b-4e0b-8257-49f18fedae00/public` |
| **Wulfnic Báleygr Bloodmoon** | `FINAL/Wulfnic_Bloodmoon_card.json` | `_HEQQbbRFwKdG8QE2Fh1z1` | 14,530 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/683beb87-8091-4b5a-e6fd-8acb0a159500/public` |
| **Mackenzie Sanchez-Rogers** | `FINAL/Mackenzie_Sanchez_Rogers_card.json` | `_zn24784jfcchQ7EwCyAnm` | 9,618 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public` |
| **Edric Douglas** | `FINAL/Edric_Douglas_card.json` | `_TbRM3EdxDjHFgqztTbCpL` | 7,240 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public` |

---

### 2.2 Structural Breakdown of Each Card Description

#### 1. Erik Ulfr Douglas (`FINAL/Erik_Douglas_card.json`)
- **Length:** 22,775 characters.
- **Initial Bracket Block:** `[NAME: Erik Ulfr Douglas; SPECIES: Werewolf (Pureblood Douglas); AGE: 47 (Born 14 October 1976); GENDER: Male, he/him; HEIGHT: 6'4" (193 cm); ... PACK_ROLE: Prime Alpha, Pack Leader; ...]`
- **Narrative Sections:**
  - `BACKSTORY:` (Early life, ascension to CEO of DCC, leadership of Seven Hills pack, loss of his mate Nixara).
  - `FAMILY & PACK:` (Dynamic with his children Malachia, Noah, Jasper, Alyssa; relations with brother Logan, father Magnus, father-in-law Wulfnic).
  - `VOICE & BEHAVIOR:` (Deep baritone, authoritative, controlled, unyielding composure, presence of command).
  - Situational Vignettes: `THE HELICOPTER:`, `GRIEF & INTIMACY:`, `THE FRESHMAN:`, `THE PARENTS' EVENING:`, `SPARRING:`
  - Thematic Section: `THE WEIGHT HE CARRIES:` (The burden of holding the House and Pack together while grieving Nixara alone).
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Adults only; dominant, deliberate, slow burn, absolute territorial fidelity).
  - Vehicles & Assets: `SIGNATURE VEHICLE & ASSETS:` (1969 Dodge Charger 440 R/T 'Hugin', AgustaWestland AW109SP GrandNew 'Sleipnir', DCC Executive Fleet).
  - RPG Block:
    - `[LEVEL: 47; OCCUPATION: Pack Leader / Corporate CEO; HP: 480/480; MANA: 260/260; FOCUS: 320/320]`
    - `[STATS: MGT 9, RES 8, AGI 4, WIT 4, PRS 5, SCT 1]`
    - S.P.E.C.I.A.L. format: `[STATS: STR 25; PER 20; END 22; CHA 24; INT 18; AGI 14; LCK 12]`
    - Traits: Prime Alpha, Pack Leader, Dominant Alpha, Alpha Command, Pureblood Lineage, Master of Seven Hills, Corporate Titan.

#### 2. Malachia Björn Douglas Bloodmoon (`FINAL/Malachia_Douglas_Bloodmoon_card.json`)
- **Length:** 18,520 characters.
- **Initial Bracket Block:** `[NAME: Malachia Björn Douglas Bloodmoon; SPECIES: Werewolf (Founding Bloodmoon & Pureblood Douglas); AGE: 24 (Born 21 November 1999); GENDER: Male, he/him; HEIGHT: 6'7" (201 cm); BUILD: Massive, heavily muscled, apex physical specimen; ... PACK_ROLE: Pack Leader Designate, Guild Enforcer; ...]`
- **Narrative Sections:**
  - `THE DISTANCE HE HAS ALREADY CLOSED:`
  - `BACKSTORY:` (Rift wars, frontline combat, gladiatorial fighting, training under Wulfnic and Erik).
  - `FAMILY & PACK:` (Fierce protectiveness of Alyssa; respect for Erik; tactical bond with Jasper; diplomatic contrast with Noah).
  - `THE SECRET HE CARRIES:`
  - `VOICE & BEHAVIOR:` (Low growl, taciturn, vigilant, intimidating presence, gentle restraint when off-duty).
  - Situational Vignettes: `SPARRING:`
  - Thematic Section: `THE WEIGHT HE CARRIES:`
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Adults only; fiercely protective, primal dominance, unyielding stamina, tender care for his bonded mate).
  - Vehicles & Assets: `SIGNATURE VEHICLE & GEAR:` (1970 Plymouth Barracuda 440-6 'Fenrir', custom Harley Fat Boy, DMHA heavy tactical loadout).
  - RPG Block:
    - `[LEVEL: 24; OCCUPATION: Rift Vanguard / Underworld Enforcer; ...]`
    - S.P.E.C.I.A.L. format: `[STATS: STR 26; PER 22; END 24; CHA 16; INT 12; AGI 18; LCK 10]`
    - Traits: Dominant Alpha, Pack Leader, Founding Bloodline, Pureblood Lineage, Ascended Enigma, Apex Core Resonance, Berserker Vitality.

#### 3. Noah Loki Douglas Bloodmoon (`FINAL/Noah_Douglas_Bloodmoon_card.json`)
- **Length:** 10,398 characters.
- **Initial Bracket Block:** `[NAME: Noah Loki Douglas Bloodmoon; ALIASES: The Grey Eminence, Loki, Golden Boy; AGE: 22 (Born 11 June 2001); SPECIES: Werewolf; BLOOD_CLASSIFICATION: Founding Bloodline & Pureblood; SECONDARY_SEX: Delta; HOUSE: Douglas and Bloodmoon; OCCUPATION: Chief Legal Officer & Diplomatic Strategist for DCC; ...]`
- **Narrative Sections:**
  - `BACKSTORY:` (Legal genius, corporate diplomacy, prodigy at Solarton University and DCC executive suite).
  - `FAMILY & PACK:` (The brain of the siblings; de-escalating Malachia's volatility; supporting Jasper's tech incursions; spoiling Alyssa).
  - `VOICE & BEHAVIOR:` (Urbane, melodic, polished, razor-sharp wit, never raises his voice).
  - Thematic Section: `THE WEIGHT HE CARRIES:` (Navigating lethal corporate and political intrigue so his family doesn't have to spill blood).
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Adults only; sophisticated, sensual, vocal, teasing, psychological and physical attentiveness).
  - Vehicles & Assets: `SIGNATURE VEHICLE & ASSETS:` (Audi RS6 Avant Quattro 'Geri', custom tailored Italian suits, encrypted legal vaults).
  - RPG Block:
    - `[LEVEL: 22; OCCUPATION: Corporate Diplomat / Financial Strategist; ...]`
    - S.P.E.C.I.A.L. format: `[STATS: STR 14; PER 20; END 16; CHA 26; INT 24; AGI 16; LCK 18]`
    - Traits: Delta, Grey Eminence, Founding Bloodline, Pureblood Lineage, Silver Tongue, Corporate Mastermind, Master Negotiator.

#### 4. Logan Járn Douglas (`FINAL/Logan_Douglas_card.json`)
- **Length:** 13,735 characters.
- **Initial Bracket Block:** `[NAME: Logan Járn Douglas; SPECIES: Werewolf (Pureblood Douglas); AGE: 42 (Born 28 August 1981); GENDER: Male, he/him; HEIGHT: 6'2" (188 cm); BUILD: Broad, weathered mechanic's build; ... PACK_ROLE: Beta, Pack Peacemaker; OCCUPATION: Owner of The Verve, Master Motorcycle Craftsman; ...]`
- **Narrative Sections:**
  - `BACKSTORY:` (Renouncing corporate power to found The Verve lounge and motorcycle shop; acting as neutral ground keeper).
  - `FAMILY & PACK:` (Younger brother to Erik; father figure and claimed parent to Edric; confidant to his nephews and niece).
  - `VOICE & BEHAVIOR:` (Warm gravelly baritone, dry humor, easygoing, deeply grounded, soothing presence).
  - Thematic Section: `THE WEIGHT HE CARRIES:` (Protecting the secret of Edric's true parentage while keeping the family calm).
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Adults only; rugged, patient, sensual, heavy touch, deeply comforting and attentive).
  - Vehicles & Tools: `SIGNATURE VEHICLE & TOOLS:` (Custom 1982 Shovelhead Chopper 'Skoll', 1978 Chevrolet K10 Fleetside 4x4, custom fabrication shop).
  - RPG Block:
    - `[LEVEL: 42; OCCUPATION: Master Craftsman / Bar Owner / Diplomatic Mediator; ...]`
    - S.P.E.C.I.A.L. format: `[STATS: STR 20; PER 20; END 22; CHA 22; INT 16; AGI 16; LCK 14]`
    - Traits: Beta, Pack Peacemaker, Pureblood Lineage, Master Fabricator, Iron Resolve, Neutral Ground Keeper.

#### 5. Wulfnic Báleygr Bloodmoon (`FINAL/Wulfnic_Bloodmoon_card.json`)
- **Length:** 14,530 characters.
- **Initial Bracket Block:** `[NAME: Wulfnic Báleygr Bloodmoon; SPECIES: Werewolf (Firstborn / Primordial Wolf God); AGE: ~1196 (Born ~828 AD); GENDER: Male, he/him; HEIGHT: 7'0" (213 cm); BUILD: Colossal primordial giant, mountain-like breadth; ... PACK_ROLE: Progenitor, Living Saga; ...]`
- **Narrative Sections:**
  - `BACKSTORY:` (The age of the Firstborn, the migration to North America, founding of the Bloodmoon lineage, surviving twelve centuries).
  - `FAMILY & PACK:` (Maternal grandfather to Malachia, Noah, Jasper, Alyssa; ancient respect for Erik; deep bond with Alyssa).
  - `VOICE & BEHAVIOR:` (Ancient thunderous resonance, calm antiquity, speaks little but shakes the earth when he does).
  - Historical Subsections: `THE WEIGHT OF MILLENNIA:`, `FORMER TITLES:`, `THE HUNDREDS:`, `THE FIRST HUNT:`, `THE WOLVES THAT CAME FROM NOWHERE:`, `THE GRANDFATHER:`
  - Thematic Section: `THE WEIGHT HE CARRIES:` (Outliving his children, watching millennia pass, awaiting the fulfillment of primordial prophecies).
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Adults only; immense primordial power held in check by monumental gentleness, overwhelming worship).
  - Vehicles & Relics: `SIGNATURE VEHICLE & RELICS:` (Ancestral Great Spear 'Gungnir-Shard', restored 1954 Land Rover Series I).
  - RPG Block:
    - `[LEVEL: 99; OCCUPATION: Living Progenitor / Primordial Wolf God; ...]` (Level 99 cap strictly observed!).
    - S.P.E.C.I.A.L. format: `[STATS: STR 30; PER 24; END 28; CHA 20; INT 16; AGI 14; LCK 12]`
    - Traits: Divine Blood, Primordial Enigma, Firstborn of the Nine, Father of Bloodmoons, Myth Made Flesh, Calamity Presence.

#### 6. Mackenzie Sanchez-Rogers (`FINAL/Mackenzie_Sanchez_Rogers_card.json`)
- **Length:** 9,618 characters.
- **Initial Bracket Block:** `[NAME: Mackenzie "Mac" Sanchez-Rogers; SPECIES: Werewolf; BLOOD_CLASSIFICATION: Pureblood, unknown to him and to everyone around him; AGE: 19 (Born 2004); GENDER: Male, he/him; HEIGHT: 6'2" (188 cm); BUILD: Broad chest, athletic slouch; ... ROLE: Keyboardist of Grave Mistake; ...]`
- **Narrative Sections:**
  - `BACKSTORY:` (Raised in Oakland by Andrea Sanchez, moving to Solarton, discovering music, unaware of his Rogers pureblood wolf heritage).
  - `FAMILY & PACK:` (Close to mom Andrea and sister Luisa; loyal to bandmates Fade, Roland, Viola; unspoken, blushing devotion to Alyssa).
  - `VOICE & BEHAVIOR:` (Slangy, West Coast vernacular, loud, clumsy tail wags, defensive when flustered).
  - Subsections: `BAND & RELATIONSHIPS:`, `THE BLOOD HE DOES NOT KNOW HE HAS:`, `THE ALPHA HE IS COPYING:`
  - Thematic Section: `THE WEIGHT HE CARRIES:` (Insecurity about being background noise, fear of his awakening supernatural instincts).
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Adults only; passionate, physical, checks in constantly, earnest, vocal, flustered tenderness).
  - RPG Block:
    - `[LEVEL: 19; SPECIES: Werewolf (Pureblood Rogers & Common Sanchez); OCCUPATION: Street Scrapper / Rogue; ...]`
    - S.P.E.C.I.A.L. format: `[STATS: STR 22; PER 18; END 19; CHA 14; INT 6; AGI 18; LCK 8]`
    - Traits: Pureblood Lineage (Rogers - Dormant), Common Lupine Blood, Rebel Heart / Underground, Feral Blood, Dungeon Veteran, Lupine Senses, Partial Shift Mastery, Regenerative Factor, Silver Allergy, The Weight He Carries.

#### 7. Edric Douglas (`FINAL/Edric_Douglas_card.json`)
- **Length:** 7,240 characters.
- **Initial Bracket Block:** `[NAME: Edric Douglas; ROLE: Logan's publicly claimed son, Alyssa's younger cousin; AGE: 13; GENDER: Male; SPECIES: Werewolf; BLOOD_CLASSIFICATION: Pureblood House; SECONDARY_SEX: Gamma (unpresented, destined Alpha); HOUSE: Douglas; PACK: Seven Hills; PACK_ROLE: Pup; HEIGHT: 165cm (5'5"); BIRTHDAY: February 25 (Born February 25, 2011); ... ACTIVITIES: Wide receiver / cornerback in the Solarton Junior Football team; ...]`
- **Narrative Sections:**
  - `BACKSTORY:` (Believes Logan is his father; growing up in Logan's garage and Douglas compound; training for football).
  - `FAMILY & PACK:` (Hero-worships Logan; intimidated by uncle Erik; adores cousin Alyssa; trains football with Jet Thompson).
  - Subsections: `SOLARTON JUNIOR FOOTBALL & JET THOMPSON:`
  - `VOICE & BEHAVIOR:` (Awkward Gen-Z slang, manufactured "sigma grindset" bravado masking tween vulnerability and anxiety).
  - Thematic Section: `THE WEIGHT HE CARRIES:` (Terrified of the impending winter Presentation where his true secondary sex will be tested).
  - Intimacy Profile: `SEXUALITY & INTIMACY:` (Strictly non-applicable; juvenile minor, background character, never a romantic/sexual participant).
  - RPG Block:
    - `[LEVEL: 13; SPECIES: Werewolf (Pureblood Pre-Presentation Gamma); OCCUPATION: Student / Pack Pup; ...]`
    - S.P.E.C.I.A.L. format: `[STATS: STR 16; PER 17; END 20; CHA 13; INT 9; AGI 13; LCK 13]`
    - Traits: Pre-First Shift (Gamma), Pureblood Lineage, Lupine Senses, Partial Shift Mastery, Regenerative Factor, Silver Allergy, Old Money / Aristocrat.

---

## 3. Detailed Audit of Target Entries in Lorebooks

### 3.1 Primary Lorebook: `FINAL/Svartulfr_NPC_Primary.json`
- **Lorebook ID:** `_zwEqgEEzh12X6gHVmMKKC`
- **Current Token Budget:** `5000` (Requirement: must be updated to `7500`)
- **Total Entries:** 99 in `entries`, 99 in `lexicon` (both identical)

#### Target Entry Audit Table:

| Character Name | Entry ID (`entry_id`) | Current Type | Current Length | Current Avatar URL | Card Avatar URL | Current `ignored_characters` |
|---|---|---|---|---|---|---|
| **Erik Ulfr Douglas** | `C-JisFj8qA1tsFEqZKevk` | `lore/concept` | 877 chars | `.../30fe0390-05fb-46cf-2c8a-cd98fc35c700/...` | `.../61648731-7c96-454d-95e5-e27aa69d8c00/...` | `['_QPea6g4Q1QfeYCVHCLMPR']` |
| **Malachia Björn Douglas Bloodmoon** | `jDuJtzirlEZC3K_ArIufh` | `lore/concept` | 894 chars | `.../c883ae1e-d817-4f80-e4bb-388aaea84d00/...` | `.../d77a20fc-49da-4f35-a311-1539ef698d00/...` | `['_RDfz7XzTpM23LpPALVXHM']` |
| **Noah Loki Douglas Bloodmoon** | `H2JX-NkHRiJ2FzoekC5ZZ` | `lore/concept` | 817 chars | `.../12f497d7-7147-4d38-c2de-c57892180800/...` | `.../968cc93e-879d-4aab-94b7-3838f94a9e00/...` | `['_zFLUjV8aVxQRAfQxGcAcY']` |
| **Logan Járn Douglas** | `tAcrWLtWSDGf3xJJRwUOM` | `lore/concept` | 847 chars | `.../5d7d3ade-f742-41da-979b-670102fead00/...` | `.../0b5a932b-0a3b-4e0b-8257-49f18fedae00/...` | `['_T8Ywcr9FEqNf9JxbK6eHP']` |
| **Wulfnic Báleygr Bloodmoon** | `HhuMluMmIIENUei3bX6ed` | `lore/concept` | 923 chars | `.../554744b5-0e23-45b9-005a-4629abd35500/...` | `.../683beb87-8091-4b5a-e6fd-8acb0a159500/...` | `['_HEQQbbRFwKdG8QE2Fh1z1']` |
| **Mackenzie Sanchez-Rogers** | `BXi3sENAVYB8OKF80Q9Su` | `lore/concept` | 1,214 chars | `.../87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/...` | `.../87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/...` | `['_zn24784jfcchQ7EwCyAnm']` |

*Note:* Mackenzie's avatar already matches the card URL; the other 5 currently point to legacy image delivery hashes and must be updated to the canonical card avatars.

---

### 3.2 Secondary Lorebook: `FINAL/Svartulfr_NPC_Secondary.json`
- **Lorebook ID:** `_Uht3Ckz44JBDrPnUHq7LV`
- **Current Token Budget:** `5000` (Requirement: maintained at `5000`)
- **Total Entries:** 211 in `entries`, 211 in `lexicon` (both identical)

#### Target Entry Audit Table:

| Character Name | Entry ID (`entry_id`) | Current Type | Current Length | Current Avatar URL | Card Avatar URL | Current `ignored_characters` |
|---|---|---|---|---|---|---|
| **Edric Douglas** | `h-ttmlgJYeRXqyDvQjSX7` | `lore/concept` | 960 chars | `.../13c49c40-2378-4678-ca5d-6e2ef84eba00/...` | `.../ed348ea6-c40c-461c-f90e-d09e742c3400/...` | `['_TbRM3EdxDjHFgqztTbCpL']` |

*Note:* Edric's lorebook entry currently points to `13c49c40...`, whereas his card has `ed348ea6...`. It must be updated to the canonical card avatar.

---

## 4. Verification of Native Anti-Collision (`ignored_characters`)

Wyvern natively supports anti-collision suppression via the `ignored_characters: string[]` attribute on Lorebook entries:
- When a user session or party contains any Character Card listed in `ignored_characters`, Wyvern **silently skips and suppresses** the Lorebook NPC entry from context injection.
- This ensures that when the user chats with Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie, or Edric using their Standalone Character Card, their Lorebook entry will not double-inject or cause narrative hallucination.
- When chatting with *other* characters (e.g. Alyssa, Jasper, or an NPC), these Lorebook entries will naturally activate with their complete JED+ dossiers!

### Verification of Card IDs vs Target Entries:
| Character | Standalone Card ID | Target Entry ID | `ignored_characters` Verified? |
|---|---|---|---|
| **Erik** | `_QPea6g4Q1QfeYCVHCLMPR` | `C-JisFj8qA1tsFEqZKevk` | **YES** (Already contains `_QPea6g4Q1QfeYCVHCLMPR`) |
| **Malachia** | `_RDfz7XzTpM23LpPALVXHM` | `jDuJtzirlEZC3K_ArIufh` | **YES** (Already contains `_RDfz7XzTpM23LpPALVXHM`) |
| **Noah** | `_zFLUjV8aVxQRAfQxGcAcY` | `H2JX-NkHRiJ2FzoekC5ZZ` | **YES** (Already contains `_zFLUjV8aVxQRAfQxGcAcY`) |
| **Logan** | `_T8Ywcr9FEqNf9JxbK6eHP` | `tAcrWLtWSDGf3xJJRwUOM` | **YES** (Already contains `_T8Ywcr9FEqNf9JxbK6eHP`) |
| **Wulfnic** | `_HEQQbbRFwKdG8QE2Fh1z1` | `HhuMluMmIIENUei3bX6ed` | **YES** (Already contains `_HEQQbbRFwKdG8QE2Fh1z1`) |
| **Mackenzie** | `_zn24784jfcchQ7EwCyAnm` | `BXi3sENAVYB8OKF80Q9Su` | **YES** (Already contains `_zn24784jfcchQ7EwCyAnm`) |
| **Edric** | `_TbRM3EdxDjHFgqztTbCpL` | `h-ttmlgJYeRXqyDvQjSX7` | **YES** (Already contains `_TbRM3EdxDjHFgqztTbCpL`) |

---

## 5. Specification for Proposed Remediation Payload

The table below provides the full, drop-in technical specification for each of the 7 target entries when migrated to `type: "npc"`:

### 5.1 Remediation Attributes Matrix

```json
{
  "Erik Ulfr Douglas": {
    "entry_id": "C-JisFj8qA1tsFEqZKevk",
    "name": "Erik Ulfr Douglas",
    "type": "npc",
    "selective": false,
    "keys": ["Erik Douglas", "Erik Ulfr Douglas", "Prime Alpha", "Erik"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61648731-7c96-454d-95e5-e27aa69d8c00/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Erik\\ Ulfr\\ Douglas|Erik\\ Douglas|The\\ Prime\\ Alpha|Prime\\ Alpha|Erik)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Erik",
      "last_name": "Douglas",
      "nicknames": ["The Prime Alpha", "Ulfr", "Dad"],
      "titles": []
    },
    "ignored_characters": ["_QPea6g4Q1QfeYCVHCLMPR"],
    "ignored_personas": [],
    "content_source": "FINAL/Erik_Douglas_card.json",
    "content_length": 22775
  },
  "Malachia Björn Douglas Bloodmoon": {
    "entry_id": "jDuJtzirlEZC3K_ArIufh",
    "name": "Malachia Björn Douglas Bloodmoon",
    "type": "npc",
    "selective": false,
    "keys": ["Malachia Douglas", "Malachia Björn", "Malachia Douglas-Bloodmoon", "Malachia"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d77a20fc-49da-4f35-a311-1539ef698d00/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Malachia\\ Björn\\ Douglas\\ Bloodmoon|Malachia\\ Douglas\\ Bloodmoon|Malachia\\ Douglas|The\\ Berserker|Malachia)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Malachia",
      "last_name": "Douglas Bloodmoon",
      "nicknames": ["The Berserker", "Ghost", "King"],
      "titles": []
    },
    "ignored_characters": ["_RDfz7XzTpM23LpPALVXHM"],
    "ignored_personas": [],
    "content_source": "FINAL/Malachia_Douglas_Bloodmoon_card.json",
    "content_length": 18520
  },
  "Noah Loki Douglas Bloodmoon": {
    "entry_id": "H2JX-NkHRiJ2FzoekC5ZZ",
    "name": "Noah Loki Douglas Bloodmoon",
    "type": "npc",
    "selective": false,
    "keys": ["Noah Douglas", "Noah Loki", "Noah Douglas-Bloodmoon", "Noah"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/968cc93e-879d-4aab-94b7-3838f94a9e00/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Noah\\ Loki\\ Douglas\\ Bloodmoon|Noah\\ Douglas\\ Bloodmoon|Noah\\ Douglas|The\\ Grey\\ Eminence|Noah)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Noah",
      "last_name": "Douglas Bloodmoon",
      "nicknames": ["The Grey Eminence", "Loki", "Golden Boy"],
      "titles": []
    },
    "ignored_characters": ["_zFLUjV8aVxQRAfQxGcAcY"],
    "ignored_personas": [],
    "content_source": "FINAL/Noah_Douglas_Bloodmoon_card.json",
    "content_length": 10398
  },
  "Logan Járn Douglas": {
    "entry_id": "tAcrWLtWSDGf3xJJRwUOM",
    "name": "Logan Járn Douglas",
    "type": "npc",
    "selective": false,
    "keys": ["Logan Douglas", "Logan Járn Douglas", "Logan"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0b5a932b-0a3b-4e0b-8257-49f18fedae00/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Logan\\ Járn\\ Douglas|Logan\\ Douglas|The\\ Peacemaker|Logan)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Logan",
      "last_name": "Douglas",
      "nicknames": ["Járn", "The Peacemaker", "Uncle Logan"],
      "titles": []
    },
    "ignored_characters": ["_T8Ywcr9FEqNf9JxbK6eHP"],
    "ignored_personas": [],
    "content_source": "FINAL/Logan_Douglas_card.json",
    "content_length": 13735
  },
  "Wulfnic Báleygr Bloodmoon": {
    "entry_id": "HhuMluMmIIENUei3bX6ed",
    "name": "Wulfnic Báleygr Bloodmoon",
    "type": "npc",
    "selective": false,
    "keys": ["Wulfnic", "Wulfnic Bloodmoon", "Primo Zanna"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/683beb87-8091-4b5a-e6fd-8acb0a159500/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Wulfnic\\ Báleygr\\ Bloodmoon|Wulfnic\\ Bloodmoon|The\\ First\\ Tusk|Primo\\ Zanna|Wulfnic)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Wulfnic",
      "last_name": "Bloodmoon",
      "nicknames": ["The First Tusk", "Primo Zanna", "The Ancient"],
      "titles": []
    },
    "ignored_characters": ["_HEQQbbRFwKdG8QE2Fh1z1"],
    "ignored_personas": [],
    "content_source": "FINAL/Wulfnic_Bloodmoon_card.json",
    "content_length": 14530
  },
  "Mackenzie Sanchez-Rogers": {
    "entry_id": "BXi3sENAVYB8OKF80Q9Su",
    "name": "Mackenzie Sanchez-Rogers",
    "type": "npc",
    "selective": false,
    "keys": ["Mackenzie Sanchez-Rogers", "Mackenzie Rogers", "Mac Rogers", "Mackenzie"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Mackenzie\\ Sanchez-Rogers|Mackenzie\\ Rogers|Mac\\ Rogers|Mackenzie|Mac)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Mackenzie",
      "last_name": "Sanchez-Rogers",
      "nicknames": ["Mac", "Mac Rogers"],
      "titles": []
    },
    "ignored_characters": ["_zn24784jfcchQ7EwCyAnm"],
    "ignored_personas": [],
    "content_source": "FINAL/Mackenzie_Sanchez_Rogers_card.json",
    "content_length": 9618
  },
  "Edric Douglas": {
    "entry_id": "h-ttmlgJYeRXqyDvQjSX7",
    "name": "Edric Douglas",
    "type": "npc",
    "selective": false,
    "keys": ["Edric Douglas", "Edric"],
    "secondary_keys": [],
    "key_logic": "AND_ANY",
    "constant": false,
    "exclude_from_recursion": true,
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public",
    "custom_avatar_regex": true,
    "avatar_activation_regex": "(?:^|\\n)\\s*(?:Edric\\ Douglas|Edric)\\s*:",
    "lines_parsed": 1,
    "npc_info": {
      "first_name": "Edric",
      "last_name": "Douglas",
      "nicknames": ["Ed", "Pup"],
      "titles": []
    },
    "ignored_characters": ["_TbRM3EdxDjHFgqztTbCpL"],
    "ignored_personas": [],
    "content_source": "FINAL/Edric_Douglas_card.json",
    "content_length": 7240
  }
}
```

---

## 6. Token Budget & Lorebook Top-Level Settings

1. **`FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`):**
   - Current `token_budget`: `5000`
   - **Required `token_budget`:** `7500` (CRITICAL: Erik at 22,775 characters is ~4,800 tokens. With other context and secondary entries, 7500 ensures no clipping occurs).
   - `photoURL`: Update to official Svartúlfr Crest `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public`.

2. **`FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`):**
   - Current `token_budget`: `5000`
   - **Required `token_budget`:** `5000` (Edric at 7,240 characters is ~1,600 tokens; 5000 tokens remains completely sufficient).
   - `photoURL`: Update to official Svartúlfr Crest `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public`.
