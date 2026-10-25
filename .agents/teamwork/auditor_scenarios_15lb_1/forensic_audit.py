import json
import requests
import pathlib
import sys
import hashlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
AUDITOR_DIR = ROOT / '.agents' / 'teamwork' / 'auditor_scenarios_15lb_1'

CANONICAL_LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",  # Svartúlfr - Lorebook I
    "_HfG7TeV6MJyj6bxMwxkpt",  # Svartúlfr - Lorebook II
    "_9zWTGqYJNJ4BCDMj8gfcD",  # Svartúlfr - Lorebook III
    "_EjXxkmPVhpCXg8xABpFkK",  # Svartúlfr - Location
    "_Uht3Ckz44JBDrPnUHq7LV",  # Svartúlfr - NPC Secondary
    "_zwEqgEEzh12X6gHVmMKKC",  # Svartúlfr - NPC Primary
    "_GV1KyHVY1RMbCnWgLkzDG",  # A0 Behavioral Realism
    "_GbWJbkhgLzWexMHrjyUUc",  # A1 Physics
    "_FaVcHfmrqcaJq8pa3WmRw",  # A2 Social Realism
    "_BbrRgrcdGPMLEbBU2b6xk",  # A3 Medical Realism
    "_gchmML4Q478zdFjhXf8rN",  # A4 Cultural Realism
    "_brNyzEdhzNAyxK8xC8hhm",  # A5 Sex Position
    "_YtKLMTwyMxNf1DNYqBx1t",  # A5.5 Scene Tone
    "_b9HgpUXtAW8VmTy82BPDV",  # A6 World Realism
    "_c8bEm1bWphwqFBXWRPrV8"   # A7 Queer Realism
]

ALYSSA_ID = "persona_1786335754946"
JASPER_ID = "1792155173728"
DUAL_IDS = [ALYSSA_ID, JASPER_ID]

TARGETS = [
    {
        "id": "char_scenario_88N1eQXqkbydKX9q9XQzp",
        "name": "Villa Douglas",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Villa_Douglas.json",
        "expected_rev": 2,
        "mode": "dual",
        "expected_greetings": 5
    },
    {
        "id": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
        "name": "Camp Mystic",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Camp_Mystic.json",
        "expected_rev": 2,
        "mode": "dual",
        "expected_greetings": 4
    },
    {
        "id": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
        "name": "DMHA Dungeons",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_DMHA_Dungeons.json",
        "expected_rev": 2,
        "mode": "dual",
        "expected_greetings": 4
    },
    {
        "id": "char_scenario_rrUCdBPH6WTNyBnQkMAKR",
        "name": "Underworld Sindacato",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Underworld_Sindacato.json",
        "expected_rev": 2,
        "mode": "dual",
        "expected_greetings": 4
    },
    {
        "id": "char_scenario_CKgwq246DyCj1NNTBV9rt",
        "name": "SUCC Route Alyssa",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "expected_rev": 2,
        "mode": "alyssa",
        "expected_greetings": 6
    },
    {
        "id": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
        "name": "SUCC Route Jasper",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json",
        "expected_rev": 2,
        "mode": "jasper",
        "expected_greetings": 5
    },
    {
        "id": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
        "name": "Master Scenario",
        "file": ROOT / "FINAL" / "Svartulfr_Master_Scenario.json",
        "expected_rev": 28,
        "mode": "master",
        "expected_greetings": 29
    }
]

def run_audit():
    token_file = ROOT / 'scratch' / 'wyvern_token.txt'
    if not token_file.exists():
        print("FAIL: Token file does not exist")
        return False
    
    token = token_file.read_text(encoding='utf-8').strip()
    if not token or len(token) < 20:
        print("FAIL: Token file is empty or invalid")
        return False

    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 ForensicAuditor/1.0'
    }

    audit_log = []
    all_passed = True

    print("\n" + "="*80)
    print("STARTING FORENSIC INTEGRITY AUDIT: 7 CHARACTER SCENARIOS")
    print("="*80)

    for target in TARGETS:
        t_id = target["id"]
        t_name = target["name"]
        t_file = target["file"]
        exp_rev = target["expected_rev"]
        mode = target["mode"]
        exp_greetings = target["expected_greetings"]

        print(f"\n[AUDIT TARGET] {t_name} ({t_id})")
        target_log = {
            "id": t_id,
            "name": t_name,
            "file": str(t_file),
            "checks": {}
        }

        # 1. Local file integrity
        if not t_file.exists():
            print(f"  [FAIL] Local file does not exist: {t_file}")
            target_log["checks"]["local_file_exists"] = "FAIL"
            all_passed = False
            continue
        target_log["checks"]["local_file_exists"] = "PASS"

        try:
            with open(t_file, 'r', encoding='utf-8') as f:
                local_raw = f.read()
                local_data = json.loads(local_raw)
            target_log["checks"]["local_json_valid"] = "PASS"
        except Exception as e:
            print(f"  [FAIL] Local file JSON corrupt: {e}")
            target_log["checks"]["local_json_valid"] = f"FAIL: {e}"
            all_passed = False
            continue

        # Check local fields
        loc_rev = local_data.get("revision")
        loc_lbs = local_data.get("lorebook_ids", [])
        loc_vis = local_data.get("visibility")
        loc_greetings = local_data.get("greetings", [])

        if loc_rev != exp_rev:
            print(f"  [FAIL] Local revision mismatch: expected {exp_rev}, got {loc_rev}")
            target_log["checks"]["local_revision"] = f"FAIL (got {loc_rev})"
            all_passed = False
        else:
            target_log["checks"]["local_revision"] = "PASS"

        if loc_lbs != CANONICAL_LOREBOOK_IDS:
            print(f"  [FAIL] Local lorebook IDs do not match canonical suite: {loc_lbs}")
            target_log["checks"]["local_lorebooks"] = "FAIL"
            all_passed = False
        else:
            target_log["checks"]["local_lorebooks"] = "PASS"

        if loc_vis != "private":
            print(f"  [FAIL] Local visibility is not private: {loc_vis}")
            target_log["checks"]["local_visibility"] = "FAIL"
            all_passed = False
        else:
            target_log["checks"]["local_visibility"] = "PASS"

        if len(loc_greetings) != exp_greetings:
            print(f"  [FAIL] Local greetings count mismatch: expected {exp_greetings}, got {len(loc_greetings)}")
            target_log["checks"]["local_greetings_count"] = "FAIL"
            all_passed = False
        else:
            target_log["checks"]["local_greetings_count"] = "PASS"

        # 2. Live API Direct Empirical Check
        api_url = f"https://app.wyvern.chat/api/character-scenarios/{t_id}"
        try:
            resp = requests.get(api_url, headers=headers, timeout=15)
            target_log["http_status"] = resp.status_code
            target_log["server_headers"] = {
                "date": resp.headers.get("Date"),
                "cf-ray": resp.headers.get("cf-ray"),
                "content-type": resp.headers.get("content-type")
            }
        except Exception as e:
            print(f"  [FAIL] Live API request exception: {e}")
            target_log["checks"]["live_api_call"] = f"FAIL: {e}"
            all_passed = False
            continue

        if resp.status_code != 200:
            print(f"  [FAIL] Live API returned HTTP {resp.status_code}: {resp.text}")
            target_log["checks"]["live_api_status"] = f"FAIL (HTTP {resp.status_code})"
            all_passed = False
            continue
        target_log["checks"]["live_api_status"] = "PASS (HTTP 200)"

        live_data = resp.json()
        live_rev = live_data.get("revision")
        live_lbs = live_data.get("lorebook_ids", [])
        live_vis = live_data.get("visibility")
        live_greetings = live_data.get("greetings", [])

        # Check live revision
        if live_rev != exp_rev:
            print(f"  [FAIL] Live revision mismatch: expected {exp_rev}, got {live_rev}")
            target_log["checks"]["live_revision"] = f"FAIL (got {live_rev})"
            all_passed = False
        else:
            target_log["checks"]["live_revision"] = f"PASS (Rev {live_rev})"

        # Check live lorebooks
        if live_lbs != CANONICAL_LOREBOOK_IDS:
            print(f"  [FAIL] Live lorebooks do not match canonical sequence: {live_lbs}")
            target_log["checks"]["live_lorebooks"] = "FAIL"
            all_passed = False
        else:
            target_log["checks"]["live_lorebooks"] = "PASS (15 canonical IDs)"

        # Check live visibility
        if live_vis != "private":
            print(f"  [FAIL] Live visibility is not private: {live_vis}")
            target_log["checks"]["live_visibility"] = "FAIL"
            all_passed = False
        else:
            target_log["checks"]["live_visibility"] = "PASS"

        # Check live greetings count
        if len(live_greetings) != exp_greetings:
            print(f"  [FAIL] Live greetings count mismatch: expected {exp_greetings}, got {len(live_greetings)}")
            target_log["checks"]["live_greetings_count"] = "FAIL"
            all_passed = False
        else:
            target_log["checks"]["live_greetings_count"] = f"PASS ({len(live_greetings)} greetings)"

        # Check greeting personas on live and local
        greeting_audit_ok = True
        for g_idx, (lg, vg) in enumerate(zip(loc_greetings, live_greetings)):
            lg_pids = lg.get("linked_persona_ids", [])
            vg_pids = vg.get("linked_persona_ids", [])
            g_name = vg.get("name", "")

            # Live and local parity
            if lg_pids != vg_pids:
                print(f"  [FAIL] Greeting {g_idx} local/live persona mismatch: {lg_pids} vs {vg_pids}")
                greeting_audit_ok = False
                break

            # Mode verification
            if mode == "dual":
                if set(vg_pids) != set(DUAL_IDS):
                    print(f"  [FAIL] Dual scenario greeting {g_idx} personas invalid: {vg_pids}")
                    greeting_audit_ok = False
                    break
            elif mode == "alyssa":
                if vg_pids != [ALYSSA_ID]:
                    print(f"  [FAIL] Alyssa scenario greeting {g_idx} personas invalid: {vg_pids}")
                    greeting_audit_ok = False
                    break
            elif mode == "jasper":
                if vg_pids != [JASPER_ID]:
                    print(f"  [FAIL] Jasper scenario greeting {g_idx} personas invalid: {vg_pids}")
                    greeting_audit_ok = False
                    break
            elif mode == "master":
                if "[FemPOV]" in g_name:
                    if vg_pids != [ALYSSA_ID]:
                        print(f"  [FAIL] Master FemPOV greeting {g_idx} personas invalid: {vg_pids}")
                        greeting_audit_ok = False
                        break
                elif "[MalePOV]" in g_name:
                    if vg_pids != [JASPER_ID]:
                        print(f"  [FAIL] Master MalePOV greeting {g_idx} personas invalid: {vg_pids}")
                        greeting_audit_ok = False
                        break
                else:
                    if set(vg_pids) != set(DUAL_IDS):
                        print(f"  [FAIL] Master dual greeting {g_idx} personas invalid: {vg_pids}")
                        greeting_audit_ok = False
                        break

        if greeting_audit_ok:
            target_log["checks"]["greeting_personas"] = "PASS"
            print(f"  [PASS] All {exp_greetings} greetings correctly configured with personas.")
        else:
            target_log["checks"]["greeting_personas"] = "FAIL"
            all_passed = False

        print(f"  -> Target {t_name} status: {'PASSED' if greeting_audit_ok and target_log['checks']['live_revision'] == f'PASS (Rev {exp_rev})' else 'FAILED'}")
        audit_log.append(target_log)

    # Save detailed forensic log
    report_file = AUDITOR_DIR / "forensic_api_audit_log.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(audit_log, f, indent=2, ensure_ascii=False)

    print("\n" + "="*80)
    print(f"FORENSIC AUDIT RESULT: {'CLEAN - ALL CHECKS PASSED' if all_passed else 'INTEGRITY VIOLATION DETECTED'}")
    print(f"Detailed log saved to: {report_file}")
    print("="*80)
    return all_passed

if __name__ == '__main__':
    ok = run_audit()
    sys.exit(0 if ok else 1)
