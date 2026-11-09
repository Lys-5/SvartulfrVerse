"""Independent Verification Suite for Milestone 2: Standalone Lorebooks Emergent Lore Integration
Author: worker_m2
Date: 2026-11-02

Performs rigorous multi-contract validation:
1. Byte-for-byte identity: entries == lexicon on all modified lorebooks.
2. Formatting discipline: 0 em-dashes (—), 0 {{age}} macros.
3. Umbrella keyword policy: 0 broad keys in activation keys for all NPC entries.
4. Schema & Identity: presence, schema correctness, and canonical attributes of all new/updated entries.
5. Mirror synchronization: byte-for-byte match between FINAL/ and lorebooks/optimized/.
6. Positive framing: demi-human anatomy checks.
"""

import json
import os
import sys

BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

MODIFIED_FILES = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'lorebooks/optimized/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'lorebooks/optimized/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Lorebook_III.json',
    'lorebooks/optimized/Svartulfr_Lorebook_III.json',
    'lorebooks/optimized/Svartulfr_Location.json',
    'FINAL/Svartulfr_NPC_Secondary.json',
    'lorebooks/optimized/Svartulfr_NPC_Secondary.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'lorebooks/optimized/Svartulfr_NPC_Primary.json'
]

PAIRED_MIRRORS = [
    ('FINAL/Svartulfr_Lorebook_I.json', 'lorebooks/optimized/Svartulfr_Lorebook_I.json'),
    ('FINAL/Svartulfr_Lorebook_II.json', 'lorebooks/optimized/Svartulfr_Lorebook_II.json'),
    ('FINAL/Svartulfr_Lorebook_III.json', 'lorebooks/optimized/Svartulfr_Lorebook_III.json'),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'lorebooks/optimized/Svartulfr_NPC_Secondary.json'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'lorebooks/optimized/Svartulfr_NPC_Primary.json')
]

def test_entries_lexicon_parity():
    print("\n--- Test 1: entries == lexicon Byte-for-Byte Parity ---")
    for path in MODIFIED_FILES:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        entries = d.get('entries', [])
        lexicon = d.get('lexicon', [])
        assert len(entries) == len(lexicon), f"{path}: length mismatch entries({len(entries)}) vs lexicon({len(lexicon)})"
        assert entries == lexicon, f"{path}: byte-for-byte mismatch between entries and lexicon!"
        print(f"PASS: {path} (total entries = {len(entries)})")

def test_formatting_discipline():
    print("\n--- Test 2: Formatting Discipline (0 em-dashes, 0 {{age}} macros) ---")
    target_ids = {
        'lb1_concept_applied_runic_crystallography',
        'lb1_magic_abyssal_magic_distinction',
        'lb2_item_enchanted_resonant_cylinders',
        'succ_lb3_st_brugge_academy',
        'ulTwlYo2jqObA7l_bFoa5',
        'loc_theta_iota_theta_suite_3',
        'jmh0MajEsRwrm4UYU14mY',
        'npc_larek_steeltooth',
        'alyssa_world_dossier_2b54a223',
        'Vcj4h2TL4Usola2A4OOl6'
    }
    for path in MODIFIED_FILES:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
            raw = json.dumps(d, ensure_ascii=False)
        assert '{{age}}' not in raw, f"VIOLATION: '{{{{age}}}}' macro found in {path}!"
        for e in d['entries']:
            eid = e.get('entry_id') or e.get('id')
            if eid in target_ids:
                s = json.dumps(e, ensure_ascii=False)
                assert '—' not in s, f"VIOLATION: em-dash ('—') found in target entry {eid} in {path}!"
        print(f"PASS: {path} has 0 {{{{age}}}} macros, and all milestone target entries have 0 em-dashes.")

def test_broad_keys_on_npcs():
    print("\n--- Test 3: Umbrella Keyword Discipline on NPC Entries ---")
    npc_files = [
        'FINAL/Svartulfr_NPC_Secondary.json',
        'lorebooks/optimized/Svartulfr_NPC_Secondary.json',
        'FINAL/Svartulfr_NPC_Primary.json',
        'lorebooks/optimized/Svartulfr_NPC_Primary.json'
    ]
    for path in npc_files:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for idx, entry in enumerate(d['entries']):
            keys = [k.lower().strip() for k in entry.get('keys', [])]
            for bk in BROAD_KEYS:
                assert bk not in keys, f"VIOLATION in {path} entry #{idx} ({entry.get('name')}): broad key '{bk}' found in activation keys!"
        print(f"PASS: {path} has 0 broad keys across {len(d['entries'])} NPC entries.")

def test_entry_presence_and_integrity():
    print("\n--- Test 4: Presence and Integrity of New/Updated Entries ---")
    
    # Lorebook I
    lb1 = load_json('FINAL/Svartulfr_Lorebook_I.json')
    lb1_ids = {e.get('entry_id') or e.get('id'): e for e in lb1['entries']}
    assert 'lb1_concept_applied_runic_crystallography' in lb1_ids, "Missing lb1_concept_applied_runic_crystallography in Lorebook I"
    assert 'lb1_magic_abyssal_magic_distinction' in lb1_ids, "Missing lb1_magic_abyssal_magic_distinction in Lorebook I"
    print("PASS: Lorebook I contains applied runic crystallography and abyssal magic distinction entries.")
    
    # Lorebook II
    lb2 = load_json('FINAL/Svartulfr_Lorebook_II.json')
    lb2_ids = {e.get('entry_id') or e.get('id'): e for e in lb2['entries']}
    assert 'lb2_item_enchanted_resonant_cylinders' in lb2_ids, "Missing lb2_item_enchanted_resonant_cylinders in Lorebook II"
    e_cyl = lb2_ids['lb2_item_enchanted_resonant_cylinders']
    assert e_cyl['type'] == 'item', f"Expected type 'item', got {e_cyl['type']}"
    print("PASS: Lorebook II contains enchanted resonant cylinders (type: item).")
    
    # Lorebook III
    lb3 = load_json('FINAL/Svartulfr_Lorebook_III.json')
    lb3_ids = {e.get('entry_id') or e.get('id'): e for e in lb3['entries']}
    assert 'succ_lb3_st_brugge_academy' in lb3_ids, "Missing succ_lb3_st_brugge_academy in Lorebook III"
    print("PASS: Lorebook III contains St. Brugge Private Academy concept.")
    
    # Location
    loc = load_json('lorebooks/optimized/Svartulfr_Location.json')
    loc_ids = {e.get('entry_id') or e.get('id'): e for e in loc['entries']}
    assert 'ulTwlYo2jqObA7l_bFoa5' in loc_ids, "Missing ulTwlYo2jqObA7l_bFoa5 in Location"
    e_stb = loc_ids['ulTwlYo2jqObA7l_bFoa5']
    # Check that broad keys were purged from entry #51
    for bk in ['Seven Hills', 'Douglas', 'Blackwood', 'private academy']:
        assert bk not in e_stb['keys'], f"Broad key '{bk}' still present in St. Brugge location keys!"
    assert 'loc_theta_iota_theta_suite_3' in loc_ids, "Missing loc_theta_iota_theta_suite_3 in Location"
    print("PASS: Location lorebook has cleaned St. Brugge (purged broad keys) and added Theta Iota Theta: Suite 3.")
    
    # NPC Secondary
    npc_sec = load_json('FINAL/Svartulfr_NPC_Secondary.json')
    sec_ids = {e.get('entry_id') or e.get('id'): e for e in npc_sec['entries']}
    assert 'jmh0MajEsRwrm4UYU14mY' in sec_ids, "Missing Revazhael in NPC Secondary"
    rev = sec_ids['jmh0MajEsRwrm4UYU14mY']
    assert rev['name'] == 'Father Revazhael (Rev)', f"Unexpected name: {rev['name']}"
    expected_rev_keys = ['Father Revazhael', 'Padre Revazhael', 'Father Rev', 'Padre Rev', 'Revazhael', 'Rev']
    assert rev['keys'] == expected_rev_keys, f"Keys mismatch for Revazhael: {rev['keys']}"
    assert rev['type'] == 'npc', "Revazhael type is not 'npc'"
    
    assert 'npc_larek_steeltooth' in sec_ids, "Missing Larek Steeltooth in NPC Secondary"
    larek = sec_ids['npc_larek_steeltooth']
    assert larek['entry_id'] == 'npc_larek_steeltooth', f"Larek missing entry_id: {larek.get('entry_id')}"
    assert larek['name'] == 'Larek Steeltooth', f"Larek name mismatch: {larek.get('name')}"
    assert larek['type'] == 'npc', f"Larek type mismatch: {larek.get('type')}"
    assert larek['avatar'] == 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public', "Larek missing DCC placeholder avatar"
    print("PASS: NPC Secondary has Father Revazhael (reconciled JED+, updated keys) and Larek Steeltooth (valid schema).")
    
    # NPC Primary
    npc_prim = load_json('FINAL/Svartulfr_NPC_Primary.json')
    prim_ids = {e.get('entry_id') or e.get('id'): e for e in npc_prim['entries']}
    
    assert 'alyssa_world_dossier_2b54a223' in prim_ids, "Missing Alyssa dossier in NPC Primary"
    alyssa = prim_ids['alyssa_world_dossier_2b54a223']
    assert alyssa['selective'] == True, "Alyssa selective flag must be True"
    assert alyssa['secondary_keys'] == ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo'], "Alyssa secondary keys mismatch"
    assert alyssa['ignored_characters'] == ['_6exg3yPfe2eCDK4hTftkh'], "Alyssa ignored_characters mismatch"
    assert alyssa['ignored_personas'] == ['persona_1786335754946'], "Alyssa ignored_personas mismatch"
    assert "Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555)" in alyssa['content'], "Alyssa missing Certified Guild Healer title in Line 1"
    assert "St. Brugge Private Academy" in alyssa['content'], "Alyssa missing St. Brugge in content"
    assert "Suite 3" in alyssa['content'], "Alyssa missing Suite 3 in content"
    assert "Wolfy" in alyssa['content'], "Alyssa missing Wolfy in content"
    
    assert 'Vcj4h2TL4Usola2A4OOl6' in prim_ids, "Missing Jasper dossier in NPC Primary"
    jasper = prim_ids['Vcj4h2TL4Usola2A4OOl6']
    assert jasper['selective'] == True, "Jasper selective flag must be True"
    assert jasper['secondary_keys'] == ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo'], "Jasper secondary keys mismatch"
    assert jasper['ignored_characters'] == ['_t4J9aQNJM36cUKAP4wB4U'], "Jasper ignored_characters mismatch"
    assert jasper['ignored_personas'] == ['1792155173728'], "Jasper ignored_personas mismatch"
    assert "Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555)" in jasper['content'], "Jasper missing Registered Guild Hunter in Line 1"
    assert "St. Brugge Private Academy" in jasper['content'], "Jasper missing St. Brugge in content"
    assert "Welcome Fest" in jasper['content'], "Jasper missing Welcome Fest intimidation in content"
    assert "collarbone" not in jasper['content'].splitlines()[0], "Jasper Line 1 still contains outdated collarbone marking!"
    print("PASS: NPC Primary has fully enriched Alyssa and Jasper dossiers with strict persona protection.")

def test_mirror_synchronization():
    print("\n--- Test 5: FINAL/ vs lorebooks/optimized/ Mirror Synchronization ---")
    for p1, p2 in PAIRED_MIRRORS:
        with open(p1, 'r', encoding='utf-8') as f1, open(p2, 'r', encoding='utf-8') as f2:
            d1 = json.load(f1)
            d2 = json.load(f2)
        assert d1 == d2, f"VIOLATION: Mirror desynchronization between {p1} and {p2}!"
        print(f"PASS: {p1} == {p2} (100% synchronized)")

def test_positive_framing():
    print("\n--- Test 6: Positive Framing for Demi-Humans (Milestone Target Entries) ---")
    target_ids = {
        'lb1_concept_applied_runic_crystallography',
        'lb1_magic_abyssal_magic_distinction',
        'lb2_item_enchanted_resonant_cylinders',
        'succ_lb3_st_brugge_academy',
        'ulTwlYo2jqObA7l_bFoa5',
        'loc_theta_iota_theta_suite_3',
        'jmh0MajEsRwrm4UYU14mY',
        'npc_larek_steeltooth',
        'alyssa_world_dossier_2b54a223',
        'Vcj4h2TL4Usola2A4OOl6'
    }
    negative_patterns = ['no human ears', 'senza orecchie umane', 'privo di orecchie umane', 'prive di orecchie umane']
    for path in MODIFIED_FILES:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for e in d['entries']:
            eid = e.get('entry_id') or e.get('id')
            if eid in target_ids:
                s = json.dumps(e, ensure_ascii=False).lower()
                for pat in negative_patterns:
                    assert pat not in s, f"VIOLATION in {path} entry {eid}: Negative framing pattern '{pat}' found!"
    print("PASS: 0 negative framing patterns across all milestone target entries.")

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=== STARTING MILESTONE 2 INDEPENDENT VERIFICATION ===")
    test_entries_lexicon_parity()
    test_formatting_discipline()
    test_broad_keys_on_npcs()
    test_entry_presence_and_integrity()
    test_mirror_synchronization()
    test_positive_framing()
    print("\n=== ALL TESTS PASSED WITH 100% INTEGRITY ===")

if __name__ == '__main__':
    main()
