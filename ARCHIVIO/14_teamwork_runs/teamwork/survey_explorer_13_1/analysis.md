# Comprehensive Survey Analysis for R1: Canonical Heights & Proportional References

**Agent**: `survey_explorer_13_1`  
**Date**: 2026-10-31  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\survey_explorer_13_1`  
**Mission**: Read-only exploration, comprehensive survey, and catalog of all files and occurrences in the SvartúlfrVerse repository related to R1 (Canonical Heights and Proportional References).

---

## 1. Executive Summary

This survey comprehensively investigates all files and occurrences related to Requirement R1 of the SvartúlfrVerse evolution roadmap:
1. **Canonical Heights**:
   - **Alyssa**: `155 cm (5' 1")`
   - **Jasper**: `193 cm (6' 4")`
   - **Noah**: `197 cm (6' 5.6")`
   - **Malachia**: `208 cm (6' 9.9")`
   - **Erik**: `213 cm (6' 11.9")`
   - **Wulfnic**: `220 cm (7' 2.6")`

2. **Canonical Proportional References**:
   - **Reference 1**: `Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).`
   - **Reference 2**: `Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.`
   - **Reference 3**: `Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno).`

### Key Findings at a Glance
- **Current Height Status**:
  - The metric values (`cm`) in the active `FINAL/` cards and `FINAL/Svartulfr_NPC_Primary.json` are generally aligned with canonical heights (155, 193, 197, 208, 213, 220), but the imperial conversions and formatting strings have significant inconsistencies:
    - **Noah**: currently has `197cm (6'6")` instead of `197 cm (6' 5.6")`.
    - **Malachia**: currently has `208cm / 6'10"` instead of `208 cm (6' 9.9")`.
    - **Erik**: currently has `213cm / 7'0"` instead of `213 cm (6' 11.9")`. Furthermore, Outfit #0 in Erik's card has an erroneous `203 cm`.
    - **Wulfnic**: currently has `220cm (7'3")` instead of `220 cm (7' 2.6")`. Furthermore, Outfit #0 in Wulfnic's card has an erroneous `210 cm`.
    - **Spacing discipline**: current brackets often use `155cm (5'1")` or `193cm (6'4")` without a space before `cm`, whereas the authoritative standard specifies `155 cm (5' 1")` and `193 cm (6' 4")`.
    - **Legacy database records** (`database/characters/*.md`) contain outdated legacy heights from an older pre-supernatural draft (e.g. Alyssa 165 cm, Jasper 191 cm, Noah 196 cm, Malachia 210 cm, Erik 205 cm, Wulfnic 195 cm).
- **Current Proportional Reference Status**:
  - **100% Absent from Character Cards, Personas, Lorebooks, Scenarios, and Visual Prompts**:
    The direct proportional references are currently **completely absent** from all active Character Cards, User Personas, Standalone Lorebooks, Scenarios, and group visual prompt files. They currently appear **only** in the prompt/dispatch metadata files (`ORIGINAL_REQUEST.md`, `prompt_draft.md`, `DISPATCH.md`, and `scratch/approved_teamwork_prompt.txt`).
- **Parity & Invariant Integrity**:
  - All 6 standalone lorebooks in `FINAL/` and `lorebooks/optimized/` currently satisfy the strict `entries == lexicon` byte-for-byte parity requirement.
  - All `FINAL/` lorebook files are currently 100% byte-for-byte identical to their `lorebooks/optimized/` counterparts.
  - All character cards and lorebook NPC entries maintain the single-line bracket block rule on line 0 (`[NAME: ...; HEIGHT: ...; ...]`).

---

## 2. Character-by-Character Survey & Discrepancy Matrix

### 2.1 Alyssa Hvit Douglas Bloodmoon
- **Canonical Target**: `155 cm (5' 1")`
- **Role**: Founding Bloodline Heiress, Healer, White Moon Twin (`Hvít Mániúlfr`), Omega / Pack Mom.
- **Occurrences in Workspace**:
  1. `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`:
     - Line 1 (JED+ bracket): `[NAME: Alyssa Hvit Douglas Bloodmoon; ... HEIGHT: 155cm (5'1"); ...]`
     - Line 29 (`visual_description`): `19-year-old petite (155 cm, 5'1") curvy hourglass young woman (Bust: 95cm, Waist: 55cm, Hips: 95cm)...`
     - Status: Metric value 155 cm matches; spacing in bracket is `155cm (5'1")` rather than canonical `155 cm (5' 1")`.
     - Proportional references: **Missing**.
  2. `FINAL/personas/Alyssa_Persona.json`:
     - Line 1 (JED+ bracket): `[NAME: Alyssa Hvit Douglas Bloodmoon; ... HEIGHT: 155cm (5'1"); ...]`
     - Appearance `Base` (ID `appearance_6_pa6kZ9BzwLC05qO5Fuk`): `Altezza minuta di 155 cm con silhouette sinuosa e femminile a clessidra accentuata (misure 95-55-95 cm)...`
     - Appearance `Hybrid`: `185 cm con postura eretta da lupo mannaro bipede...` (combat hybrid shift).
     - Status: Base metric matches; bracket formatting has no space (`155cm (5'1")`).
     - Proportional references: **Missing**.
  3. `FINAL/Svartulfr_NPC_Primary.json` (ID `alyssa_world_dossier_2b54a223`):
     - Line 1 of `content`: `[NAME: Alyssa Hvit Douglas Bloodmoon; ... HEIGHT: 155cm (5'1"); ...]`
     - Mirror in `lorebooks/optimized/Svartulfr_NPC_Primary.json`: Identical.
     - Status: Metric 155 cm matches; bracket formatting has no space.
     - Proportional references: **Missing**.
  4. `database/characters/C_Alyssa_Douglas_Bloodmoon.md`:
     - Line 36: `| Height | 165 cm | — |`
     - Status: **Legacy Discrepancy (+10 cm error)**. Needs update to `155 cm (5' 1")`.

---

### 2.2 Jasper Svartr Douglas Bloodmoon
- **Canonical Target**: `193 cm (6' 4")`
- **Role**: Founding Bloodline Heir, Tech specialist / DJ Frequency, Solar Wolf Twin (`Svartr Sólúlfr`), Delta enforcer.
- **Occurrences in Workspace**:
  1. `FINAL/Jasper_Douglas_Bloodmoon_card.json`:
     - Line 1 (JED+ bracket): `[NAME: Jasper Svartr Douglas Bloodmoon; ... HEIGHT: 193cm (6'4"); ...]`
     - Outfit #9 (`Hybrid Shift`): `223 cm (7'4")` (hybrid combat shift).
     - Status: Metric 193 cm matches; bracket formatting is `193cm (6'4")` without internal spacing.
     - Proportional references: **Missing**.
  2. `FINAL/personas/Jasper_Persona.json`:
     - Line 1 (JED+ bracket): `[NAME: Jasper Svartr Douglas Bloodmoon; ... HEIGHT: 193cm (6'4"); ...]`
     - Appearance `Human Form (Glamour)`: `193 cm (6'4")`.
     - Appearance `Partial Shift`: `193 cm (6'4")`.
     - Status: Metric matches; bracket formatting has no space.
     - Proportional references: **Missing**.
  3. `FINAL/Svartulfr_NPC_Primary.json` (ID `Vcj4h2TL4Usola2A4OOl6`):
     - Line 1 of `content`: `[NAME: Jasper Svartr Douglas Bloodmoon; ... HEIGHT: 193cm (6'4"); ...]`
     - Mirror in `lorebooks/optimized/Svartulfr_NPC_Primary.json`: Identical.
     - Status: Metric matches; bracket formatting has no space.
     - Proportional references: **Missing**.
  4. `database/characters/C_Jasper_Douglas_Bloodmoon.md`:
     - Line 35: `| Height | 191 cm | — |`
     - Status: **Legacy Discrepancy (-2 cm error)**. Needs update to `193 cm (6' 4")`.
  5. `ARCHIVIO/02_Drive_and_Raw_Sources/Sources/Famiglia Lupina Fantasy.html`:
     - Line 52: `Altezza: 1,92 m`.

---

### 2.3 Noah Loki Douglas Bloodmoon
- **Canonical Target**: `197 cm (6' 5.6")`
- **Role**: Founding Bloodline Heir, UCLA 3L Law Student, Diplomat / Pack Beta, Gourmet Chef.
- **Occurrences in Workspace**:
  1. `FINAL/Noah_Douglas_Bloodmoon_card.json`:
     - Line 1 (JED+ bracket): `[NAME: Noah Loki Douglas Bloodmoon; ... HEIGHT: 197cm (6'6"); ...]`
     - Outfit #6 (`Hybrid Shift`): `227 cm (7'5")`.
     - Status: **Imperial Discrepancy** (`6'6"` instead of `6' 5.6"`). Metric matches (197 cm). Spacing is `197cm` without space.
     - Proportional references: **Missing**.
  2. `FINAL/Svartulfr_NPC_Primary.json` (ID `H2JX-NkHRiJ2FzoekC5ZZ`):
     - Line 1 of `content`: `[NAME: Noah Loki Douglas Bloodmoon; ... HEIGHT: 197cm (6'6"); ...]`
     - Mirror in `lorebooks/optimized/Svartulfr_NPC_Primary.json`: Identical.
     - Status: **Imperial Discrepancy** (`6'6"` instead of `6' 5.6"`).
     - Proportional references: **Missing**.
  3. `database/characters/C_Noah_Douglas_Bloodmoon.md`:
     - Line 35: `| Height | 196 cm | — |`
     - Status: **Legacy Discrepancy (-1 cm error)**. Needs update to `197 cm (6' 5.6")`.
  4. `ARCHIVIO/02_Drive_and_Raw_Sources/Sources/Famiglia Lupina Fantasy.html`:
     - Line 67: `Altezza: 1,98 m`.

---

### 2.4 Malachia Björn Douglas Bloodmoon
- **Canonical Target**: `208 cm (6' 9.9")`
- **Role**: Eldest Brother, Heavyweight MMA Fighter, Head of Security / War Enforcer, Delta Alpha.
- **Occurrences in Workspace**:
  1. `FINAL/Malachia_Douglas_Bloodmoon_card.json`:
     - Line 1 (JED+ bracket): `[NAME: Malachia Björn Douglas Bloodmoon; ... HEIGHT: 208cm / 6'10" human form, 258cm / 8'6" hybrid shift; ...]`
     - Outfit #0 (`Allenamento / Combattimento`): `208 cm. Pantaloni da tuta...`
     - Outfit #6 (`Hybrid Shift`): `258 cm (8'6")`.
     - Status: **Imperial Discrepancy** (`6'10"` instead of `6' 9.9"`). Metric matches (208 cm).
     - Proportional references: **Missing**.
  2. `FINAL/Svartulfr_NPC_Primary.json` (ID `jDuJtzirlEZC3K_ArIufh`):
     - Line 1 of `content`: `[NAME: Malachia Björn Douglas Bloodmoon; ... HEIGHT: 208cm / 6'10" human form, 258cm / 8'6" hybrid shift; ...]`
     - Mirror in `lorebooks/optimized/Svartulfr_NPC_Primary.json`: Identical.
     - Status: **Imperial Discrepancy** (`6'10"` instead of `6' 9.9"`).
     - Proportional references: **Missing**.
  3. `database/characters/C_Malachia_Douglas_Bloodmoon.md`:
     - Line 35: `| Height | 210 cm | — |`
     - Status: **Legacy Discrepancy (+2 cm error)**. Needs update to `208 cm (6' 9.9")`.
  4. `ARCHIVIO/02_Drive_and_Raw_Sources/Sources/Famiglia Lupina Fantasy.html`:
     - Line 22: `Altezza: 2,08 m`. Matches 208 cm.

---

### 2.5 Erik Ulfr Douglas
- **Canonical Target**: `213 cm (6' 11.9")`
- **Role**: Douglas Patriarch, CEO of DCC (Douglas Commerce Coalition), Pureblood Alpha Prime.
- **Occurrences in Workspace**:
  1. `FINAL/Erik_Douglas_card.json`:
     - Line 1 (JED+ bracket): `[NAME: Erik Ulfr Douglas; ... HEIGHT: 213cm / 7'0" human form, 263cm / 8'7" hybrid shift; ...]`
     - Outfit #0 (`Casual / Home`): **Severe Discrepancy**: Line says `203 cm. Pantaloni sartoriali in lino grigio antracite...` (error carried over from early Gemini prompt generation).
     - Outfit #4 (`Hybrid Shift`): `263 cm (8'7")`.
     - Description text: `213cm nightmare of muscle and fur...`
     - Status: **Imperial Discrepancy** (`7'0"` instead of `6' 11.9"`). **Internal Discrepancy in Outfit #0** (`203 cm` must be updated to `213 cm`).
     - Proportional references: **Missing**.
  2. `FINAL/Svartulfr_NPC_Primary.json` (ID `C-JisFj8qA1tsFEqZKevk`):
     - Line 1 of `content`: `[NAME: Erik Ulfr Douglas; ... HEIGHT: 213cm / 7'0" human form, 263cm / 8'7" hybrid shift; ...]`
     - Note: In content section for Outfit #0, `203 cm` is also present!
     - Mirror in `lorebooks/optimized/Svartulfr_NPC_Primary.json`: Identical.
     - Status: **Imperial Discrepancy** (`7'0"` instead of `6' 11.9"`). **Internal Discrepancy in Outfit #0** (`203 cm`).
     - Proportional references: **Missing**.
  3. `database/characters/C_Erik_Douglas.md`:
     - Line 45: `| Height | 205 cm | Visual Authority |`
     - Status: **Legacy Discrepancy (-8 cm error)**. Needs update to `213 cm (6' 11.9")`.
  4. `database/assets/argon_gemini_prompts_reference.md`:
     - Turn 20 mentions `203 cm` in Erik's casual outfit prompt.
  5. `ARCHIVIO/02_Drive_and_Raw_Sources/Sources/Famiglia Lupina Fantasy.html`:
     - Line 7: `Altezza: 2,13 m`. Matches 213 cm.

---

### 2.6 Wulfnic Báleygr Bloodmoon
- **Canonical Target**: `220 cm (7' 2.6")`
- **Role**: Primordial Firstborn (827 AD), Bloodmoon Patriarch, Sacred Custodian of Fenris Heritage, One-Eyed Colossus.
- **Occurrences in Workspace**:
  1. `FINAL/Wulfnic_Bloodmoon_card.json`:
     - Line 1 (JED+ bracket): `[NAME: Wulfnic Báleygr Bloodmoon; ... HEIGHT: 220cm (7'3") human form, 300cm (9'10") primeval bipedal wolf shift; ...]`
     - Outfit #0 (`Sanctuary / Longhouse`): **Severe Discrepancy**: Line says `...petto colossale da 210 cm solcato da antiche cicatrici rituali...` (legacy text error from when Wulfnic was drafted at 210 cm before being stabilized at 220 cm).
     - Outfit #9 (`Hybrid Shift`): `285 cm`.
     - Outfit #10 (`Full Shift`): `150 cm al garrese`.
     - Description text: `220cm of heavily scarred primeval muscle...`
     - Status: **Imperial Discrepancy** (`7'3"` instead of `7' 2.6"`). **Internal Discrepancy in Outfit #0** (`210 cm` must be updated to `220 cm`).
     - Proportional references: **Missing**.
  2. `FINAL/Svartulfr_NPC_Primary.json` (ID `HhuMluMmIIENUei3bX6ed`):
     - Line 1 of `content`: `[NAME: Wulfnic Báleygr Bloodmoon; ... HEIGHT: 220cm (7'3") human form, 300cm (9'10") primeval bipedal wolf shift; ...]`
     - Note: In content section for Outfit #0, `210 cm` is also present!
     - Mirror in `lorebooks/optimized/Svartulfr_NPC_Primary.json`: Identical.
     - Status: **Imperial Discrepancy** (`7'3"` instead of `7' 2.6"`). **Internal Discrepancy in Outfit #0** (`210 cm`).
     - Proportional references: **Missing**.
  3. `database/characters/C_Wulfnic_Bloodmoon.md`:
     - Line 152: `| Height | 195 cm | Visual Authority |`
     - Status: **Legacy Discrepancy (-25 cm error)** from early draft. Needs update to `220 cm (7' 2.6")`.
  4. `database/assets/argon_gemini_prompts_reference.md`:
     - Turn 8 mentions `Wulfnic, un gigante di 210 cm di statura`.

---

## 3. Secondary Characters Survey (Edric, Logan, Mackenzie)

For complete situational awareness and boundary verification:
- **Edric Douglas** (`FINAL/Edric_Douglas_card.json` & Secondary Lorebook ID `h-ttmlgJYeRXqyDvQjSX7`):
  - Bracket HEIGHT: `165cm (5'5"), remarkably tall and broad for a thirteen-year-old`
  - Outfit #7: `182 cm` (projected adult height)
  - Outfit #8 (`Hybrid Shift`): `230 cm`
  - Non-target for R1 direct change, but consistent.
- **Logan Járn Douglas** (`FINAL/Logan_Douglas_card.json` & Primary Lorebook ID `tAcrWLtWSDGf3xJJRwUOM`):
  - Bracket HEIGHT: `198cm / 6'6" human form, 228cm / 7'6" hybrid shift`
  - Outfit #5 (`Garage / Officina`): `196 cm`
  - Database record `database/characters/C_Logan_Douglas.md`: `198 cm`.
- **Mackenzie Sanchez-Rogers** (`FINAL/Mackenzie_Sanchez_Rogers_card.json` & Primary Lorebook ID `BXi3sENAVYB8OKF80Q9Su`):
  - Bracket HEIGHT: `6'2" (188 cm)`
  - Outfit #9: `172 cm`
  - Outfit #10 (`Hybrid Shift`): `235 cm`.

---

## 4. Proportional References Survey

### 4.1 Specification of Required Proportional References
The authoritative user request specifies three mandatory direct proportional references:
1. **Reference 1 (Alyssa vs Jasper)**:
   > *"Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm)."*
   - Height Delta: $-38\text{ cm}$.
   - Anatomical anchor: Her head/crown aligns with Jasper's shoulder seam.
2. **Reference 2 (Malachia vs Alyssa)**:
   > *"Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico."*
   - Height Delta: $+53\text{ cm}$ (more than half a meter).
   - Anatomical anchor: The top of Alyssa's head barely reaches mid-chest on Malachia's massive frame.
3. **Reference 3 (Erik & Wulfnic vs Alyssa)**:
   > *"Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno)."*
   - Height Delta: $+58\text{ cm}$ (Erik) to $+65\text{ cm}$ (Wulfnic).
   - Anatomical anchor: Alyssa reaches only to their lower chest / sternum line.

### 4.2 Comprehensive Audit of Existing Files
Every category of candidate files was searched for these three clauses:

| File Category | Total Files Inspected | Proportional References Found | Status |
|---------------|-----------------------|--------------------------------|--------|
| **Character Cards** (`FINAL/*_card.json`, `ARCHIVIO/cards_legacy/`) | 15 files | 0 files | **100% Missing** |
| **User Personas** (`FINAL/personas/*.json`) | 3 files | 0 files | **100% Missing** |
| **Standalone Lorebooks** (`FINAL/*.json`, `lorebooks/optimized/*.json`) | 12 files (1,009 entries) | 0 entries | **100% Missing** |
| **Character Scenarios** (`FINAL/scenarios/*.json`, `Master_Scenario.json`) | 8 files (55 greetings) | 0 greetings | **100% Missing** |
| **Group Visual Prompts** (`database/assets/`, `ARCHIVIO/.../Sources/`) | 6 prompt files | 0 prompts | **100% Missing** |
| **System Prompts & Assistants** (`FINAL/assistants/`, `FINAL/prompts/`) | 2 files | 0 files | **100% Missing** |

### 4.3 Where These Proportional References MUST Be Integrated
To satisfy Requirement R1 thoroughly and permanently, the implementer agent should inject the canonical proportional block into the following locations:
1. **Character Cards & Personas (`description`)**:
   - In `Alyssa_Douglas_Bloodmoon_card.json`, `Alyssa_Persona.json`, and Lorebook Entry `alyssa_world_dossier_2b54a223`: Under a dedicated section or subsection inside `FAMILY & PACK:` or `VOICE & BEHAVIOR:`.
   - In `Jasper_Douglas_Bloodmoon_card.json`, `Jasper_Persona.json`, and Lorebook Entry `Vcj4h2TL4Usola2A4OOl6`: Directly noting the twin height disparity ($-38\text{ cm}$, Alyssa at his shoulder).
   - In `Malachia_Douglas_Bloodmoon_card.json` and Lorebook Entry `jDuJtzirlEZC3K_ArIufh`: Under `FAMILY & PACK:`, describing his protective stance over Alyssa (+53 cm, head to mid-chest).
   - In `Erik_Douglas_card.json` and Lorebook Entry `C-JisFj8qA1tsFEqZKevk`: Under `FAMILY & PACK:`, describing the patriarch towering over his daughter (+58 cm, head to lower chest/sternum).
   - In `Wulfnic_Bloodmoon_card.json` and Lorebook Entry `HhuMluMmIIENUei3bX6ed`: Under `FAMILY & PACK:`, describing the ancient grandfather towering over his granddaughter (+65 cm, head to sternum).
2. **Visual Prompts & Style Guide**:
   - `database/assets/style_guide.md`: Add a new Section "5. Canonical Proportions & Scale Reference in Group Compositions" containing the exact height deltas and framing guidelines.
   - `database/assets/argon_gemini_prompts_reference.md`: Add the group composition scale guidelines in the introductory standard.
   - Any new group visual prompts generated for the pack.
3. **Scenarios**:
   - In `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`, `Svartulfr_Scenario_SUCC_Route_Jasper.json`, and `Svartulfr_Master_Scenario.json`: Add explicit proportional stage directions in greeting text where the twins, Malachia, Erik, and Wulfnic stand together.

---

## 5. Invariant and Parity Verification

### 5.1 Lorebook Parity (`entries == lexicon`)
- **Surveyed Lorebooks**:
  1. `Svartulfr_NPC_Primary.json`: 99 entries == 99 lexicon (Parity: `True`)
  2. `Svartulfr_NPC_Secondary.json`: 211 entries == 211 lexicon (Parity: `True`)
  3. `Svartulfr_Lorebook_I.json`: 237 entries == 237 lexicon (Parity: `True`)
  4. `Svartulfr_Lorebook_II.json`: 142 entries == 142 lexicon (Parity: `True`)
  5. `Svartulfr_Lorebook_III.json`: 46 entries == 46 lexicon (Parity: `True`)
  6. `Svartulfr_Location.json`: 225 entries == 225 lexicon (Parity: `True`)
- **Optimization Mirror Parity**:
  - All files in `lorebooks/optimized/*.json` are 100% byte-for-byte identical to `FINAL/`.
- **Constraint for Implementer**:
  - Whenever updating `Svartulfr_NPC_Primary.json` with the remediated heights and proportional references, **both `entries` and `lexicon` arrays must be updated in exact synchronization**, and the result mirrored immediately to `lorebooks/optimized/Svartulfr_NPC_Primary.json`.

### 5.2 Single-Line JED+ Bracket Block Invariant
- **Rule**: `[NAME: ...; SPECIES: ...; AGE: ...; HEIGHT: ...; ...]` must occupy **strictly line 0** without line breaks.
- **Verification**: Confirmed on all 8 active cards in `FINAL/`, all legacy cards in `ARCHIVIO/cards_legacy/`, all 3 personas in `FINAL/personas/`, and all 310 NPC entries across Primary and Secondary.
- **Implementation Precaution**:
  - When replacing `HEIGHT: 197cm (6'6")` with `HEIGHT: 197 cm (6' 5.6")`, or `HEIGHT: 208cm / 6'10"` with `HEIGHT: 208 cm (6' 9.9")`, the edit must stay on the single line within the bracket block.

### 5.3 Formatting Discipline
- **Em-Dash Rule**: Zero em-dashes (`—`) in all character and lorebook text; use commas (`,`) or periods (`.`).
- **Dialogue Enclosure**: Standard ASCII double quotes (`"..."`).
- **Markdown Restriction**: No bold asterisks (`**`) in lorebook entries or narrative text.

---

## 6. Detailed File-by-File Remediation Catalog

Below is the concrete inventory of target files requiring edits during the implementation phase:

| File Target | Entity | Field | Current Value | Canonical Target Value |
|-------------|--------|-------|---------------|------------------------|
| `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json` | Alyssa | Line 0 Bracket | `HEIGHT: 155cm (5'1")` | `HEIGHT: 155 cm (5' 1")` |
| `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json` | Alyssa | `description` | Lacks proportional references | Add Reference 1, 2, 3 block |
| `FINAL/personas/Alyssa_Persona.json` | Alyssa | Line 0 Bracket | `HEIGHT: 155cm (5'1")` | `HEIGHT: 155 cm (5' 1")` |
| `FINAL/personas/Alyssa_Persona.json` | Alyssa | `description` | Lacks proportional references | Add Reference 1, 2, 3 block |
| `FINAL/Svartulfr_NPC_Primary.json` (`alyssa_world_dossier_2b54a223`) | Alyssa | Line 0 Bracket & Content | `HEIGHT: 155cm (5'1")` | `HEIGHT: 155 cm (5' 1")` + Reference block |
| `lorebooks/optimized/Svartulfr_NPC_Primary.json` | Alyssa | Mirror | Synced with above | Synced with above |
| `database/characters/C_Alyssa_Douglas_Bloodmoon.md` | Alyssa | Table Row | `\| Height \| 165 cm \| — \|` | `\| Height \| 155 cm (5' 1") \| — \|` |
| `FINAL/Jasper_Douglas_Bloodmoon_card.json` | Jasper | Line 0 Bracket | `HEIGHT: 193cm (6'4")` | `HEIGHT: 193 cm (6' 4")` |
| `FINAL/Jasper_Douglas_Bloodmoon_card.json` | Jasper | `description` | Lacks proportional reference | Add Reference 1 |
| `FINAL/personas/Jasper_Persona.json` | Jasper | Line 0 Bracket | `HEIGHT: 193cm (6'4")` | `HEIGHT: 193 cm (6' 4")` |
| `FINAL/personas/Jasper_Persona.json` | Jasper | `description` | Lacks proportional reference | Add Reference 1 |
| `FINAL/Svartulfr_NPC_Primary.json` (`Vcj4h2TL4Usola2A4OOl6`) | Jasper | Line 0 Bracket & Content | `HEIGHT: 193cm (6'4")` | `HEIGHT: 193 cm (6' 4")` + Reference 1 |
| `lorebooks/optimized/Svartulfr_NPC_Primary.json` | Jasper | Mirror | Synced with above | Synced with above |
| `database/characters/C_Jasper_Douglas_Bloodmoon.md` | Jasper | Table Row | `\| Height \| 191 cm \| — \|` | `\| Height \| 193 cm (6' 4") \| — \|` |
| `FINAL/Noah_Douglas_Bloodmoon_card.json` | Noah | Line 0 Bracket | `HEIGHT: 197cm (6'6")` | `HEIGHT: 197 cm (6' 5.6")` |
| `FINAL/Svartulfr_NPC_Primary.json` (`H2JX-NkHRiJ2FzoekC5ZZ`) | Noah | Line 0 Bracket & Content | `HEIGHT: 197cm (6'6")` | `HEIGHT: 197 cm (6' 5.6")` |
| `lorebooks/optimized/Svartulfr_NPC_Primary.json` | Noah | Mirror | Synced with above | Synced with above |
| `database/characters/C_Noah_Douglas_Bloodmoon.md` | Noah | Table Row | `\| Height \| 196 cm \| — \|` | `\| Height \| 197 cm (6' 5.6") \| — \|` |
| `FINAL/Malachia_Douglas_Bloodmoon_card.json` | Malachia | Line 0 Bracket | `HEIGHT: 208cm / 6'10" human form...` | `HEIGHT: 208 cm (6' 9.9") human form...` |
| `FINAL/Malachia_Douglas_Bloodmoon_card.json` | Malachia | `description` | Lacks proportional reference | Add Reference 2 |
| `FINAL/Svartulfr_NPC_Primary.json` (`jDuJtzirlEZC3K_ArIufh`) | Malachia | Line 0 Bracket & Content | `HEIGHT: 208cm / 6'10" human form...` | `HEIGHT: 208 cm (6' 9.9") human form...` + Ref 2 |
| `lorebooks/optimized/Svartulfr_NPC_Primary.json` | Malachia | Mirror | Synced with above | Synced with above |
| `database/characters/C_Malachia_Douglas_Bloodmoon.md` | Malachia | Table Row | `\| Height \| 210 cm \| — \|` | `\| Height \| 208 cm (6' 9.9") \| — \|` |
| `FINAL/Erik_Douglas_card.json` | Erik | Line 0 Bracket | `HEIGHT: 213cm / 7'0" human form...` | `HEIGHT: 213 cm (6' 11.9") human form...` |
| `FINAL/Erik_Douglas_card.json` | Erik | Outfit #0 | `203 cm. Pantaloni sartoriali...` | `213 cm. Pantaloni sartoriali...` |
| `FINAL/Erik_Douglas_card.json` | Erik | `description` | Lacks proportional reference | Add Reference 3 |
| `FINAL/Svartulfr_NPC_Primary.json` (`C-JisFj8qA1tsFEqZKevk`) | Erik | Line 0 Bracket & Content | `HEIGHT: 213cm / 7'0"` & `203 cm` | `HEIGHT: 213 cm (6' 11.9")` & `213 cm` + Ref 3 |
| `lorebooks/optimized/Svartulfr_NPC_Primary.json` | Erik | Mirror | Synced with above | Synced with above |
| `database/characters/C_Erik_Douglas.md` | Erik | Table Row | `\| Height \| 205 cm \| Visual Authority \|` | `\| Height \| 213 cm (6' 11.9") \| Visual Authority \|` |
| `FINAL/Wulfnic_Bloodmoon_card.json` | Wulfnic | Line 0 Bracket | `HEIGHT: 220cm (7'3") human form...` | `HEIGHT: 220 cm (7' 2.6") human form...` |
| `FINAL/Wulfnic_Bloodmoon_card.json` | Wulfnic | Outfit #0 | `...petto colossale da 210 cm...` | `...petto colossale da 220 cm...` |
| `FINAL/Wulfnic_Bloodmoon_card.json` | Wulfnic | `description` | Lacks proportional reference | Add Reference 3 |
| `FINAL/Svartulfr_NPC_Primary.json` (`HhuMluMmIIENUei3bX6ed`) | Wulfnic | Line 0 Bracket & Content | `HEIGHT: 220cm (7'3")` & `210 cm` | `HEIGHT: 220 cm (7' 2.6")` & `220 cm` + Ref 3 |
| `lorebooks/optimized/Svartulfr_NPC_Primary.json` | Wulfnic | Mirror | Synced with above | Synced with above |
| `database/characters/C_Wulfnic_Bloodmoon.md` | Wulfnic | Table Row | `\| Height \| 195 cm \| Visual Authority \|` | `\| Height \| 220 cm (7' 2.6") \| Visual Authority \|` |
| `database/assets/style_guide.md` | Group Prompts | End of File | Lacks group scale section | Add Section 5: Group Proportions & Scale |

---

## 7. Recommended Standard Proportional Block Format

To maintain aesthetic uniformity, zero em-dash compliance, and readability across Character Cards, User Personas, Lorebooks, and Prompts, the following standard text block is recommended for insertion into character profiles and group prompts:

### For Alyssa (Card, Persona, Lorebook):
```text
PROPORTIONS & SCALE: Statura minuta di 155 cm (5' 1"). Arriva all'altezza della spalla del gemello Jasper (193 cm, -38 cm). Malachia (208 cm) la supera di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a meta del torace mastodontico. Erik (213 cm) e Wulfnic (220 cm) la sovrastano di 58-65 cm, facendola arrivare alla parte bassa del petto o sterno.
```

### For Jasper (Card, Persona, Lorebook):
```text
PROPORTIONS & SCALE: Statura slanciata di 193 cm (6' 4"). Sovrasta la gemella Alyssa (155 cm) di 38 cm, la cui testa gli arriva esattamente all'altezza della spalla.
```

### For Malachia (Card, Lorebook):
```text
PROPORTIONS & SCALE: Statura imponente di 208 cm (6' 9.9"). Supera la sorella minore Alyssa (155 cm) di oltre mezzo metro (+53 cm), la cui testa gli arriva a malapena a meta del torace mastodontico.
```

### For Erik (Card, Lorebook):
```text
PROPORTIONS & SCALE: Statura colossale di 213 cm (6' 11.9"). Sovrasta la figlia Alyssa (155 cm) di 58 cm, che gli arriva alla parte bassa del petto o sterno.
```

### For Wulfnic (Card, Lorebook):
```text
PROPORTIONS & SCALE: Statura primordiale di 220 cm (7' 2.6"). Sovrasta la nipote Alyssa (155 cm) di 65 cm, che gli arriva alla parte bassa del petto o sterno.
```

### For Group Visual Prompts (`style_guide.md`):
```text
## 5. Group Scale & Proportional Guardrails (Pack Lineup)
When depicting the Douglas-Bloodmoon family members together in a group composition or visual prompt, enforce exact physical height deltas:
- Alyssa: 155 cm (5' 1") — petite hourglass frame.
- Jasper: 193 cm (6' 4") — Alyssa's head reaches Jasper's shoulder seam (-38 cm difference).
- Noah: 197 cm (6' 5.6") — lithe, tall swimmer build.
- Malachia: 208 cm (6' 9.9") — massive scarred heavyweight colossus. Alyssa reaches only to mid-chest (+53 cm difference).
- Erik: 213 cm (6' 11.9") — towering corporate alpha patriarch. Alyssa reaches lower chest / sternum (+58 cm difference).
- Wulfnic: 220 cm (7' 2.6") — ancient Firstborn dire colossus. Alyssa reaches lower chest / sternum (+65 cm difference).
```

---

## 8. Conclusion

The codebase currently has:
1. Solid baseline alignment on metric integer heights (155, 193, 197, 208, 213, 220), but noticeable drift in imperial conversions (`6'6"` instead of `6' 5.6"`, `6'10"` instead of `6' 9.9"`, `7'0"` instead of `6' 11.9"`, `7'3"` instead of `7' 2.6"`).
2. Spurious localized outfit typos (`203 cm` in Erik Outfit 0, `210 cm` in Wulfnic Outfit 0).
3. 100% absence of the explicit proportional references across all character cards, personas, lorebooks, scenarios, and visual prompts.
4. Outdated legacy height entries in `database/characters/*.md`.
5. Perfect baseline parity (`entries == lexicon = True`) in all lorebooks ready for safe, synchronized updates.

This comprehensive catalog provides the exact blueprints and file-level guidance for the implementation agent to execute R1 cleanly and deterministically.
