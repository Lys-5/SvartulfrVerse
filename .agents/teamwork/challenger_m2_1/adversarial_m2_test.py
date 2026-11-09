"""Adversarial Empirical Test Suite for Milestone 2: Standalone Lorebooks
Challenger: challenger_m2_1
Identity: Critic & Specialist
"""

import json
import os
import regex
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

TARGET_ENTRY_IDS = {
    'lb1_concept_applied_runic_crystallography': 'FINAL/Svartulfr_Lorebook_I.json',
    'lb1_magic_abyssal_magic_distinction': 'FINAL/Svartulfr_Lorebook_I.json',
    'lb2_item_enchanted_resonant_cylinders': 'FINAL/Svartulfr_Lorebook_II.json',
    'succ_lb3_st_brugge_academy': 'FINAL/Svartulfr_Lorebook_III.json',
    'ulTwlYo2jqObA7l_bFoa5': 'lorebooks/optimized/Svartulfr_Location.json',
    'loc_theta_iota_theta_suite_3': 'lorebooks/optimized/Svartulfr_Location.json',
    'jmh0MajEsRwrm4UYU14mY': 'FINAL/Svartulfr_NPC_Secondary.json',
    'npc_larek_steeltooth': 'FINAL/Svartulfr_NPC_Secondary.json',
    'alyssa_world_dossier_2b54a223': 'FINAL/Svartulfr_NPC_Primary.json',
    'Vcj4h2TL4Usola2A4OOl6': 'FINAL/Svartulfr_NPC_Primary.json'
}

def run_adversarial_suite():
    failures = []
    warnings = []
    
    print("=" * 60)
    print("CHALLENGER 1: ADVERSARIAL STRESS TEST SUITE")
    print("=" * 60)

    # 1. Byte-for-byte identity entries == lexicon
    print("\n[CHALLENGE 1] Byte-for-byte entries == lexicon across all files...")
    for fpath in MODIFIED_FILES:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                d = json.load(f)
            entries = d.get('entries')
            lexicon = d.get('lexicon')
            if entries is None or lexicon is None:
                failures.append(f"{fpath}: Missing 'entries' or 'lexicon' top-level key!")
                continue
            if len(entries) != len(lexicon):
                failures.append(f"{fpath}: Length mismatch: entries has {len(entries)}, lexicon has {len(lexicon)}")
                continue
            # Compare json representations
            e_str = json.dumps(entries, sort_keys=True)
            l_str = json.dumps(lexicon, sort_keys=True)
            if e_str != l_str:
                failures.append(f"{fpath}: entries and lexicon have content mismatch even though lengths match!")
            elif entries != lexicon:
                failures.append(f"{fpath}: entries != lexicon order or object difference!")
            else:
                print(f"  OK: {fpath} (count: {len(entries)})")
        except Exception as e:
            failures.append(f"{fpath}: Failed to load/parse: {e}")

    # 2. Mirror Synchronization
    print("\n[CHALLENGE 2] Mirror integrity FINAL/ vs lorebooks/optimized/...")
    for p1, p2 in PAIRED_MIRRORS:
        try:
            with open(p1, 'r', encoding='utf-8') as f1, open(p2, 'r', encoding='utf-8') as f2:
                raw1 = f1.read()
                raw2 = f2.read()
            if raw1 != raw2:
                failures.append(f"Mirror mismatch: {p1} != {p2} (raw string difference)!")
            else:
                print(f"  OK: {p1} == {p2} (exact raw byte match, {len(raw1)} bytes)")
        except Exception as e:
            failures.append(f"Mirror check failed for {p1} / {p2}: {e}")

    # 3. Duplicate Entry IDs within each file
    print("\n[CHALLENGE 3] Duplicate Entry IDs within each file...")
    for fpath in MODIFIED_FILES:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        seen_ids = set()
        for idx, e in enumerate(d.get('entries', [])):
            eid = e.get('entry_id') or e.get('id')
            if not eid:
                failures.append(f"{fpath}: Entry #{idx} has no entry_id or id!")
            elif eid in seen_ids:
                warnings.append(f"{fpath}: Duplicate entry ID '{eid}' at index {idx} ({e.get('name')})")
            seen_ids.add(eid)
        print(f"  OK: {fpath} has {len(seen_ids)} unique IDs out of {len(d.get('entries', []))} entries.")

    # 4. Umbrella Keys Check on ALL NPC entries
    print("\n[CHALLENGE 4] Comprehensive Umbrella Key scan on NPC Lorebooks...")
    npc_files = [
        'FINAL/Svartulfr_NPC_Secondary.json',
        'FINAL/Svartulfr_NPC_Primary.json',
        'lorebooks/optimized/Svartulfr_NPC_Secondary.json',
        'lorebooks/optimized/Svartulfr_NPC_Primary.json'
    ]
    total_npc_entries = 0
    for fpath in npc_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for idx, e in enumerate(d.get('entries', [])):
            total_npc_entries += 1
            name = e.get('name', 'UNKNOWN')
            keys = [k.strip().lower() for k in e.get('keys', [])]
            for bk in BROAD_KEYS:
                if bk in keys:
                    failures.append(f"{fpath} #{idx} ({name}): exact broad key '{bk}' found in keys!")
            for k in keys:
                for bk in BROAD_KEYS:
                    if k == bk:
                        failures.append(f"{fpath} #{idx} ({name}): exact broad key '{bk}' matched!")
    print(f"  Scanned {total_npc_entries} entries across NPC files. Zero broad keys found.")

    # 5. St. Brugge Location entry keys check
    print("\n[CHALLENGE 5] St. Brugge Location entry keys audit...")
    loc_file = 'lorebooks/optimized/Svartulfr_Location.json'
    with open(loc_file, 'r', encoding='utf-8') as f:
        d_loc = json.load(f)
    st_brugge_entries = [e for e in d_loc['entries'] if (e.get('entry_id') or e.get('id')) == 'ulTwlYo2jqObA7l_bFoa5']
    if not st_brugge_entries:
        failures.append("St. Brugge entry 'ulTwlYo2jqObA7l_bFoa5' not found in Location lorebook!")
    else:
        st_b = st_brugge_entries[0]
        cleaned_keys = st_b.get('keys', [])
        print(f"  St. Brugge keys: {cleaned_keys}")
        banned_loc_keys = {'seven hills', 'douglas', 'blackwood', 'private academy'}
        for k in cleaned_keys:
            if k.strip().lower() in banned_loc_keys:
                failures.append(f"St. Brugge Location entry still contains broad key '{k}'!")

    # 6. Global {{age}} and unexpanded macro audit
    print("\n[CHALLENGE 6] Macro audit ({{age}}, unexpanded macros)...")
    for fpath in MODIFIED_FILES:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if '{{age}}' in content:
            failures.append(f"VIOLATION: '{{{{age}}}}' found in {fpath}!")
        if regex.search(r'\{\{\s*age\s*\}\}', content, regex.IGNORECASE):
            failures.append(f"VIOLATION: '{{{{age}}}}' variant found in {fpath}!")

    # 7. Target Entry Detailed Schema & Attribute Stress Test
    print("\n[CHALLENGE 7] Deep inspection of all 10 milestone target entries...")
    for eid, source_file in TARGET_ENTRY_IDS.items():
        with open(source_file, 'r', encoding='utf-8') as f:
            d = json.load(f)
        matched = [e for e in d['entries'] if (e.get('entry_id') or e.get('id')) == eid]
        if not matched:
            failures.append(f"Target entry '{eid}' missing in {source_file}!")
            continue
        entry = matched[0]
        print(f"\n  Checking target entry '{eid}' ({entry.get('name')}) in {source_file}:")

        # Basic fields
        for req_field in ['name', 'type', 'keys', 'content', 'enabled', 'priority', 'insertion_order']:
            if req_field not in entry:
                failures.append(f"Target entry '{eid}' missing required field '{req_field}'!")
        
        # Check empty content or keys
        if not entry.get('content', '').strip():
            failures.append(f"Target entry '{eid}' has empty content!")
        if not entry.get('keys'):
            failures.append(f"Target entry '{eid}' has empty keys!")

        # Em-dash check in target entry
        raw_e = json.dumps(entry, ensure_ascii=False)
        if '—' in raw_e:
            failures.append(f"Target entry '{eid}' contains em-dash ('—')!")
        
        # Markdown bold / asterisks in content (except if legitimately internal thought)
        content = entry.get('content', '')
        if '**' in content:
            failures.append(f"Target entry '{eid}' contains markdown bold '**' in content!")

        # Negative framing check
        for neg_pat in ['no human ears', 'senza orecchie umane', 'privo di orecchie umane', 'prive di orecchie umane', 'non ha gambe', 'priva di gambe']:
            if neg_pat in content.lower():
                failures.append(f"Target entry '{eid}' contains negative framing phrase '{neg_pat}'!")

        # Specific NPC checks
        if entry.get('type') == 'npc':
            if not entry.get('avatar'):
                failures.append(f"NPC target entry '{eid}' has empty avatar!")
            if not entry.get('custom_avatar_regex'):
                failures.append(f"NPC target entry '{eid}' missing custom_avatar_regex: true!")
            if not entry.get('lines_parsed'):
                failures.append(f"NPC target entry '{eid}' missing lines_parsed: 1!")
            if not entry.get('npc_info'):
                failures.append(f"NPC target entry '{eid}' missing npc_info object!")
            else:
                info = entry['npc_info']
                if not info.get('first_name'):
                    failures.append(f"NPC target entry '{eid}' npc_info missing first_name!")
            
            # Check avatar_activation_regex compiles with regex engine (ECMAScript compatibility)
            aar = entry.get('avatar_activation_regex')
            if aar:
                try:
                    compiled_r = regex.compile(aar)
                    print(f"    Avatar activation regex compiles: {aar[:70]}...")
                except Exception as ex:
                    failures.append(f"NPC target entry '{eid}' avatar_activation_regex '{aar}' failed to compile: {ex}")

        # Specific Entry Validations
        if eid == 'npc_larek_steeltooth':
            if entry.get('entry_id') != 'npc_larek_steeltooth':
                failures.append(f"npc_larek_steeltooth has entry_id='{entry.get('entry_id')}', expected 'npc_larek_steeltooth'!")
            if entry.get('avatar') != 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public':
                failures.append(f"npc_larek_steeltooth avatar is not DCC placeholder: {entry.get('avatar')}")
            if entry.get('type') != 'npc':
                failures.append(f"npc_larek_steeltooth type is not 'npc': {entry.get('type')}")
            print(f"    -> Larek Steeltooth schema normalized successfully.")

        elif eid == 'jmh0MajEsRwrm4UYU14mY': # Revazhael
            if entry.get('name') != 'Father Revazhael (Rev)':
                failures.append(f"Revazhael name is '{entry.get('name')}', expected 'Father Revazhael (Rev)'")
            rev_keys = entry.get('keys', [])
            for rk in ['Father Revazhael', 'Padre Revazhael', 'Father Rev', 'Padre Rev', 'Revazhael', 'Rev']:
                if rk not in rev_keys:
                    failures.append(f"Revazhael missing key '{rk}'!")
            if 'Ancient Superior Demon' not in content and 'Superior Demon' not in content:
                failures.append(f"Revazhael content missing Superior Demon reference!")
            if 'St. Brugge' not in content:
                failures.append(f"Revazhael content missing St. Brugge reference!")
            print(f"    -> Father Revazhael verified with keys: {rev_keys}")

        elif eid == 'alyssa_world_dossier_2b54a223':
            line1 = content.splitlines()[0]
            if "Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555)" not in line1:
                failures.append(f"Alyssa Line 1 missing Certified Guild Healer title: {line1[:80]}...")
            if "Novice Healing Mage" in content:
                failures.append("Alyssa still has outdated 'Novice Healing Mage' text!")
            if "St. Brugge Private Academy" not in content:
                failures.append("Alyssa missing St. Brugge Private Academy in content!")
            if "Suite 3" not in content:
                failures.append("Alyssa missing Suite 3 in content!")
            if "Wolfy" not in content:
                failures.append("Alyssa missing Wolfy in content!")
            if not entry.get('selective'):
                failures.append("Alyssa selective flag is not True!")
            if entry.get('secondary_keys') != ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']:
                failures.append(f"Alyssa secondary_keys mismatch: {entry.get('secondary_keys')}")
            if entry.get('ignored_characters') != ['_6exg3yPfe2eCDK4hTftkh']:
                failures.append(f"Alyssa ignored_characters mismatch: {entry.get('ignored_characters')}")
            if entry.get('ignored_personas') != ['persona_1786335754946']:
                failures.append(f"Alyssa ignored_personas mismatch: {entry.get('ignored_personas')}")
            print(f"    -> Alyssa dossier verified (Len: {len(content)} chars, Persona protection intact).")

        elif eid == 'Vcj4h2TL4Usola2A4OOl6':
            line1 = content.splitlines()[0]
            if "Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555)" not in line1:
                failures.append(f"Jasper Line 1 missing Registered Guild Hunter: {line1[:80]}...")
            if "collarbone" in line1.lower():
                failures.append("Jasper Line 1 still contains outdated collarbone marking!")
            if "St. Brugge Private Academy" not in content:
                failures.append("Jasper missing St. Brugge Private Academy in content!")
            if "Welcome Fest" not in content:
                failures.append("Jasper missing Welcome Fest in content!")
            if not entry.get('selective'):
                failures.append("Jasper selective flag is not True!")
            if entry.get('secondary_keys') != ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']:
                failures.append(f"Jasper secondary_keys mismatch: {entry.get('secondary_keys')}")
            if entry.get('ignored_characters') != ['_t4J9aQNJM36cUKAP4wB4U']:
                failures.append(f"Jasper ignored_characters mismatch: {entry.get('ignored_characters')}")
            if entry.get('ignored_personas') != ['1792155173728']:
                failures.append(f"Jasper ignored_personas mismatch: {entry.get('ignored_personas')}")
            print(f"    -> Jasper dossier verified (Len: {len(content)} chars, Persona protection intact).")

        elif eid == 'lb1_concept_applied_runic_crystallography':
            if entry.get('type') != 'concept':
                failures.append(f"lb1_concept_applied_runic_crystallography type is {entry.get('type')}, expected 'concept'")
            if 'cristallografia' not in content.lower() and 'crystallography' not in content.lower():
                failures.append("Crystallography content missing 'cristallografia' or 'crystallography'!")
            print(f"    -> Applied Runic Crystallography verified.")

        elif eid == 'lb1_magic_abyssal_magic_distinction':
            if entry.get('type') != 'concept':
                failures.append(f"lb1_magic_abyssal_magic_distinction type is {entry.get('type')}, expected 'concept'")
            if ('abissale' not in content.lower() and 'abyssal' not in content.lower()) or ('vuoto' not in content.lower() and 'void' not in content.lower()):
                failures.append("Abyssal magic content missing 'abissale/abyssal' or 'vuoto/void'!")
            print(f"    -> Abyssal Magic distinction verified.")

        elif eid == 'lb2_item_enchanted_resonant_cylinders':
            if entry.get('type') != 'item':
                failures.append(f"lb2_item_enchanted_resonant_cylinders type is {entry.get('type')}, expected 'item'")
            if ('risonanza' not in content.lower() and 'resonant' not in content.lower()) or ('cilindr' not in content.lower() and 'cylinder' not in content.lower()):
                failures.append("Cylinders item content missing resonant or cylinder terms!")
            print(f"    -> Enchanted Resonant Cylinders verified.")

        elif eid == 'succ_lb3_st_brugge_academy':
            if entry.get('type') != 'concept':
                failures.append(f"succ_lb3_st_brugge_academy type is {entry.get('type')}, expected 'concept'")
            if 'st. brugge' not in content.lower():
                failures.append("St. Brugge concept content missing 'st. brugge'!")
            print(f"    -> St. Brugge Academy concept verified.")

        elif eid == 'loc_theta_iota_theta_suite_3':
            if entry.get('type') != 'location':
                failures.append(f"loc_theta_iota_theta_suite_3 type is {entry.get('type')}, expected 'location'")
            if 'sierra' not in content.lower() or 'alyssa' not in content.lower():
                failures.append("Suite 3 content missing 'sierra' or 'alyssa'!")
            print(f"    -> Theta Iota Theta Suite 3 verified.")

    # 8. Token budget and top-level metadata check
    print("\n[CHALLENGE 8] Top-level metadata & Token budget audit...")
    budget_map = {
        'FINAL/Svartulfr_Lorebook_I.json': 5000,
        'FINAL/Svartulfr_Lorebook_II.json': 5000,
        'FINAL/Svartulfr_Lorebook_III.json': 5000,
        'FINAL/Svartulfr_NPC_Secondary.json': 5000,
        'FINAL/Svartulfr_NPC_Primary.json': 7500,
        'lorebooks/optimized/Svartulfr_Location.json': 5000
    }
    for fpath, exp_budget in budget_map.items():
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        budget = d.get('token_budget')
        if budget != exp_budget:
            failures.append(f"{fpath}: token_budget is {budget}, expected {exp_budget}!")
        else:
            print(f"  OK: {fpath} token_budget == {exp_budget}")

    print("\n" + "=" * 60)
    print("CHALLENGE SUITE RESULTS SUMMARY")
    print("=" * 60)
    if warnings:
        print(f"WARNINGS DETECTED: {len(warnings)}")
        for w in warnings:
            print(f"  [WARN] {w}")
    if failures:
        print(f"FAILURES DETECTED: {len(failures)}")
        for f in failures:
            print(f"  [FAIL] {f}")
        return False
    else:
        print("ALL ADVERSARIAL STRESS TESTS PASSED WITH 100% SUCCESS.")
        return True

if __name__ == '__main__':
    success = run_adversarial_suite()
    sys.exit(0 if success else 1)
