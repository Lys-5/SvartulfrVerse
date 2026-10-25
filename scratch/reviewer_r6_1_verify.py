"""
Reviewer R6-1 Independent Live & Local Verification Script (v2)
Audits R1, R2, R3 implementation for SvartulfrVerse.
"""

import os
import json
import re
import urllib.request
import urllib.error

def main():
    print("=== REVIEWER R6-1 INDEPENDENT VERIFICATION ===")
    
    # Read token
    token_path = os.path.join("scratch", "wyvern_token.txt")
    with open(token_path, "r", encoding="utf-8") as f:
        token = f.read().strip()
        
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "ReviewerR6-1/1.0",
        "Accept": "application/json"
    }
    
    results = {
        "passed": 0,
        "failed": 0,
        "findings": []
    }
    
    def log_check(name, passed, detail=""):
        if passed:
            results["passed"] += 1
            print(f"[PASS] {name}: {detail}")
        else:
            results["failed"] += 1
            results["findings"].append(f"{name}: {detail}")
            print(f"[FAIL] {name}: {detail}")
            
    # -------------------------------------------------------------
    # 1. Local Scenarios Files Check
    # -------------------------------------------------------------
    final_scenarios_dir = os.path.join("FINAL", "scenarios")
    archivio_scenarios_dir = os.path.join("ARCHIVIO", "scenarios")
    
    final_scen_files = sorted([f for f in os.listdir(final_scenarios_dir) if f.endswith(".json")])
    archivio_scen_files = sorted([f for f in os.listdir(archivio_scenarios_dir) if f.endswith(".json")])
    
    expected_final_scen = [
        "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "Svartulfr_Scenario_SUCC_Route_Jasper.json"
    ]
    expected_archivio_scen = [
        "Svartulfr_Scenario_Camp_Mystic.json",
        "Svartulfr_Scenario_DMHA_Dungeons.json",
        "Svartulfr_Scenario_Underworld_Sindacato.json",
        "Svartulfr_Scenario_Villa_Douglas.json"
    ]
    
    log_check("Local FINAL/scenarios/ count", len(final_scen_files) == 2, f"Found {len(final_scen_files)} files: {final_scen_files}")
    log_check("Local FINAL/scenarios/ exact match", final_scen_files == expected_final_scen, f"{final_scen_files}")
    
    log_check("Local ARCHIVIO/scenarios/ count", len(archivio_scen_files) == 4, f"Found {len(archivio_scen_files)} files: {archivio_scen_files}")
    log_check("Local ARCHIVIO/scenarios/ exact match", archivio_scen_files == expected_archivio_scen, f"{archivio_scen_files}")

    # -------------------------------------------------------------
    # 2. Local Cards Check
    # -------------------------------------------------------------
    final_dir = "FINAL"
    final_cards = sorted([f for f in os.listdir(final_dir) if f.endswith("_card.json")])
    expected_final_cards = sorted([
        "Edric_Douglas_card.json",
        "Erik_Douglas_card.json",
        "Jasper_Douglas_Bloodmoon_card.json",
        "Logan_Douglas_card.json",
        "Mackenzie_Sanchez_Rogers_card.json",
        "Malachia_Douglas_Bloodmoon_card.json",
        "Noah_Douglas_Bloodmoon_card.json",
        "Wulfnic_Bloodmoon_card.json"
    ])
    log_check("Local FINAL/ cards count", len(final_cards) == 8, f"Found {len(final_cards)} cards: {final_cards}")
    log_check("Local FINAL/ cards exact match", final_cards == expected_final_cards, f"{final_cards}")

    legacy_cards_dir = os.path.join("ARCHIVIO", "cards_legacy")
    legacy_cards = sorted([f for f in os.listdir(legacy_cards_dir) if f.endswith("_card.json")])
    expected_legacy_cards = sorted([
        "Alyssa_Douglas_Bloodmoon_card.json",
        "Jared_Thompson_card.json",
        "Russ_card.json",
        "Scarlett_Rose_card.json",
        "Sierra_Cruz_card.json",
        "Stan_Davies_Jr_card.json"
    ])
    log_check("Local ARCHIVIO/cards_legacy/ count", len(legacy_cards) == 6, f"Found {len(legacy_cards)} cards: {legacy_cards}")
    log_check("Local ARCHIVIO/cards_legacy/ exact match", legacy_cards == expected_legacy_cards, f"{legacy_cards}")

    # -------------------------------------------------------------
    # 3. Live Wyvern GET on /characters/mine
    # -------------------------------------------------------------
    mine_url = "https://app.wyvern.chat/api/characters/mine"
    mine_req = urllib.request.Request(mine_url, headers=headers)
    try:
        with urllib.request.urlopen(mine_req) as resp:
            status = resp.status
            mine_data = json.loads(resp.read().decode("utf-8"))
            live_chars = mine_data.get("characters", [])
            log_check("Live GET /characters/mine HTTP 200", status == 200, f"HTTP {status}")
            log_check("Live /characters/mine count exactly 8", len(live_chars) == 8, f"Found {len(live_chars)} cards")
            
            approved_ids = {
                "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
                "_RDfz7XzTpM23LpPALVXHM": "Malachia Björn Douglas Bloodmoon",
                "_t4J9aQNJM36cUKAP4wB4U": "Jasper Svartr Douglas Bloodmoon",
                "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
                "_TbRM3EdxDjHFgqztTbCpL": "Edric Douglas",
                "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Dominic Járn Douglas",
                "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Báleygr Bloodmoon",
                "_zn24784jfcchQ7EwCyAnm": "Mackenzie Sanchez-Rogers"
            }
            live_ids = {c["id"]: c.get("name") for c in live_chars}
            log_check("Live /characters/mine approved IDs set match", set(live_ids.keys()) == set(approved_ids.keys()), f"Live IDs: {list(live_ids.keys())}")
            for cid, cname in approved_ids.items():
                match = cid in live_ids
                log_check(f"Live card present: {cname} ({cid})", match, f"Matched: {live_ids.get(cid)}")
    except Exception as e:
        log_check("Live GET /characters/mine", False, f"Exception: {e}")

    # -------------------------------------------------------------
    # 4. Live Wyvern GET on Jared Thompson (_xJVPtBLL3dxy69RLKL9X9)
    # -------------------------------------------------------------
    jared_url = "https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9"
    jared_req = urllib.request.Request(jared_url, headers=headers)
    try:
        with urllib.request.urlopen(jared_req) as resp:
            log_check("Live GET Jared Thompson deleted (HTTP 404 expected)", False, f"Unexpected HTTP {resp.status} - Card still exists!")
    except urllib.error.HTTPError as e:
        log_check("Live GET Jared Thompson deleted (HTTP 404 expected)", e.code == 404, f"HTTP {e.code} {e.reason}")
    except Exception as e:
        log_check("Live GET Jared Thompson", False, f"Unexpected error: {e}")

    # -------------------------------------------------------------
    # 5. Live Wyvern GET on Scenarios
    # -------------------------------------------------------------
    scenarios_to_check = [
        ("Alyssa SUCC Route", "char_scenario_CKgwq246DyCj1NNTBV9rt", 11, 7, ["twin", "crush"]),
        ("Jasper SUCC Route", "char_scenario_Kq4mJEBH83j7Q7DdVfFnF", 5, 6, [])
    ]
    
    for label, sc_id, min_rev, expected_greetings, allowed_pool_slots in scenarios_to_check:
        sc_url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
        sc_req = urllib.request.Request(sc_url, headers=headers)
        try:
            with urllib.request.urlopen(sc_req) as resp:
                status = resp.status
                sc_data = json.loads(resp.read().decode("utf-8"))
                
                log_check(f"{label} ({sc_id}) HTTP 200", status == 200, f"HTTP {status}")
                
                # Check revision
                rev = sc_data.get("revision")
                log_check(f"{label} revision >= {min_rev}", rev >= min_rev, f"Revision: {rev}")
                
                # Check slots: unavailable_count == 0
                slots = sc_data.get("slots", [])
                log_check(f"{label} slots count == 8", len(slots) == 8, f"Slots count: {len(slots)}")
                all_clean_slots = True
                bad_slots = []
                for s in slots:
                    k = s.get("key")
                    unavail = s.get("unavailable_count", 0)
                    plen = len(s.get("pool", []))
                    if unavail != 0:
                        all_clean_slots = False
                        bad_slots.append(f"{k}: unavailable_count={unavail}")
                    if k not in allowed_pool_slots and plen > 0:
                        all_clean_slots = False
                        bad_slots.append(f"{k}: unexpected pool_len={plen}")
                log_check(f"{label} all slots clean (unavailable_count=0 & correct pools)", all_clean_slots, f"Issues: {bad_slots}")
                
                # Check greetings
                greetings = sc_data.get("greetings", [])
                log_check(f"{label} greetings count == {expected_greetings}", len(greetings) == expected_greetings, f"Found {len(greetings)} greetings")
                
                # Check greeting invariants: speaker_slot matches message 0
                all_speakers_match = True
                speaker_mismatches = []
                for idx, g in enumerate(greetings):
                    msgs = g.get("messages", [])
                    if msgs:
                        first_speaker = msgs[0].get("speaker_slot")
                        g_speaker = g.get("speaker_slot")
                        if g_speaker != first_speaker:
                            all_speakers_match = False
                            speaker_mismatches.append(f"Greeting {idx} ('{g.get('name')}'): g.speaker={g_speaker} != msg0.speaker={first_speaker}")
                log_check(f"{label} speaker_slot matches messages[0].speaker_slot", all_speakers_match, f"Mismatches: {speaker_mismatches}")
                
                # Check orphan macros in greetings (retired NPCs)
                retired_keys = ['best_friend', 'roommate', 'friend', 'quarterback', 'childhood_friend', 'sports_rival', 'male_roommate']
                if label == "Jasper SUCC Route":
                    retired_keys.append('twin') # In Jasper route, twin was also retired from pool
                
                retired_in_greetings = []
                for gi, g in enumerate(greetings):
                    gtext = g.get("content", "")
                    for mi, m in enumerate(g.get("messages", [])):
                        mtext = m.get("content", "")
                        for rk in retired_keys:
                            target = f'{{{{scenarioChar "{rk}"}}}}'
                            if target in gtext or target in mtext:
                                retired_in_greetings.append(f"G{gi} (M{mi}) contains {target}")
                log_check(f"{label} zero retired NPC scenarioChar in greetings", len(retired_in_greetings) == 0, f"Found: {retired_in_greetings}")

                # Check formatting: em-dashes
                raw_text = json.dumps(sc_data, ensure_ascii=False)
                em_dashes = re.findall(r'—', raw_text)
                log_check(f"{label} zero em-dashes in live payload", len(em_dashes) == 0, f"Found {len(em_dashes)} em-dashes")

        except Exception as e:
            log_check(f"{label} ({sc_id}) verification", False, f"Exception: {e}")

    # -------------------------------------------------------------
    # 6. Local Scenarios Formatting Check
    # -------------------------------------------------------------
    for fname in final_scen_files:
        fpath = os.path.join(final_scenarios_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            local_scen = json.load(f)
            local_text = json.dumps(local_scen, ensure_ascii=False)
            
            # Zero em-dashes
            local_em_dashes = re.findall(r'—', local_text)
            log_check(f"Local {fname} zero em-dashes", len(local_em_dashes) == 0, f"Found {len(local_em_dashes)} em-dashes")
            
            # Check greeting 0 name
            greetings = local_scen.get("greetings", [])
            if greetings:
                g0_name = greetings[0].get("name", "")
                log_check(f"Local {fname} greeting 0 name is 'SUCC Welcome Day'", g0_name == "SUCC Welcome Day", f"Name: {g0_name}")
                
            # Check retired NPC macros in greetings
            retired_in_greetings = []
            retired_keys = ['best_friend', 'roommate', 'friend', 'quarterback', 'childhood_friend', 'sports_rival', 'male_roommate']
            if "Jasper" in fname:
                retired_keys.append('twin')
            for gi, g in enumerate(greetings):
                gtext = g.get("content", "")
                for mi, m in enumerate(g.get("messages", [])):
                    mtext = m.get("content", "")
                    for rk in retired_keys:
                        target = f'{{{{scenarioChar "{rk}"}}}}'
                        if target in gtext or target in mtext:
                            retired_in_greetings.append(f"G{gi} (M{mi}) contains {target}")
            log_check(f"Local {fname} zero retired NPC scenarioChar in greetings", len(retired_in_greetings) == 0, f"Found: {retired_in_greetings}")

            # Check action asterisks in messages
            asterisk_actions = []
            for idx, g in enumerate(greetings):
                for midx, m in enumerate(g.get("messages", [])):
                    content = m.get("content", "")
                    ast_count = content.count("*")
                    if ast_count > 0:
                        asterisk_actions.append(f"G{idx}M{midx} ({ast_count} asterisks): {content[:60]}...")
            log_check(f"Local {fname} zero action asterisks in messages", len(asterisk_actions) == 0, f"Found: {len(asterisk_actions)}")

    print(f"\nTOTAL CHECKS: {results['passed'] + results['failed']} | PASSED: {results['passed']} | FAILED: {results['failed']}")
    if results['failed'] > 0:
        print("\nFAILURES:")
        for finding in results['findings']:
            print(f" - {finding}")
    else:
        print("\nALL REVIEW CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    main()
