# Comprehensive Layout & Formatting Discipline Investigation (R2 & R4)
**Target Lorebooks**: `FINAL/Svartulfr_NPC_Primary.json` (99 entries) & `FINAL/Svartulfr_NPC_Secondary.json` (211 entries) — Total 310 Entries  
**Investigator**: Explorer R7-2  
**Date**: October 21, 2026  

---

## 1. Executive Summary & Audit Matrix

An exhaustive, deterministic programmatic survey was conducted across all 310 NPC entries contained in `FINAL/Svartulfr_NPC_Primary.json` (ID: `_zwEqgEEzh12X6gHVmMKKC`) and `FINAL/Svartulfr_NPC_Secondary.json` (ID: `_Uht3Ckz44JBDrPnUHq7LV`).

### Audit Scorecard

| Check Parameter | Requirement | Primary (99) | Secondary (211) | Combined Total (310) | Compliance Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Initial Bracket Block `[...]`** | 100% start with `[...]` | 99 / 99 (100%) | 208 / 211 (98.58%) | 307 / 310 (99.03%) | **PASS with 3 Known Irregulars** |
| **Standard `BACKSTORY:`** | Standard JED+ header | 92 / 99 (92.9%)* | 104 / 211 (49.3%)** | 196 / 310 (63.2%) | **Requires Normalization** |
| **Standard `FAMILY & PACK:` or `CLAN AND COMPANY:`** | Standard JED+ header | 85 / 99 (85.9%) | 32 / 211 (15.2%) | 117 / 310 (37.7%) | **Requires Normalization** |
| **Standard `VOICE & BEHAVIOR:`** | Standard JED+ header | 90 / 99 (90.9%) | 94 / 211 (44.5%) | 184 / 310 (59.4%) | **Requires Normalization** |
| **Non-Standard `VOICE AND BEHAVIOR:`** | Must use ampersand `&` | 1 entry | 9 entries | 10 entries | **Action Required** |
| **Alternative `PERSONALITY:` Header** | Camp Mystic Schema | 0 entries | 100 entries | 100 entries | **Documented Architectural Variant** |
| **3 Irregular Entries Encapsulated** | Full JED+ encapsulation | 0 irregulars | 3 irregulars | 3 irregulars | **Action Required (Remediation Ready)** |
| **Em-Dashes (`—` / `\u2014`)** | 0 em-dashes allowed | 0 occurrences | 0 occurrences | 0 occurrences | **100% COMPLIANT** |
| **Markdown Asterisks (`*`)** | Plain text, 0 asterisks | 0 occurrences | 0 occurrences | 0 occurrences | **100% COMPLIANT** |
| **Residual `{{age}}` Macros** | 0 macros allowed | 0 occurrences | 0 occurrences | 0 occurrences | **100% COMPLIANT** |
| **Umbrella `BROAD_KEYS` in `keys`** | 0 umbrella trigger keys | 0 occurrences | 0 occurrences | 0 occurrences | **100% COMPLIANT** |
| **`exclude_from_recursion: true`** | Must be `true` on 100% | 0 / 99 (0%) | 0 / 211 (0%) | 0 / 310 (0%) | **Action Required (Remediation Missing)** |

*\* In Primary, the 7 entries missing `BACKSTORY:` are the 6 core characters (Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie) which are currently short stubs awaiting full JED+ restoration under R1, plus Echo.*  
*\*\* In Secondary, 100 entries belong to the Camp Mystic cohort, which employ an alternative sub-schema (`CAMP MYSTIC BACKGROUND & ROLE:`, `PERSONALITY:`, `STRENGTHS & WEAKNESSES:`, `RPG STATS & TRAITS:`).*

---

## 2. Standard JED+ Layout Survey (310 Entries)

The JED+ standard defined in `GEMINI.md` Section 2 mandates:
1. Attribute header block enclosed in brackets: `[NAME: ...; SPECIES: ...; AGE: ...; ROLE/OCCUPATION: ...]`
2. Narrative prose section: `BACKSTORY: ...`
3. Group / affiliation prose section: `FAMILY & PACK: ...` (or `CLAN AND COMPANY: ...` for non-pack civilians, academics, or corporate entities)
4. Voice and behavioral profile: `VOICE & BEHAVIOR: ...`
5. Thematic closure block: e.g. `[THE WEIGHT HE CARRIES]`, `[CORE TRAGEDY]`, or uppercase thematic section.

### 2.1 Initial Bracket Block `[...]` Status
- **Primary Lorebook (`_zwEqgEEzh12X6gHVmMKKC`)**: **99 / 99 entries (100%)** begin with an opening bracket `[` containing structured PList attributes separated by semicolons.
- **Secondary Lorebook (`_Uht3Ckz44JBDrPnUHq7LV`)**: **208 / 211 entries (98.58%)** begin with an opening bracket `[`.
- **Anomalies**: Exactly **3 entries** in Secondary fail to start with a bracket block:
  1. `NQd7n3QacMcK-TzowQ2LE` — Bruce
  2. `oov5UWuVhZ3RGgoxMkaTS` — Campus Staff Rat
  3. `Og7V6v67guXXAaP0_PsTM` — Adrian

### 2.2 Section Headers Census

#### Primary Lorebook (99 Entries)
- `BACKSTORY:`: **92 / 99**. The 7 entries lacking `BACKSTORY:` are:
  - `C-JisFj8qA1tsFEqZKevk` (Erik Ulfr Douglas) — Stub (to be restored under R1)
  - `jDuJtzirlEZC3K_ArIufh` (Malachia Björn Douglas Bloodmoon) — Stub (to be restored under R1)
  - `H2JX-NkHRiJ2FzoekC5ZZ` (Noah Loki Douglas Bloodmoon) — Stub (to be restored under R1)
  - `tAcrWLtWSDGf3xJJRwUOM` (Logan Járn Douglas) — Stub (to be restored under R1)
  - `HhuMluMmIIENUei3bX6ed` (Wulfnic Báleygr Bloodmoon) — Stub (to be restored under R1)
  - `BXi3sENAVYB8OKF80Q9Su` (Mackenzie Sanchez-Rogers) — Stub (to be restored under R1)
  - `p6pFnpGB9kQihhdPqcuht` (Echo) — AI Companion digital entity profile
- `FAMILY & PACK:`: **81 / 99**.
- `CLAN AND COMPANY:` / `CLAN & COMPANY:`: **4 / 99**.
- `VOICE & BEHAVIOR:`: **90 / 99**.
- Non-standard variant voice header:
  - `TG-Nl8HyTHt4QWaUW4nhm` (Dominic Rogers): Uses `VOICE AND BEHAVIOR:` instead of `VOICE & BEHAVIOR:`, and `FAMILY:` instead of `FAMILY & PACK:`.
- Thematic closures: 60 entries conclude with `THE WEIGHT HE CARRIES:`, 16 entries with `THE WEIGHT SHE CARRIES:`, and several with thematic bracket closures (`[CORE TRAGEDY]`, `[THE BURDEN OF COMMAND]`).

#### Secondary Lorebook (211 Entries)
The Secondary Lorebook is partitioned into two distinct architectural groups:
1. **The Camp Mystic Sub-Cohort (100 Entries)**:
   - Entries from `JzBo3WokPdNfzBYIB_vr0` (Wren Holloway) through `IFL-CMlndgnmPfTeW2di7` (Sabine Fen).
   - Uniform structural pattern:
     - `[...]` Bracket Attribute Block
     - `PERSONALITY: ...` (used in place of `VOICE & BEHAVIOR:`)
     - `STRENGTHS & WEAKNESSES: ...` (sub-items: `- SUPERNATURAL GIFTS:`, `- INNATE RESILIENCE:`, `- CAMP PROTOCOL & CONDITIONING:`)
     - `CAMP MYSTIC BACKGROUND & ROLE: ...` (used in place of `BACKSTORY:`)
     - `RPG STATS & TRAITS: ...`
2. **General Secondary NPCs (111 Entries)**:
   - `BACKSTORY:` present in **104 entries**.
   - `VOICE & BEHAVIOR:` present in **94 entries**.
   - `VOICE AND BEHAVIOR:` (conjunction variant) present in **9 entries**:
     1. `QeicBpVQvmhrnLgITDnrU` — Alicia Virtuoso
     2. `XT_eNxjZEjC9myvvGT2Ij` — Arturo Cardona
     3. `3uD5gouQOVTQlamjaSjtv` — Neon Purr
     4. `vSSG--FDlVsb0CrAMr0iP` — Siebren Dijkstra
     5. `npc_sec_thrakgor_deathspine` — Thrakgor Deathspine
     6. `npc_sec_feral_hound_crowe` — Crowe
     7. `npc_sec_morgeth_steeltooth` — Morgeth Steeltooth
     8. `npc_sec_thorvald_bloodmoon` — Thorvald
     9. `npc_sec_harald_sigurdsson` — Harald Sigurdsson
   - Non-standard Family/Pack variants:
     - `FAMILY & CONNECTIONS:` present in 10 entries (`3F2SpKHI3RkG2wPWJgp6O` Allegra Lumsden, `CyZknaH7OmYQi5S3ESpNJ` Ariadne Cirillo, `m6PNxuNGvi7YmlFRVgFWr` Luisa Sanchez Rogers, `2fVb0f4i9MbaNqPlsTR3r` Alistair Ambrose DeVille, `wYF_tF1nKpL4wSaaV0XkP` Cato, `oXk8N2cO9JqF4wZZU1aLm` Damien Bishop, `zKp8W1yH9McaF2qAABxOP` Everett Rottmore, `qW9Lm0aBvVxp7J12dRT5u` Vasile Ionescu, `p1X9YzaaMhka4V89OPtrQ` Eira Elloway, `8bMza22_19OPvVcaRT5uq` Vespera Thorne).
     - `FAMILY:` present in 6 entries (`aAil89Op_11VbMq77Rptx` Ailsa Hourie, `bBri89Vp_22NcaL88Xqtr` Brittany Willow, `cCoa99Xp_33MbaR99Ptzv` Coach Mithers, `dHid00Yp_44NcbS00Qtsw` Hideo Reid, `3V4l_B9kP2MmN1ZaBCdeF` Evan, `7N9k_C2mP4VvO8XyDEFgh` Silas).
     - `ACADEMY AND RIVALRIES:` present in 2 entries (`eChr11Zp_55PcdT11Raux` Professor Marit Christiansen, `fMor22Aq_66QdeU22Sbvy` Professor Mollusk Moreau).
     - `JUNIOR FOOTBALL & EDRIC DOUGLAS:` present in 1 entry (`1Y2z_A3bC4dE5fG6hI7jK` Coach Mack).
   - 3 Irregular Entries with **0 headers** (Bruce, Campus Staff Rat, Adrian).

---

## 3. The 3 Irregular Entries in `FINAL/Svartulfr_NPC_Secondary.json`

### 3.1 Bruce (`NQd7n3QacMcK-TzowQ2LE`)

#### Current State
- **Entry ID**: `NQd7n3QacMcK-TzowQ2LE`
- **Name**: `Bruce`
- **Trigger Keys**: `["Bruce", "Bruce KSA"]`
- **Type**: `npc`
- **Current Avatar**: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public` (old placeholder)
- **Current Raw Content**:
```text
Bruce is a demi-human bear and the president of the KSA organization at SUCC. On the morning of August 28, 2024, Bruce became incapacitated after accepting a drinking challenge from a member of the BRO, resulting in a massive drunken stupor that prevented Bruce from delivering the scheduled presentation speech. This failure forced the organization to urgently recruit Noah Douglas-Bloodmoon as a replacement speaker.
```
- **Defects**: Lacks initial bracket attribute block `[...]`, lacks `BACKSTORY:`, lacks `CLAN AND COMPANY:`, lacks `VOICE & BEHAVIOR:`, lacks thematic closure, uses legacy avatar URL.

#### Encapsulated Standard JED+ Text Replacement
```text
[NAME: Bruce; SPECIES: Bear Demi-Human; AGE: 22 (Born October 14, 2002); GENDER: Male; HEIGHT: 198 cm (6'6"); BUILD: Massive, burly, powerhouse bear demi-human frame with broad shoulders, dense chest, and thick arms; FEATURES: Rounded dark brown bear ears atop head (no human ears), short coarse dark fur trimming cheekbones and jawline, heavy stubble, dark brown eyes, thick brown bear tail; OCCUPATION: Undergraduate Student at SUCC, President of KSA (Kappa Sigma Alpha); RESIDENCE: KSA Fraternity House, Fraternity Row, Solarton Campus; AFFILIATION: KSA Fraternity, SUCC Student Council; SCENT: Bourbon, cedarwood, fresh malt, and clean musk]

BACKSTORY: Bruce is a bear demi-human and the presiding head of Kappa Sigma Alpha (KSA) at Solarton University of the Crescent Coast (SUCC). Respected across Greek Row for his formidable physical size and easygoing boisterous charisma, Bruce regularly navigates the volatile campus social scene. On the morning of August 28, 2024, Bruce became incapacitated after recklessly accepting an intense drinking challenge from a member of the rival BRO fraternity, collapsing into a massive drunken stupor that left him completely unable to deliver his high-stakes presentation speech. This high-profile failure forced KSA leadership to scramble urgently, recruiting Noah Douglas-Bloodmoon as their emergency replacement speaker.

CLAN AND COMPANY: As president of KSA, Bruce maintains extensive ties across SUCC fraternities, student athletics, and Greek life councils. He shares an intense, volatile rivalry with the brothers of BRO, whose drinking challenges frequently test his judgment and pride. While deeply indebted to Noah Douglas-Bloodmoon for salvaging his catastrophic speech absence, Bruce remains wary of the political leverage Noah holds over the fraternity.

VOICE & BEHAVIOR: Boisterous, booming baritone that easily carries over fraternity parties and crowded lecture halls. Naturally hearty and convivial, he masks sudden lapses in discipline behind loud laughter and aggressive back-slaps. When sober and focused, he displays genuine administrative pride in KSA, though his impulsive competitive streak leaves him vulnerable to provocations and campus drinking games.

[FRATERNITY PRIDE & HIDDEN EMBARRASSMENT]
Bruce carries lingering humiliation over collapsing during the August 28 Welcome Day festivities, knowing that only Noah Douglas-Bloodmoon's eleventh-hour intervention preserved KSA's public standing. He constantly strives to reassert his authority among the brothers while dreading the day Noah calls in the favor.
```

---

### 3.2 Campus Staff Rat (`oov5UWuVhZ3RGgoxMkaTS`)

#### Current State
- **Entry ID**: `oov5UWuVhZ3RGgoxMkaTS`
- **Name**: `Campus Staff Rat`
- **Trigger Keys**: `["Campus Staff Rat"]`
- **Type**: `npc`
- **Current Avatar**: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public` (old placeholder)
- **Current Raw Content**:
```text
An unnamed rodent demi-human employed as campus staff at SUCC. He was observed distributing maps to newcomers in the Lunar Quad on August 28, 2024. The staff member reacted with visible embarrassment and shock when Alyssa Douglas Bloodmoon treated him with sincere kindness and gratitude, a reaction noted by Jasper as unusual for the staff's typical treatment.
```
- **Defects**: Lacks initial bracket attribute block `[...]`, lacks `BACKSTORY:`, lacks `CLAN AND COMPANY:`, lacks `VOICE & BEHAVIOR:`, lacks thematic closure, uses legacy avatar URL.

#### Encapsulated Standard JED+ Text Replacement
```text
[NAME: Campus Staff Rat; ALIASES: Rodent Campus Worker, SUCC Facilities Staff; SPECIES: Rodent Demi-Human (Rat); AGE: 26 (Born May 19, 1998); GENDER: Male; HEIGHT: 162 cm (5'4"); BUILD: Slight, wiry, hunched frame built for scurrying and maintenance utility; FEATURES: Single pair of large translucent pinkish-gray rat ears atop head (no human ears), long pink prehensile rat tail, sharp twitching whiskers along cheeks, dark beady eyes, weathered hands accustomed to industrial cleaning chemicals; ATTIRE: Faded navy-blue SUCC Facilities jumpsuit, heavy utility belt, worn steel-toed work boots; OCCUPATION: Facilities & Groundskeeper Staff at SUCC; RESIDENCE: Solarton Campus Staff Quarters; AFFILIATION: SUCC Facilities Department, Campus Maintenance Service; SCENT: Industrial disinfectant, damp cardboard, machine oil, and floor wax]

BACKSTORY: Employed as lower-tier campus staff at Solarton University of the Crescent Coast (SUCC), this rodent demi-human performs the unglamorous custodial, maintenance, and logistics work that keeps the sprawling university operational. Accustomed to casual contempt and systemic disregard from aristocratic pureblood students and predatory alpha factions, he learned early to keep his head down and his presence minimal. On August 28, 2024, while distributing orientation maps to newcomers in the Lunar Quad, he experienced an unprecedented moment of shock when Alyssa Douglas Bloodmoon treated him with sincere courtesy, warm eye contact, and genuine gratitude, an interaction noted by Jasper as startlingly alien to the campus caste hierarchy.

CLAN AND COMPANY: Subordinated to SUCC Facilities management and Campus Maintenance Services. He works alongside fellow working-class demi-humans who keep Solarton's campus functioning behind the scenes, largely invisible to the high-society students who treat Greek Row and the academic quads as their private kingdom.

VOICE & BEHAVIOR: Soft-spoken, hurried, squeaky tenor that trails off nervously when addressed by influential students or campus security. Constantly averts direct eye contact, bowing slightly and clutching his clipboard or cleaning cart. When shown unexpected kindness, he stammers with wide-eyed disbelief and flustered gratitude, visibly unaccustomed to being acknowledged as an equal living person.

[INVISIBLE WORKER OF THE LUNAR QUAD]
Having spent years navigating the brutal social hierarchy of SUCC, the memory of Alyssa Douglas Bloodmoon's polite gratitude remains a quiet beacon of dignity in an otherwise callous work environment, prompting him to subtly assist the Douglas twins whenever their paths cross on campus grounds.
```

---

### 3.3 Adrian (`Og7V6v67guXXAaP0_PsTM`)

#### Current State
- **Entry ID**: `Og7V6v67guXXAaP0_PsTM`
- **Name**: `Adrian`
- **Trigger Keys**: `["Adrian", "Adrian Baker"]`
- **Type**: `npc`
- **Current Avatar**: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public` (old placeholder)
- **Current Raw Content**:
```text
Adrian was a cream-furred werewolf baker employed at the Sugar Moon bakery in Arcadia. As a member of the Seven Hills pack's artisan class, Adrian existed within the protective circle of the pack's military elite rather than participating in combat. Adrian functioned as a new father to three werewolf pups born recently, often displaying visible anxiety regarding their care while balancing duties behind the bakery counter.
```
- **Defects**: Lacks initial bracket attribute block `[...]`, lacks `BACKSTORY:`, lacks `FAMILY & PACK:`, lacks `VOICE & BEHAVIOR:`, lacks thematic closure, uses legacy avatar URL.

#### Encapsulated Standard JED+ Text Replacement
```text
[NAME: Adrian; ALIASES: Adrian the Baker; SPECIES: Werewolf (Seven Hills Pack Artisan Class); AGE: 28 (Born March 12, 1996); GENDER: Male; HEIGHT: 178 cm (5'10"); BUILD: Soft athletic artisan build, dusted with flour, gentle demeanor; FEATURES: Single pair of cream-furred wolf ears perched atop head (no human ears), cream wolf tail that swishes nervously, warm hazel eyes, soft facial features, light stubble; ATTIRE: Linen apron over rolled-up cotton shirt, durable work trousers, comfortable kitchen clogs; OCCUPATION: Baker & Confectioner at Sugar Moon Bakery; RESIDENCE: Residential district, Arcadia; AFFILIATION: Seven Hills Pack Artisan Class; SCENT: Yeast, warm vanilla, browned butter, powdered sugar, and clean wolf musk]

BACKSTORY: Adrian is a cream-furred werewolf baker employed at the renowned Sugar Moon Bakery in Arcadia. Born into the civilian artisan class of the Seven Hills pack, Adrian is shielded from direct military combat by the pack's frontline enforcers, contributing to pack stability through culinary craft, communal nutrition, and economic trade. Having recently become a new father to three lively werewolf pups, Adrian constantly juggles early morning dough kneading with the sleep-deprived anxiety of domestic pack fatherhood, worrying over teething, shifting instincts, and pup nursery security.

FAMILY & PACK: A dedicated civilian member of the Seven Hills Pack, thriving within the artisan district under the protection of the pack's military guardians. Fiercely devoted to his partner and their three newborn werewolf pups, Adrian views his bakery as both a community sanctuary and the lifeline securing his family's future within the pack's communal territory.

VOICE & BEHAVIOR: Warm, gentle, slightly breathless tenor with an earnest, hospitable cadence. He frequently wipes his hands on his apron and fusses over pastry displays while speaking. When discussing his newborn pups, his voice softens with overwhelming paternal pride and flustered worry, occasionally checking his pocket watch or fretting over feeding schedules.

[THE GENTLE ARTISAN'S DEVOTION]
Adrian embodies the often-overlooked civilian backbone of werewolf pack society, where strength is measured not by battlefield ferocity or alpha command, but by unwavering devotion to his pups, warmth given to neighbors, and flour-dusted resilience behind the bakery counter.
```

---

## 4. Formatting Discipline Audit (Requirements R2 & R4)

### 4.1 Em-Dashes (`—` / `\u2014`)
- **Inspection Method**: Exact Unicode code-point search for `\u2014` (em-dash), `\u2013` (en-dash), and `\u2015` (horizontal bar) across `content`, `name`, and metadata strings.
- **Findings**:
  - `FINAL/Svartulfr_NPC_Primary.json`: **0 occurrences**.
  - `FINAL/Svartulfr_NPC_Secondary.json`: **0 occurrences**.
- **Assessment**: **100% Compliant**. Past remediation passes have successfully eradicated all em-dashes from lorebook contents.

### 4.2 Markdown Asterisks (`*...*` or `**...**`)
- **Inspection Method**: Full text search for asterisk characters `*` across all lines of `content` in all 310 entries.
- **Findings**:
  - `FINAL/Svartulfr_NPC_Primary.json`: **0 occurrences**.
  - `FINAL/Svartulfr_NPC_Secondary.json`: **0 occurrences**.
- **Assessment**: **100% Compliant**. Narration and character descriptions are written entirely in plain text without markdown formatting or bold/italic markers.

### 4.3 Residual `{{age}}` Macros
- **Inspection Method**: Case-insensitive substring matching for `{{age` across `content`, `keys`, `secondary_keys`, `name`, and `comment`.
- **Findings**:
  - `FINAL/Svartulfr_NPC_Primary.json`: **0 occurrences**.
  - `FINAL/Svartulfr_NPC_Secondary.json`: **0 occurrences**.
- **Assessment**: **100% Compliant**. All age parameters are statically evaluated with calendar birth years and fixed ages at World-Age 2024.

### 4.4 Umbrella `BROAD_KEYS` in Trigger `keys`
- **Target Keywords**: `solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`.
- **Inspection Method**: Strict token intersection matching against `keys` and `secondary_keys` arrays for every entry.
- **Findings**:
  - **In `keys` (Lorebook Trigger Keys)**: **0 occurrences** across all 310 entries.
  - **In `secondary_keys`**: **0 occurrences** across all 310 entries.
  - **In `labels` (UI Categorization Tags)**: 215 occurrences exist in `FINAL/Svartulfr_NPC_Secondary.json` (e.g. `blackwood`, `solarton`, `succ`).
- **Assessment**:
  - **Requirement R2/R4 Compliance**: **100% Compliant for Trigger Keys**. Because Wyvern's retrieval engine matches prompt context only against `keys` (and `secondary_keys` when `selective: true`), the absence of umbrella keywords in `keys` guarantees that broad terms will NOT cause mass activation of all 310 NPCs.
  - *Note*: `labels` are inert metadata in Wyvern used solely for UI filtering in the lorebook editor.

### 4.5 `exclude_from_recursion` Status
- **Inspection Method**: Checking `e.get("exclude_from_recursion")` on every entry.
- **Findings**:
  - `FINAL/Svartulfr_NPC_Primary.json`: **0 entries** have `exclude_from_recursion: true` (99 are `None` / unset).
  - `FINAL/Svartulfr_NPC_Secondary.json`: **0 entries** have `exclude_from_recursion: true` (211 are `None` / unset).
- **Assessment**: **Action Required**. Requirement R4 explicitly mandates:
  > "`exclude_from_recursion: true` on all NPC entries to prevent cyclic activation cascades."
  Currently, 310 out of 310 entries lack this field. The remediation script must inject `"exclude_from_recursion": true` across all entries in both `entries` and `lexicon` arrays.

---

## 5. Strategic Recommendations for Implementer

1. **Encapsulate the 3 Irregular Entries**:
   - Replace the `content` of `NQd7n3QacMcK-TzowQ2LE` (Bruce), `oov5UWuVhZ3RGgoxMkaTS` (Campus Staff Rat), and `Og7V6v67guXXAaP0_PsTM` (Adrian) with the production-ready JED+ texts provided in Section 3.
2. **Normalize Variant Voice Headers**:
   - In Primary: Replace `VOICE AND BEHAVIOR:` with `VOICE & BEHAVIOR:` on Dominic Rogers (`TG-Nl8HyTHt4QWaUW4nhm`).
   - In Secondary: Replace `VOICE AND BEHAVIOR:` with `VOICE & BEHAVIOR:` on the 9 identified entries (`QeicBpVQvmhrnLgITDnrU`, `XT_eNxjZEjC9myvvGT2Ij`, `3uD5gouQOVTQlamjaSjtv`, `vSSG--FDlVsb0CrAMr0iP`, `npc_sec_thrakgor_deathspine`, `npc_sec_feral_hound_crowe`, `npc_sec_morgeth_steeltooth`, `npc_sec_thorvald_bloodmoon`, `npc_sec_harald_sigurdsson`).
3. **Set `exclude_from_recursion: true`**:
   - Iterate over all entries in `lexicon` and `entries` in both `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`, setting `entry["exclude_from_recursion"] = True`.
4. **Update Placeholders to Official DCC Placeholder**:
   - Ensure the 3 irregular entries (and all other entries lacking personal portraits) have their avatar updated to:
     `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`
5. **Preserve Camp Mystic Cohort Architecture**:
   - The 100 Camp Mystic camper/peer entries in Secondary are structurally sound and internally consistent. Do NOT dismantle their specialized `PERSONALITY:`, `STRENGTHS & WEAKNESSES:`, and `CAMP MYSTIC BACKGROUND & ROLE:` schema into generic backstories.
