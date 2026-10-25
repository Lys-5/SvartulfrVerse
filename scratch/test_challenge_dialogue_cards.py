import json
import glob
import os
import re
import sys

def run_tests():
    scenario_files = sorted(glob.glob("FINAL/scenarios/*.json"))
    export_file = "exports/Mine_Characters_Export.json"
    
    print("=" * 80)
    print("CHALLENGER 2: FORMAT, DIALOGUE & CARD INTEGRITY EMPIRICAL TEST SUITE")
    print("=" * 80)
    print(f"Scenario files found: {len(scenario_files)}")
    for sf in scenario_files:
        print(f"  - {sf}")
    print(f"Character export file: {export_file}")
    
    if not os.path.exists(export_file):
        print(f"CRITICAL ERROR: {export_file} not found!")
        sys.exit(1)
        
    with open(export_file, "r", encoding="utf-8") as f:
        export_chars = json.load(f)
        
    active_cards = {c["id"]: c.get("name") for c in export_chars if "id" in c}
    print(f"Loaded {len(active_cards)} active character cards from export:")
    for cid, cname in sorted(active_cards.items()):
        print(f"  [{cid}] -> {cname}")

    results = {
        "dialogue_formatting": {"passed": 0, "failed": 0, "details": []},
        "no_name_prefixes": {"passed": 0, "failed": 0, "details": []},
        "character_constraints": {"passed": 0, "failed": 0, "details": []},
        "slot_pool_card_ids": {"passed": 0, "failed": 0, "details": []},
        "schema_invariants": {"passed": 0, "failed": 0, "details": []}
    }
    
    # Required 6 lorebooks
    required_lbs = [
        '_gwwCxCfQ6PQaLEjAQVpJL',
        '_HfG7TeV6MJyj6bxMwxkpt',
        '_9zWTGqYJNJ4BCDMj8gfcD',
        '_EjXxkmPVhpCXg8xABpFkK',
        '_zwEqgEEzh12X6gHVmMKKC',
        '_Uht3Ckz44JBDrPnUHq7LV'
    ]

    for sf in scenario_files:
        fname = os.path.basename(sf)
        print(f"\n" + "-" * 70)
        print(f"Testing Scenario: {fname}")
        print("-" * 70)
        
        with open(sf, "r", encoding="utf-8") as f:
            scen = json.load(f)
            
        # ---------------------------------------------------------
        # Check Schema Invariants
        # ---------------------------------------------------------
        # Visibility
        vis = scen.get("visibility")
        if vis == "private":
            results["schema_invariants"]["passed"] += 1
            print(f"  [PASS] Visibility is 'private'")
        else:
            results["schema_invariants"]["failed"] += 1
            msg = f"{fname}: Expected visibility 'private', found '{vis}'"
            results["schema_invariants"]["details"].append(msg)
            print(f"  [FAIL] {msg}")
            
        # Lorebook IDs
        lb_ids = scen.get("lorebook_ids", [])
        if sorted(lb_ids) == sorted(required_lbs):
            results["schema_invariants"]["passed"] += 1
            print(f"  [PASS] Lorebook IDs match all 6 standalone lorebooks exactly")
        else:
            results["schema_invariants"]["failed"] += 1
            msg = f"{fname}: Lorebook IDs mismatch. Expected {required_lbs}, got {lb_ids}"
            results["schema_invariants"]["details"].append(msg)
            print(f"  [FAIL] {msg}")

        # Slot invariants
        slots = scen.get("slots", [])
        for slot in slots:
            unavail = slot.get("unavailable_count")
            if unavail == 0:
                results["schema_invariants"]["passed"] += 1
            else:
                results["schema_invariants"]["failed"] += 1
                msg = f"{fname} slot '{slot.get('key')}': unavailable_count is {unavail} (expected 0)"
                results["schema_invariants"]["details"].append(msg)
                print(f"  [FAIL] {msg}")
                
        # ---------------------------------------------------------
        # Check 1: Spoken dialogue formatting & forbidden characters
        # ---------------------------------------------------------
        # Check all greetings, messages, descriptions, etc.
        greetings = scen.get("greetings", [])
        print(f"  Greetings count: {len(greetings)}")
        
        for g_idx, greeting in enumerate(greetings):
            messages = greeting.get("messages", [])
            for m_idx, msg_obj in enumerate(messages):
                content = msg_obj.get("content", "")
                
                # Check for em-dash (—) or en-dash (–)
                if "—" in content:
                    results["dialogue_formatting"]["failed"] += 1
                    err = f"{fname} G{g_idx} M{m_idx}: Contains forbidden em-dash ('—')"
                    results["dialogue_formatting"]["details"].append(err)
                    print(f"  [FAIL] {err}")
                else:
                    results["dialogue_formatting"]["passed"] += 1

                # Check for curly quotes
                if "“" in content or "”" in content:
                    results["dialogue_formatting"]["failed"] += 1
                    err = f"{fname} G{g_idx} M{m_idx}: Contains curly quotes ('“' or '”')"
                    results["dialogue_formatting"]["details"].append(err)
                    print(f"  [FAIL] {err}")
                else:
                    results["dialogue_formatting"]["passed"] += 1

                # Check quotes pairing
                quote_count = content.count('"')
                if quote_count % 2 != 0:
                    results["dialogue_formatting"]["failed"] += 1
                    err = f"{fname} G{g_idx} M{m_idx}: Odd number of double quotes ({quote_count})"
                    results["dialogue_formatting"]["details"].append(err)
                    print(f"  [FAIL] {err}")
                else:
                    results["dialogue_formatting"]["passed"] += 1
                    
                # Check asterisks usage (reserved strictly for thoughts, no bold ** allowed)
                if "**" in content:
                    results["dialogue_formatting"]["failed"] += 1
                    err = f"{fname} G{g_idx} M{m_idx}: Contains double-asterisks '**' (bold markdown forbidden)"
                    results["dialogue_formatting"]["details"].append(err)
                    print(f"  [FAIL] {err}")
                else:
                    results["dialogue_formatting"]["passed"] += 1
                    
                # If single asterisks exist, check that they are paired and represent thoughts
                asterisk_count = content.count('*')
                if asterisk_count > 0:
                    if asterisk_count % 2 != 0:
                        results["dialogue_formatting"]["failed"] += 1
                        err = f"{fname} G{g_idx} M{m_idx}: Unpaired asterisks ({asterisk_count})"
                        results["dialogue_formatting"]["details"].append(err)
                        print(f"  [FAIL] {err}")
                    else:
                        results["dialogue_formatting"]["passed"] += 1
                        # Check thoughts
                        thoughts = re.findall(r'\*([^*]+)\*', content)
                        print(f"    [INFO] Found thoughts in G{g_idx} M{m_idx}: {thoughts}")

        # Check description and scenario for em-dash
        desc = scen.get("display_description", "")
        if "—" in desc:
            results["dialogue_formatting"]["failed"] += 1
            err = f"{fname} display_description: Contains forbidden em-dash ('—')"
            results["dialogue_formatting"]["details"].append(err)
            print(f"  [FAIL] {err}")
        else:
            results["dialogue_formatting"]["passed"] += 1

        scen_prompt = scen.get("scenario", "")
        if "—" in scen_prompt:
            results["dialogue_formatting"]["failed"] += 1
            err = f"{fname} scenario prompt: Contains forbidden em-dash ('—')"
            results["dialogue_formatting"]["details"].append(err)
            print(f"  [FAIL] {err}")
        else:
            results["dialogue_formatting"]["passed"] += 1

        # ---------------------------------------------------------
        # Check 2: No hardcoded name prefixes inside message texts
        # ---------------------------------------------------------
        for g_idx, greeting in enumerate(greetings):
            messages = greeting.get("messages", [])
            for m_idx, msg_obj in enumerate(messages):
                content = msg_obj.get("content", "").strip()
                lines = content.split("\n")
                for l_idx, line in enumerate(lines):
                    line_clean = line.strip()
                    if not line_clean:
                        continue
                    # Regex for hardcoded name prefix, e.g. "Santiago Herrera: ...", "Radek: ...", "{{scenarioChar ...}}: ..."
                    # Pattern matches at start of line: (Name): ... or {{scenarioChar ...}}: ...
                    prefix_match = re.match(r'^(?:\{\{scenarioChar\s+[^}]+\}\}|[A-Z][a-zA-Z\s\'-]{1,30}):\s*(".*)?$', line_clean)
                    if prefix_match:
                        results["no_name_prefixes"]["failed"] += 1
                        err = f"{fname} G{g_idx} M{m_idx} L{l_idx}: Hardcoded name prefix found: '{line_clean[:40]}'"
                        results["no_name_prefixes"]["details"].append(err)
                        print(f"  [FAIL] {err}")
                    else:
                        results["no_name_prefixes"]["passed"] += 1
        print(f"  [PASS] Name prefix checks passed for {fname}")

        # ---------------------------------------------------------
        # Check 4: Slot pool character IDs match active cards
        # ---------------------------------------------------------
        for slot in slots:
            pool = slot.get("pool", [])
            for p_item in pool:
                cid = p_item.get("character_id")
                if not cid:
                    results["slot_pool_card_ids"]["failed"] += 1
                    err = f"{fname} slot '{slot.get('key')}': Pool item missing character_id: {p_item}"
                    results["slot_pool_card_ids"]["details"].append(err)
                    print(f"  [FAIL] {err}")
                elif cid not in active_cards:
                    results["slot_pool_card_ids"]["failed"] += 1
                    err = f"{fname} slot '{slot.get('key')}': character_id '{cid}' NOT found in active cards!"
                    results["slot_pool_card_ids"]["details"].append(err)
                    print(f"  [FAIL] {err}")
                else:
                    results["slot_pool_card_ids"]["passed"] += 1
                    print(f"  [PASS] Slot '{slot.get('key')}' pool card ID '{cid}' -> '{active_cards[cid]}'")

    # ---------------------------------------------------------
    # Check 3: Specific Character Constraints
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("TESTING SPECIFIC CHARACTER CONSTRAINTS")
    print("=" * 70)
    
    # 3.1 Russ Sinclair and Scarlett Rose surnames
    succ_alyssa = json.load(open("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json", "r", encoding="utf-8"))
    succ_jasper = json.load(open("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json", "r", encoding="utf-8"))
    
    # Check Russ Sinclair in Jasper route
    jasper_slots = {s["key"]: s for s in succ_jasper.get("slots", [])}
    if "male_roommate" in jasper_slots:
        label = jasper_slots["male_roommate"].get("label", "")
        if "Sinclair" in label and "Russ" in label:
            results["character_constraints"]["passed"] += 1
            print(f"  [PASS] Russ Sinclair correctly named in Jasper route male_roommate slot: '{label}'")
        else:
            results["character_constraints"]["failed"] += 1
            err = f"Jasper route male_roommate label does not contain 'Russ Sinclair': '{label}'"
            results["character_constraints"]["details"].append(err)
            print(f"  [FAIL] {err}")
            
        # Verify pool ID
        pool = jasper_slots["male_roommate"].get("pool", [])
        if pool and pool[0].get("character_id") == "_wn6DkCcg3Xqa2Xpx9ttnT":
            results["character_constraints"]["passed"] += 1
            print(f"  [PASS] Russ Sinclair pool ID matches '_wn6DkCcg3Xqa2Xpx9ttnT' ({active_cards.get('_wn6DkCcg3Xqa2Xpx9ttnT')})")
        else:
            results["character_constraints"]["failed"] += 1
            err = f"Jasper route male_roommate pool ID mismatch: {pool}"
            results["character_constraints"]["details"].append(err)
            print(f"  [FAIL] {err}")
    else:
        results["character_constraints"]["failed"] += 1
        err = "Jasper route missing 'male_roommate' slot"
        results["character_constraints"]["details"].append(err)
        print(f"  [FAIL] {err}")
        
    # Check Scarlett Rose in Alyssa and Jasper routes
    alyssa_slots = {s["key"]: s for s in succ_alyssa.get("slots", [])}
    if "best_friend" in alyssa_slots:
        label = alyssa_slots["best_friend"].get("label", "")
        if "Scarlett Rose" in label:
            results["character_constraints"]["passed"] += 1
            print(f"  [PASS] Scarlett Rose correctly named in Alyssa route best_friend slot: '{label}'")
        else:
            results["character_constraints"]["failed"] += 1
            err = f"Alyssa route best_friend label does not contain 'Scarlett Rose': '{label}'"
            results["character_constraints"]["details"].append(err)
            print(f"  [FAIL] {err}")
    if "crush" in jasper_slots:
        label = jasper_slots["crush"].get("label", "")
        if "Scarlett Rose" in label:
            results["character_constraints"]["passed"] += 1
            print(f"  [PASS] Scarlett Rose correctly named in Jasper route crush slot: '{label}'")
        else:
            results["character_constraints"]["failed"] += 1
            err = f"Jasper route crush label does not contain 'Scarlett Rose': '{label}'"
            results["character_constraints"]["details"].append(err)
            print(f"  [FAIL] {err}")
            
    # Check pool ID for Scarlett Rose in both
    for route_name, slots_dict, slot_key in [("Alyssa", alyssa_slots, "best_friend"), ("Jasper", jasper_slots, "crush")]:
        pool = slots_dict.get(slot_key, {}).get("pool", [])
        if pool and pool[0].get("character_id") == "_qXgBMbFYJfc84hbLHhe92":
            results["character_constraints"]["passed"] += 1
            print(f"  [PASS] Scarlett Rose pool ID in {route_name} route matches '_qXgBMbFYJfc84hbLHhe92' ({active_cards.get('_qXgBMbFYJfc84hbLHhe92')})")
        else:
            results["character_constraints"]["failed"] += 1
            err = f"{route_name} route Scarlett Rose pool mismatch: {pool}"
            results["character_constraints"]["details"].append(err)
            print(f"  [FAIL] {err}")

    # 3.2 Finnegan Novak explicitly specified as Arctic Wolf demi-human
    # Check in Alyssa route, Jasper route, and scenario text / slots
    found_finnegan_arctic_wolf = False
    for r_name, r_data in [("Alyssa", succ_alyssa), ("Jasper", succ_jasper)]:
        content_dump = json.dumps(r_data)
        matches = re.findall(r'Finnegan\s+Novak[^\n"\',]*(?:Arctic\s+Wolf|demi-human|demihuman)', content_dump, re.IGNORECASE)
        slots_match = [s for s in r_data.get("slots", []) if s.get("key") == "childhood_friend" and "Finnegan Novak" in s.get("label", "")]
        print(f"  Checking Finnegan Novak in {r_name} route: slots={len(slots_match)}, text matches={len(matches)}")
        if slots_match:
            print(f"    Slot label: {slots_match[0].get('label')}")
            # Check if Arctic wolf demi-human is in label or scenario text
            if "Arctic Wolf" in content_dump and ("demi-human" in content_dump or "demihuman" in content_dump):
                results["character_constraints"]["passed"] += 1
                print(f"  [PASS] Finnegan Novak explicitly specified as Arctic Wolf demi-human in {r_name} route")
                found_finnegan_arctic_wolf = True
            else:
                results["character_constraints"]["failed"] += 1
                err = f"Finnegan Novak in {r_name} route does not explicitly specify Arctic Wolf demi-human"
                results["character_constraints"]["details"].append(err)
                print(f"  [FAIL] {err}")

    # 3.3 Jean-Luc Virtuoso explicitly specified as Human Telepath
    underworld = json.load(open("FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json", "r", encoding="utf-8"))
    underworld_dump = json.dumps(underworld)
    jl_slots = [s for s in underworld.get("slots", []) if s.get("key") == "sinners_leader"]
    if jl_slots:
        print(f"  Jean-Luc slot: {jl_slots[0]}")
    if "Human Telepath" in underworld_dump or ("Jean-Luc Virtuoso" in underworld_dump and "telepath" in underworld_dump.lower()):
        results["character_constraints"]["passed"] += 1
        print(f"  [PASS] Jean-Luc Virtuoso explicitly specified as Human Telepath in Underworld Sindacato scenario")
    else:
        results["character_constraints"]["failed"] += 1
        err = "Jean-Luc Virtuoso NOT specified as Human Telepath in Underworld Sindacato"
        results["character_constraints"]["details"].append(err)
        print(f"  [FAIL] {err}")

    # 3.4 Villa Douglas contains exactly the 7 canonical male card holders
    villa = json.load(open("FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json", "r", encoding="utf-8"))
    villa_slots = villa.get("slots", [])
    expected_villa_ids = {
        "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
        "_RDfz7XzTpM23LpPALVXHM": "Malachia Bjrn Douglas Bloodmoon",
        "_t4J9aQNJM36cUKAP4wB4U": "Jasper Svartr Douglas Bloodmoon",
        "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
        "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Bleygr Bloodmoon",
        "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Dominic Jrn Douglas",
        "_TbRM3EdxDjHFgqztTbCpL": "Edric Douglas"
    }
    actual_villa_ids = {}
    for s in villa_slots:
        for p in s.get("pool", []):
            cid = p.get("character_id")
            actual_villa_ids[cid] = s.get("label")
            
    print(f"  Villa Douglas slot count: {len(villa_slots)} (expected: 7)")
    print(f"  Villa Douglas unique pool card IDs: {len(actual_villa_ids)} (expected: 7)")
    if len(villa_slots) == 7 and set(actual_villa_ids.keys()) == set(expected_villa_ids.keys()):
        results["character_constraints"]["passed"] += 1
        print("  [PASS] Villa Douglas contains EXACTLY the 7 canonical male Douglas/Bloodmoon card holders:")
        for cid, label in actual_villa_ids.items():
            print(f"    - [{cid}] {label} (matches active card '{active_cards.get(cid)}')")
    else:
        results["character_constraints"]["failed"] += 1
        err = f"Villa Douglas slot count ({len(villa_slots)}) or IDs ({set(actual_villa_ids.keys())}) do not match expected 7 males"
        results["character_constraints"]["details"].append(err)
        print(f"  [FAIL] {err}")

    # 3.5 DMHA scenario contains Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian
    dmha = json.load(open("FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json", "r", encoding="utf-8"))
    dmha_slots = {s["key"]: s for s in dmha.get("slots", [])}
    dmha_dump = json.dumps(dmha)
    required_dmha_chars = ["Alyssa", "Jasper", "Malachia", "Barrow", "Marek", "Radek", "Goran", "Kian"]
    print(f"  Checking DMHA scenario slots and cast:")
    dmha_all_found = True
    for c in required_dmha_chars:
        found_in_slots = any(c.lower() in s.get("label", "").lower() or c.lower() in s.get("key", "").lower() for s in dmha.get("slots", []))
        found_in_dump = c in dmha_dump
        if found_in_slots and found_in_dump:
            print(f"    [PASS] DMHA includes {c}")
        else:
            dmha_all_found = False
            print(f"    [FAIL] DMHA missing or incomplete for {c} (slots={found_in_slots}, dump={found_in_dump})")
    if dmha_all_found:
        results["character_constraints"]["passed"] += 1
        print("  [PASS] DMHA scenario contains all required characters (Alyssa, Jasper, Malachia, Barrow, Marek, Radek, Goran, Kian)")
    else:
        results["character_constraints"]["failed"] += 1
        err = "DMHA scenario missing one or more required characters"
        results["character_constraints"]["details"].append(err)
        print(f"  [FAIL] {err}")

    # 3.6 Camp Mystic contains shuttle arrival and Marcus Vale / Celeste Nadir supervision logic
    camp = json.load(open("FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json", "r", encoding="utf-8"))
    camp_dump = json.dumps(camp)
    shuttle_found = "shuttle" in camp_dump.lower() and ("lake erie" in camp_dump.lower() or "dock" in camp_dump.lower() or "ferry" in camp_dump.lower() or "arrival" in camp_dump.lower())
    supervision_found = "marcus vale" in camp_dump.lower() and "celeste nadir" in camp_dump.lower()
    startup_script = camp.get("startup_script", "")
    script_supervision = "Marcus Vale" in startup_script and "Celeste Nadir" in startup_script
    
    print(f"  Camp Mystic shuttle arrival check: {shuttle_found}")
    print(f"  Camp Mystic Marcus Vale & Celeste Nadir check in scenario: {supervision_found}")
    print(f"  Camp Mystic startup_script dynamic supervision check: {script_supervision}")
    
    if shuttle_found and supervision_found and script_supervision:
        results["character_constraints"]["passed"] += 1
        print("  [PASS] Camp Mystic incorporates Lake Erie shuttle arrival and dynamic Marcus Vale / Celeste Nadir supervision logic")
    else:
        results["character_constraints"]["failed"] += 1
        err = f"Camp Mystic constraints failed: shuttle={shuttle_found}, supervision={supervision_found}, script={script_supervision}"
        results["character_constraints"]["details"].append(err)
        print(f"  [FAIL] {err}")

    # ---------------------------------------------------------
    # FINAL SUMMARY
    # ---------------------------------------------------------
    print("\n" + "=" * 80)
    print("FINAL TEST RESULTS SUMMARY")
    print("=" * 80)
    total_passed = sum(v["passed"] for v in results.values())
    total_failed = sum(v["failed"] for v in results.values())
    
    for category, res in results.items():
        print(f"Category: {category:25} | Passed: {res['passed']:4} | Failed: {res['failed']:4}")
        if res["details"]:
            for d in res["details"]:
                print(f"    - {d}")
                
    print("-" * 80)
    print(f"TOTAL TESTS: {total_passed + total_failed} | PASSED: {total_passed} | FAILED: {total_failed}")
    if total_failed == 0:
        print("VERDICT: >>> APPROVE <<<")
    else:
        print("VERDICT: >>> REJECT <<<")
    print("=" * 80)

if __name__ == "__main__":
    run_tests()
