import json
import requests
import pathlib

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

ALYSSA_PERSONA_ID = "persona_1786335754946"
JASPER_PERSONA_ID = "1792155173728"
DUAL_PERSONA_IDS = [ALYSSA_PERSONA_ID, JASPER_PERSONA_ID]

SCENARIOS = [
    {
        "name": "Villa Douglas",
        "id": "char_scenario_88N1eQXqkbydKX9q9XQzp",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Villa_Douglas.json",
        "mode": "dual",
        "expected_greetings": 5
    },
    {
        "name": "Camp Mystic",
        "id": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Camp_Mystic.json",
        "mode": "dual",
        "expected_greetings": 4
    },
    {
        "name": "DMHA Dungeons",
        "id": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_DMHA_Dungeons.json",
        "mode": "dual",
        "expected_greetings": 4
    },
    {
        "name": "Underworld Sindacato",
        "id": "char_scenario_rrUCdBPH6WTNyBnQkMAKR",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Underworld_Sindacato.json",
        "mode": "dual",
        "expected_greetings": 4
    },
    {
        "name": "SUCC Route Alyssa",
        "id": "char_scenario_CKgwq246DyCj1NNTBV9rt",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "mode": "alyssa",
        "expected_greetings": 6
    },
    {
        "name": "SUCC Route Jasper",
        "id": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json",
        "mode": "jasper",
        "expected_greetings": 5
    },
    {
        "name": "Master Scenario",
        "id": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
        "local_path": ROOT / "FINAL" / "Svartulfr_Master_Scenario.json",
        "mode": "master",
        "expected_greetings": 29
    }
]

def verify_all():
    token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    all_passed = True
    print("="*80)
    print("INDEPENDENT VERIFICATION OF 7 CHARACTER SCENARIOS (LIVE API & LOCAL FILES)")
    print("="*80)

    for sc in SCENARIOS:
        name = sc["name"]
        sc_id = sc["id"]
        local_path = sc["local_path"]
        mode = sc["mode"]
        exp_greetings = sc["expected_greetings"]

        print(f"\nVerifying '{name}' ({sc_id})...")

        # 1. Check local file exists and parses
        assert local_path.exists(), f"Local file does not exist: {local_path}"
        with open(local_path, "r", encoding="utf-8") as f:
            loc = json.load(f)

        assert loc.get("visibility") == "private", f"Local visibility is not private: {loc.get('visibility')}"
        loc_lbs = loc.get("lorebook_ids", [])
        assert len(loc_lbs) == 15, f"Local lorebook_ids length != 15: {len(loc_lbs)}"
        assert loc_lbs == CANONICAL_LOREBOOK_IDS, "Local lorebook_ids do not match canonical order!"

        loc_greetings = loc.get("greetings", [])
        assert len(loc_greetings) == exp_greetings, f"Local greetings count {len(loc_greetings)} != {exp_greetings}"

        # 2. Check live API
        resp = requests.get(f"https://app.wyvern.chat/api/character-scenarios/{sc_id}", headers=headers)
        assert resp.status_code == 200, f"Live GET failed: HTTP {resp.status_code} - {resp.text}"
        live = resp.json()

        assert live.get("visibility") == "private", f"Live visibility is not private: {live.get('visibility')}"
        live_lbs = live.get("lorebook_ids", [])
        assert len(live_lbs) == 15, f"Live lorebook_ids length != 15: {len(live_lbs)}"
        assert live_lbs == CANONICAL_LOREBOOK_IDS, "Live lorebook_ids do not match canonical order!"

        live_greetings = live.get("greetings", [])
        assert len(live_greetings) == exp_greetings, f"Live greetings count {len(live_greetings)} != {exp_greetings}"

        # 3. Check revision matches
        assert loc.get("revision") == live.get("revision"), f"Revision mismatch: local {loc.get('revision')} != live {live.get('revision')}"

        # 4. Check linked_persona_ids on both local and live
        dual_count = 0
        alyssa_count = 0
        jasper_count = 0

        for i, (lg, vg) in enumerate(zip(loc_greetings, live_greetings)):
            lg_pids = lg.get("linked_persona_ids", [])
            vg_pids = vg.get("linked_persona_ids", [])
            gname = lg.get("name", "")

            # Verify local and live match
            assert lg_pids == vg_pids, f"Greeting {i} persona ID mismatch between local and live: {lg_pids} vs {vg_pids}"

            if mode == "dual":
                assert set(lg_pids) == set(DUAL_PERSONA_IDS), f"Greeting {i} in dual scenario lacks dual personas: {lg_pids}"
                dual_count += 1
            elif mode == "alyssa":
                assert lg_pids == [ALYSSA_PERSONA_ID], f"Greeting {i} in Alyssa scenario expected Alyssa only: {lg_pids}"
                alyssa_count += 1
            elif mode == "jasper":
                assert lg_pids == [JASPER_PERSONA_ID], f"Greeting {i} in Jasper scenario expected Jasper only: {lg_pids}"
                jasper_count += 1
            elif mode == "master":
                if "[FemPOV]" in gname:
                    assert lg_pids == [ALYSSA_PERSONA_ID], f"Master FemPOV greeting {i} expected Alyssa only: {lg_pids}"
                    alyssa_count += 1
                elif "[MalePOV]" in gname:
                    assert lg_pids == [JASPER_PERSONA_ID], f"Master MalePOV greeting {i} expected Jasper only: {lg_pids}"
                    jasper_count += 1
                else:
                    assert set(lg_pids) == set(DUAL_PERSONA_IDS), f"Master neutral greeting {i} lacks dual personas: {lg_pids}"
                    dual_count += 1

        print(f"  [OK] Revision: {live.get('revision')}")
        print(f"  [OK] 15 Lorebooks Canonical Sequence: Verified")
        print(f"  [OK] Visibility: private")
        print(f"  [OK] Greetings: {exp_greetings} total (Dual: {dual_count}, Alyssa: {alyssa_count}, Jasper: {jasper_count})")
        print(f"  [OK] Local file synchronized: {local_path.name}")

    print("\n" + "="*80)
    print("ALL VERIFICATION CHECKS PASSED PERFECTLY (100% COMPLIANT)!")
    print("="*80)

if __name__ == "__main__":
    verify_all()
