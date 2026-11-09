#!/usr/bin/env python3
"""
scripts/verify_heights_parity.py

Automated verification script for Milestone 1: Canonical Heights & Proportions.
Validates height alignment, proportional reference clauses, zero em-dashes,
single-line bracket rules, outfit corrections, and lorebook parity across the Svartúlfr Verse.
"""

import sys
import os
import json
import re
import filecmp

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CANONICAL_HEIGHTS = {
    'Alyssa': {
        'cm': '155 cm',
        'imperial': "5' 1\"",
        'full': "155 cm (5' 1\")"
    },
    'Jasper': {
        'cm': '193 cm',
        'imperial': "6' 4\"",
        'full': "193 cm (6' 4\")"
    },
    'Noah': {
        'cm': '197 cm',
        'imperial': "6' 5.6\"",
        'full': "197 cm (6' 5.6\")"
    },
    'Malachia': {
        'cm': '208 cm',
        'imperial': "6' 9.9\"",
        'full': "208 cm (6' 9.9\")"
    },
    'Erik': {
        'cm': '213 cm',
        'imperial': "6' 11.9\"",
        'full': "213 cm (6' 11.9\")"
    },
    'Wulfnic': {
        'cm': '220 cm',
        'imperial': "7' 2.6\"",
        'full': "220 cm (7' 2.6\")"
    }
}

PROPORTIONAL_CLAUSES = [
    "Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).",
    "Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.",
    "Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno)."
]

MD_FILES = {
    'Alyssa': 'database/characters/C_Alyssa_Douglas_Bloodmoon.md',
    'Jasper': 'database/characters/C_Jasper_Douglas_Bloodmoon.md',
    'Noah': 'database/characters/C_Noah_Douglas_Bloodmoon.md',
    'Malachia': 'database/characters/C_Malachia_Douglas_Bloodmoon.md',
    'Erik': 'database/characters/C_Erik_Douglas.md',
    'Wulfnic': 'database/characters/C_Wulfnic_Bloodmoon.md'
}

CARD_FILES = {
    'Alyssa': 'ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json',
    'Jasper': 'FINAL/Jasper_Douglas_Bloodmoon_card.json',
    'Noah': 'FINAL/Noah_Douglas_Bloodmoon_card.json',
    'Malachia': 'FINAL/Malachia_Douglas_Bloodmoon_card.json',
    'Erik': 'FINAL/Erik_Douglas_card.json',
    'Wulfnic': 'FINAL/Wulfnic_Bloodmoon_card.json'
}

PERSONA_FILES = {
    'Alyssa': 'FINAL/personas/Alyssa_Persona.json',
    'Jasper': 'FINAL/personas/Jasper_Persona.json'
}

LOREBOOK_PRIMARY = 'FINAL/Svartulfr_NPC_Primary.json'
LOREBOOK_OPTIMIZED = 'lorebooks/optimized/Svartulfr_NPC_Primary.json'

TARGET_ENTRY_IDS = {
    'alyssa_world_dossier_2b54a223': 'Alyssa',
    'Vcj4h2TL4Usola2A4OOl6': 'Jasper',
    'H2JX-NkHRiJ2FzoekC5ZZ': 'Noah',
    'jDuJtzirlEZC3K_ArIufh': 'Malachia',
    'C-JisFj8qA1tsFEqZKevk': 'Erik',
    'HhuMluMmIIENUei3bX6ed': 'Wulfnic'
}

errors = []

def record_error(msg):
    print(f"[ERROR] {msg}")
    errors.append(msg)

def record_ok(msg):
    print(f"[OK] {msg}")

print("=== Starting Milestone 1 Heights & Proportions Parity Verification ===")

# 1. Database Markdown Files
print("\n--- 1. Database Character Markdown Records ---")
for char_name, path in MD_FILES.items():
    if not os.path.exists(path):
        record_error(f"Markdown file not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    expected_full = CANONICAL_HEIGHTS[char_name]['full']
    if expected_full not in content:
        record_error(f"{char_name} in {path} does not contain '{expected_full}'")
    else:
        record_ok(f"{char_name} markdown has canonical height '{expected_full}'")

# 2. Style Guide
print("\n--- 2. Database Assets Style Guide ---")
style_path = 'database/assets/style_guide.md'
if not os.path.exists(style_path):
    record_error(f"Style guide not found: {style_path}")
else:
    with open(style_path, 'r', encoding='utf-8') as f:
        style_content = f.read()
    for char_name, data in CANONICAL_HEIGHTS.items():
        if data['full'] not in style_content:
            record_error(f"Style guide missing canonical height for {char_name}: '{data['full']}'")
    for clause in PROPORTIONAL_CLAUSES:
        if clause not in style_content:
            record_error(f"Style guide missing proportional clause: '{clause}'")
    if not errors:
        record_ok("Style guide contains all 6 canonical heights and all 3 proportional clauses")

# 3. Standalone Character Cards
print("\n--- 3. Standalone Character Cards ---")
for char_name, path in CARD_FILES.items():
    if not os.path.exists(path):
        record_error(f"Card file not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    desc = data.get('description', '')
    lines = desc.split('\n')
    line0 = lines[0] if lines else ''

    # Line 0 single line bracket rule
    if not (line0.startswith('[') and line0.endswith(']')):
        record_error(f"{char_name} card line 0 does not follow single-line bracket rule")
    
    # Canonical height in bracket
    expected_height = CANONICAL_HEIGHTS[char_name]['full']
    if expected_height not in line0:
        record_error(f"{char_name} card line 0 missing '{expected_height}'")
    else:
        record_ok(f"{char_name} card bracket has '{expected_height}'")

    # Proportions & Scale block
    if 'PROPORTIONS & SCALE' not in desc:
        record_error(f"{char_name} card missing PROPORTIONS & SCALE block")
    else:
        record_ok(f"{char_name} card has PROPORTIONS & SCALE block")

    # Em-dash check
    if '—' in desc or '—' in data.get('personality', ''):
        record_error(f"{char_name} card contains forbidden em-dash ('—')")

    # Outfit fixes for Erik and Wulfnic
    if char_name == 'Erik':
        outfits = data.get('outfits', [])
        if outfits and '213 cm' not in outfits[0].get('description', ''):
            record_error("Erik outfit 0 does not contain updated height '213 cm'")
        else:
            record_ok("Erik outfit 0 verified with '213 cm'")
    elif char_name == 'Wulfnic':
        outfits = data.get('outfits', [])
        if outfits and '220 cm' not in outfits[0].get('description', ''):
            record_error("Wulfnic outfit 0 does not contain updated height '220 cm'")
        else:
            record_ok("Wulfnic outfit 0 verified with '220 cm'")

# 4. Personas
print("\n--- 4. User Personas ---")
for char_name, path in PERSONA_FILES.items():
    if not os.path.exists(path):
        record_error(f"Persona file not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    desc = data.get('description', '')
    lines = desc.split('\n')
    line0 = lines[0] if lines else ''

    # Line 0 bracket rule
    if not (line0.startswith('[') and line0.endswith(']')):
        record_error(f"{char_name} persona line 0 violates single-line bracket rule")

    expected_height = CANONICAL_HEIGHTS[char_name]['full']
    if expected_height not in line0:
        record_error(f"{char_name} persona line 0 missing '{expected_height}'")
    else:
        record_ok(f"{char_name} persona bracket has '{expected_height}'")

    if 'PROPORTIONS & SCALE' not in desc:
        record_error(f"{char_name} persona missing PROPORTIONS & SCALE block")
    else:
        record_ok(f"{char_name} persona has PROPORTIONS & SCALE block")

    if '—' in desc:
        record_error(f"{char_name} persona contains forbidden em-dash ('—')")

# 5. Lorebooks Primary & Optimized
print("\n--- 5. Primary and Optimized Lorebooks ---")
for lb_path, lb_name in [(LOREBOOK_PRIMARY, "FINAL Primary Lorebook"), (LOREBOOK_OPTIMIZED, "Optimized Primary Lorebook")]:
    if not os.path.exists(lb_path):
        record_error(f"{lb_name} not found at {lb_path}")
        continue
    with open(lb_path, 'r', encoding='utf-8') as f:
        lb_data = json.load(f)

    # Parity check inside file
    if lb_data.get('entries') != lb_data.get('lexicon'):
        record_error(f"{lb_name} internal parity failure: entries != lexicon")
    else:
        record_ok(f"{lb_name} internal parity confirmed: entries == lexicon (100% identical)")

    # Target entries validation
    found_ids = set()
    for entry in lb_data.get('entries', []):
        eid = entry.get('entry_id')
        if eid in TARGET_ENTRY_IDS:
            char_name = TARGET_ENTRY_IDS[eid]
            found_ids.add(eid)
            content = entry.get('content', '')
            lines = content.split('\n')
            line0 = lines[0] if lines else ''

            # Bracket check
            if not (line0.startswith('[') and line0.endswith(']')):
                record_error(f"{lb_name} entry {char_name} ({eid}) line 0 violates bracket rule")

            expected_height = CANONICAL_HEIGHTS[char_name]['full']
            if expected_height not in line0:
                record_error(f"{lb_name} entry {char_name} ({eid}) line 0 missing '{expected_height}'")
            else:
                record_ok(f"{lb_name} entry {char_name} has canonical height in bracket")

            if 'PROPORTIONS & SCALE' not in content:
                record_error(f"{lb_name} entry {char_name} ({eid}) missing PROPORTIONS & SCALE block")
            else:
                record_ok(f"{lb_name} entry {char_name} has PROPORTIONS & SCALE block")

            if '—' in content:
                record_error(f"{lb_name} entry {char_name} ({eid}) contains forbidden em-dash ('—')")

    if len(found_ids) != len(TARGET_ENTRY_IDS):
        record_error(f"{lb_name} missing target entries! Found {len(found_ids)} of {len(TARGET_ENTRY_IDS)}")

# 6. Mirror Parity Between Primary and Optimized
print("\n--- 6. Byte-for-Byte Mirror Parity ---")
if not filecmp.cmp(LOREBOOK_PRIMARY, LOREBOOK_OPTIMIZED, shallow=False):
    record_error(f"Mirror mismatch: {LOREBOOK_PRIMARY} != {LOREBOOK_OPTIMIZED}")
else:
    record_ok(f"Mirror verified: {LOREBOOK_PRIMARY} is byte-for-byte identical to {LOREBOOK_OPTIMIZED}")

# 7. Summary
print("\n=== Verification Summary ===")
if errors:
    print(f"FAILED: {len(errors)} error(s) detected.")
    sys.exit(1)
else:
    print("SUCCESS: All Milestone 1 Canonical Heights & Proportions checks passed flawlessly with exit code 0.")
    sys.exit(0)
