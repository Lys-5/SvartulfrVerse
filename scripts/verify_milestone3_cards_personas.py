"""Independent Verification Suite for Milestone 3: Character Cards & Personas Synchronization
Author: worker_m3
Date: 2026-11-02

Performs rigorous multi-contract validation across all 4 target files:
- FINAL/Jasper_Douglas_Bloodmoon_card.json
- FINAL/personas/Jasper_Persona.json
- FINAL/personas/Alyssa_Persona.json
- ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json

Checks:
1. Valid JSON syntax in all 4 files.
2. Single-line line 1 bracket block in all 4 files.
3. Level 19 in Jasper card (residual Level 3 bug fixed).
4. Registered Hunter JDB-555 and St. Brugge in Jasper files.
5. Certified Guild Healer ADB-555 and St. Brugge in Alyssa files; exactly 0 occurrences of 'Novice Healing Mage'.
6. 0 em-dashes ('—') across all 4 files.
7. 0 markdown bold asterisks in narrative fields.
8. Positive framing for demi-human ears (no negative constraints in narrative).
9. Signature items & personality alignment in Alyssa legacy card.
10. World Clock 2024 consistency.
"""

import json
import os
import re
import sys

TARGET_FILES = {
    'jasper_card': 'FINAL/Jasper_Douglas_Bloodmoon_card.json',
    'jasper_persona': 'FINAL/personas/Jasper_Persona.json',
    'alyssa_persona': 'FINAL/personas/Alyssa_Persona.json',
    'alyssa_card': 'ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json'
}


def test_1_valid_json_syntax():
    print("\n--- Test 1: Valid JSON Syntax ---")
    for key, path in TARGET_FILES.items():
        assert os.path.exists(path), f"File not found: {path}"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        assert isinstance(data, dict), f"{path}: Root must be a JSON object"
        assert 'description' in data, f"{path}: Missing 'description' field"
        assert 'name' in data, f"{path}: Missing 'name' field"
        print(f"PASS: {path} is valid JSON ({len(data)} keys)")


def test_2_single_line_line1_bracket_block():
    print("\n--- Test 2: Single-Line Line 1 Bracket Block [NAME: ...] ---")
    for key, path in TARGET_FILES.items():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        desc = data['description']
        first_block = desc.split('\n\n')[0]
        
        assert first_block.startswith('['), f"{path}: Line 1 block must start with '['"
        assert first_block.endswith(']'), f"{path}: Line 1 block must end with ']'"
        assert '\n' not in first_block, f"{path}: Line 1 block must occupy exactly ONE single continuous line (no embedded newlines)!"
        assert first_block.startswith('[NAME: '), f"{path}: Line 1 block must start with '[NAME: '"
        
        # Verify required tags per character
        if 'jasper' in key:
            assert 'EDUCATION: St. Brugge Private Academy alumnus;' in first_block, f"{path}: Missing St. Brugge education tag"
            assert 'Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555)' in first_block, f"{path}: Missing Registered Guild Hunter tag"
            assert 'radiant black sun birthmark on right hip (Mark of Sol)' in first_block, f"{path}: Missing Mark of Sol birthmark"
            assert 'lazy single caramel wolf ears that flick when amused' in first_block, f"{path}: Missing positive framed wolf ears"
        elif 'alyssa' in key:
            assert 'EDUCATION: St. Brugge Private Academy alumnus;' in first_block, f"{path}: Missing St. Brugge education tag"
            assert 'Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555)' in first_block, f"{path}: Missing Certified Guild Healer tag"
            assert 'single pair of lupine ears nestled naturally in waves' in first_block, f"{path}: Missing positive framed lupine ears"
            assert 'Novice Healing Mage' not in first_block, f"{path}: Residual 'Novice Healing Mage' found in Line 1 block!"
            
        print(f"PASS: {path} line 1 bracket block is single-line with all mandatory credentials ({len(first_block)} chars)")


def test_3_level_19_in_jasper_card_and_all_files():
    print("\n--- Test 3: RPG Stats Level 19 Alignment ---")
    jasper_card_path = TARGET_FILES['jasper_card']
    with open(jasper_card_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    desc = data['description']
    
    assert '[LEVEL: 3;' not in desc, f"{jasper_card_path}: Residual [LEVEL: 3; bug still present!"
    assert '[LEVEL: 19;' in desc, f"{jasper_card_path}: Missing [LEVEL: 19; in RPG stats!"
    print(f"PASS: {jasper_card_path} correctly aligned to [LEVEL: 19;")
    
    # Verify all 4 files have LEVEL: 19
    for key, path in TARGET_FILES.items():
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        assert '[LEVEL: 19;' in d['description'], f"{path}: Expected [LEVEL: 19; in RPG stats"
        print(f"PASS: {path} has [LEVEL: 19;")


def test_4_jasper_emergent_lore_synchronization():
    print("\n--- Test 4: Jasper Emergent Lore Synchronization ---")
    jasper_files = [TARGET_FILES['jasper_card'], TARGET_FILES['jasper_persona']]
    for path in jasper_files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        desc = data['description']
        
        # Check Backstory
        assert 'St. Brugge Private Academy' in desc, f"{path}: Missing St. Brugge Private Academy in BACKSTORY"
        assert 'Father Revazhael' in desc, f"{path}: Missing Father Revazhael in BACKSTORY"
        assert 'translating ancient abyssal ciphers' in desc, f"{path}: Missing runic translation at adjoining desk in BACKSTORY"
        assert 'attune the individual resonance of Alyssa\'s enchanted cylinders' in desc, f"{path}: Missing cylinder resonance attunement in BACKSTORY"
        assert 'Abyssal Armor' in desc, f"{path}: Missing Abyssal Armor in BACKSTORY"
        assert 'Mor\'gath xul vrak\'thar, kor\'eth zaram' in desc, f"{path}: Missing Abyssal Armor summoning formula in BACKSTORY"
        assert 'Grade A Guild Hunter (Hunter ID JDB-555, Vanguard Tech & Infiltrator)' in desc, f"{path}: Missing Grade A Guild Hunter in BACKSTORY"
        assert 'Dragon Glass Katana' in desc, f"{path}: Missing Dragon Glass Katana in BACKSTORY"
        
        # Check Family & Pack
        assert 'Beyond their telepathic and empathic twin bond' in desc, f"{path}: Missing twin craft collaboration in FAMILY & PACK"
        assert 'Acoustic and Sound Engineering training to calibrate the harmonic resonance frequencies' in desc, f"{path}: Missing Acoustic resonance calibration in FAMILY & PACK"
        assert 'refuses to be corralled into Greek Row fraternity politics' in desc, f"{path}: Missing KSA refusal in FAMILY & PACK"
        
        # Check Voice & Behavior
        assert 'putting three aggressive Kappa Sigma Alpha brothers to flight at the Welcome Fest' in desc, f"{path}: Missing Welcome Fest KSA intimidation in VOICE & BEHAVIOR"
        assert 'auditing its firewall to ensure her security' in desc, f"{path}: Missing TIT router audit in VOICE & BEHAVIOR"
        
        print(f"PASS: {path} fully synchronized with Jasper emergent lore (Backstory, Family & Pack, Voice & Behavior)")


def test_5_alyssa_emergent_lore_synchronization():
    print("\n--- Test 5: Alyssa Emergent Lore Synchronization & 0 Novice Mage ---")
    alyssa_files = [TARGET_FILES['alyssa_persona'], TARGET_FILES['alyssa_card']]
    for path in alyssa_files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            raw = json.dumps(data, ensure_ascii=False)
        
        # Check 0 occurrences of 'Novice Healing Mage' across the entire file
        assert 'Novice Healing Mage' not in raw, f"{path}: Violation - 'Novice Healing Mage' still present in file!"
        
        desc = data['description']
        assert 'St. Brugge Private Academy' in desc, f"{path}: Missing St. Brugge Private Academy in BACKSTORY"
        assert 'Father Revazhael' in desc, f"{path}: Missing Father Revazhael in BACKSTORY"
        assert 'applied runic crystallography' in desc, f"{path}: Missing applied runic crystallography in BACKSTORY"
        assert 'intricate crafting of enchanted cylinders' in desc, f"{path}: Missing enchanted cylinders crafting in BACKSTORY"
        assert 'theoretical foundations of Abyssal magic' in desc, f"{path}: Missing Abyssal magic theory in BACKSTORY"
        assert 'Absolute Pacifist Vow' in desc, f"{path}: Missing Absolute Pacifist Vow in BACKSTORY"
        assert 'Certified Guild Healer & Field Medic' in desc, f"{path}: Missing Certified Guild Healer title in BACKSTORY"
        assert 'ADB-555' in desc, f"{path}: Missing Hunter ID ADB-555 in BACKSTORY"
        
        print(f"PASS: {path} fully synchronized with Alyssa emergent lore (0 'Novice Healing Mage', St. Brugge, Revazhael, ADB-555)")


def test_6_alyssa_signature_items_and_personality():
    print("\n--- Test 6: Alyssa Signature Items & Personality (Legacy Card) ---")
    path = TARGET_FILES['alyssa_card']
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    desc = data['description']
    # Check Signature items
    assert 'Enchanted Cylinders: Specialized tactical magitech crystal cylinders handcrafted by Alyssa' in desc, f"{path}: Missing updated Enchanted Cylinders in SIGNATURE ITEMS"
    assert 'miniature colored flashlights' in desc, f"{path}: Missing flashlight description in Enchanted Cylinders"
    assert 'calibrate the spell matrix to the unique magical resonance of the specific hunter' in desc, f"{path}: Missing individual resonance tuning in Enchanted Cylinders"
    assert 'alchemical glassware (distillation flasks, ground-joint condensers, and alembics)' in desc, f"{path}: Missing lab glassware in Bag of Holding"
    assert 'estate maintained by the spirit butler Kobal' in desc, f"{path}: Missing Kobal in Dimensional Refuge Key"
    
    # Check Personality
    pers = data['personality']
    assert 'Certified Guild Healer & Field Medic (Rank A)' in pers, f"{path}: Missing Certified Guild Healer in personality"
    assert 'Novice Healing Mage' not in pers, f"{path}: Residual Novice Healing Mage in personality"
    
    print(f"PASS: {path} signature items and personality correctly updated and verified")


def test_7_zero_em_dashes():
    print("\n--- Test 7: Formatting Discipline (Zero Em-Dashes '—') ---")
    for key, path in TARGET_FILES.items():
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert '—' not in content, f"{path}: VIOLATION - em-dash ('—') found in file!"
        print(f"PASS: {path} has exactly 0 em-dashes")


def test_8_zero_markdown_bold_in_narrative():
    print("\n--- Test 8: Formatting Discipline (Zero Markdown Bold '**' in Narrative) ---")
    narrative_fields = ['description', 'first_mes', 'personality', 'scenario']
    for key, path in TARGET_FILES.items():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for field in narrative_fields:
            if field in data and isinstance(data[field], str):
                assert '**' not in data[field], f"{path}: Markdown bold '**' found in '{field}'!"
        print(f"PASS: {path} narrative fields have zero markdown bold ('**')")


def test_9_positive_framing_demi_human_ears():
    print("\n--- Test 9: Positive Framing for Demi-Human Anatomy ---")
    # Verify narrative descriptions do not contain negative framing like "(no human ears)"
    prohibited_phrases = [
        '(no human ears)',
        'no human ears',
        'senza orecchie umane',
        'prive di orecchie umane',
        'lacking human ears',
        'without human ears'
    ]
    
    for key, path in TARGET_FILES.items():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check narrative fields (excluding post_history_instructions which contains the instruction text itself)
        fields_to_check = ['description', 'visual_description', 'personality', 'first_mes']
        for field in fields_to_check:
            if field in data and isinstance(data[field], str):
                text_lower = data[field].lower()
                for phrase in prohibited_phrases:
                    assert phrase not in text_lower, f"{path}: Negative framing phrase '{phrase}' found in '{field}'!"
                    
        # Check that post_history_instructions in cards contains the positive framing rule
        if 'post_history_instructions' in data:
            phi = data['post_history_instructions']
            assert 'treat single animal ears as the natural norm' in phi, f"{path}: Missing positive framing instruction in post_history_instructions"
            
        print(f"PASS: {path} complies 100% with positive framing rules")


def test_10_world_clock_2024():
    print("\n--- Test 10: World Clock 2024 Alignment ---")
    for key, path in TARGET_FILES.items():
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        desc = data['description']
        assert 'Born April 22, 2005' in desc, f"{path}: Missing birth date April 22, 2005"
        assert 'AGE: 19' in desc, f"{path}: Missing AGE: 19"
        print(f"PASS: {path} adheres to World Clock 2024 (Age 19, Born April 22, 2005)")


def main():
    print("=" * 70)
    print("RUNNING MILESTONE 3 VERIFICATION SUITE")
    print("=" * 70)
    
    test_1_valid_json_syntax()
    test_2_single_line_line1_bracket_block()
    test_3_level_19_in_jasper_card_and_all_files()
    test_4_jasper_emergent_lore_synchronization()
    test_5_alyssa_emergent_lore_synchronization()
    test_6_alyssa_signature_items_and_personality()
    test_7_zero_em_dashes()
    test_8_zero_markdown_bold_in_narrative()
    test_9_positive_framing_demi_human_ears()
    test_10_world_clock_2024()
    
    print("\n" + "=" * 70)
    print("ALL 10 VERIFICATION TESTS PASSED WITH 0 FAILURES")
    print("=" * 70)
    sys.exit(0)


if __name__ == '__main__':
    main()
