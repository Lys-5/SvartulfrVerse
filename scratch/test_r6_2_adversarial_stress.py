import json
import os
import re
import sys
import urllib.request

def run_adversarial_tests():
    print("======================================================================")
    print("CHALLENGER R6-2: ADVERSARIAL STRESS TEST & EDGE-CASE HARNESS")
    print("======================================================================")
    failures = []
    passes = []

    def assert_true(cond, msg):
        if cond:
            passes.append(msg)
            print(f"[PASS] {msg}")
        else:
            failures.append(msg)
            print(f"[FAIL] {msg}")

    # ---------------------------------------------------------
    # TEST 1: SCENARIOS ARCHIVE & ACTIVE INVARIANTS
    # ---------------------------------------------------------
    print("\n--- Test 1: Scenarios Structure and Macro Invariants ---")
    final_scenarios = [f for f in os.listdir("FINAL/scenarios") if f.endswith(".json")]
    assert_true(len(final_scenarios) == 2, f"FINAL/scenarios contains exactly 2 JSON files (actual: {len(final_scenarios)})")
    assert_true(set(final_scenarios) == {"Svartulfr_Scenario_SUCC_Route_Alyssa.json", "Svartulfr_Scenario_SUCC_Route_Jasper.json"}, "FINAL/scenarios has exact 2 active SUCC scenarios")

    arch_scenarios = [f for f in os.listdir("ARCHIVIO/scenarios") if f.endswith(".json")]
    assert_true(len(arch_scenarios) == 4, f"ARCHIVIO/scenarios contains exactly 4 JSON files (actual: {len(arch_scenarios)})")
    expected_arch = {
        "Svartulfr_Scenario_Camp_Mystic.json",
        "Svartulfr_Scenario_DMHA_Dungeons.json",
        "Svartulfr_Scenario_Underworld_Sindacato.json",
        "Svartulfr_Scenario_Villa_Douglas.json"
    }
    assert_true(set(arch_scenarios) == expected_arch, "ARCHIVIO/scenarios has exact 4 retired scenarios")

    # Check for retired macro references in active scenarios
    retired_slots = ["best_friend", "roommate", "quarterback", "friend", "male_roommate", "crush", "sports_rival"]
    
    with open("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json", "r", encoding="utf-8") as f:
        alyssa_scen = json.load(f)
    with open("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json", "r", encoding="utf-8") as f:
        jasper_scen = json.load(f)

    # In Alyssa Route, macro for twin (Jasper) or crush (Mackenzie) might exist, but NPC slots (best_friend, roommate, quarterback, friend, sports_rival) should NOT be in scenarioChar
    alyssa_str = json.dumps(alyssa_scen)
    jasper_str = json.dumps(jasper_scen)

    for slot in ["best_friend", "roommate", "quarterback", "friend"]:
        pat = r'\{\{\s*scenarioChar\s+"' + slot + r'"\s*\}\}'
        m_aly = re.findall(pat, alyssa_str)
        assert_true(len(m_aly) == 0, f"Alyssa scenario has ZERO {{{{scenarioChar \"{slot}\"}}}} macros (found: {len(m_aly)})")

    for slot in ["male_roommate", "crush", "quarterback", "friend", "sports_rival"]:
        pat = r'\{\{\s*scenarioChar\s+"' + slot + r'"\s*\}\}'
        m_jas = re.findall(pat, jasper_str)
        assert_true(len(m_jas) == 0, f"Jasper scenario has ZERO {{{{scenarioChar \"{slot}\"}}}} macros (found: {len(m_jas)})")

    # ---------------------------------------------------------
    # TEST 2: SYNTHETIC GREETING MATCH AGAINST NPC REGEXES
    # ---------------------------------------------------------
    print("\n--- Test 2: Matching Scenario Greeting Dialogue Headers Against Primary NPC Regexes ---")
    with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
        primary_data = json.load(f)
    
    entries = primary_data.get("entries", [])
    regex_map = {}
    for e in entries:
        eid = e.get("entry_id") or e.get("id")
        reg = e.get("avatar_activation_regex")
        if reg:
            regex_map[e.get("name")] = re.compile(reg, re.MULTILINE)

    # Check actual greetings in Alyssa Route
    for g_idx, greeting in enumerate(alyssa_scen.get("greetings", [])):
        for m_idx, msg in enumerate(greeting.get("messages", [])):
            content = msg.get("content", "")
            # If line starts with a speaker name (e.g. Scarlett Rose:), verify matching regex
            lines = content.split("\n")
            for line in lines:
                m = re.match(r'^\s*([^":\n]+)\s*:', line)
                if m:
                    speaker_name = m.group(1).strip()
                    # Check if speaker_name matches one of our NPCs
                    matched_npc = None
                    for npc_name, r_compiled in regex_map.items():
                        if r_compiled.search(line):
                            matched_npc = npc_name
                            break
                    if speaker_name in ["Scarlett Rose", "Scarlett", "Sierra Cruz", "Sierra", "Russ Sinclair", "Russ", "Stan Davies Jr.", "Stan", "Jared Thompson", "Jared", "Jasper", "Alyssa"]:
                        assert_true(matched_npc is not None, f"Alyssa Scen G{g_idx} M{m_idx}: speaker '{speaker_name}' matched regex for NPC '{matched_npc}'")

    # Check actual greetings in Jasper Route
    for g_idx, greeting in enumerate(jasper_scen.get("greetings", [])):
        for m_idx, msg in enumerate(greeting.get("messages", [])):
            content = msg.get("content", "")
            lines = content.split("\n")
            for line in lines:
                m = re.match(r'^\s*([^":\n]+)\s*:', line)
                if m:
                    speaker_name = m.group(1).strip()
                    matched_npc = None
                    for npc_name, r_compiled in regex_map.items():
                        if r_compiled.search(line):
                            matched_npc = npc_name
                            break
                    if speaker_name in ["Scarlett Rose", "Scarlett", "Sierra Cruz", "Sierra", "Russ Sinclair", "Russ", "Stan Davies Jr.", "Stan", "Jared Thompson", "Jared", "Jasper", "Alyssa"]:
                        assert_true(matched_npc is not None, f"Jasper Scen G{g_idx} M{m_idx}: speaker '{speaker_name}' matched regex for NPC '{matched_npc}'")

    # ---------------------------------------------------------
    # TEST 3: GLOBAL LOREBOOK HYGIENE ACROSS ALL 99 ENTRIES
    # ---------------------------------------------------------
    print("\n--- Test 3: Global Hygiene Audit Across All 99 Primary Entries ---")
    seen_ids = set()
    umbrella_keys = {"solarton", "succ", "blackwood", "vampire", "werewolf", "college", "student", "alpha", "omega"}

    for e in entries:
        eid = e.get("entry_id") or e.get("id")
        assert_true(eid not in seen_ids, f"Unique entry ID: {eid} ({e.get('name')})")
        seen_ids.add(eid)

        etype = e.get("type")
        if etype != "npc":
            assert_true("npc_info" not in e, f"Non-NPC entry {e.get('name')} has no spurious npc_info")
            assert_true("custom_avatar_regex" not in e, f"Non-NPC entry {e.get('name')} has no spurious custom_avatar_regex")
        else:
            # Check umbrella keywords
            keys = set(k.lower() for k in e.get("keys", []))
            overlap = keys.intersection(umbrella_keys)
            assert_true(len(overlap) == 0, f"NPC entry {e.get('name')} has ZERO umbrella keywords (overlap: {overlap})")
            
            # Check selective vs secondary_keys
            if e.get("selective") is True:
                assert_true(bool(e.get("secondary_keys")), f"Selective NPC {e.get('name')} has secondary_keys populated")

    # ---------------------------------------------------------
    # TEST 4: APPROVED CARD INTEGRITY (OUTFITS >= 9, JED+ FORMAT)
    # ---------------------------------------------------------
    print("\n--- Test 4: Approved 8 Character Cards Deep Inspection ---")
    final_cards = [f for f in os.listdir("FINAL") if f.endswith("_card.json")]
    for fc in final_cards:
        fpath = os.path.join("FINAL", fc)
        with open(fpath, "r", encoding="utf-8") as f:
            c = json.load(f)
        cname = c.get("name", "")
        cid = c.get("id", "")
        outfits = c.get("outfits", [])
        assert_true(len(outfits) >= 9, f"Card {cname} ({fc}) has at least 9 outfits (actual: {len(outfits)})")
        desc = c.get("description", "")
        assert_true(len(desc) > 2000, f"Card {cname} ({fc}) description > 2000 chars (actual: {len(desc)})")
        assert_true("—" not in desc, f"Card {cname} ({fc}) zero em-dashes in description")
        assert_true("{{age}}" not in desc, f"Card {cname} ({fc}) zero raw {{{{age}}}} macros")

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------
    print("\n======================================================================")
    print(f"ADVERSARIAL AUDIT COMPLETE: {len(passes)} PASSED, {len(failures)} FAILED")
    print("======================================================================")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f" - {f}")
        return False
    else:
        print("\nALL ADVERSARIAL STRESS TESTS PASSED PERFECTLY!")
        return True

if __name__ == "__main__":
    success = run_adversarial_tests()
    sys.exit(0 if success else 1)
