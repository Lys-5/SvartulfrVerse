# Handoff Report: Svartúlfr World 188 Locations & 7 Environments Topology

**Author**: Explorer Subagent (M1 Locations Topology)  
**Recipient**: Project Orchestrator (`23c2db8d-c021-4817-8a28-93080f41c7e4`)  
**Date**: 2026-10-24T22:30:00Z  
**Target File**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_locations\handoff.md`  

---

## 1. Observation

### 1.1 Source Files & Entry Counts Inspected
Direct inspection was performed on all repository location files and historical snapshots:

1. **`exports/Svartulfr_Export.json`**:
   - `world_locations`: **Exactly 188 locations** (`len(exp['world_locations']) == 188`).
   - `world_environments`: 2 legacy environments (`Voidspace` and `California Coast`).
2. **`FINAL/Svartulfr_Location.json` (`_EjXxkmPVhpCXg8xABpFkK`)**:
   - Standalone Lorebook format.
   - `entries`: 225 entries; `lexicon`: 225 entries (`entries == lexicon` parity confirmed).
   - Breakdown: **188 canonical world locations** + **37 Camp Mystic granular cabin/facility entries** = 225 entries total.
   - Mirrored byte-for-byte in `lorebooks/optimized/Svartulfr_Location.json`.
3. **`scratch/backup_consolidated_snapshot/world_locations.json`**:
   - Contains 196 total location records from earlier database dumps.
   - 8 entries are decommissioned botanical sub-locations under the older `Digitalis` cluster:
     - `_p6WUaYcTJURrTXejecchk` — Seedpod
     - `_RNU9Fx2pLD6PJ8LcKAdg6` — The Hothouse
     - `_J1B6d2DnNNyJhpnKWNcXz` — Nectary
     - `_94hRP4ywVYTHaUDDGfLqg` — The Ovary
     - `_qe962a69a6PBbaHWCbP8r` — Digitalis
     - `_BEnFGJPqBFJnTtrAHQQ9F` — Narcissus
     - `_VMwRTPXdGTARktqnDLRTA` — Taproot
     - `_2rTUXXxAyYh8WYnGNtV2M` — Graft
   - Excluding these 8 decommissioned records leaves **exactly 188 active canonical locations** (matching `CHANGELOG.md` lines 282, 353, 1072, 1114, 1309).

### 1.2 Hierarchy & Orphan Node Audit
Audited all 188 active canonical locations for parent-child pointer integrity:
- **Root Locations (`parent_location: None`)**: Exactly 8 roots:
  1. `Bakersfield` (`_fekTA9NRygQ49q7cxRz8A`) — 7 direct children
  2. `Blackwood City` (`_D8B9QAfHPn3NfD4mAnJen`) — 11 direct children
  3. `Camp Mystic` (`_yPxa34RwGz9wbjm1zjhLJ`) — 0 children (macro root in World)
  4. `DDM Inc. // Voidspace` (`_BUfxJEGc4Td36H8kMmVD3`) — 2 direct children
  5. `Hex Valley` (`_k118p3PTLgG88pkXn48BQ`) — 3 direct children
  6. `Los Angeles` (`_X4A8gWVr43a7dRr9TbJ4m`) — 10 direct children
  7. `Solarton` (`_761mFFeCcQyR9JxhLCWcy`) — 14 direct children
  8. `Zone di Transito e Confine` (`_zjA9MJEAVjjFn64jjtcb6`) — 5 direct children
- **Nested Nodes (`parent_location` populated)**: Exactly 180 locations.
- **Orphan Nodes**: **0 (Zero)**. Every single child resolves to a valid, existing ancestor node.
- **Maximum Depth**: 4 levels (e.g., `Blackwood City` -> `Blackwood Forest` -> `Bloodmoon Pack Territory` -> `Bloodmoon Longhouse` -> `Bloodmoon Longhouse Baths`).

### 1.3 'The Verve' and 'Logan's Custom Garage' Configuration
Direct inspection of `_hfm1W4nYnXfQEqcNGwNxr` ("The Verve"):
- **ID**: `_hfm1W4nYnXfQEqcNGwNxr`
- **Parent Location**: `_MkkwDR7AHq4tYLmnk134f` ("Bluemoon", District of Blackwood City).
- **Physical Address**: 808 Neon Avenue, Bluemoon District, Blackwood City.
- **Architectural Mechanics & Entrance**:
  - The location entity `The Verve` embodies both **Logan's Custom Garage** (daytime operation) and the **Secret Bar / Speakeasy Nightclub** (nighttime operation).
  - *Daytime*: Working-class auto repair garage bay equipped with a heavy two-post hydraulic vehicle lift, red toolboxes, motorcycle bay, "Gasoline Filling Station" neon sign, and a long wooden taproom serving blue-collar regulars.
  - *Nighttime Transition & Entrance*: An automated hydraulic lift system hoists the entire workshop bay (vehicles, benches, tools) into the upper mezzanine ceiling. In its place, a sunken stage, dance floor, DJ booth, and exclusive subterranean nightclub drop into position.
  - *Logan's Loft*: Positioned above the mezzanine, accessible via a private steel service stairwell, serving as the home loft for Logan and Edric Douglas.
  - *Under-the-Counter Speakeasy*: While functioning as a nightclub, the back bar distributes off-the-books DCC Black Market contraband (unregistered donor blood, harvested organs, black-market amulets).
  - *Counter-Surveillance*: Enclosed within Logan's personal DCC jamming ward (scrambles drones, RFID biometrics, and Kaladin network surveillance).
- **Keys**: `['The Verve', 'garage', 'nightclub', 'neutral territory', 'Logan Douglas', 'no surveillance']`
- **Included Lexicon Entries**:
  - `_YxGJRFDkjdVyeH1mJNM1T` (Lighter — Logan's Custom Brass Zippo)
  - `_UVX1RAqE8CWz8ywYkT4Fm` (Wireless Earbuds)
  - `_BRjbkk8JM3Jw1xyJGgzDH` (Keys — Logan's Master Keychain)

### 1.4 Wyvern World Location Object Schema
Inspection of active location records confirms the standard JSON schema:
- `name`: `string`
- `description`: 3-part structured JED+ bracketed metadata block:
  - `[LOCATION INFO: Era: 2024 ...; Location: ...; Setting: ...; Factions: ...; Conflicts: ...; Society: ...]`
  - `[LORE & ENVIRONMENT: Environment: ...; Architecture: ...; Security & Wards: ...; Demographics: ...; Rules & Restrictions: ...]`
  - `[CONTEXT & SECRETS: History: ...; Secrets: ...]`
- `context_description`: Narrative atmospheric prose describing lighting, smells, day/night shifts, physical layout, and concluding with `[LOCATION INSTRUCTIONS: ...]`. Populated on 164 of 188 locations.
- `brief_context_description`: Optional 1-line summary string.
- `environment_config`: Object `{ "background": "", "ambient_sound": "", "music": "", "particles": "" }`.
- `included_lexicon_entries`: Array of Lexicon ID strings (e.g., `["_YxGJRFDkjdVyeH1mJNM1T", ...]`). Populated on 11 specialized hub locations.
- `excluded_lexicon_entries`: Array of Lexicon ID strings to suppress.
- `parent_location`: Object `{ id, _id, name, ... }` or ID string referencing parent location.
- `environment`: Object `{ id, _id, name, ... }` or ID string referencing environment.
- `keys`: Array of trigger strings (populated on 176 locations).
- `secondary_keys`: Array of secondary filter strings.
- `key_logic`: `"AND_ANY"`.
- `whole_words_only`: `true`.
- `case_sensitive`: `false`.
- `key_position`: `"after_char"`.

---

## 2. Logic Chain

1. **Reconciliation of Discrepant Entry Counts**:
   - *Observation*: Three differing counts exist across sources: 196 in raw snapshot, 225 in Lorebook, and 188 in World export.
   - *Reasoning*:
     - In `scratch/backup_consolidated_snapshot/world_locations.json`, 8 entries are tagged to the deprecated "Digitalis" sub-rooms. Removing those 8 inactive entries leaves $196 - 8 = 188$ canonical locations.
     - In `FINAL/Svartulfr_Location.json`, 37 granular locations (cabins B-01/B-08, G-01/G-08, clinic, docks, boathouse, etc.) were created specifically for the Camp Mystic Character Scenario. Adding 37 to the 188 core world locations equals $188 + 37 = 225$.
     - In `exports/Svartulfr_Export.json`, Camp Mystic exists strictly as 1 macro location entry (`_yPxa34RwGz9wbjm1zjhLJ`). The total count of `world_locations` is exactly 188.
   - *Conclusion*: The canonical World topology consists of **exactly 188 locations**.

2. **Hierarchical Topology & Orphan Verification**:
   - *Observation*: Building the adjacency graph of `parent_location` pointers across all 188 locations yields 8 root nodes and 180 child nodes.
   - *Reasoning*: Every child node has a valid parent pointing either to a root or to another valid child that terminates at a root.
   - *Conclusion*: Zero orphan nodes exist. The topology is fully connected.

3. **Distribution Across 7 Canonical Environments**:
   - *Observation*: Tracing every node up to its root and evaluating geographic/thematic boundaries defined in Orchestrator 9 dispatch:
     - Root nodes `Los Angeles`, `Bakersfield`, `Hex Valley`, `Camp Mystic`, and transit routes (`Ventura / Route 101`) map to **1. California Coast**.
     - `Supernatural University of Central California` and all 62 sub-locations (Greek Row, Basilica Library, Bulls Stadium, Wyrm Dorms, Labs, etc.) form **2. SUCC campus**.
     - `Solarton` urban district, Bricklane Mall, Solarton Square, and coastal residential spots form **3. Solarton**.
     - `Blackwood City` urban districts (Uptown, Arcadia, Bluemoon, Oldtown, Dockside, Ironworks, Cable District, Paradise) and Blackwood Forest form **4. Blackwood**.
     - The Douglas Pack stronghold (`Seven Hills`, `Villa Douglas`, and all 14 internal rooms/wings) forms **5. Seven Hills**.
     - `Simi Valley`, `Simi Valley Infopoint`, `The Simi Valley Grid`, and `Team Ukiyo Operational Base` form **6. DMHA HQ & Guild District**.
     - Extra-planar/dimensional fractures (`DDM Inc. // Voidspace`, `Dead Dog Motel / Voidspace`, `The Otherworld` under Blackwood Forest, and `Trial Dungeon: Hive Apex Rift Floors 1-18`) form **7. Voidspace/Otherworld**.
   - *Conclusion*: The 188 locations partition cleanly across the 7 environments:
     - 1. California Coast: **34 locations**
     - 2. SUCC campus: **63 locations**
     - 3. Solarton: **27 locations**
     - 4. Blackwood: **33 locations**
     - 5. Seven Hills: **16 locations**
     - 6. DMHA HQ & Guild District: **4 locations**
     - 7. Voidspace/Otherworld: **11 locations**
     - **Total: $34 + 63 + 27 + 33 + 16 + 4 + 11 = 188 locations**.

---

## 3. Caveats

1. **Camp Mystic Scope Difference**:
   - In the World topology, `Camp Mystic` is represented as a single macro hub (`_yPxa34RwGz9wbjm1zjhLJ`). The 37 granular sub-locations (cabins G-01 through G-08, B-01 through B-08, Boathouse, Amphitheater) exist in the standalone Lorebook `_EjXxkmPVhpCXg8xABpFkK` and the Camp Mystic Character Scenario, but are intentionally not separate World Location records to avoid exceeding the World context budget.
2. **Decommissioned Botanical Cluster ("Digitalis")**:
   - The 8 locations (`Digitalis`, `Taproot`, `Graft`, `Narcissus`, `Seedpod`, `The Hothouse`, `Nectary`, `The Ovary`) are preserved in legacy dumps (`scratch/`) but are explicitly deactivated in the active World to prevent lore conflicts with DDM Voidspace canon.
3. **Legacy Environment Fields**:
   - In older snapshot files, only 2 environment records existed (`Voidspace` and `California Coast`). When implementing R3, the 7 canonical Environments must be instantiated, and each location's `environment` foreign key updated to its respective environment ID.

---

## 4. Conclusion & Complete Topology Tree

The Svartúlfr World topology is completely verified, structured, and free of defects.

### 4.1 Environment Distribution Summary

| Environment # | Canonical Environment Name | Parent / Domain | Location Count | Key Anchor Locations |
|:---:|---|---|:---:|---|
| **1** | **California Coast** | Root / Regional | **34** | Los Angeles, Bakersfield, Hex Valley, CUMS, Ventura / Route 101, Camp Mystic |
| **2** | **SUCC campus** | California Coast | **63** | 129 Hocus Way, Basilica Library, Bulls Stadium, Greek Row (10 houses), Wyrm Dorms |
| **3** | **Solarton** | California Coast | **27** | Solarton Square, Bricklane Mall (9 shops), Sidewinders Bar, Dullahan's Condo |
| **4** | **Blackwood** | California Coast | **33** | Blackwood City, Bluemoon, The Verve, Dockside, Ironworks, Oldtown, Arcadia |
| **5** | **Seven Hills** | Blackwood | **16** | Seven Hills district, Villa Douglas (14 sanctuary wings & rooms) |
| **6** | **DMHA HQ & Guild District** | California Coast / Simi Valley | **4** | Simi Valley, Infopoint, The Grid, Team Ukiyo Operational Base |
| **7** | **Voidspace/Otherworld** | Extra-Planar Rift Expanse | **11** | DDM Inc. HQ, Dead Dog Motel, The Otherworld, Trial Dungeon Floors 1-18 |
| **TOTAL** | **7 Environments** | — | **188** | **188 Active Locations (0 Orphans)** |

---

### 4.2 Full Hierarchical Nesting Tree (188 Nodes, 8 Roots)

```text
├── ROOT: Bakersfield [_fekTA9NRygQ49q7cxRz8A] (Env: California Coast)
│   ├── Bakersfield Square [_11LzwJB9B6rGrEQTTd7xd]
│   ├── Campi Petroliferi di Kern River [_VEXr9e9eUWwEpFNCRUm9V]
│   ├── Kern River Canyon [_jx7cMhrTAtCztbPMJTb1H]
│   ├── Mercato Contadino (Farmer's Market) [_tbbaxN7A3pgFQ8x73xGNr]
│   ├── Parco Roulotte di Oildale [_CFdc6hPMPCQMja7ABT3zP]
│   ├── Rhodes Farm [_FQVVaJrXtd4Y66mPna87C]
│   └── The Dusty Coyote Diner [_mfW6WAcWPcwkPxWyfPCye]
│
├── ROOT: Blackwood City [_D8B9QAfHPn3NfD4mAnJen] (Env: Blackwood)
│   ├── Arcadia [_X6R6dKTzkjdFk6cqdt2we]
│   │   ├── Arcadia School [_Y18rdHTpAT3QX82DfLFLF]
│   │   ├── Blackwood General Hospital [_nXCafeG32thtDKqyX8zV1]
│   │   └── Sugar Moon Bakery [_63BP7yfwEpEJbDgEqP2ew]
│   ├── Blackwood Forest [_HN1tmm3Ex4LBh2HtWGUbq]
│   │   ├── Bloodmoon Pack Territory [_xEB9X8wUGwQrELYzKX7gt]
│   │   │   └── Bloodmoon Longhouse [_RXULtwFjxCBUcxBbTfWrh]
│   │   │       └── Bloodmoon Longhouse Baths [_qUkFeCX37Agez4XtPhtqp]
│   │   ├── The Otherworld [_AqRjXRDRm23gAHJFaWC39] (Env: Voidspace/Otherworld)
│   │   │   ├── Crystal Caves [_3tAAgRefjD7VntWhHYRfg]
│   │   │   ├── Dragonide Sanctum [_FyNLmfUAaxCea1Ny6mBtm]
│   │   │   └── Silver Marshes [_3EALFJfmG91xVpUjnzrEk]
│   │   └── Yarrow River [_jXp8TKEpTNkrtMtENy2Wg]
│   ├── Bluemoon [_MkkwDR7AHq4tYLmnk134f]
│   │   └── The Verve [_hfm1W4nYnXfQEqcNGwNxr] (Logan's Custom Garage / Secret Nightclub)
│   ├── Dockside [_B7Eq8K8CUXrCe9NKATXGE]
│   │   ├── Dockside Ferry Landing [_AWyPeCP8QWhD4D1M6hfzT]
│   │   └── The Horns [_MxFzj8MUgHPXd8Y9m8hX4]
│   │       ├── Apartment C [_CPWKPYwWeDY7ktNgBLWAy]
│   │       └── Diner del Sud [_7jtmcqHPpFemAnhtghdxq]
│   ├── Ironworks [_fyC1LJ8CAK8rP7k8Dr2a2]
│   │   ├── Club House Ironhorn Nomads [_DJxYBCM7rNrXMj1WracGM]
│   │   └── The Underground Fighting Ring [_gpBY7HGddd4KHfqaDyy3c]
│   ├── Oldtown [_Gnm9WMQNjhUWJLhrkpqQk]
│   │   ├── Braceria McKay (McKay's Smokehouse) [_fBmdJReXCqdRLzYzyKw7w]
│   │   ├── Market-Zone [_FVygCThfwJP77BRNc8qYL]
│   │   └── Old Cedar Clearing [_pA2pCqnF2FenCeHAmyd37]
│   ├── Paradise [_H6PUHPMMUEmM2wJbfd8et]
│   │   ├── Eidolon Creative [_4w7Npw7VkhbAyU1Qy1Wt2]
│   │   │   └── Eidolon Creative Private Suites [_RTxCmM7pKQGx8VVA83B7Q]
│   │   └── L'Iris d'Oro [_K1qQL7wBcWpkyyeyw76TU]
│   ├── Seven Hills [_EwMMJ7KEg9ATJ3mTXBaha] (Env: Seven Hills)
│   │   └── Villa Douglas [_9H2EmzRm92QxBpkmJUR1z]
│   │       ├── Jasper's Cavern (Villa Douglas West Wing) [_hcmcH3jKtU82P8Bh11mF1]
│   │       ├── The Nursery [_FfUxT1htx6HW9LJAHhdqw]
│   │       ├── Villa Douglas: Alyssa's Sanctuary / Omega Nest [_kfXfwkXrzPTRetcBmUt9T]
│   │       ├── Villa Douglas: Council Room [_xDrAxmgeq3tfgwxYKJwkq]
│   │       ├── Villa Douglas: Erik's Sanctuary [_rpBxnqzbc2EPg4eUdhrhx]
│   │       ├── Villa Douglas: Garage & Security Perimeter [_LVkMH48tkbdC41T7kCFFV]
│   │       ├── Villa Douglas: Gardens & Pools [_4X1A2UgJkcjhYHMXcL4Xh]
│   │       ├── Villa Douglas: Guest Wing [_mUHCbXLjDAy8YqraaR7jf]
│   │       ├── Villa Douglas: Main Atrium [_cU3JC9R4VJJrcEJ8GtAFt]
│   │       ├── Villa Douglas: Malachia's East Wing & Den [_Uqpphc8B1L86DVjRAaJxR]
│   │       ├── Villa Douglas: Noah's Gourmet Kitchen [_P78yNW43E1fayK9cXzGpd]
│   │       ├── Villa Douglas: Pack Bathhouse [_EYXqbQkgmU98JBfc8agjF]
│   │       ├── Villa Douglas: The Attic Sanctuary [_gUjcJKTyq3K3LFF3BbVzd]
│   │       └── Villa Douglas: Throne Room [_gKQqD84T3ymHd3XKVBjFF]
│   ├── St. Brugge Private Academy [_4wJ11ttfz78gfH2cqdx4R]
│   ├── The Cable District [_RVRf9PtEdwhGt3rGGFjMC]
│   │   └── The Void [_xJ9zaHVxUNnWw6UwwpAVe]
│   └── Uptown [_8fRJTJVkd7VjkQ3jfJWQ1]
│       └── Aetheris Clinic [_8mEgKeWWt4hP1M1AYMQPW]
│
├── ROOT: Camp Mystic [_yPxa34RwGz9wbjm1zjhLJ] (Env: California Coast)
│
├── ROOT: DDM Inc. // Voidspace [_BUfxJEGc4Td36H8kMmVD3] (Env: Voidspace/Otherworld)
│   ├── DDM Inc. Headquarters [_eUkmTYmVng7bdJTAb8cdC]
│   │   ├── Dullahan's Quarters [_kTjtqx6n2r6JVhFFXe8D7]
│   │   └── The Euclidean Division [_N36MDPCGy43ymPfBMUXnx]
│   └── The Lower Levels [_PVTXK3yRKjVPcxRCg61R3]
│
├── ROOT: Hex Valley [_k118p3PTLgG88pkXn48BQ] (Env: California Coast)
│   ├── California University of Magical Sciences (CUMS) [_Caw9nRwKf4Gx9VzW21QJj]
│   │   ├── Apollo Dorms [_wEkzHgpxfetQr16bTWNUP]
│   │   ├── Artemis Dorms [_9YKj9HxFkRWnNJUJk84Tr]
│   │   ├── Evirein Academy of Magic [_yPNABkfHwWeDpEjHfehAz]
│   │   ├── Magick Research Labs [_QJUgPg6nGLqwdTgCL62NH]
│   │   ├── Nightwine Hall [_nKAXKmzHrCbRTQeqqFx3T]
│   │   └── Nocturnal Hall [_3kFK6JCz9WEM2wGNRXnxq]
│   ├── Hex Valley Estates [_9qzfFrQrFW1X3yBznanaT]
│   └── Hex Valley Ferry Stop [_C7Nj1emPcrhDQb1gFYMDr]
│
├── ROOT: Los Angeles [_X4A8gWVr43a7dRr9TbJ4m] (Env: California Coast)
│   ├── Beverly Hills [_yqQeB1GzKJyqfwjUPRP2M]
│   ├── DCC Tower [_XD2gWgyhTYmDEXWkxMLer]
│   ├── Fort MacArthur [_cDDqVXg3jbxEhBd3qJ3ME]
│   ├── Hollywood [_pTqkAfBAEFUtEA3BqUjRz]
│   ├── Molo 42 [_jABzFFNTGRdRLEkNYTKx2]
│   ├── Osservatorio Griffith [_N923td3fCdLPXBDDftp2T]
│   ├── Pershing Square [_16nUQjhqXaFaUEKy1zgpA]
│   ├── Rory's Estate [_TLEaxwQCB24kQYfYHy8pq]
│   ├── Skid Row [_NqaNWcjcwHXmXFTptBEbP]
│   └── The Neon Mirage [_NNtDFU6T1h929Kc79Uej1]
│
├── ROOT: Solarton [_761mFFeCcQyR9JxhLCWcy] (Env: Solarton)
│   ├── Bricklane Mall [_hGpPMY77NaH4j6AxNGLVe]
│   │   ├── A&Co. [_R7Cz4Uah9Tjkn4KDC7rxM]
│   │   ├── Claws Steel & Ink [_3tNeXcGBfcUX6J1mtjqAw]
│   │   ├── Kerrigan & Sons Butchers [_UW8r3dr8VW7T6e1pFEd6U]
│   │   ├── La Segunda Luna [_Jyg1XPDHyNkyJKyzJf13F]
│   │   ├── Medusa [_Ft3eYhJaqKPK23edMnPfV]
│   │   ├── Suds & Such [_tLc7FjRTTAgkdy9qjX2zE]
│   │   ├── The Long Table [_KeBE9zTg2zV72Y17bKnex]
│   │   ├── Tidewrack Surf & Rental [_Vhqnmrg3YAdWMTfPcGGxP]
│   │   └── Yeti Shack [_cXC2KcP9yMAtPGFkNrTVj]
│   ├── Clinica Ortus [_aWcjmPKnChpzGndYD62gP]
│   ├── Coastal Residential [_UeKEhHTnCP6yQk7mhMVU1]
│   ├── Dullahan's Condo [_88QNj8BnFMN143XxNat1n]
│   ├── La Dimora del Rifugio [_BD8F76PngMyD2yURFWV76]
│   ├── Rogers' Bargain Motors [_CAhgArEXA2eBDQPpPe1gE]
│   ├── Sidewinders Bar & Nightclub [_VbjcwqJnc7BaED9A9t2Dq]
│   ├── Solarton Ferry Terminal [_NVALjebTDk1kPC9AjWhWt]
│   ├── Solarton High School [_BgLjFRGNj9YX7tzybBzda]
│   ├── Solarton Public Beach (Bay Area) [_a2pRKBjYnQ1Q1LaN6xdeh]
│   ├── Solarton Square [_Mq1DYmKdnkR83YBjNRyXr]
│   │   ├── Directions & Dragons [_7LmyTdEgVPeFbmkG4Rwe7]
│   │   │   └── Flat above Directions & Dragons [_WX48nzYX28GRM1gj9gQBf]
│   │   ├── Full Moon Market [_GYF4znCTjcJgLH9XYVbg8]
│   │   └── The Lunar Pharmacy [_1wcb4XHMXfg2YBwa2PFkM]
│   ├── Static & Ink [_CKkP1PfqRJDQLBPQeFyWF]
│   ├── Supernatural University of Central California [_j67Dp2PVwFCpdrfWRYV2M] (Env: SUCC campus)
│   │   ├── Additional Student Housing [_xLd2GzGayGJXUhjAdTPye]
│   │   ├── Administration [_938z2ywf8QND6cA1MwVEr]
│   │   ├── Archer Wolfwood Hall [_A3V3pEPJjBEtNK4nMCqwP]
│   │   │   ├── Classrooms [_kCTbCQQpXzmkD4pUX6e8J]
│   │   │   └── Main Lecture Hall [_DrzEq6E6WcC7AtUrwUcYj]
│   │   ├── Arts Building [_Dw9VQxmgEDGTyQdJzwJgG]
│   │   ├── Basilica Library [_jYJxF7fte2Gz1F2HGXpUR]
│   │   │   ├── Basement Meeting Room 005 [_4FMaQm3xQCUVHeRf3AWYk]
│   │   │   │   └── Anime Club [_cXU4CwaxexhU823DAH1M6]
│   │   │   ├── Magical Sections [_nUfUjnM83KnD1PUBtRmML]
│   │   │   ├── Study Rooms [_kCDTdBmhMMnTDNT4FWDHp]
│   │   │   ├── The Roasted Bean [_XUV6jWXTXG6wgj2WKBEpr]
│   │   │   └── Trophy Room [_GkEhhnk7nWEpMmRUazFe1]
│   │   ├── Building A [_Red8pjJGjMhP2XDBejrt2]
│   │   ├── Building B [_t4pLDVa4j3PpBbyb7CqGa]
│   │   ├── Building C [_Len9cGpbmncYB2qLArTFM]
│   │   ├── Bulls Stadium (St. Neptune Athletic Complex) [_Bx2U1xzg1D3wpFRe39L7y]
│   │   │   ├── Bulls Football Field [_VzByV4y4PKCw7N7hJyDkV]
│   │   │   ├── Ice Rink [_YHVnw9ytGd3V4mNhdbFh3]
│   │   │   └── Indoor Pool & Sauna [_JTRYG4tbNaYd72V7cKNVQ]
│   │   ├── Dragon's Shortcut [_8hdAHhey4MxWd3r1BjqL2]
│   │   ├── Fraternity & Sorority Row (Greek Row) [_yXApVAkzqLrFkLkhW7fdU]
│   │   │   ├── Alpha Rho Omega (ARO or ΑΡΩ) [_E6ga9CmYQ31CwNkrHkGX9]
│   │   │   ├── Alpha Sigma Sigma (ASS or ΑΣΣ) [_tFj1yzTVDaEhdJLYe13YM]
│   │   │   ├── Beta Epsilon Epsilon (BEE or ΒΕΕ) [_Wj2hkqUxDrB4aDaGDM8q9]
│   │   │   ├── Beta Rho Omega (BRO or ΒΡΩ) [_p1JatqFwBPeKPQrh6CmGe]
│   │   │   ├── Delta Omicron Epsilon (DOE or ΔΟΕ) [_Ug2jTR6Wq3XGhQGzchcft]
│   │   │   ├── Kappa Sigma Alpha (KSA or ΚΣΑ) [_jrpjEjGF6eFNcVWATaH91]
│   │   │   ├── Mu Alpha Nu (MAN or ΜΑΝ) [_89J6GpNndcJnAEUB33DqP]
│   │   │   ├── Mu Omega Omega (MOO or ΜΩΩ) [_bpQD4kCGHK1LW7WjahdU4]
│   │   │   ├── Phi Omicron Chi (FOX or ΦΟΧ) [_C1qMV6LyhPA7yAJLXDFxN]
│   │   │   └── Theta Iota Theta (TIT or ΘΙΘ) [_Ep6xM191zpn6jpUygJakP]
│   │   ├── Gallery [_L8UpkDzCNTFWH7gBWep2r]
│   │   ├── Griffin Clocktower [_ptpGD1VeVep7YknRmhFXM]
│   │   ├── Gym & Changing Facilities [_EmJg3zdjTT8kwteJJkyUR]
│   │   ├── Helsing Chapel [_jX3bYbn8FHra6qNYUC3Ux]
│   │   │   └── Vampire & Undead Association [_XQH8GCkktUMfgDa8KbyxK]
│   │   ├── Law & Engineering Theatres [_UP6GLYJtbYpFDN41TjDrW]
│   │   ├── Lunar Quad [_WrymW8qTETkm7r1QXQGaT]
│   │   │   └── The Pack [_eb8aWLJfT3Yw1E6nxQEJ4]
│   │   ├── Main Parking Lot [_pG2ryjWVzDPN4AWX13Vyh]
│   │   ├── Main Pool [_GnNYqapde8TGQtemCwJHT]
│   │   ├── Nocturnal Club Space [_YwTGV1TtRLa2Cchtmdp14]
│   │   ├── Parking Lot B [_t3ReTGT1AjzaKqVM7PtDT]
│   │   ├── Science Quarter [_DA14L9eU8wdcfFR1acpbn]
│   │   │   ├── Greenhouse [_MWLFXbYrV82JMcaQHkpBE]
│   │   │   ├── Med/Bioengineering Labs [_CWPhKE4Y7wC4eLdfgdejn]
│   │   │   └── Specimen Containment [_3zkxkP9RjhMf4X3pMkk7b]
│   │   ├── Sports Fields [_WRBThTNK3wJawVdLRhA1e]
│   │   ├── Storage & Supplies [_Ra4fXd8BEdKUeKTbGAw3b]
│   │   ├── Student Association Building [_aLqMW6UHHj1D9M4xxENF7]
│   │   │   ├── S.H.A. Meeting Room [_JtEUrHrrYAGTCyRQRA8XQ]
│   │   │   └── Supernatural & Human Alliance [_BmQdEBKrrBeWXhJzbhcE9]
│   │   ├── Supernatural Support Center (SSC) [_G33ABhpFceN7HanHwp8rr]
│   │   ├── Unicorn Hall [_nhdQ7xkycT1yfn1wWXN8U]
│   │   │   └── Bigfeet Hiking Club [_XAgh9YLPYdmeDUwAeXXDY]
│   │   └── Wyrm Dormitories [_6KT7hL8LMFzU3dK6h1wax]
│   │       ├── Blood Bank [_mdtyCwD2hL3L4eKnycFNz]
│   │       ├── North Wing (Human) [_AdgYjLPG44QV2Xrq9ePgJ]
│   │       ├── South Wing (Supernatural) [_Wrg47JYXUBq7R2yT47Nrm]
│   │       ├── Sun/Moon Rooms [_4JrzkmYjdmLEUGNDatEmD]
│   │       └── West & East Wings (Mixed) [_WAHzgab11F3k9BRqNJHb2]
│   └── The Open Casket [_EK4EPeKCjmFd3EbPNTCkT]
│
└── ROOT: Zone di Transito e Confine [_zjA9MJEAVjjFn64jjtcb6] (Env: California Coast)
    ├── Dead Dog Motel / Voidspace [_qBt3jf1kppwrmMwTBbYJB] (Env: Voidspace/Otherworld)
    ├── Simi Valley [_4k3RT1nxw994yHRM66LQb] (Env: DMHA HQ & Guild District)
    │   ├── Simi Valley Infopoint [_82cNpDwVJwVd8qGRUgFw8]
    │   └── The Simi Valley Grid [_KAa4FrdtffjCETKPEK7fr]
    ├── Team Ukiyo Operational Base [_erHMcydnPVEyk7NY3K9wf] (Env: DMHA HQ & Guild District)
    ├── Trial Dungeon: Hive Apex Rift [_CaKc8CcYADYxLRmb2GYpG] (Env: Voidspace/Otherworld)
    └── Ventura / Route 101 [_FrXnp2CALTP44CP3KVAhb] (Env: California Coast)
        ├── Area di Servizio "The Halfway House" [_XeqYfUxwTWKmy6rpmqaQC]
        └── Ventura Square [_h9UDyMzPtBwnzfbjj3DP3]
```

---

## 5. Verification Method

To independently reproduce and verify all observations, counts, and findings, run the following commands in the workspace root:

```powershell
# 1. Verify exact 188 count in canonical export
python -c "import json; exp = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8')); print('Export locations:', len(exp['world_locations']))"

# 2. Verify tree connectivity and 0 orphans
python .agents/teamwork/explorer_m1_locations/tree_inspector.py

# 3. Verify exact 7-environment distribution
python -c "
import sys; sys.path.append('.agents/teamwork/explorer_m1_locations')
from map_environments import env_buckets
for k in sorted(env_buckets.keys()):
    print(f'{k}: {len(env_buckets[k])}')
print('Total:', sum(len(v) for v in env_buckets.values()))
"

# 4. Inspect The Verve details and keys
python -c "
import json
with open('scratch/backup_consolidated_snapshot/world_locations.json', encoding='utf-8') as f:
    locs = json.load(f)
v = next(l for l in locs if (l.get('id') or l.get('_id')) == '_hfm1W4nYnXfQEqcNGwNxr')
print('Name:', v['name'])
print('Parent:', v['parent_location']['name'])
print('Keys:', v['keys'])
print('Included Lexicon:', v['included_lexicon_entries'])
"
```

### Invalidation Conditions
- If any node in the 188 set has a `parent_location` ID that cannot be resolved to another member of the 188 set or `None`.
- If the sum of locations across the 7 canonical Environments deviates from 188.
- If The Verve loses its dual day/night garage-nightclub specification or its 3 wired item lexicon IDs.
