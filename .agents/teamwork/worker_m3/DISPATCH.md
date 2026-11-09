# Task Assignment: Milestone 3 — Character Cards & Personas Synchronization

## Objective
Synchronize the newly established emergent lore (St. Brugge Private Academy, Father Revazhael joint tutelage, applied runic crystallography, individual resonant cylinder calibration, registered Hunter/Healer credentials, Welcome Fest KSA intimidation, and Suite 3 details) across all 4 character cards and personas:
1. `FINAL/Jasper_Douglas_Bloodmoon_card.json`
2. `FINAL/personas/Jasper_Persona.json`
3. `FINAL/personas/Alyssa_Persona.json`
4. `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`

## Inputs & Source of Truth
- Authoritative Drop-In Text: `.agents/teamwork/explorer_survey_3/handoff.md` (Sections 4.2 & 4.3).
- Repository Rules: `GEMINI.md` (Rules 1-5, JED+ formatting, positive framing, 0 em-dashes, double quotes for dialogue).
- Master Project Scope: `PROJECT.md` (Feature Inventory items 1, 2, 4, 6, 7, 11).

## Scope & File Ownership
You have exclusive write ownership of:
- `FINAL/Jasper_Douglas_Bloodmoon_card.json`
- `FINAL/personas/Jasper_Persona.json`
- `FINAL/personas/Alyssa_Persona.json`
- `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`
- `scripts/verify_milestone3_cards_personas.py` (verification script)

DO NOT modify files outside this ownership without approval.

## Detailed Requirements

### 1. `FINAL/Jasper_Douglas_Bloodmoon_card.json`
- **Line 1 Bracket Block `[...]`**:
  Update to single-line PList including:
  `EDUCATION: St. Brugge Private Academy alumnus;`
  `SOCIAL_STATUS: Citizen, Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555), Black-Market Info-Broker, Outlaw;`
  `OCCUPATION: 1st-year undergrad (SUCC) Acoustic and Sound Engineering, Underground DJ, Tecnomancer, Cyber-Rogue and Arcane Hacker specialized in digital locks, demonic seals, and runic cipher translation, Caretaker and Left Hand designate to Malachia;`
  Canonical birthmark: `radiant black sun birthmark on right hip (Mark of Sol)`.
- **RPG Stats Block**:
  Fix residual bug `[LEVEL: 3; ...]` -> `[LEVEL: 19; ...]`.
- **`BACKSTORY:`**:
  Replace with proposed drop-in text detailing St. Brugge Private Academy joint apprenticeship with Father Revazhael, translating runes while Alyssa shaped crystal matrices, Abyssal Armor gift and formula, Dragon Glass Katana bearer as Alyssa's lethal shadow, Grade A Guild Hunter ID JDB-555.
- **`FAMILY & PACK:`**:
  Add paragraph detailing twin craft collaboration (Acoustic and Sound Engineering resonance tuning for Alyssa's cylinders) and refusal to pledge KSA.
- **`VOICE & BEHAVIOR:`**:
  Add SUCC campus reputation (putting 3 KSA brothers to flight at Welcome Fest with an icy glare, auditing TIT router).

### 2. `FINAL/personas/Jasper_Persona.json`
- **Line 1 Bracket Block `[...]`**:
  Single-line PList matching card (St. Brugge alumnus, Registered Guild Hunter JDB-555, Mark of Sol on right hip).
- **`BACKSTORY:`**:
  Update to match collaborative St. Brugge tutelage with Father Rev and Guild Hunter status.
- **`FAMILY & PACK:`**:
  Add twin craft collaboration and KSA independence.
- **`VOICE & BEHAVIOR:`**:
  Add Welcome Fest KSA intimidation reputation.

### 3. `FINAL/personas/Alyssa_Persona.json`
- **Line 1 Bracket Block `[...]`**:
  Single-line PList: purge "Novice Healing Mage", add `EDUCATION: St. Brugge Private Academy alumnus;`, `OCCUPATION: 1st-year undergrad (SUCC) Pre-Med, Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555), Applied Runic Crystallographer, Botanist, Pack Mom designate (inheriting office from Elizabeth Duskwood at 21);`.
- **`BACKSTORY:`**:
  Update to match collaborative St. Brugge tutelage with Father Revazhael (applied runic crystallography, enchanted cylinders, Abyssal magic theory), Absolute Pacifist Vow, passing katana to Jasper, Certified Guild Healer Rank A ADB-555.

### 4. `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`
- **Line 1 Bracket Block `[...]`**:
  Single-line PList matching Alyssa Persona (St. Brugge alumnus, Certified Guild Healer Rank A ADB-555).
- **`BACKSTORY:`**:
  Update to match collaborative St. Brugge tutelage.
- **`SIGNATURE ITEMS & VEHICLE:`**:
  Update `Enchanted Cylinders` (flashlight-sized, frozen spells, individual resonance tuning vs fragile DMHA cylinders) and add alchemical laboratory glassware in Bag of Holding.
- **`personality`**:
  Update role to `ROLE: Dominant Omega (4th White Moon / Hvit Reborn), SUCC Pre-Med, Certified Guild Healer & Field Medic (Rank A), Pack Mom Designate;`.

## Formatting & Integrity Disciplines
- **Zero Em-Dashes (`—`)**: Strict prohibition across all edited fields. Use commas or periods.
- **Spoken Dialogue**: Double quotes `"..."`.
- **Narration & Prose**: Plain text, zero asterisks `*` or `**`.
- **Positive Framing for Demi-Humans**: Single animal ears on crown described naturally; never state or imply absence of human ears.
- **Single-Line PList**: Initial `[...]` block must be on a single continuous line.
- **Verification Script**: Create `scripts/verify_milestone3_cards_personas.py` and run it via terminal to verify 100% compliance.

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Completion Criteria
- All 4 target JSON files updated, valid JSON syntax, JED+ format preserved.
- `scripts/verify_milestone3_cards_personas.py` exits with 0 and all checks pass.
- Write a complete handoff report to `.agents/teamwork/worker_m3/handoff.md`.


## 2026-11-02T07:24:17Z
[Message] timestamp=2026-11-02T07:24:17Z sender=a6280f2d-32ae-4a10-82fa-5604ad40f230 priority=MESSAGE_PRIORITY_HIGH content=You are worker_m3, assigned to Milestone 3: Character Cards & Personas Synchronization for Svartúlfr Verse.

Your working directory is: `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m3\`

You MUST first read:
1. `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m3\DISPATCH.md`
2. `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md`
3. `e:\repository\SvartulfrVerse\PROJECT.md`
4. `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_survey_3\handoff.md` (Sections 4.2 & 4.3 contain the exact drop-in texts and specifications)

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

SCOPE & EXCLUSIVE WRITE OWNERSHIP:
- `FINAL/Jasper_Douglas_Bloodmoon_card.json`
- `FINAL/personas/Jasper_Persona.json`
- `FINAL/personas/Alyssa_Persona.json`
- `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`
- `scripts/verify_milestone3_cards_personas.py` (verification script)

KEY CHANGES TO EXECUTE:
1. `FINAL/Jasper_Douglas_Bloodmoon_card.json`:
   - Line 1 bracket block: update single-line PList with Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555), St. Brugge Private Academy alumnus, Mark of Sol birthmark on right hip.
   - RPG Stats: fix residual bug `[LEVEL: 3; ...]` -> `[LEVEL: 19; ...]`.
   - `BACKSTORY:`: replace with drop-in text (St. Brugge joint tutelage with Revazhael, translating runes while Alyssa shaped crystal matrices, Abyssal Armor gift and formula, Dragon Glass Katana bearer as Alyssa's shadow, Grade A Guild Hunter JDB-555).
   - `FAMILY & PACK:`: add paragraph detailing twin craft collaboration (Acoustic and Sound Engineering resonance tuning for Alyssa's cylinders) and KSA independence.
   - `VOICE & BEHAVIOR:`: add lethal campus reputation (putting 3 KSA brothers to flight at Welcome Fest with an icy glare, auditing TIT router).
2. `FINAL/personas/Jasper_Persona.json`:
   - Line 1 bracket block: single-line PList matching card (St. Brugge alumnus, Registered Hunter JDB-555, Mark of Sol on right hip).
   - `BACKSTORY:`: update to match collaborative St. Brugge backstory.
   - `FAMILY & PACK:`: add twin craft collaboration and KSA independence.
   - `VOICE & BEHAVIOR:`: add Welcome Fest reputation.
3. `FINAL/personas/Alyssa_Persona.json`:
   - Line 1 bracket block: single-line PList: purge "Novice Healing Mage", add `Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555)`, `EDUCATION: St. Brugge Private Academy alumnus;`.
   - `BACKSTORY:`: update to match collaborative St. Brugge tutelage with Father Rev (applied runic crystallography, enchanted cylinders, Abyssal magic theory), Absolute Pacifist Vow, passing katana to Jasper, Certified Guild Healer Rank A ADB-555.
4. `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`:
   - Line 1 bracket block: single-line PList matching Alyssa Persona (St. Brugge alumnus, Certified Guild Healer Rank A ADB-555).
   - `BACKSTORY:`: update to match collaborative St. Brugge tutelage.
   - `SIGNATURE ITEMS & VEHICLE:`: update Enchanted Cylinders (flashlight-sized, frozen spells, individual resonance tuning vs fragile DMHA cylinders) and add alchemical laboratory glassware in Bag of Holding.
   - `personality`: update role to `ROLE: Dominant Omega (4th White Moon / Hvit Reborn), SUCC Pre-Med, Certified Guild Healer & Field Medic (Rank A), Pack Mom Designate;`.

FORMATTING & INTEGRITY RULES:
- Exactly 0 em-dashes (`—`), use commas or periods.
- Spoken dialogue in standard double quotes `"..."`.
- Narration and prose in plain text, strictly 0 markdown asterisks `*` or `**`.
- Positive framing for demi-humans (single pair of animal ears on crown described naturally; never state or imply absence of human ears).
- Single-line PList header: the initial `[...]` block must occupy exactly one continuous line.
- World Clock: 2024.

VERIFICATION:
Create and run `scripts/verify_milestone3_cards_personas.py` checking:
- Valid JSON syntax in all 4 files.
- Single-line line 1 bracket block in all 4 files.
- Level 19 in Jasper card.
- Registered Hunter JDB-555 and St. Brugge in Jasper files.
- Certified Guild Healer ADB-555 and St. Brugge in Alyssa files; 0 occurrences of "Novice Healing Mage".
- 0 em-dashes across all 4 files.
- 0 markdown bold asterisks in narrative fields.
- Positive framing for demi-human ears.

Deliver your complete report to `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m3\handoff.md` and send a message back when finished.
