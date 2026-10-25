#!/usr/bin/env python3
"""
auditor_m2_1/adversarial_syntax_stress.py
Adversarial stress testing for Scenario and Chat VN Syntax and Formatting Rules.
"""

import re
import sys
import json
from pathlib import Path

# Import validator from worker's script
sys.path.insert(0, str(Path("e:/repository/SvartulfrVerse/scripts")))
from patch_welcome_day_scenario_and_chat import validate_formatting_discipline

def run_adversarial_tests():
    print("=== ADVERSARIAL STRESS TEST: VN SYNTAX & FORMATTING DISCIPLINE ===")
    
    valid_sample = '=>Narrator:\nIl sole splende.\n\n=>Erik:\n"Tutti pronti."'
    
    # Baseline test
    tags = validate_formatting_discipline(valid_sample, "Valid Sample")
    assert tags == ['Narrator', 'Erik']
    print("[PASS] Baseline valid sample accepted.")

    # 1. Attack: Injected Em-Dash
    attack_em = '=>Narrator:\nIl sole splende—ma fa freddo.\n\n=>Erik:\n"Tutti pronti."'
    try:
        validate_formatting_discipline(attack_em, "Attack Em-Dash")
        raise AssertionError("Failed to detect em-dash!")
    except ValueError as e:
        print(f"[PASS] Successfully blocked em-dash: {e}")

    # 2. Attack: Injected Asterisks
    attack_ast = '=>Narrator:\nIl sole splende. *cammina*\n\n=>Erik:\n"Tutti pronti."'
    try:
        validate_formatting_discipline(attack_ast, "Attack Asterisk")
        raise AssertionError("Failed to detect asterisk!")
    except ValueError as e:
        print(f"[PASS] Successfully blocked asterisk: {e}")

    # 3. Attack: Missing Narrator opening
    attack_no_narr = '=>Erik:\n"Tutti pronti."'
    try:
        validate_formatting_discipline(attack_no_narr, "Attack Missing Narrator")
        raise AssertionError("Failed to detect missing Narrator start!")
    except ValueError as e:
        print(f"[PASS] Successfully blocked missing Narrator: {e}")

    # 4. Attack: Plain un-prefixed speaker
    attack_plain = '=>Narrator:\nIl sole splende.\n\nErik:\n"Tutti pronti."'
    try:
        validate_formatting_discipline(attack_plain, "Attack Plain Speaker")
        raise AssertionError("Failed to detect plain speaker prefix!")
    except ValueError as e:
        print(f"[PASS] Successfully blocked plain speaker prefix: {e}")

    # 5. Attack: Full name un-prefixed speaker
    attack_fullname = '=>Narrator:\nIl sole splende.\n\nErik Ulfr Douglas:\n"Tutti pronti."'
    try:
        validate_formatting_discipline(attack_fullname, "Attack Fullname Plain Speaker")
        raise AssertionError("Failed to detect full name plain speaker prefix!")
    except ValueError as e:
        print(f"[PASS] Successfully blocked full name plain speaker prefix: {e}")

    # 6. Parse and test all beats using Wyvern's frontend regex
    print("\n--- Testing Beat Splitting Against Wyvern Module 93312/nC Specs ---")
    local_sc_path = Path("e:/repository/SvartulfrVerse/FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json")
    with open(local_sc_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 13 primary characters + Narrator
    CANONICAL_SPEAKERS = {
        'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Jasper',
        'Alyssa', 'Wulfnic', 'Zefir', 'Mackenzie', 'Finn', 'Sierra', 'Scarlett'
    }

    BEAT_SPLIT_REGEX = re.compile(r'(?:^|\n)\s*=>\s*([^:\n]{1,35}):\s*', flags=re.MULTILINE)

    for i, s in enumerate(data['premade_scenes']):
        text = s['scene_text']
        scene_id = s['id']
        matches = list(BEAT_SPLIT_REGEX.finditer(text))
        print(f"Scene {i} [{scene_id}]: found {len(matches)} beats")
        assert len(matches) > 0, f"Scene {i} has 0 beats"

        speakers = [m.group(1).strip() for m in matches]
        print(f"  Speakers: {speakers}")
        for spk in speakers:
            assert spk in CANONICAL_SPEAKERS, f"Scene {i} has non-canonical speaker: {spk}"

    print("[PASS] All beats across all scenes map 100% to canonical character names and Narrator!")
    print("\n=== ALL ADVERSARIAL STRESS TESTS PASSED CLEANLY ===")

if __name__ == '__main__':
    run_adversarial_tests()
