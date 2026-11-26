# Comprehensive Analysis — Explorer R6-2: Character Cards Mine & Legacy Archive (R3)

**Author**: Explorer R6-2  
**Date**: 2026-10-21  
**Target Milestone**: Survey & Discovery for R3 (Character Cards Reduction to 8, Jared Thompson Deletion & Legacy Card Archive)  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_2`

---

## 1. Wyvern API `/characters/mine` Investigation

### 1.1 Live API Query Results
A live HTTP GET request was executed against `https://app.wyvern.chat/api/characters/mine` using the active Bearer token in `scratch/wyvern_token.txt`.
The endpoint returned HTTP 200 with an array of **9 characters** currently active under the authenticated user's account:

| # | ID | Character Name | Status on Wyvern | Role in Svartúlfr Verse |
|---|----|----------------|------------------|-------------------------|
| 1 | `_t4J9aQNJM36cUKAP4wB4U` | Jasper Svartr Douglas Bloodmoon | Active | Approved Canon (Twin Brother / Beta Technomancer) |
| 2 | `_QPea6g4Q1QfeYCVHCLMPR` | Erik Ulfr Douglas | Active | Approved Canon (Father / Pack Leader / DCC Chairman) |
| 3 | `_T8Ywcr9FEqNf9JxbK6eHP` | Logan Járn Douglas | Active | Approved Canon (Uncle / The Verve Owner) |
| 4 | `_RDfz7XzTpM23LpPALVXHM` | Malachia Björn Douglas Bloodmoon | Active | Approved Canon (Eldest Brother / Dominant Alpha) |
| 5 | `_zFLUjV8aVxQRAfQxGcAcY` | Noah Loki Douglas Bloodmoon | Active | Approved Canon (Politician Brother / Delta Strategist) |
| 6 | `_TbRM3EdxDjHFgqztTbCpL` | Edric Douglas | Active | Approved Canon (Cousin / Junior Football Running Back) |
| 7 | `_HEQQbbRFwKdG8QE2Fh1z1` | Wulfnic Báleygr Bloodmoon | Active | Approved Canon (Maternal Grandfather / Bloodmoon Patriarch) |
| 8 | `_xJVPtBLL3dxy69RLKL9X9` | Jared Thompson | **Active (Target for Deletion)** | SUCC Bulls Quarterback (Transitioning to NPC) |
| 9 | `_zn24784jfcchQ7EwCyAnm` | Mackenzie Sanchez-Rogers | Active | Approved Canon (Crush / Track Co-Captain) |

### 1.2 Inspection of Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`)
Direct inspection via `GET https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9` confirmed:
- **HTTP Status**: 200 OK
- **ID**: `_xJVPtBLL3dxy69RLKL9X9` (internal `_id`: `_xJVPtBLL3dxy69RLKL9X9`)
- **Name**: Jared Thompson
- **Created At**: `2026-10-16T13:37:03.814Z`
- **Updated At**: `2026-10-18T15:29:42.649Z`
- **Visibility**: `private`
- **Outfits**: 11 configured outfits
- **Description Length**: 8,696 characters (complete JED+ profile)
- **First Message Length**: 2,453 characters
- **Avatar URL**: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7476db0-8dae-4450-8c84-3408b375c000/public`

### 1.3 DELETE Endpoint Syntax, Headers & Requirements
Based on historical platform conventions (documented in `CHANGELOG.md` line 223, `scratch/execute_delete_scenarios.py`, and `GEMINI.md` section 11/15), the character deletion endpoint is:

- **Method**: `DELETE`
- **URL**: `https://app.wyvern.chat/api/characters/{id}`
  - Specifically for Jared: `DELETE https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9`
- **Request Headers**:
  - `Authorization: Bearer <token>` (from `scratch/wyvern_token.txt`)
  - `Accept: application/json`
  - `User-Agent: Mozilla/5.0`
- **Request Body**: None (empty body)
- **Expected Response**: `HTTP 204 No Content` (or `HTTP 200 OK`)
- **Pre-Delete Protocol (Mandatory)**:
  - In accordance with `GEMINI.md` (§11 "Pre-deletion Snapshot"): Save a local pre-delete snapshot of the complete live JSON object in `scratch/backup_deleted_cards_20261021/DELETED_Jared_Thompson__xJVPtBLL3dxy69RLKL9X9.json`.
- **Post-Delete Verification**:
  1. `GET https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9` must return `HTTP 404 Not Found`.
  2. `GET https://app.wyvern.chat/api/characters/mine` must return exactly 8 characters.

---

## 2. Confirmation of the 8 Approved Cards

The 8 approved character cards that must remain active on Wyvern `/characters/mine` and present in `FINAL/` were verified both locally and live over the Wyvern REST API:

| # | Live Character ID | Local File in `FINAL/` | Canonical Name | Local Outfits | Live Outfits | API Status |
|---|-------------------|------------------------|----------------|---------------|--------------|------------|
| 1 | `_QPea6g4Q1QfeYCVHCLMPR` | `Erik_Douglas_card.json` | Erik Ulfr Douglas | 10 | 10 | HTTP 200 OK |
| 2 | `_RDfz7XzTpM23LpPALVXHM` | `Malachia_Douglas_Bloodmoon_card.json` | Malachia Björn Douglas Bloodmoon | 11 | 11 | HTTP 200 OK |
| 3 | `_t4J9aQNJM36cUKAP4wB4U` | `Jasper_Douglas_Bloodmoon_card.json` | Jasper Svartr Douglas Bloodmoon | 11 | 11 | HTTP 200 OK |
| 4 | `_zFLUjV8aVxQRAfQxGcAcY` | `Noah_Douglas_Bloodmoon_card.json` | Noah Loki Douglas Bloodmoon | 9 | 9 | HTTP 200 OK |
| 5 | `_TbRM3EdxDjHFgqztTbCpL` | `Edric_Douglas_card.json` | Edric Douglas | 9 | 9 | HTTP 200 OK |
| 6 | `_T8Ywcr9FEqNf9JxbK6eHP` | `Logan_Douglas_card.json` | Logan Járn Douglas | 10 | 10 | HTTP 200 OK |
| 7 | `_HEQQbbRFwKdG8QE2Fh1z1` | `Wulfnic_Bloodmoon_card.json` | Wulfnic Báleygr Bloodmoon | 12 | 12 | HTTP 200 OK |
| 8 | `_zn24784jfcchQ7EwCyAnm` | `Mackenzie_Sanchez_Rogers_card.json` | Mackenzie Sanchez-Rogers | 11 | 11 | HTTP 200 OK |

**Result**: 100% parity verified between local files and live API. All 8 cards have valid JED+ descriptions, verified family and pack lore, and meet the >=9 outfit requirement.

---

## 3. Inspection of `FINAL/` Character Files & Identification of 6 Disused Cards

### 3.1 Inventory of `FINAL/` Character Cards
There are currently exactly **14 card files** in `FINAL/`:

```
14 Total Card Files in FINAL/
├── 8 Approved (To Keep):
│   ├── Edric_Douglas_card.json
│   ├── Erik_Douglas_card.json
│   ├── Jasper_Douglas_Bloodmoon_card.json
│   ├── Logan_Douglas_card.json
│   ├── Mackenzie_Sanchez_Rogers_card.json
│   ├── Malachia_Douglas_Bloodmoon_card.json
│   ├── Noah_Douglas_Bloodmoon_card.json
│   └── Wulfnic_Bloodmoon_card.json
└── 6 Disused (To Move to ARCHIVIO/cards_legacy/):
    ├── Alyssa_Douglas_Bloodmoon_card.json
    ├── Jared_Thompson_card.json
    ├── Russ_card.json
    ├── Scarlett_Rose_card.json
    ├── Sierra_Cruz_card.json
    └── Stan_Davies_Jr_card.json
```

### 3.2 Detailed Profile of the 6 Disused Cards

| Card File in `FINAL/` | Target Character ID | Character Name | Desc Length | Avatar URL | Outfits | Target NPC Record in `Svartulfr_NPC_Primary.json` |
|-----------------------|---------------------|----------------|-------------|------------|---------|---------------------------------------------------|
| `Alyssa_Douglas_Bloodmoon_card.json` | `_6exg3yPfe2eCDK4hTftkh` | Alyssa Hvit Douglas Bloodmoon | 16,957 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public` | 19 | `alyssa_world_dossier_2b54a223` (`type: "lore/concept"`, `selective: true`, secondary keys: `['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`) |
| `Jared_Thompson_card.json` | `_xJVPtBLL3dxy69RLKL9X9` | Jared Thompson | 8,696 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7476db0-8dae-4450-8c84-3408b375c000/public` | 11 | `RM6rcwv8MlY1XWaCTQp0M` (`type: "npc"`, `selective: false`, regex: `(?:^\|\n)\s*(?:Jared Thompson\|Jared\|J-Man)\s*:`) |
| `Russ_card.json` | `_wn6DkCcg3Xqa2Xpx9ttnT` | Russell 'Russ' Sinclair | 5,505 chars | `https://ella.janitorai.com/bot-avatars/9yrobVTbiGDRLHlS6GtIz.webp` | 9 | `YCxAqNoShpefVvk0_Pc7i` (`type: "npc"`, `selective: false`, regex: `(?:^\|\n)\s*(?:Russell Sinclair\|Russell 'Russ' Sinclair\|Russell 'Russ'\|Russ)\s*:`) |
| `Scarlett_Rose_card.json` | `_qXgBMbFYJfc84hbLHhe92` | Scarlett Rose | 4,777 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public` | 9 | `4NzXF4_0hYxmN7Idltzpw` (`type: "npc"`, `selective: false`, regex: `(?:^\|\n)\s*(?:Scarlett Rose\|Scarlett)\s*:`) |
| `Sierra_Cruz_card.json` | `_pnrXbkWqcgmFAf3meRWFY` | Sierra Cruz | 5,117 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public` | 9 | `ijy8vrlphNv19-p-gbYuY` (`type: "npc"`, `selective: false`, regex: `(?:^\|\n)\s*(?:Sierra Cruz\|Sierra)\s*:`) |
| `Stan_Davies_Jr_card.json` | `_Xd3NhKnRJByMTtdb6PjxJ` | Stanley Davies Jr. | 8,008 chars | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7c9c7d1-51e6-4441-82e3-c6ab5f537500/public` | 9 | `ekdQjq63xP7HtNuaPQJQE` (`type: "npc"`, `selective: false`, regex: `(?:^\|\n)\s*(?:Stanley Davies Jr\.\|Stanley Davies\|Stan Davies\|Stan)\s*:`) |

**Key Observation**: All 6 card files contain complete, rich JED+ descriptions (>4,700 chars, up to 16,957 chars for Alyssa), valid avatar image URLs, and 9 to 19 outfits. They provide the authoritative text source needed to restore the 6 NPC records in `FINAL/Svartulfr_NPC_Primary.json` (Requirement R4).

---

## 4. Status of `ARCHIVIO/cards_legacy/`

- **Directory Existence**: `ARCHIVIO/cards_legacy/` **does not exist** currently.
- **Current `ARCHIVIO/` Structure**:
  - `ARCHIVIO/01_Drafts/`
  - `ARCHIVIO/02_Drive_and_Raw_Sources/`
  - `ARCHIVIO/03_Claude_Docs_and_Memories/`
  - `ARCHIVIO/04_Wyvern_Local_Legacy/`
  - `ARCHIVIO/05_Snapshots_and_Extractions/`
  - `ARCHIVIO/06_Archived_Standalone_Cards/` (contains older archived cards: Elizabeth, Magnus, Kaladin, Marek, Neon Purr, Russ v1, Zeera)
  - `ARCHIVIO/07_Purged_Disabled_Entries/`
  - `ARCHIVIO/janitor_sources/`
- **Worker Action Required**:
  The Worker must execute `os.makedirs('ARCHIVIO/cards_legacy', exist_ok=True)` (or powershell `New-Item -ItemType Directory -Path ARCHIVIO/cards_legacy -Force`) and then move the 6 disused card files from `FINAL/` into `ARCHIVIO/cards_legacy/`.

---

## 5. Cross-Dependency and Impact Analysis

### 5.1 Scenario Slots Dependency (R2 Interlock)
Live inspection of the two active SUCC scenarios on Wyvern (`char_scenario_CKgwq246DyCj1NNTBV9rt` and `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`) revealed:
1. `quarterback` slot currently references `_xJVPtBLL3dxy69RLKL9X9` (Jared Thompson). Because Jared is still active on `/characters/mine`, Wyvern reports `unavailable_count: 0`.
2. As soon as Jared Thompson is deleted from `/characters/mine`, Wyvern's scenario engine will flag the slot as `unavailable_count: 1` if the pool still references `_xJVPtBLL3dxy69RLKL9X9`.
3. Furthermore, slots for Scarlett (`_qXgBMbFYJfc84hbLHhe92`), Sierra (`_pnrXbkWqcgmFAf3meRWFY`), Stan (`_Xd3NhKnRJByMTtdb6PjxJ`), and Russ (`_wn6DkCcg3Xqa2Xpx9ttnT`) are currently flagged with `unavailable_count: 1` on live Wyvern because their standalone cards are not accessible in the user's active `/characters/mine`.
4. **Resolution Strategy**:
   - For all converted characters (Scarlett, Sierra, Russ, Jared, Stan), the scenario slots must have their pools emptied (`pool: []`) or reset with `unavailable_count: 0`.
   - In scenario greeting texts, any occurrence of macro `{{scenarioChar "quarterback"}}`, `{{scenarioChar "best_friend"}}`, `{{scenarioChar "roommate"}}`, `{{scenarioChar "male_roommate"}}`, `{{scenarioChar "crush"}}` (referring to Scarlett), or `{{scenarioChar "friend"}}` must be replaced with their literal names ("Jared", "Scarlett", "Sierra", "Russ", "Stan").
   - This cleanly decouples the scenarios from the deleted standalone cards, eliminating all `unavailable_count: 1` warnings and preventing macro expansion failures.

### 5.2 NPC Primary Lorebook Interlock (R4 Interlock)
Inspection of `FINAL/Svartulfr_NPC_Primary.json` showed that the 6 records currently have short synthetic dossiers (760–1,385 chars) without NPC avatar regex fields.
- The 6 card files in `FINAL/` (`Alyssa_Douglas_Bloodmoon_card.json`, `Jared_Thompson_card.json`, `Russ_card.json`, `Scarlett_Rose_card.json`, `Sierra_Cruz_card.json`, `Stan_Davies_Jr_card.json`) contain the exact JED+ texts and avatar URLs to restore into `FINAL/Svartulfr_NPC_Primary.json`.
- **Execution Order Recommendation for Worker**:
  1. Read full JED+ texts and avatars from the 6 card files in `FINAL/`.
  2. Populate the 6 records in `FINAL/Svartulfr_NPC_Primary.json` and deploy Lorebook `_zwEqgEEzh12X6gHVmMKKC` via `PUT`.
  3. Delete Jared Thompson from Wyvern API (`DELETE /api/characters/_xJVPtBLL3dxy69RLKL9X9`).
  4. Move the 6 card files to `ARCHIVIO/cards_legacy/`.
  5. Update SUCC scenarios (R2) and deploy via `PUT`.

### 5.3 Persona Anti-Duplicate Invariant (Alyssa & Jasper)
- Alyssa Hvit Douglas Bloodmoon (`alyssa_world_dossier_2b54a223`) must retain `selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `key_logic: 'AND_ANY'` and `type: "lore/concept"` (identical to Jasper `Vcj4h2TL4Usola2A4OOl6`).
- This guarantees that when the user plays as Persona Alyssa, her lorebook entry will NOT inject spuriously during casual conversation.

### 5.4 Repository Tracking & Documentation
- `README.md` (section 3 "Le 14 Character Card Canoniche") will need to be updated to list the 8 approved cards in `FINAL/` and reference the 6 legacy cards in `ARCHIVIO/cards_legacy/`.
- `CHANGELOG.md` will record the R3 reduction to 8 cards, Jared's deletion, and the legacy archiving.

---

## 6. Actionable Implementation Checklist for Worker

1. [ ] **Snapshot Jared**: Save `scratch/backup_deleted_cards_20261021/DELETED_Jared_Thompson__xJVPtBLL3dxy69RLKL9X9.json`.
2. [ ] **API DELETE Jared**: Send `DELETE https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9`.
3. [ ] **Verify Live `/characters/mine`**: GET `/api/characters/mine` -> Confirm exactly 8 characters remain.
4. [ ] **Create Directory**: `mkdir -p ARCHIVIO/cards_legacy`.
5. [ ] **Move 6 Files**: Move `Alyssa_Douglas_Bloodmoon_card.json`, `Jared_Thompson_card.json`, `Russ_card.json`, `Scarlett_Rose_card.json`, `Sierra_Cruz_card.json`, `Stan_Davies_Jr_card.json` from `FINAL/` to `ARCHIVIO/cards_legacy/`.
6. [ ] **Verify `FINAL/`**: Confirm exactly 8 `*_card.json` files remain in `FINAL/`.
