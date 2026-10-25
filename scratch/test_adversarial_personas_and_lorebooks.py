import json
import pathlib
import sys
import requests

ROOT = pathlib.Path(r"e:\repository\SvartulfrVerse")
TOKEN_PATH = ROOT / "scratch" / "wyvern_token.txt"

# Canonical 15 Lorebook IDs in exact required order
CANONICAL_LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",  # 00: Svartúlfr - Lorebook I
    "_HfG7TeV6MJyj6bxMwxkpt",  # 01: Svartúlfr - Lorebook II
    "_9zWTGqYJNJ4BCDMj8gfcD",  # 02: Svartúlfr - Lorebook III
    "_EjXxkmPVhpCXg8xABpFkK",  # 03: Svartúlfr - Location
    "_Uht3Ckz44JBDrPnUHq7LV",  # 04: Svartúlfr - NPC Secondary
    "_zwEqgEEzh12X6gHVmMKKC",  # 05: Svartúlfr - NPC Primary
    "_GV1KyHVY1RMbCnWgLkzDG",  # 06: A0 Behavioral Realism
    "_GbWJbkhgLzWexMHrjyUUc",  # 07: A1 Physics
    "_FaVcHfmrqcaJq8pa3WmRw",  # 08: A2 Social Realism
    "_BbrRgrcdGPMLEbBU2b6xk",  # 09: A3 Medical Realism
    "_gchmML4Q478zdFjhXf8rN",  # 10: A4 Cultural Realism
    "_brNyzEdhzNAyxK8xC8hhm",  # 11: A5 Sex Position
    "_YtKLMTwyMxNf1DNYqBx1t",  # 12: A5.5 Scene Tone
    "_b9HgpUXtAW8VmTy82BPDV",  # 13: A6 World Realism
    "_c8bEm1bWphwqFBXWRPrV8",  # 14: A7 Queer Realism
]

# Canonical Persona IDs
ALYSSA_PERSONA_ID = "persona_1786335754946"
JASPER_PERSONA_ID = "1792155173728"
ALLOWED_PERSONA_IDS = {ALYSSA_PERSONA_ID, JASPER_PERSONA_ID}

SCENARIO_CONFIGS = [
    {
        "name": "Villa Douglas",
        "id": "char_scenario_88N1eQXqkbydKX9q9XQzp",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Villa_Douglas.json",
        "mode": "dual",
        "expected_greetings": 5,
        "expected_slots": 7,
    },
    {
        "name": "Camp Mystic",
        "id": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Camp_Mystic.json",
        "mode": "dual",
        "expected_greetings": 4,
        "expected_slots": 8,
    },
    {
        "name": "DMHA Dungeons",
        "id": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_DMHA_Dungeons.json",
        "mode": "dual",
        "expected_greetings": 4,
        "expected_slots": 9,
    },
    {
        "name": "Underworld Sindacato",
        "id": "char_scenario_rrUCdBPH6WTNyBnQkMAKR",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Underworld_Sindacato.json",
        "mode": "dual",
        "expected_greetings": 4,
        "expected_slots": 6,
    },
    {
        "name": "SUCC Route Alyssa",
        "id": "char_scenario_CKgwq246DyCj1NNTBV9rt",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "mode": "alyssa",
        "expected_greetings": 6,
        "expected_slots": 8,
    },
    {
        "name": "SUCC Route Jasper",
        "id": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
        "file": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json",
        "mode": "jasper",
        "expected_greetings": 5,
        "expected_slots": 8,
    },
    {
        "name": "Master Scenario",
        "id": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
        "file": ROOT / "FINAL" / "Svartulfr_Master_Scenario.json",
        "mode": "master",
        "expected_greetings": 29,
        "expected_slots": 13,
    },
]

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def load_token():
    assert TOKEN_PATH.exists(), f"Token file not found: {TOKEN_PATH}"
    token = TOKEN_PATH.read_text(encoding="utf-8").strip()
    assert len(token) > 20, "Token appears empty or too short"
    return token

def run_adversarial_suite():
    token = load_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }

    report = {
        "total_scenarios": len(SCENARIO_CONFIGS),
        "checks_passed": 0,
        "checks_failed": 0,
        "failures": [],
        "scenarios_details": {},
    }

    def record_check(scenario_name, check_name, condition, error_msg):
        if condition:
            report["checks_passed"] += 1
        else:
            report["checks_failed"] += 1
            err = f"[{scenario_name}] FAIL: {check_name} -> {error_msg}"
            report["failures"].append(err)
            print(f"  [FAIL] {err}")

    print("=" * 80)
    print("STARTING ADVERSARIAL STRESS TEST: 15 LOREBOOKS & PERSONA MAPPINGS")
    print("=" * 80)

    for cfg in SCENARIO_CONFIGS:
        sc_name = cfg["name"]
        sc_id = cfg["id"]
        sc_file = cfg["file"]
        mode = cfg["mode"]
        exp_greetings = cfg["expected_greetings"]
        exp_slots = cfg["expected_slots"]

        print(f"\n[+] Testing Scenario: '{sc_name}' ({sc_id})")
        sc_report = {"local": {}, "live": {}, "greetings": []}
        report["scenarios_details"][sc_name] = sc_report

        # ---------------------------------------------------------------------
        # 1. Local File Existence & JSON Parsing
        # ---------------------------------------------------------------------
        record_check(sc_name, "Local file exists", sc_file.exists(), f"File missing at {sc_file}")
        if not sc_file.exists():
            continue

        try:
            with open(sc_file, "r", encoding="utf-8") as f:
                loc_data = json.load(f)
        except Exception as e:
            record_check(sc_name, "Local file JSON valid", False, f"JSON parse error: {e}")
            continue

        # ---------------------------------------------------------------------
        # 2. Live API GET
        # ---------------------------------------------------------------------
        api_url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
        try:
            resp = requests.get(api_url, headers=headers, timeout=15)
            record_check(sc_name, "Live API HTTP 200", resp.status_code == 200, f"HTTP {resp.status_code}: {resp.text[:200]}")
            live_data = resp.json() if resp.status_code == 200 else None
        except Exception as e:
            record_check(sc_name, "Live API Request", False, f"Request exception: {e}")
            live_data = None

        if live_data is None:
            continue

        # ---------------------------------------------------------------------
        # 3. Revision & Visibility Parity
        # ---------------------------------------------------------------------
        loc_rev = loc_data.get("revision")
        live_rev = live_data.get("revision")
        record_check(sc_name, "Revision match", loc_rev == live_rev, f"Local rev {loc_rev} != Live rev {live_rev}")

        loc_vis = loc_data.get("visibility")
        live_vis = live_data.get("visibility")
        record_check(sc_name, "Local visibility private", loc_vis == "private", f"Got '{loc_vis}'")
        record_check(sc_name, "Live visibility private", live_vis == "private", f"Got '{live_vis}'")

        # ---------------------------------------------------------------------
        # 4. Slots Invariant Check
        # ---------------------------------------------------------------------
        loc_slots = loc_data.get("slots", [])
        live_slots = live_data.get("slots", [])
        record_check(sc_name, f"Slots count == {exp_slots}", len(loc_slots) == exp_slots, f"Local slots count {len(loc_slots)}")
        record_check(sc_name, "Slots match live count", len(loc_slots) == len(live_slots), f"Local {len(loc_slots)} != Live {len(live_slots)}")

        # ---------------------------------------------------------------------
        # 5. Lorebook IDs Strict Validation (Length, Exact Sequence, Blacklist)
        # ---------------------------------------------------------------------
        for env_label, data_obj in [("Local", loc_data), ("Live", live_data)]:
            lbs = data_obj.get("lorebook_ids", [])
            record_check(sc_name, f"{env_label} lorebook_ids is list", isinstance(lbs, list), f"Type is {type(lbs)}")
            record_check(sc_name, f"{env_label} lorebook_ids length == 15", len(lbs) == 15, f"Length is {len(lbs)}")
            record_check(sc_name, f"{env_label} lorebook_ids has no duplicates", len(lbs) == len(set(lbs)), f"Duplicates found in {lbs}")
            record_check(sc_name, f"{env_label} lorebook_ids exact canonical sequence", lbs == CANONICAL_LOREBOOK_IDS, f"Sequence mismatch: {lbs}")

            # Negative check: Blacklist deprecated or alien IDs
            for idx, lb_id in enumerate(lbs):
                record_check(sc_name, f"{env_label} LB #{idx} starts with '_'", lb_id.startswith("_"), f"Rogue ID: {lb_id}")
                record_check(sc_name, f"{env_label} LB #{idx} in canonical suite", lb_id in CANONICAL_LOREBOOK_IDS, f"Unexpected LB ID: {lb_id}")

        # ---------------------------------------------------------------------
        # 6. Persona Mappings & Routing Stress Testing
        # ---------------------------------------------------------------------
        loc_greetings = loc_data.get("greetings", [])
        live_greetings = live_data.get("greetings", [])

        record_check(sc_name, f"Local greetings count == {exp_greetings}", len(loc_greetings) == exp_greetings, f"Count {len(loc_greetings)}")
        record_check(sc_name, f"Live greetings count == {exp_greetings}", len(live_greetings) == exp_greetings, f"Count {len(live_greetings)}")

        # Detailed breakdown per greeting
        fempov_count = 0
        malepov_count = 0
        neutral_count = 0

        for g_idx in range(max(len(loc_greetings), len(live_greetings))):
            g_loc = loc_greetings[g_idx] if g_idx < len(loc_greetings) else {}
            g_live = live_greetings[g_idx] if g_idx < len(live_greetings) else {}

            g_name = g_loc.get("name") or g_live.get("name") or f"Greeting_{g_idx}"
            loc_pids = g_loc.get("linked_persona_ids")
            live_pids = g_live.get("linked_persona_ids")

            # Check: NO greeting has linked_persona_ids as None or empty []
            record_check(sc_name, f"G#{g_idx} local linked_persona_ids not None", loc_pids is not None, f"Local linked_persona_ids is None")
            record_check(sc_name, f"G#{g_idx} live linked_persona_ids not None", live_pids is not None, f"Live linked_persona_ids is None")
            record_check(sc_name, f"G#{g_idx} local linked_persona_ids not empty", bool(loc_pids), f"Local linked_persona_ids is empty")
            record_check(sc_name, f"G#{g_idx} live linked_persona_ids not empty", bool(live_pids), f"Live linked_persona_ids is empty")

            # Check: local and live match exactly
            record_check(sc_name, f"G#{g_idx} local vs live persona IDs match", loc_pids == live_pids, f"Local {loc_pids} != Live {live_pids}")

            if not loc_pids:
                continue

            # Check: no duplicates inside linked_persona_ids
            record_check(sc_name, f"G#{g_idx} no duplicate persona IDs", len(loc_pids) == len(set(loc_pids)), f"Duplicate IDs: {loc_pids}")

            # Check: no foreign/unauthorized persona IDs
            for pid in loc_pids:
                record_check(sc_name, f"G#{g_idx} ID {pid} in allowed set", pid in ALLOWED_PERSONA_IDS, f"Foreign persona ID found: {pid}")

            # Scenario-specific routing logic
            if mode == "dual":
                # Must contain BOTH Alyssa and Jasper, exactly 2 IDs
                record_check(sc_name, f"G#{g_idx} Dual length == 2", len(loc_pids) == 2, f"Length {len(loc_pids)}: {loc_pids}")
                record_check(sc_name, f"G#{g_idx} Dual contains Alyssa", ALYSSA_PERSONA_ID in loc_pids, f"Missing Alyssa: {loc_pids}")
                record_check(sc_name, f"G#{g_idx} Dual contains Jasper", JASPER_PERSONA_ID in loc_pids, f"Missing Jasper: {loc_pids}")
                neutral_count += 1

            elif mode == "alyssa":
                # Route Alyssa: ONLY Alyssa, NO Jasper, length == 1
                record_check(sc_name, f"G#{g_idx} Route Alyssa length == 1", len(loc_pids) == 1, f"Length {len(loc_pids)}: {loc_pids}")
                record_check(sc_name, f"G#{g_idx} Route Alyssa has Alyssa", loc_pids == [ALYSSA_PERSONA_ID], f"Mismatch: {loc_pids}")
                record_check(sc_name, f"G#{g_idx} Route Alyssa NEVER has Jasper", JASPER_PERSONA_ID not in loc_pids, f"Jasper found: {loc_pids}")
                fempov_count += 1

            elif mode == "jasper":
                # Route Jasper: ONLY Jasper, NO Alyssa, length == 1
                record_check(sc_name, f"G#{g_idx} Route Jasper length == 1", len(loc_pids) == 1, f"Length {len(loc_pids)}: {loc_pids}")
                record_check(sc_name, f"G#{g_idx} Route Jasper has Jasper", loc_pids == [JASPER_PERSONA_ID], f"Mismatch: {loc_pids}")
                record_check(sc_name, f"G#{g_idx} Route Jasper NEVER has Alyssa", ALYSSA_PERSONA_ID not in loc_pids, f"Alyssa found: {loc_pids}")
                malepov_count += 1

            elif mode == "master":
                # Master Scenario POV-specific checks
                is_fem = "[FemPOV]" in g_name
                is_male = "[MalePOV]" in g_name

                # Adversarial check: cannot have both tags simultaneously!
                record_check(sc_name, f"G#{g_idx} Not both FemPOV and MalePOV", not (is_fem and is_male), f"Ambiguous name: {g_name}")

                if is_fem:
                    fempov_count += 1
                    record_check(sc_name, f"G#{g_idx} [FemPOV] has Alyssa ONLY", loc_pids == [ALYSSA_PERSONA_ID], f"Mismatch for '{g_name}': {loc_pids}")
                    record_check(sc_name, f"G#{g_idx} [FemPOV] NO Jasper", JASPER_PERSONA_ID not in loc_pids, f"Jasper present in FemPOV '{g_name}'")
                elif is_male:
                    malepov_count += 1
                    record_check(sc_name, f"G#{g_idx} [MalePOV] has Jasper ONLY", loc_pids == [JASPER_PERSONA_ID], f"Mismatch for '{g_name}': {loc_pids}")
                    record_check(sc_name, f"G#{g_idx} [MalePOV] NO Alyssa", ALYSSA_PERSONA_ID not in loc_pids, f"Alyssa present in MalePOV '{g_name}'")
                else:
                    neutral_count += 1
                    record_check(sc_name, f"G#{g_idx} [Neutral] has Dual Personas", set(loc_pids) == {ALYSSA_PERSONA_ID, JASPER_PERSONA_ID}, f"Neutral missing dual personas: '{g_name}' -> {loc_pids}")

            sc_report["greetings"].append({
                "index": g_idx,
                "name": g_name,
                "linked_persona_ids": loc_pids,
            })

        if mode == "master":
            record_check(sc_name, "Master exactly 7 FemPOV greetings", fempov_count == 7, f"Got {fempov_count} FemPOV greetings")
            record_check(sc_name, "Master exactly 6 MalePOV greetings", malepov_count == 6, f"Got {malepov_count} MalePOV greetings")
            record_check(sc_name, "Master exactly 16 Neutral greetings", neutral_count == 16, f"Got {neutral_count} Neutral greetings")
            record_check(sc_name, "Master greeting sum 7+6+16 == 29", (fempov_count + malepov_count + neutral_count) == 29, f"Sum is {fempov_count + malepov_count + neutral_count}")

        print(f"  -> Greetings analyzed: {len(loc_greetings)} (FemPOV: {fempov_count}, MalePOV: {malepov_count}, Neutral/Dual: {neutral_count})")
        print(f"  -> Revision: {live_rev} | Lorebooks: {len(loc_data.get('lorebook_ids', []))} | Visibility: {live_vis}")

    # ---------------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("STRESS TEST EXECUTION SUMMARY")
    print("=" * 80)
    print(f"Total Checks Executed : {report['checks_passed'] + report['checks_failed']}")
    print(f"Total Passed          : {report['checks_passed']}")
    print(f"Total Failed          : {report['checks_failed']}")

    if report["checks_failed"] == 0:
        print("\n🎉 ALL ADVERSARIAL STRESS TESTS PASSED WITH 0 DEFECTS!")
        verdict = "APPROVE"
    else:
        print(f"\n⚠️ FOUND {report['checks_failed']} FAILURES!")
        for f in report["failures"]:
            print(f" - {f}")
        verdict = "REQUEST_CHANGES"

    report["verdict"] = verdict

    out_json = ROOT / "scratch" / "challenger_stress_test_report.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\nDetailed report written to: {out_json}")

    return report

if __name__ == "__main__":
    rep = run_adversarial_suite()
    if rep["checks_failed"] > 0:
        sys.exit(1)
    sys.exit(0)
