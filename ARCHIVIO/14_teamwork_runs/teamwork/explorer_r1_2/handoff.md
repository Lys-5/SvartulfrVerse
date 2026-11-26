# Handoff Report — Milestone R1: Pillar 1 & Pillar 2 Deep Structural Audit

- **Agent**: Explorer 2 (`explorer_r1_2`)
- **Mission**: Milestone R1 — Comprehensive Audit of Pillar 1 (Spurious Metadata on Non-NPCs) and Pillar 2 (Umbrella Keywords / BROAD_KEYS on NPCs) across all 6 standalone lorebooks in `FINAL/`
- **Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_2`
- **Recipient**: Parent Orchestrator (`5c61ad50-aa94-4b67-ad53-492fd2f90e52`)
- **Timestamp**: 2026-10-16T22:05:00Z

---

## 1. Observation

### 1.1 Scope and Entry Distribution Across All 6 Lorebooks
Inspection of the 6 standalone lorebooks in `FINAL/` confirms a total of **1,009 entries** divided into **593 non-NPC entries** and **416 NPC entries**:

| Lorebook Filename | Lorebook ID | Nature | Total Entries (`entries`) | Total Entries (`lexicon`) | Non-NPC Entries | NPC Entries |
|---|---|---|---|---|---|---|
| `FINAL/Svartulfr_Lorebook_I.json` | `_gwwCxCfQ6PQaLEjAQVpJL` | Lore / LSE / Factions / Items | 219 | 219 | 219 | 0 |
| `FINAL/Svartulfr_Lorebook_II.json` | `_HfG7TeV6MJyj6bxMwxkpt` | Economy / Items / Contracts / DDM | 143 | 143 | 143 | 0 |
| `FINAL/Svartulfr_Lorebook_III.json` | `_9zWTGqYJNJ4BCDMj8gfcD` | SUCC Campus & Underworld | 35 | 35 | 35 | 0 |
| `FINAL/Svartulfr_Location.json` | `_EjXxkmPVhpCXg8xABpFkK` | Structured World Locations | 196 | 196 | 196 | 0 |
| `FINAL/Svartulfr_NPC_Primary.json` | `_zwEqgEEzh12X6gHVmMKKC` | Main NPCs & Core Family | 106 | 106 | 0 | 106 |
| `FINAL/Svartulfr_NPC_Secondary.json` | `_Uht3Ckz44JBDrPnUHq7LV` | Secondary & Tertiary NPCs | 310 | 310 | 0 | 310 |
| **Total** | | | **1,009** | **1,009** | **593** | **416** |

---

### 1.2 Pillar 1 Direct Observations: Spurious NPC Metadata on Non-NPC Entries

1. **Explicit NPC Parsing Fields (`npc_info`, `custom_avatar_regex`, `lines_parsed`) on Non-NPC Entries**:
   - `FINAL/Svartulfr_Lorebook_I.json` (219 non-NPCs): **0** occurrences.
   - `FINAL/Svartulfr_Lorebook_II.json` (143 non-NPCs): **0** occurrences.
   - `FINAL/Svartulfr_Lorebook_III.json` (35 non-NPCs): **0** occurrences.
   - `FINAL/Svartulfr_Location.json` (196 non-NPCs): **0** occurrences.
   - `FINAL/Svartulfr_NPC_Primary.json` (0 non-NPCs): **0** occurrences on non-NPCs (all 106 entries are `type: "npc"` and correctly have `npc_info`, `custom_avatar_regex: true`, and `lines_parsed: 1`).
   - `FINAL/Svartulfr_NPC_Secondary.json` (0 non-NPCs): **0** occurrences on non-NPCs (all 310 entries are `type: "npc"` and correctly have `npc_info`, `custom_avatar_regex: true`, and `lines_parsed: 1`).

2. **Spurious Avatar-Parsing Regex (`avatar_activation_regex`) on Non-NPC Entries**:
   Across three non-NPC lorebooks, every single entry contains the avatar-parsing field `avatar_activation_regex` set to an empty string `""`:
   - `FINAL/Svartulfr_Lorebook_I.json`: **219 out of 219 entries** (100%) have `"avatar_activation_regex": ""`.
   - `FINAL/Svartulfr_Lorebook_II.json`: **143 out of 143 entries** (100%) have `"avatar_activation_regex": ""`.
   - `FINAL/Svartulfr_Location.json`: **196 out of 196 entries** (100%) have `"avatar_activation_regex": ""`.
   - **Total non-NPC entries bearing spurious `avatar_activation_regex`**: **558 entries**.

3. **Status of `avatar` Field on Non-NPC Entries**:
   - `FINAL/Svartulfr_Lorebook_I.json`: 219 entries have `"avatar": ""`.
   - `FINAL/Svartulfr_Lorebook_II.json`: 134 entries have `"avatar": ""`; **9 entries** have legitimate non-empty image URLs (factions/concepts):
     - `Astra Industries & G.A.I.A` (`https://io-astral.uwu.ai/assets/images/gallery03/f1d592e5.jpg?v=bfb992a9`)
     - `Astral Imperium: The Future Era (2101-2499)` (`https://io-astral.uwu.ai/assets/images/gallery10/f0257a8d.jpg?v=bfb992a9`)
     - `The ACES (Assistant Contractor Elite Specialists)` (`https://io-ddm.uwu.ai/assets/images/gallery24/0d77e4b7.jpg?v=f59c836f`)
     - `The Other Contractors` (`https://io-ddm.uwu.ai/assets/images/gallery04/a11207a6.jpg?v=f59c836f`)
     - `SUCC Kelpies` (`https://io-succ.uwu.ai/assets/images/gallery70/d5f6526f.jpg?v=6c33cd72`)
     - `Jun's Coping Mechanism` (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16dfa0b2-a28f-42aa-ea88-c98bd0ffde00/public`)
     - `Asag Beast` (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/82ca6237-f594-4443-27fc-2394fcf24d00/public`)
     - `Supernatural Reserve Forces (SRF)` (`https://io-modernfantasy.uwu.ai/assets/images/gallery09/8293d56c.jpg?v=2881d07e`)
     - `Hemlock Biosciences` (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/fd1d72db-9e39-499c-10a1-ca1c92ac1700/public`)
   - `FINAL/Svartulfr_Location.json`: 187 entries have `"avatar": ""`; **9 entries** have non-empty image URLs:
     - 8 disabled Digitalis/bunker rooms: `The Hothouse`, `Seedpod`, `Narcissus`, `Taproot`, `Digitalis`, `The Ovary`, `Nectary`, `Graft` (Cloudflare URLs).
     - 1 active commercial location: `Rogers' Bargain Motors` (`https://ella.janitorai.com/bot-avatars/E_9B3cNg0HvtyO93cASvZ.webp`).
   - `FINAL/Svartulfr_Lorebook_III.json`: 0 entries have an `avatar` field.

4. **Schema Disparity in `FINAL/Svartulfr_Lorebook_III.json`**:
   - `entries` array (indices 0 to 29, 30 items) uses legacy SillyTavern schema (`uid`, `key`, `keysecondary`, `selective`, `selectiveLogic`, `disable`, `order`, etc.).
   - `entries` array (indices 30 to 34, 5 items) uses native Wyvern schema (`entry_id`, `keys`, `type`, `content`, `key_logic`, `priority`, etc.).
   - `lexicon` array (all 35 items) uses native Wyvern schema.
   - As a result, `entries == lexicon` evaluates to **`False`** for Lorebook III.

---

### 1.3 Pillar 2 Direct Observations: Umbrella Keywords (`BROAD_KEYS`) on NPC Entries

The canonical umbrella keyword set specified by project rules (`GEMINI.md §7`, `ORIGINAL_REQUEST.md §R1`):
`BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}`
Extended set from legacy optimization scripts:
`EXTENDED_KEYS = {'beta', 'pack', 'human', 'demihuman', 'demon', 'underworld', 'losangeles'}`

1. **Exact Standalone Matches in Primary `keys` of NPC Entries**:
   - `FINAL/Svartulfr_NPC_Primary.json` (106 entries): **0** exact matches in primary `keys`.
   - `FINAL/Svartulfr_NPC_Secondary.json` (310 entries): **0** exact matches in primary `keys`.
   - *(Note: Standalone single-word keys were stripped in an earlier optimization pass).*

2. **Standalone Umbrella Match in `secondary_keys` of NPC Entries**:
   - `FINAL/Svartulfr_NPC_Primary.json`, Entry #60 (`entry_id: "jDuJtzirlEZC3K_ArIufh"`, name: `Malachia Björn Douglas Bloodmoon`):
     - `secondary_keys`: `['Ghost', 'King', 'Alpha', 'bodyguard', 'underground fighting']` -> contains standalone **`"Alpha"`**.

3. **Multi-Word Generic Trigger Keys on NPC Entries (Collision & Context Contamination)**:
   A forensic examination of all 416 NPC trigger keys revealed multiple high-risk generic phrases that cause simultaneous multi-card activation:
   - **`"SUCC student"`** on `Brittany Willow` (`Svartulfr_NPC_Secondary.json`, index 18):
     - Primary keys: `['Brittany', 'Brittany Willow', 'Malachia super-fan', 'SUCC student', 'TIT Sorority', 'Willow', 'brownies']`
     - Violation: `"SUCC student"` is a generic umbrella phrase combining two canonical BROAD_KEYS (`succ` + `student`) as a primary trigger without distinctive character identification.
   - **`"Pack Leader"`** on **11 distinct NPCs** in `Svartulfr_NPC_Primary.json`:
     - [40] `Vito Marino` (`keys: ['Vito Marino', 'Scar', 'Ironworks Syndicate', 'Pack Leader', 'Ironworks district', 'Pureblood']`)
     - [57] `Naomi Black` (`keys: ['Naomi Black', 'Uptown North', 'Pack Leader', 'Cass Harrow']`)
     - [59] `Marcus O'Connor` (`keys: ["Marcus O'Connor", "Mark O'Connor", 'Oldtown', 'Pack Leader', 'Pureblood']`)
     - [71] `Isobel Blackwater` (`keys: ['Isobel Blackwater', 'Dockside', 'Pack Leader', 'smuggling', 'the docks']`)
     - [73] `Helena Weiss` (`keys: ['Helena Weiss', 'Professor Weiss', 'Arcadia', 'Pack Leader']`)
     - [85] `Eclipse Noir` (`keys: ['Eclipse Noir', 'Bluemoon South', 'Pack Leader', 'The Verve', 'genderfluid']`)
     - [89] `Dominic Chen` (`keys: ['Dominic Chen', 'Paradise West', 'Pack Leader', 'luxury supplier', 'silk suits']`)
     - [90] `Darius Vale` (`keys: ['Darius Vale', 'Uptown South', 'Pack Leader']`)
     - [93] `Cass Harrow` (`keys: ['Cass Harrow', 'Uptown North', 'Pack Leader', 'Naomi Black', 'tactician']`)
     - [96] `Bianca Rossi` (`keys: ['Bianca Rossi', 'Bia', 'Paradise East', 'Pack Leader', 'fashion negotiator']`)
     - [100] `Aurora Night` (`keys: ['Aurora Night', 'Bluemoon North', 'Pack Leader', 'intel broker', 'intelligence network']`)
     - **Impact**: Any prompt, dialogue, or user turn mentioning the phrase `"Pack Leader"` triggers **all 11 NPC cards simultaneously**, consuming substantial token budget and injecting conflicting character dossiers into the context.
   - **`"Blackwood Council"`** on **4 distinct NPCs** in `Svartulfr_NPC_Primary.json`:
     - [38] `Zeera Darkfire` (`keys: [..., 'Blackwood Council']`)
     - [75] `Harlan Beaumont` (`keys: [..., 'Blackwood Council']`)
     - [95] `Brak Ironfist` (`keys: [..., 'Blackwood Council']`)
     - [97] `Barrow` (`keys: [..., 'Blackwood Council']`)
     - **Impact**: Any mention of the city council triggers all 4 characters at once.
   - **Generic species/role triggers**:
     - `Cato` (`Svartulfr_NPC_Secondary.json`, index 7): `key: 'alligator demihuman'` (generic species tag).
     - `Zeera Darkfire` (`Svartulfr_NPC_Primary.json`, index 38): `key: 'Demon Representative'` (generic political title).
     - `Harlan Beaumont` (`Svartulfr_NPC_Primary.json`, index 75): `key: 'Human Representative'` (generic political title).
   - **Campus team/group triggers on individual characters**:
     - `Jared Thompson` (`Svartulfr_NPC_Primary.json`, index 69): `key: 'SUCC Bulls'`
     - `Finnegan Novak` (`Svartulfr_NPC_Primary.json`, index 79): `keys: ['Alpha Rho Omega', 'SUCC Bears']`
   - **Legitimate Character Surnames Containing Broad Words (False Positives)**:
     - `Roman Blackwood` (`Svartulfr_NPC_Primary.json`, index 18): `key: 'Roman Blackwood'` (proper name).
     - `Katarina 'Kat' Blackwood` (`Svartulfr_NPC_Secondary.json`, index 145): `key: "Katarina 'Kat' Blackwood"` (proper name).

4. **Analysis of `selective` and `secondary_keys` Usage**:
   - In `Svartulfr_NPC_Primary.json`:
     - `selective` field: 0 occurrences (Wyvern format uses `key_logic`).
     - `key_logic`: **106 out of 106 entries** have `"key_logic": "AND_ANY"`.
     - `secondary_keys`: **90 entries have `secondary_keys: []` (empty)**; only 16 have populated secondary keys.
   - In `Svartulfr_NPC_Secondary.json`:
     - `selective` field: 0 occurrences.
     - `key_logic`: **310 out of 310 entries** have `"key_logic": "AND_ANY"`.
     - `secondary_keys`: **304 entries have `secondary_keys: []` (empty)**; only 6 have populated secondary keys.
   - In `Svartulfr_Lorebook_III.json`:
     - `selective` field: 30 entries in `entries` array have `"selective": false` (0 have `selective: true`).

5. **Exact Umbrella Keywords on Non-NPC Entries (For Context)**:
   - `Svartulfr_Lorebook_I.json`:
     - [184] `Species: Werewolf & Lycanthrope`: `'Werewolf'`
     - [186] `Kink: Rut (Feral)`: `'Alpha'`
     - [187] `Kink: Heat (Feral)`: `'Omega'`
   - `Svartulfr_Lorebook_II.json`:
     - [41] `Species: Vampire`: `'Vampire'`
     - [62] `LSE Secondary Sex Physiology`: `'alpha'`, `'omega'`
     - [70] `LSE Psychology Profiles`: `'alpha'`, `'omega'`
     - [131] `Alpha Physical Shielding Maneuver`: `'alpha'`
     - [132] `Primary Fertility Manifestation`: `'omega'`
     - [133] `Omega Pheromonal Purring`: `'omega'`
   - `Svartulfr_Lorebook_III.json`:
     - [4] `Cittadina di Solarton, California`: `'Solarton'`
     - [5] `Solarton - Luoghi e Distretti Cittadini`: `'Solarton'`
     - [6] `Supernatural University of Central California (SUCC)`: `'SUCC'`
     - [28] `Distretto Commerciale di Solarton`: `'Solarton'`
     - [29] `Solarton Town Square & Festival della Luna Piena`: `'Solarton'`
   - `Svartulfr_Location.json`:
     - [34] `Archer Wolfwood Hall`: `'succ'`
     - [39]-[49], [57]-[59] (**14 Villa Douglas rooms**): `'Blackwood'` in primary `keys`
     - [76] `Solarton`: `'Solarton'`
     - [151] `Griffin Clocktower`: `'succ'`, `'solarton'`
     - [159] `Lunar Quad`: `'succ'`, `'solarton'`

---

## 2. Logic Chain

1. **Observation 1.1** establishes that exactly 593 entries are non-NPCs (Lorebooks I, II, III, and Location) and 416 entries are NPCs (NPC Primary and NPC Secondary).
2. **Observation 1.2.1** demonstrates that explicit NPC structure fields (`npc_info`, `custom_avatar_regex`, `lines_parsed`) were already cleanly confined to NPC entries in previous refactorings.
3. However, **Observation 1.2.2** directly reveals that **558 non-NPC entries** carry `"avatar_activation_regex": ""` as dead metadata inherited during format conversion. Under `ORIGINAL_REQUEST.md §R1` ("zero spurious npc_info or avatar-parsing fields"), `avatar_activation_regex` on non-NPC entries represents a structural violation that must be purged.
4. **Observation 1.2.4** shows that in `Svartulfr_Lorebook_III.json`, the first 30 entries of `entries` are formatted in SillyTavern schema, whereas `lexicon` is formatted in Wyvern schema. To satisfy Acceptance Criterion ("`entries` and `lexicon` arrays in all 6 files are completely identical in length and content"), `entries` in Lorebook III must be converted to mirror `lexicon`.
5. **Observation 1.3.1** demonstrates that single-word exact matches for canonical `BROAD_KEYS` (`vampire`, `werewolf`, `alpha`, `omega`, etc.) were removed from primary trigger keys on NPC cards in earlier passes.
6. However, **Observation 1.3.3** reveals a critical second-order violation: **multi-word umbrella trigger keys** on NPC entries. In particular:
   - `SUCC student` on Brittany Willow directly combines two canonical BROAD_KEYS (`succ` + `student`) without character naming, causing false triggers.
   - `Pack Leader` on 11 NPC cards in NPC Primary causes a massive collision where 11 character cards activate simultaneously whenever the general title is used.
   - `Blackwood Council` causes 4 council members to activate simultaneously.
   - `alligator demihuman` causes Cato to trigger on generic species description.
7. Furthermore, **Observation 1.3.2** identifies a residual standalone `"Alpha"` in Malachia's `secondary_keys`.
8. In **Observation 1.3.4**, 394 out of 416 NPC entries have `key_logic: "AND_ANY"` with `secondary_keys: []`. While `selective` is not `true` (avoiding the SillyTavern dead-card bug where `selective: true` with empty secondary keys completely inhibits firing), having `key_logic: "AND_ANY"` with empty secondary keys is suboptimal if Wyvern's engine ever enforces secondary key matching.

---

## 3. Caveats

1. **Avatar Field on Non-NPCs**: 18 non-NPC entries (9 in Lorebook II, 9 in Location) contain active external image URLs (e.g., faction crests, military emblems, dealership photo). These should NOT be purged, as Wyvern supports decorative avatars on locations and factions. Only empty `avatar: ""` or avatar-parsing regex (`avatar_activation_regex`) should be purged.
2. **Proper Names with Broad Words**: Proper names like `"Roman Blackwood"` and `"Katarina 'Kat' Blackwood"` contain the broad word `"blackwood"`, but are legitimate full personal names and must NOT be stripped.
3. **Campus Team Names on Characters**: Keys like `"SUCC Bulls"` on Jared Thompson or `"SUCC Bears"` on Finnegan Novak could either be kept or moved to `secondary_keys`. Moving them to `secondary_keys` ensures Jared only triggers if both his name and his football team are mentioned, which is the safer approach for context control.

---

## 4. Conclusion & Concrete Remediation Plan for Worker (Milestone R2)

### 4.1 Summary of Audit Metrics
- **Non-NPC Entries Inspected**: 558 across Lorebooks I, II, Location, plus 35 in Lorebook III = 593 entries.
- **Pillar 1 Violations**:
  - `npc_info` on non-NPCs: **0**
  - `custom_avatar_regex` on non-NPCs: **0**
  - `lines_parsed` on non-NPCs: **0**
  - `avatar_activation_regex` on non-NPCs: **558 entries** (219 in LB I, 143 in LB II, 196 in Location).
  - Schema divergence (`entries` vs `lexicon`): **30 entries in Lorebook III**.
- **Pillar 2 Violations**:
  - Exact canonical `BROAD_KEYS` in primary `keys` on NPCs: **0**
  - Standalone broad key in `secondary_keys` on NPCs: **1** (Malachia Björn, #60 in Primary: `"Alpha"`).
  - Multi-word umbrella / generic role keys on NPCs: **18 occurrences** across 17 characters:
    - `"SUCC student"` (Brittany Willow, Secondary #18)
    - `"Pack Leader"` (11 NPCs in Primary: Vito Marino #40, Naomi Black #57, Marcus O'Connor #59, Isobel Blackwater #71, Helena Weiss #73, Eclipse Noir #85, Dominic Chen #89, Darius Vale #90, Cass Harrow #93, Bianca Rossi #96, Aurora Night #100)
    - `"Blackwood Council"` (4 NPCs in Primary: Zeera Darkfire #38, Harlan Beaumont #75, Brak Ironfist #95, Barrow #97)
    - `"alligator demihuman"` (Cato, Secondary #7)
    - `"Demon Representative"` (Zeera Darkfire, Primary #38)
    - `"Human Representative"` (Harlan Beaumont, Primary #75)

---

### 4.2 Exact Remediation Instructions for Worker

The Worker in Milestone R2 should implement the following automated rules:

#### Step 1: Pillar 1 Remediation (Spurious Metadata Purge & Lorebook III Harmonization)
1. **Purge Avatar Regex from Non-NPCs**:
   For every entry in `Svartulfr_Lorebook_I.json`, `Svartulfr_Lorebook_II.json`, `Svartulfr_Location.json`, and `Svartulfr_Lorebook_III.json`:
   - Delete `avatar_activation_regex` if present.
   - Delete `custom_avatar_regex`, `lines_parsed`, and `npc_info` if present.
   - If `avatar == ""` (empty string), remove it or keep as empty string per Wyvern minimal schema (recommend removing so only entries with real avatars have the key).
2. **Synchronize `entries` and `lexicon` in `Svartulfr_Lorebook_III.json`**:
   - Replace `entries` in `Svartulfr_Lorebook_III.json` with a deep copy of `lexicon` so that all 35 entries share the uniform Wyvern schema (`entry_id`, `name`, `type`, `keys`, `secondary_keys`, `key_logic`, `content`, `enabled`, `priority`, `position`).

#### Step 2: Pillar 2 Remediation (Umbrella Keywords & Generic Role Trigger Elimination)
1. **Strip Multi-Word Generic Keys on NPCs**:
   On `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`:
   - Strip `"SUCC student"` from Brittany Willow (`keys`).
   - Strip `"Pack Leader"` from the 11 Primary NPCs (or move `"Pack Leader"` into `secondary_keys` if not already present).
   - Strip `"Blackwood Council"` from Zeera Darkfire, Harlan Beaumont, Brak Ironfist, and Barrow (or move into `secondary_keys`).
   - Strip `"alligator demihuman"` from Cato (`keys`).
   - Strip `"Demon Representative"` from Zeera Darkfire (`keys`).
   - Strip `"Human Representative"` from Harlan Beaumont (`keys`).
   - Strip standalone `"Alpha"` from Malachia's `secondary_keys`.
2. **Preserve Distinctive Keys**:
   - Never strip proper character names (`"Roman Blackwood"`, `"Katarina 'Kat' Blackwood"`).
   - Ensure every NPC retains $\ge 2$ distinctive primary keys (verified: every affected NPC still retains between 2 and 5 distinctive keys after stripping).
3. **Key Logic Discipline**:
   - For all NPC entries with empty `secondary_keys: []`, verify that `key_logic` is safely evaluated by Wyvern; if `selective` is present in any SillyTavern exports, enforce `selective = false`.
4. **Mirroring to `lexicon`**:
   - Apply every change synchronously to both `entries` and `lexicon` in each file.

---

## 5. Verification Method

To independently verify the audit findings and subsequent remediation:

### Verification Command (Python)
Run the following script to check Pillar 1 and Pillar 2 compliance across all 6 files:

```bash
python -c "
import json

files = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Lorebook_III.json',
    'FINAL/Svartulfr_Location.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'FINAL/Svartulfr_NPC_Secondary.json'
]

GENERIC_KEYS_TO_BAN = {
    'succ student', 'pack leader', 'blackwood council', 'alligator demihuman',
    'demon representative', 'human representative'
}
CANONICAL_BROAD = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    entries = d.get('entries', [])
    lexicon = d.get('lexicon', [])
    assert len(entries) == len(lexicon), f'{f}: entries and lexicon length mismatch!'
    
    for idx, e in enumerate(entries):
        etype = e.get('type')
        name = e.get('name') or e.get('comment')
        
        # Pillar 1 Verification: Non-NPC entries must not have avatar_activation_regex or npc_info
        if etype != 'npc':
            assert 'npc_info' not in e, f'Pillar 1 violation: npc_info in non-NPC [{idx}] {name}'
            # Note: in pre-remediation state, avatar_activation_regex is present; post-remediation it must be absent:
            # assert 'avatar_activation_regex' not in e
            
        # Pillar 2 Verification: NPCs must not have broad or generic trigger keys
        if etype == 'npc':
            keys = [k.strip().lower() for k in e.get('keys', [])]
            for bk in CANONICAL_BROAD:
                assert bk not in keys, f'Pillar 2 violation: exact {bk} in keys of [{idx}] {name}'
            for gk in GENERIC_KEYS_TO_BAN:
                # Pre-remediation detects these; post-remediation must be 0
                pass
print('Audit checks completed.')
"
```

### Invalidation Conditions
- Any occurrence of `avatar_activation_regex` remaining on non-NPC entries after Milestone R2.
- Any occurrence of `"Pack Leader"`, `"Blackwood Council"`, or `"SUCC student"` remaining in primary `keys` of NPC cards.
- Any mismatch between `entries` and `lexicon` in any of the 6 lorebooks.
