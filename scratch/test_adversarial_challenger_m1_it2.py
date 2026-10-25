#!/usr/bin/env python3
"""
scratch/test_adversarial_challenger_m1_it2.py
Empirical Challenger Test Harness for Milestone 1 Iteration 2:
Adversarial stress testing of normalize_wyvern_regex_pattern and detect_duplicate_surnames.
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Add repo root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.verify_npc_schema_contract import (
    normalize_wyvern_regex_pattern,
    detect_duplicate_surnames,
    compile_wyvern_avatar_regex,
)

def run_tests():
    print("=" * 70)
    print("EMPIRICAL CHALLENGER ADVERSARIAL STRESS TEST SUITE")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # 1. Escaped Characters & Whitespace Normalization
    # --------------------------------------------------------------------------
    print("\n--- 1. Testing Escaped Characters & Whitespace Normalization ---")
    norm_cases = [
        # (input_pattern, expected_substring_or_match, description)
        (r"Alpha\ Rivers\ Rivers", "Alpha Rivers Rivers", "Backslash-escaped spaces"),
        (r"Alpha\\ Rivers\\ Rivers", "Alpha Rivers Rivers", "Double-backslash escaped spaces"),
        (r"Alpha\   Rivers\ \ \ Rivers", "Alpha Rivers Rivers", "Multiple escaped spaces"),
        (r"Alpha\s+Rivers\s*Rivers", "Alpha Rivers Rivers", "Regex whitespace tokens \\s+ and \\s*"),
        (r"Alpha\s*Rivers\s+Rivers", "Alpha Rivers Rivers", "Mixed \\s* and \\s+"),
        ("Alpha\t\tRivers\n\nRivers", "Alpha Rivers Rivers", "Literal tabs and newlines"),
        (r"Mr\.\ Rogers\ Rogers", "Mr. Rogers Rogers", "Escaped period"),
        (r"Jean\-Luc\ Virtuoso\ Virtuoso", "Jean-Luc Virtuoso Virtuoso", "Escaped hyphen"),
        (r"O\'Connor\ O\'Connor", "O'Connor O'Connor", "Escaped apostrophe"),
        (r"\"Danny\"\ Boone\ Boone", '"Danny" Boone Boone', "Escaped quotes"),
        (r"O['‘’ʼ‛′]Connor O['‘’ʼ‛′]Connor", "O'Connor O'Connor", "Quote character class to apostrophe"),
        (r"Sanchez[-‐‑‒–—−]Rogers Sanchez[-‐‑‒–—−]Rogers", "Sanchez-Rogers Sanchez-Rogers", "Hyphen character class to hyphen"),
        (r"(?:^|\n)\s*(?:Erik\ Douglas)\s*:", "(?:^|\\n) (?:Erik Douglas) :", "Full Wyvern regex envelope"),
        (None, "", "None pattern returns empty string"),
        ("", "", "Empty pattern returns empty string"),
        ("   ", "", "Whitespace-only pattern returns empty string"),
    ]

    for raw, expected, desc in norm_cases:
        res = normalize_wyvern_regex_pattern(raw)
        if expected in res or (expected == "" and res == ""):
            print(f"  [PASS] {desc}: {repr(raw)[:40]} -> {repr(res)[:40]}")
        else:
            print(f"  [FAIL] {desc}: expected {repr(expected)} in {repr(res)}")
            assert False, f"Failed: {desc}"

    # --------------------------------------------------------------------------
    # 2. Duplicate Surname Detection on Clean Patterns (Zero False Positives)
    # --------------------------------------------------------------------------
    print("\n--- 2. Testing Zero False Positives on Clean Patterns ---")
    clean_cases = [
        (r"(?:^|\n)\s*(?:Hugh\ Rivers|Alpha\ Rivers|The\ Mountain\ Sovereign)\s*:", "Rivers", "Clean Rivers"),
        (r"(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers|Dominic)\s*:", "Rogers", "Clean Rogers"),
        (r"(?:^|\n)\s*(?:Daniel\ \"Danny\"\ Boone|Danny\ Boone|Daniel)\s*:", "Boone", "Clean Boone"),
        (r"(?:^|\n)\s*(?:Harrison\ Black|Harry\ Black|Councilman\ Black)\s*:", "Black", "Clean Black"),
        (r"(?:^|\n)\s*(?:Marcus\ O['‘’ʼ‛′]Connor|Oldtown|Marcus)\s*:", "O'Connor", "Clean O'Connor"),
        (r"(?:^|\n)\s*(?:Jean[-‐‑‒–—−]Luc\ Virtuoso|Master\ Virtuoso)\s*:", "Virtuoso", "Clean Virtuoso with hyphenated first name"),
        (r"(?:^|\n)\s*(?:Roman\ Blackwood|Alpha\ Rivers|Douglas\ Pack)\s*:", "Blackwood", "Compound valid names with broad words"),
        (r"(?:^|\n)\s*(?:Wulfnic\ Báleygr\ Bloodmoon|Jarl\ of\ Svartúlfr)\s*:", "Bloodmoon", "Accented Norse name"),
        (r"(?:^|\n)\s*(?:Erik\ Ulfr\ Douglas|Lord\ Douglas|The\ Old\ Wolf)\s*:", "Douglas", "Multi-title clean pattern"),
        (r"(?:^|\n)\s*(?:Bruce)\s*:", None, "Single word name Bruce"),
    ]

    for pat, ln, desc in clean_cases:
        dupes = detect_duplicate_surnames(pat, ln)
        if len(dupes) == 0:
            print(f"  [PASS] Zero false positives: {desc} -> {dupes}")
        else:
            print(f"  [FAIL] False positive on {desc}: detected {dupes}")
            assert False, f"False positive: {desc}"

    # Also test cleanly compiled patterns from compile_wyvern_avatar_regex
    clean_npcs = [
        {"first_name": "Erik", "middle_names": ["Ulfr"], "last_name": "Douglas", "nicknames": ["The Old Wolf"], "titles": ["Alpha"]},
        {"first_name": "Scarlett", "middle_names": [], "last_name": "Rose", "nicknames": ["Red"], "titles": []},
        {"first_name": "Sierra", "middle_names": [], "last_name": "Cruz", "nicknames": ["Rainbow Lamia"], "titles": []},
        {"first_name": "Jean-Luc", "middle_names": [], "last_name": "Virtuoso", "nicknames": ["The Human Telepath"], "titles": ["Master"]},
        {"first_name": "Marcus", "middle_names": [], "last_name": "O'Connor", "nicknames": ["Mark"], "titles": ["Officer"]},
        {"first_name": "Mackenzie", "middle_names": [], "last_name": "Sanchez-Rogers", "nicknames": ["Mac"], "titles": []},
        {"first_name": "Wulfnic", "middle_names": ["Báleygr"], "last_name": "Bloodmoon", "nicknames": ["The One-Eyed Wolf"], "titles": ["Jarl"]},
        {"first_name": "Bruce", "middle_names": [], "last_name": None, "nicknames": [], "titles": ["President"]},
        {"first_name": "Adrian", "middle_names": [], "last_name": None, "nicknames": ["Ade"], "titles": []},
        {"first_name": "Alistair", "middle_names": ["Ambrose"], "last_name": "DeVille", "nicknames": ["The Collector"], "titles": ["Mr."]},
    ]
    for npc in clean_npcs:
        pat = compile_wyvern_avatar_regex(npc)
        dupes = detect_duplicate_surnames(pat, npc.get("last_name"))
        fn = npc["first_name"]
        ln = npc.get("last_name") or ""
        assert len(dupes) == 0, f"Compiled pattern for {fn} {ln} produced false positive dupes: {dupes}"
        print(f"  [PASS] Compiled Module 93312 regex for '{fn} {ln}' -> 0 false positives")

    # --------------------------------------------------------------------------
    # 3. Duplicate Surname Detection on Defective / Corrupt Patterns
    # --------------------------------------------------------------------------
    print("\n--- 3. Testing Detection on Defective Patterns ---")
    defective_cases = [
        (r"(?:^|\n)\s*(?:Alpha\ Rivers\ Rivers|Alpha\ Rivers)\s*:", "Rivers", "Rivers Rivers", "Legacy escaped Rivers"),
        (r"(?:^|\n)\s*(?:Mr\.\ Rogers\ Rogers|Mr\.\ Rogers)\s*:", "Rogers", "Rogers Rogers", "Legacy escaped Rogers"),
        (r"(?:^|\n)\s*(?:Boone\ Boone|Boone)\s*:", "Boone", "Boone Boone", "Legacy escaped Boone"),
        (r"(?:^|\n)\s*(?:Councilman\ Black\ Black|Councilman\ Black)\s*:", "Black", "Black Black", "Legacy escaped Black"),
        (r"(?:^|\n)\s*(?:Mark\ O'Connor\ O'Connor|Mark\ O'Connor)\s*:", "O'Connor", "O'Connor O'Connor", "Legacy escaped O'Connor"),
        (r"(?:^|\n)\s*(?:Mark\ O['‘’ʼ‛′]Connor\ O['‘’ʼ‛′]Connor)\s*:", "O'Connor", "O'Connor O'Connor", "Quote character class O'Connor"),
        (r"(?:^|\n)\s*(?:Sanchez[-‐‑‒–—−]Rogers\ Sanchez[-‐‑‒–—−]Rogers)\s*:", "Sanchez-Rogers", "Sanchez-Rogers Sanchez-Rogers", "Hyphen character class Sanchez-Rogers"),
        (r"(?:^|\n)\s*(?:Mrs\ Virtuoso\ Virtuoso|Mrs\ Virtuoso)\s*:", "Virtuoso", "Virtuoso Virtuoso", "Legacy escaped Virtuoso"),
        (r"(?:^|\n)\s*(?:Nurse\ Cirillo\ Cirillo)\s*:", "Cirillo", "Cirillo Cirillo", "Legacy escaped Cirillo"),
        (r"(?:^|\n)\s*(?:Mr\.\ DeVille\ DeVille)\s*:", "DeVille", "DeVille DeVille", "Legacy escaped DeVille"),
        (r"(?:^|\n)\s*(?:rat\ Rat)\s*:", "Rat", "Rat Rat", "Legacy escaped Rat"),
        (r"(?:^|\n)\s*(?:Professor\ Weiss\ Weiss)\s*:", "Weiss", "Weiss Weiss", "Legacy escaped Weiss"),
        (r"(?:^|\n)\s*(?:Major\ Purcell\ Purcell)\s*:", "Purcell", "Purcell Purcell", "Legacy escaped Purcell"),
        (r"(?:^|\n)\s*(?:Coach\ Coso\ Coso)\s*:", "Coso", "Coso Coso", "Legacy escaped Coso"),
        (r"(?:^|\n)\s*(?:Bishop\ Bishop)\s*:", "Bishop", "Bishop Bishop", "Legacy escaped Bishop"),
        (r"(?:^|\n)\s*(?:Lady\ Duskwood\ Duskwood)\s*:", "Duskwood", "Duskwood Duskwood", "Legacy escaped Duskwood"),
        (r"(?:^|\n)\s*(?:Huck\ Beaumont\ Beaumont)\s*:", "Beaumont", "Beaumont Beaumont", "Legacy escaped Beaumont"),
        (r"(?:^|\n)\s*(?:Federico\ Savini\ Savini)\s*:", "Savini", "Savini Savini", "Legacy escaped Savini"),
        (r"(?:^|\n)\s*(?:ms\ davies\ Davies)\s*:", "Davies", "Davies Davies", "Legacy escaped Davies"),
        (r"(?:^|\n)\s*(?:Professor\ Christiansen\ Christiansen)\s*:", "Christiansen", "Christiansen Christiansen", "Legacy escaped Christiansen"),
        (r"(?:^|\n)\s*(?:Professor\ Moreau\ Moreau)\s*:", "Moreau", "Moreau Moreau", "Legacy escaped Moreau"),
    ]

    for pat, ln, expected, desc in defective_cases:
        dupes = detect_duplicate_surnames(pat, ln)
        matched = any(expected.lower() in d.lower() for d in dupes)
        if matched:
            print(f"  [PASS] {desc}: detected '{expected}' in {pat[:45]}...")
        else:
            print(f"  [FAIL] {desc}: failed to detect '{expected}' in: {pat} -> got {dupes}")
            assert False, f"Defect not detected: {expected}"

    # --------------------------------------------------------------------------
    # 4. Stress Testing Boundary & Extreme Edge Cases
    # --------------------------------------------------------------------------
    print("\n--- 4. Stress Testing Boundary & Extreme Edge Cases ---")

    # Triple duplicate: "Rivers Rivers Rivers"
    pat_triple = r"(?:^|\n)\s*(?:Alpha Rivers Rivers Rivers)\s*:"
    dupes_triple = detect_duplicate_surnames(pat_triple, "Rivers")
    print(f"  [RESULT] Triple repetition 'Rivers Rivers Rivers' -> {dupes_triple}")
    assert len(dupes_triple) > 0, "Triple repetition missed"

    # Multi-word surname: "Van Der Bilt Van Der Bilt"
    pat_multi_part = r"(?:^|\n)\s*(?:Van Der Bilt Van Der Bilt)\s*:"
    dupes_multi_part = detect_duplicate_surnames(pat_multi_part, "Van Der Bilt")
    print(f"  [RESULT] Multi-part surname 'Van Der Bilt Van Der Bilt' -> {dupes_multi_part}")
    assert "Van Der Bilt Van Der Bilt" in dupes_multi_part, "Multi-part surname dupe missed"

    # Accented surname with explicit last_name: "Báleygr Báleygr"
    pat_nordic = r"(?:^|\n)\s*(?:Wulfnic Báleygr Báleygr)\s*:"
    dupes_nordic_explicit = detect_duplicate_surnames(pat_nordic, "Báleygr")
    print(f"  [RESULT] Accented surname with last_name='Báleygr' -> {dupes_nordic_explicit}")
    assert len(dupes_nordic_explicit) > 0, "Accented surname with last_name missed"

    # Accented surname WITHOUT explicit last_name: "Báleygr Báleygr"
    dupes_nordic_implicit = detect_duplicate_surnames(pat_nordic, None)
    print(f"  [RESULT] Accented surname WITHOUT explicit last_name -> {dupes_nordic_implicit}")
    # Note: this is an empirical property of the generic ASCII-only [A-Za-z] regex

    # Case sensitivity check: "rivers RIVERS"
    pat_case = r"(?:^|\n)\s*(?:Alpha rivers RIVERS)\s*:"
    dupes_case = detect_duplicate_surnames(pat_case, "Rivers")
    print(f"  [RESULT] Mixed case 'rivers RIVERS' -> {dupes_case}")
    assert len(dupes_case) > 0, "Mixed case duplicate missed"

    # Punctuation immediately adjacent: "O'Connor, O'Connor:"
    pat_punct = r"(?:^|\n)\s*(?:O'Connor, O'Connor)\s*:"
    dupes_punct = detect_duplicate_surnames(pat_punct, "O'Connor")
    print(f"  [RESULT] Comma-separated 'O'Connor, O'Connor' -> {dupes_punct}")

    print("\n" + "=" * 70)
    print("ALL EMPIRICAL CHALLENGE TESTS COMPLETED")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
