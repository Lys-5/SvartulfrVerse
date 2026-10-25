# Technical Analysis: Avatar Survey, Metadata & Wyvern API Deployment Mechanics (R3 & R5)

**Investigator**: Explorer R7-3 (Avatar & Deployment API Investigator)  
**Date**: 2026-10-21  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r7_3`  
**Target Files**: `FINAL/Svartulfr_NPC_Primary.json`, `FINAL/Svartulfr_NPC_Secondary.json`, `lorebooks/optimized/`  
**Target Wyvern Entities**: Lorebook Primary (`_zwEqgEEzh12X6gHVmMKKC`), Lorebook Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)

---

## Executive Summary

This investigation analyzed all 310 NPC entries across `Svartulfr_NPC_Primary.json` (99 entries) and `Svartulfr_NPC_Secondary.json` (211 entries), top-level lorebook metadata, live Wyvern Web API connectivity, and deployment payload mechanics.

### Key Metrics At a Glance

| Metric | Primary (`_zwEqgEEzh12X6gHVmMKKC`) | Secondary (`_Uht3Ckz44JBDrPnUHq7LV`) | Total Combined |
| :--- | :--- | :--- | :--- |
| **Total Entries** | 99 | 211 | **310** |
| **Custom Character Portraits** | 57 (57.6%) | 53 (25.1%) | **110 (35.5%)** |
| **Current Placeholder/Fallback** (`6f8b7c78...`) | 42 (42.4%) | 158 (74.9%) | **200 (64.5%)** |
| **Empty / Null Avatars (Local)** | 0 | 0 | **0 (0.0%)** |
| **Empty Avatars (Live Wyvern)** | 1 (Logan Járn Douglas) | 0 | **1 (Live anomaly)** |
| **Target DCC Placeholder Entries** | 42 to update | 158 to update | **200 to update** |
| **Projected Valid HTTPS Avatars** | 99 (100%) | 211 (100%) | **310 (100%)** |
| **Current `token_budget`** | 5,000 | 5,000 | — |
| **Target `token_budget`** | **7,500** | **5,000** | — |
| **Current Live `photoURL`** | `ef47523e-b173-4fdf-7cb6...` | `1a251dac-8d4a-4091-3eda...` | Legacy covers |
| **Target Lorebook Cover `photoURL`** | House Svartúlfr Emblem (`1e5124b4...`) | House Svartúlfr Emblem (`1e5124b4...`) | Unified Emblem |
| **Live API GET Status** | HTTP 200 OK | HTTP 200 OK | Authenticated |

---

## 1. Avatar Portraits & Distribution Survey (310 Entries)

### 1.1 Mathematical Distribution of Avatars

Across all 310 entries, exactly 109 unique avatar URLs are in use:
- **1 URL appears 200 times**: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public`. This is the older fallback image (DCC wolf silhouette with glowing eyes).
- **2 URLs appear 2 times**:
  - `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public`: Shared between Scarlett Rose and Sierra Cruz in Primary (SUCC sorority duo card).
  - `https://io-modernfantasy.uwu.ai/assets/images/gallery03/650ea6f4.jpg?v=2881d07e`: Shared between Jayce Collins and Rhett Moore in Secondary.
- **106 URLs appear 1 time each**: Individual character portraits from official cards, JanitorAI bot avatars, and modernfantasy character assets.

Total custom portrait entries: `106 + (2 * 2) = 110 entries`.  
Total placeholder entries: `200 entries`.  
Total: `110 + 200 = 310 entries`.

### 1.2 Breakdown by Lorebook

#### Svartúlfr - NPC Primary (`FINAL/Svartulfr_NPC_Primary.json` - 99 entries)
- **Custom Portraits (57 entries)**:
  - 48 Cloudflare CDN URLs (`imagedelivery.net`), including canonical Douglas family cards:
    - Erik Ulfr Douglas: `30fe0390-05fb-46cf-2c8a-cd98fc35c700`
    - Malachia Björn Douglas Bloodmoon: `c883ae1e-d817-4f80-e4bb-388aaea84d00`
    - Noah Loki Douglas Bloodmoon: `12f497d7-7147-4d38-c2de-c57892180800`
    - Logan Járn Douglas: `5d7d3ade-f742-41da-979b-670102fead00`
    - Wulfnic Báleygr Bloodmoon: `554744b5-0e23-45b9-005a-4629abd35500`
    - Mackenzie Sanchez-Rogers: `87f28fb6-557f-4eaf-9c7c-0cddfbe5c300`
    - Alyssa Hvit Douglas Bloodmoon: `oppv5DrhxEK7cSH1vUV6p.webp`
    - Jasper Svartr Douglas Bloodmoon: `48de55c8-7e23-4d5e-be33-d25611810a00`
  - 6 JanitorAI CDN URLs (`ella.janitorai.com`)
  - 3 Universe hub URLs (`io-modernfantasy.uwu.ai`)
- **Fallback Entries (42 entries)**:
  - Currently use `6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100`.
  - Includes secondary campus students, minor underworld contacts, and support personnel:
    - Sample names: Hugh Rivers, Liam O'Connor, Bessie May, Neve, Jaelyn, Kian, Goran, Radek, Roman Blackwood, Eric, Dean, Javier Reyes, Raymond, Sully Jones, Vasile Ionescu.
  - Target: All 42 entries must be updated to the official DCC placeholder: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`.

#### Svartúlfr - NPC Secondary (`FINAL/Svartulfr_NPC_Secondary.json` - 211 entries)
- **Custom Portraits (53 entries)**:
  - Edric Douglas (core card): `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/13c49c40-2378-4678-ca5d-6e2ef84eba00/public`
  - 27 Universe hub URLs (`io-modernfantasy.uwu.ai`)
  - 20 JanitorAI CDN URLs (`ella.janitorai.com`)
  - 5 Cloudflare CDN URLs (`imagedelivery.net`)
  - 1 SUCC portal URL (`io-succ.uwu.ai`)
- **Fallback Entries (158 entries)**:
  - Currently use `6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100`.
  - Encompasses 100 Camp Mystic campers/counselors lacking personal art (e.g. Jet Thompson, Allegra Lumsden, Luisa Sanchez Rogers, Eira Elloway, Vespera Thorne, Evan, Bramble Mossmere, Silas, Ailsa Hourie, Adelin Coso) + 58 regional background figures.
  - Target: All 158 entries must be updated to the official DCC placeholder: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`.

### 1.3 Live Wyvern Avatar Anomaly Detected

During live GET inspection of `_zwEqgEEzh12X6gHVmMKKC`:
- **Logan Járn Douglas (`tAcrWLtWSDGf3xJJRwUOM`, index 57)** currently has an empty string avatar (`avatar: ""`) on the live Wyvern cloud.
- In `FINAL/Svartulfr_NPC_Primary.json`, Logan already has his valid card avatar:
  `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5d7d3ade-f742-41da-979b-670102fead00/public`.
- **Root Cause**: An earlier live update omitted or cleared Logan's avatar field.
- **Remediation**: The deployment of `FINAL/Svartulfr_NPC_Primary.json` to Wyvern will automatically resolve this live defect.

### 1.4 Verification of Official Placeholder URLs

| Resource | Target URL | HTTP Status | Content-Type | Size |
| :--- | :--- | :--- | :--- | :--- |
| **Official DCC Avatar Placeholder** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public` | **200 OK** | `image/jpeg` | 50,486 bytes |
| **Official House Svartúlfr Emblem (Cover)** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public` | **200 OK** | `image/jpeg` | 125,978 bytes |
| **Legacy Fallback Avatar (6f8b7c78)** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public` | **200 OK** | `image/jpeg` | 49,814 bytes |
| **Legacy Crest Avatar (98e2d06d)** | `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public` | **200 OK** | `image/jpeg` | 136,498 bytes |

Both official assets (`99d10d9b...` for DCC placeholder and `1e5124b4...` for House Emblem) are live, publicly accessible, and correctly served with `image/jpeg` headers.

---

## 2. Lorebook Covers and Top-Level Metadata

### 2.1 Cover PhotoURL Audit

1. **Lorebook Primary (`_zwEqgEEzh12X6gHVmMKKC`)**:
   - Live Wyvern: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ef47523e-b173-4fdf-7cb6-bfdeee19e400/public`
   - Local `FINAL/Svartulfr_NPC_Primary.json`: Missing top-level `photoURL` key (defaults to None).
   - Target: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public`.

2. **Lorebook Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)**:
   - Live Wyvern: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1a251dac-8d4a-4091-3eda-e888aedbf500/public`
   - Local `FINAL/Svartulfr_NPC_Secondary.json`: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1a251dac-8d4a-4091-3eda-e888aedbf500/public`.
   - Target: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public`.

Both lorebooks must have their `photoURL` updated to the official House Svartúlfr emblem.

### 2.2 Token Budget Audit

- **Lorebook Primary (`_zwEqgEEzh12X6gHVmMKKC`)**:
  - Current value (live and local): `5000`
  - Target value: `7500`
  - **Rationale**: Primary contains extensive JED+ character profiles with complete backstories, intimacy profiles, vehicle specs, and RPG stats for the 6 core family cards (Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie) as well as Alyssa, Jasper, Scarlett, Sierra, Russ, Stan, and Jared. A budget of 7,500 tokens is required so multiple active characters can be injected into the context window without premature truncation.
- **Lorebook Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)**:
  - Current value (live and local): `5000`
  - Target value: `5000`
  - **Rationale**: Secondary contains Edric Douglas (7.2k chars) plus 210 secondary/tertiary/camper NPCs. The 5,000 token ceiling provides optimal context density for peripheral characters.

### 2.3 Top-Level Metadata Parity Matrix

| Field | Primary Target | Secondary Target | Notes |
| :--- | :--- | :--- | :--- |
| `name` | `Svartúlfr - NPC Primary` | `Svartúlfr - NPC Secondary` | Preserve unicode 'ú' |
| `description` | `Primary recurring NPC profiles...` | `Secondary and tertiary supernatural NPCs...` | Standard descriptions |
| `photoURL` | `.../1e5124b4.../public` | `.../1e5124b4.../public` | Official House Emblem |
| `token_budget` | `7500` | `5000` | Scaled for JED+ dossiers |
| `scan_depth` | `5` | `5` | Standard depth |
| `recursive_scanning` | `true` | `true` | Enabled |
| `visibility` | `"private"` | `"private"` | Enforce private visibility |
| `rating` | `"explicit"` | `"explicit"` | Enforce explicit rating |

---

## 3. Wyvern API Connectivity and Deployment Mechanics

### 3.1 Authentication & Token Health

- **Bearer Token**: Verified in `scratch/wyvern_token.txt`. Current token length is 1,142 bytes.
- **Connectivity Test**: Authenticated GET calls to `https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` and `_Uht3Ckz44JBDrPnUHq7LV` succeeded with **HTTP 200 OK**.
- **Refresh Fallback**: Verified `scratch/refresh_token.py` connects to Firebase Auth (`https://securetoken.googleapis.com/v1/token`) using the refresh token stored in `scratch/refresh_token.txt` and updates `scratch/wyvern_token.txt` dynamically if an HTTP 401 or 403 occurs.

### 3.2 Deployment Payload Invariant: Compact Payload vs Duplicate `entries`

When deploying to `PUT /api/lorebooks/:id`:
1. **The `lexicon` Array**: Wyvern's backend stores and returns lorebook entries under the `lexicon` property. In the live API GET response, `len(data['lexicon']) == 99` (Primary) and `211` (Secondary), while `entries` is empty or omitted.
2. **Exclusion of Duplicate `entries` Array**: In the local JSON files, both `entries` and `lexicon` exist for backward compatibility with certain local tools. However, when assembling the PUT HTTP payload:
   - **DO NOT** send `entries` in the JSON body.
   - Send only top-level metadata + `lexicon`.
   - **Impact**: Including both arrays doubles payload size from ~1.3 MB to ~2.6 MB (Primary) and ~2.1 MB to ~4.2 MB (Secondary), which increases the likelihood of HTTP 413 (Payload Too Large), network timeouts, or partial parsing failures.
3. **Pacing Delay**: Enforce a mandatory `time.sleep(2.5)` delay between the PUT request for Primary and Secondary to respect API rate limits.
4. **Serialization Settings**: `json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')`.

### 3.3 Target Mirror Directory: `lorebooks/optimized/`

- The repository maintains a synchronized mirror of all finalized lorebooks in `lorebooks/optimized/`.
- File inspection confirmed that `lorebooks/optimized/Svartulfr_NPC_Primary.json` and `lorebooks/optimized/Svartulfr_NPC_Secondary.json` currently match `FINAL/` byte-for-byte.
- **Deployment Requirement**: When `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json` are modified (updating placeholders, covers, budgets, and core cards), both local files and their counterparts in `lorebooks/optimized/` must be written simultaneously before or alongside live Wyvern API deployment.

---

## 4. Remediation Checklist for Implementers

1. **Avatar Placeholder Update (200 entries)**:
   - In `Svartulfr_NPC_Primary.json`: Replace `6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100` with `99d10d9b-611c-45b7-566a-79c3ed2e9800` across all 42 entries (in both `entries` and `lexicon`).
   - In `Svartulfr_NPC_Secondary.json`: Replace `6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100` with `99d10d9b-611c-45b7-566a-79c3ed2e9800` across all 158 entries (in both `entries` and `lexicon`).
2. **Lorebook Cover Emblem Update**:
   - Primary: Set `photoURL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"`.
   - Secondary: Set `photoURL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"`.
3. **Token Budget Adjustment**:
   - Primary: Set `token_budget = 7500`.
   - Secondary: Confirm `token_budget = 5000`.
4. **Mirror Synchronization**:
   - Overwrite `lorebooks/optimized/Svartulfr_NPC_Primary.json` and `lorebooks/optimized/Svartulfr_NPC_Secondary.json` with the updated JSON.
5. **Live API Deployment (Compact PUT)**:
   - Send PUT payload with `name`, `description`, `photoURL`, `token_budget`, `scan_depth`, `recursive_scanning`, `visibility`, `rating`, and `lexicon`.
   - Primary: `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC`.
   - Wait 2.5 seconds.
   - Secondary: `PUT /api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV`.
6. **Live Post-Deploy Verification**:
   - Execute GET on both endpoints, asserting status 200, entry counts (99, 211), `photoURL`, and zero empty avatars.
