import json
import requests
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

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

ALYSSA_PERSONA = "persona_1786335754946"
JASPER_PERSONA = "1792155173728"
DUAL_PERSONAS = [ALYSSA_PERSONA, JASPER_PERSONA]

SCENARIO_SPECS = [
    {
        "name": "Master Scenario",
        "id": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
        "local_path": ROOT / "FINAL" / "Svartulfr_Master_Scenario.json",
        "expected_revision": 28,
        "mode": "master",
        "expected_slots_count": 13,
        "expected_greetings_count": 29
    },
    {
        "name": "Villa Douglas",
        "id": "char_scenario_88N1eQXqkbydKX9q9XQzp",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Villa_Douglas.json",
        "expected_revision": 2,
        "mode": "dual",
        "expected_slots_count": 7,
        "expected_greetings_count": 5
    },
    {
        "name": "Camp Mystic",
        "id": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Camp_Mystic.json",
        "expected_revision": 2,
        "mode": "dual",
        "expected_slots_count": 8,
        "expected_greetings_count": 4
    },
    {
        "name": "DMHA Dungeons",
        "id": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_DMHA_Dungeons.json",
        "expected_revision": 2,
        "mode": "dual",
        "expected_slots_count": 9,
        "expected_greetings_count": 4
    },
    {
        "name": "Underworld Sindacato",
        "id": "char_scenario_rrUCdBPH6WTNyBnQkMAKR",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Underworld_Sindacato.json",
        "expected_revision": 2,
        "mode": "dual",
        "expected_slots_count": 6,
        "expected_greetings_count": 4
    },
    {
        "name": "SUCC Route Alyssa",
        "id": "char_scenario_CKgwq246DyCj1NNTBV9rt",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "expected_revision": 2,
        "mode": "alyssa",
        "expected_slots_count": 8,
        "expected_greetings_count": 6
    },
    {
        "name": "SUCC Route Jasper",
        "id": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json",
        "expected_revision": 2,
        "mode": "jasper",
        "expected_slots_count": 8,
        "expected_greetings_count": 5
    }
]

def run_parity_review():
    token_path = ROOT / 'scratch' / 'wyvern_token.txt'
    if not token_path.exists():
        print(f"ERROR: Token file not found at {token_path}")
        sys.exit(1)
        
    token = token_path.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    report = {
        "summary": {},
        "scenarios": {},
        "failures": []
    }

    print("=" * 80)
    print("REVIEWER 2: INDEPENDENT LIVE API & LOCAL SCHEMA PARITY AUDIT")
    print("=" * 80)

    for spec in SCENARIO_SPECS:
        s_name = spec["name"]
        s_id = spec["id"]
        loc_path = spec["local_path"]
        exp_rev = spec["expected_revision"]
        mode = spec["mode"]
        exp_slots = spec["expected_slots_count"]
        exp_greetings = spec["expected_greetings_count"]

        print(f"\n[AUDITING] {s_name} ({s_id})")
        sc_report = {
            "name": s_name,
            "id": s_id,
            "checks": {},
            "diffs": []
        }

        # 1. Load Local JSON
        if not loc_path.exists():
            msg = f"Local file missing: {loc_path}"
            print(f"  FAIL: {msg}")
            report["failures"].append(msg)
            continue

        with open(loc_path, 'r', encoding='utf-8') as f:
            local_data = json.load(f)

        # 2. Fetch Live Wyvern API Data
        url = f"https://app.wyvern.chat/api/character-scenarios/{s_id}"
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code != 200:
            msg = f"API GET returned HTTP {resp.status_code} for {s_id}: {resp.text}"
            print(f"  FAIL: {msg}")
            report["failures"].append(msg)
            continue

        live_data = resp.json()

        # Check A: ID Parity
        local_id = local_data.get("id")
        live_id = live_data.get("id")
        id_ok = (local_id == s_id == live_id)
        sc_report["checks"]["id_parity"] = {"pass": id_ok, "local": local_id, "live": live_id}
        if not id_ok:
            sc_report["diffs"].append(f"ID mismatch: local={local_id}, live={live_id}, expected={s_id}")

        # Check B: Revision
        local_rev = local_data.get("revision")
        live_rev = live_data.get("revision")
        rev_ok = (local_rev == exp_rev and live_rev == exp_rev)
        sc_report["checks"]["revision"] = {"pass": rev_ok, "local": local_rev, "live": live_rev, "expected": exp_rev}
        if not rev_ok:
            sc_report["diffs"].append(f"Revision mismatch: local={local_rev}, live={live_rev}, expected={exp_rev}")

        # Check C: Visibility Private
        local_vis = local_data.get("visibility")
        live_vis = live_data.get("visibility")
        vis_ok = (local_vis == "private" and live_vis == "private")
        sc_report["checks"]["visibility_private"] = {"pass": vis_ok, "local": local_vis, "live": live_vis}
        if not vis_ok:
            sc_report["diffs"].append(f"Visibility is not 'private': local={local_vis}, live={live_vis}")

        # Check D: Lorebook IDs Parity (Count and Sequence)
        local_lbs = local_data.get("lorebook_ids", [])
        live_lbs = live_data.get("lorebook_ids", [])
        lbs_count_ok = (len(local_lbs) == 15 and len(live_lbs) == 15)
        lbs_match_canonical_local = (local_lbs == CANONICAL_LOREBOOK_IDS)
        lbs_match_canonical_live = (live_lbs == CANONICAL_LOREBOOK_IDS)
        lbs_match_exact = (local_lbs == live_lbs)
        lbs_ok = (lbs_count_ok and lbs_match_canonical_local and lbs_match_canonical_live and lbs_match_exact)
        sc_report["checks"]["lorebook_ids_canonical_15"] = {
            "pass": lbs_ok,
            "local_len": len(local_lbs),
            "live_len": len(live_lbs),
            "exact_sequence_match": lbs_ok
        }
        if not lbs_ok:
            sc_report["diffs"].append(f"Lorebook IDs mismatch: local_len={len(local_lbs)}, live_len={len(live_lbs)}, canonical_match={lbs_match_canonical_live}")

        # Check E: Slots Parity (Count and Slot Structure)
        local_slots = local_data.get("slots", [])
        live_slots = live_data.get("slots", [])
        slots_count_ok = (len(local_slots) == exp_slots and len(live_slots) == exp_slots)
        
        # Verify slot content matching
        slots_match = True
        slot_diffs = []
        if len(local_slots) != len(live_slots):
            slots_match = False
            slot_diffs.append(f"Slot count mismatch: local={len(local_slots)}, live={len(live_slots)}")
        else:
            for idx, (ls, vs) in enumerate(zip(local_slots, live_slots)):
                for k in ["key", "label", "unavailable_count", "pool", "default_char_id"]:
                    ls_v = ls.get(k)
                    vs_v = vs.get(k)
                    if ls_v != vs_v:
                        slots_match = False
                        slot_diffs.append(f"Slot {idx} ({ls.get('key')}) key '{k}' mismatch: local={ls_v} vs live={vs_v}")
        
        sc_report["checks"]["slots"] = {
            "pass": (slots_count_ok and slots_match),
            "expected_count": exp_slots,
            "local_count": len(local_slots),
            "live_count": len(live_slots),
            "diffs": slot_diffs
        }
        if not (slots_count_ok and slots_match):
            sc_report["diffs"].extend(slot_diffs)

        # Check F: Startup Script
        local_script = local_data.get("startup_script", "")
        live_script = live_data.get("startup_script", "")
        script_match = (local_script == live_script)
        sc_report["checks"]["startup_script_parity"] = {
            "pass": script_match,
            "has_script": bool(live_script),
            "len_local": len(local_script),
            "len_live": len(live_script)
        }
        if not script_match:
            sc_report["diffs"].append(f"Startup script mismatch: len_local={len(local_script)}, len_live={len(live_script)}")

        # Check G: Scenario Text Parity
        local_sc_text = local_data.get("scenario", "")
        live_sc_text = live_data.get("scenario", "")
        sc_text_match = (local_sc_text == live_sc_text)
        sc_report["checks"]["scenario_text_parity"] = {
            "pass": sc_text_match,
            "len_local": len(local_sc_text),
            "len_live": len(live_sc_text)
        }
        if not sc_text_match:
            sc_report["diffs"].append(f"Scenario text mismatch: len_local={len(local_sc_text)}, len_live={len(live_sc_text)}")

        # Check H: Greetings Parity & Linked Persona Routing
        local_greetings = local_data.get("greetings", [])
        live_greetings = live_data.get("greetings", [])
        greetings_count_ok = (len(local_greetings) == exp_greetings and len(live_greetings) == exp_greetings)

        greeting_errors = []
        greetings_parity = True

        for g_idx, (lg, vg) in enumerate(zip(local_greetings, live_greetings)):
            lg_name = lg.get("name", "")
            vg_name = vg.get("name", "")
            lg_pids = lg.get("linked_persona_ids", [])
            vg_pids = vg.get("linked_persona_ids", [])
            lg_msg = lg.get("message", "")
            vg_msg = vg.get("message", "")

            # Exact match between local and live
            if lg_name != vg_name:
                greetings_parity = False
                greeting_errors.append(f"Greeting {g_idx} name mismatch: local '{lg_name}' != live '{vg_name}'")
            if lg_pids != vg_pids:
                greetings_parity = False
                greeting_errors.append(f"Greeting {g_idx} linked_persona_ids mismatch: local {lg_pids} != live {vg_pids}")
            if lg_msg != vg_msg:
                greetings_parity = False
                greeting_errors.append(f"Greeting {g_idx} message text mismatch: len local {len(lg_msg)} != live {len(vg_msg)}")

            # Check linked_persona_ids rule compliance
            if mode == "dual":
                if set(vg_pids) != set(DUAL_PERSONAS) or len(vg_pids) != 2:
                    greeting_errors.append(f"Dual greeting {g_idx} ('{vg_name}') does not have exactly dual personas: got {vg_pids}")
            elif mode == "alyssa":
                if vg_pids != [ALYSSA_PERSONA]:
                    greeting_errors.append(f"Alyssa route greeting {g_idx} ('{vg_name}') expected [{ALYSSA_PERSONA}], got {vg_pids}")
            elif mode == "jasper":
                if vg_pids != [JASPER_PERSONA]:
                    greeting_errors.append(f"Jasper route greeting {g_idx} ('{vg_name}') expected [{JASPER_PERSONA}], got {vg_pids}")
            elif mode == "master":
                if "[FemPOV]" in vg_name:
                    if vg_pids != [ALYSSA_PERSONA]:
                        greeting_errors.append(f"Master FemPOV greeting {g_idx} ('{vg_name}') expected Alyssa only [{ALYSSA_PERSONA}], got {vg_pids}")
                elif "[MalePOV]" in vg_name:
                    if vg_pids != [JASPER_PERSONA]:
                        greeting_errors.append(f"Master MalePOV greeting {g_idx} ('{vg_name}') expected Jasper only [{JASPER_PERSONA}], got {vg_pids}")
                else:
                    if set(vg_pids) != set(DUAL_PERSONAS) or len(vg_pids) != 2:
                        greeting_errors.append(f"Master shared greeting {g_idx} ('{vg_name}') expected dual personas, got {vg_pids}")

        greetings_ok = (greetings_count_ok and greetings_parity and len(greeting_errors) == 0)
        sc_report["checks"]["greetings_and_persona_routing"] = {
            "pass": greetings_ok,
            "expected_count": exp_greetings,
            "local_count": len(local_greetings),
            "live_count": len(live_greetings),
            "errors": greeting_errors
        }
        if not greetings_ok:
            sc_report["diffs"].extend(greeting_errors)

        # Print quick status
        all_passed = (id_ok and rev_ok and vis_ok and lbs_ok and slots_count_ok and slots_match and script_match and sc_text_match and greetings_ok)
        print(f"  -> Revision: {live_rev} (Local: {local_rev}) [{'PASS' if rev_ok else 'FAIL'}]")
        print(f"  -> Lorebooks (15 canonical): [{'PASS' if lbs_ok else 'FAIL'}]")
        print(f"  -> Visibility Private: [{'PASS' if vis_ok else 'FAIL'}]")
        print(f"  -> Slots ({exp_slots}): [{'PASS' if (slots_count_ok and slots_match) else 'FAIL'}]")
        print(f"  -> Greetings ({exp_greetings}) & Persona IDs: [{'PASS' if greetings_ok else 'FAIL'}]")
        print(f"  -> Startup Script Parity: [{'PASS' if script_match else 'FAIL'}]")
        print(f"  -> Scenario Text Parity: [{'PASS' if sc_text_match else 'FAIL'}]")
        print(f"  -> Overall Scenario Status: [{'PASS' if all_passed else 'FAIL'}]")

        if not all_passed:
            report["failures"].append(f"{s_name} failed parity checks: {sc_report['diffs']}")

        report["scenarios"][s_name] = sc_report

    # Save detailed audit report for analysis.md
    out_json = ROOT / "scratch" / "reviewer2_audit_results.json"
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nWrote full audit JSON to {out_json}")

    print("\n" + "=" * 80)
    if len(report["failures"]) == 0:
        print("REVIEWER 2 VERDICT: ALL 7 SCENARIOS MEET 100% LIVE API & LOCAL SCHEMA PARITY!")
    else:
        print(f"REVIEWER 2 VERDICT: FAILURES DETECTED ({len(report['failures'])})")
        for f in report["failures"]:
            print(f" - {f}")
    print("=" * 80)

if __name__ == '__main__':
    run_parity_review()
