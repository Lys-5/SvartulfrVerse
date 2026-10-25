import json
import time
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

ALYSSA_PERSONA_OBJ = {
    "persona_id": "persona_1786335754946",
    "name": "Alyssa",
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public",
    "title": "The White Moon",
    "comment": "Seven Hills Pack Princess & Dominant Omega Healer"
}

JASPER_PERSONA_OBJ = {
    "persona_id": "1792155173728",
    "name": "Jasper",
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public",
    "title": "Jasper Svartr Douglas Bloodmoon",
    "comment": "MalePOV Twin Protagonist — Technomancer & Cyber-Mage at SUCC"
}

DUAL_PERSONA_OBJS = [ALYSSA_PERSONA_OBJ, JASPER_PERSONA_OBJ]

SCENARIO_CONFIGS = [
    {
        "name": "Villa Douglas",
        "id": "char_scenario_88N1eQXqkbydKX9q9XQzp",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Villa_Douglas.json",
        "mode": "dual"
    },
    {
        "name": "Camp Mystic",
        "id": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Camp_Mystic.json",
        "mode": "dual"
    },
    {
        "name": "DMHA Dungeons",
        "id": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_DMHA_Dungeons.json",
        "mode": "dual"
    },
    {
        "name": "Underworld Sindacato",
        "id": "char_scenario_rrUCdBPH6WTNyBnQkMAKR",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_Underworld_Sindacato.json",
        "mode": "dual"
    },
    {
        "name": "SUCC Route Alyssa",
        "id": "char_scenario_CKgwq246DyCj1NNTBV9rt",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "mode": "alyssa"
    },
    {
        "name": "SUCC Route Jasper",
        "id": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json",
        "mode": "jasper"
    },
    {
        "name": "Master Scenario",
        "id": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
        "local_path": ROOT / "FINAL" / "Svartulfr_Master_Scenario.json",
        "mode": "master"
    }
]

def get_headers():
    token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

def update_scenario(cfg):
    name = cfg["name"]
    sc_id = cfg["id"]
    local_path = cfg["local_path"]
    mode = cfg["mode"]
    
    print("\n" + "="*70)
    print(f"PROCESSING: {name} ({sc_id}) | Mode: {mode}")
    print("="*70)
    
    headers = get_headers()
    
    # 1. Fetch fresh live state to get current revision
    get_url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
    resp_get = requests.get(get_url, headers=headers)
    if resp_get.status_code != 200:
        raise RuntimeError(f"GET failed for {sc_id}: HTTP {resp_get.status_code} - {resp_get.text}")
    
    live_data = resp_get.json()
    live_rev = live_data.get("revision", 1)
    print(f"  [GET] Current live revision: {live_rev}")
    print(f"  [GET] Current live lorebook count: {len(live_data.get('lorebook_ids', []))}")
    print(f"  [GET] Current live greetings count: {len(live_data.get('greetings', []))}")
    
    # 2. Read local JSON file
    with open(local_path, "r", encoding="utf-8") as f:
        local_data = json.load(f)
    
    # 3. Update Lorebook IDs in canonical order
    local_data["lorebook_ids"] = list(CANONICAL_LOREBOOK_IDS)
    
    # 4. Update linked_persona_ids on greetings
    greetings = local_data.get("greetings", [])
    
    if mode == "dual":
        for g in greetings:
            g["linked_persona_ids"] = list(DUAL_PERSONA_IDS)
    elif mode == "alyssa":
        for g in greetings:
            g["linked_persona_ids"] = [ALYSSA_PERSONA_ID]
    elif mode == "jasper":
        for g in greetings:
            g["linked_persona_ids"] = [JASPER_PERSONA_ID]
    elif mode == "master":
        for idx, g in enumerate(greetings):
            gid = g.get("id", "")
            gname = g.get("name", "")
            current_pids = g.get("linked_persona_ids", [])
            
            # Check POV tag
            if "[FemPOV]" in gname or current_pids == [ALYSSA_PERSONA_ID]:
                g["linked_persona_ids"] = [ALYSSA_PERSONA_ID]
                g["linked_personas"] = [ALYSSA_PERSONA_OBJ]
                print(f"    Master greeting [{idx:02d}] '{gname[:40]}...': PRESERVED FemPOV Alyssa")
            elif "[MalePOV]" in gname or current_pids == [JASPER_PERSONA_ID]:
                g["linked_persona_ids"] = [JASPER_PERSONA_ID]
                g["linked_personas"] = [JASPER_PERSONA_OBJ]
                print(f"    Master greeting [{idx:02d}] '{gname[:40]}...': PRESERVED MalePOV Jasper")
            else:
                g["linked_persona_ids"] = list(DUAL_PERSONA_IDS)
                g["linked_personas"] = list(DUAL_PERSONA_OBJS)
                print(f"    Master greeting [{idx:02d}] '{gname[:40]}...': ASSIGNED Dual (Alyssa & Jasper)")
    
    # 5. Build PUT payload
    put_payload = {
        "name": local_data.get("name"),
        "display_description": local_data.get("display_description", ""),
        "avatar": local_data.get("avatar", ""),
        "tags": local_data.get("tags", []),
        "visibility": "private",
        "rating": local_data.get("rating", "explicit"),
        "revision": live_rev,
        "linked_world_id": local_data.get("linked_world_id", ""),
        "scenario": local_data.get("scenario", ""),
        "startup_script": local_data.get("startup_script", ""),
        "slots": local_data.get("slots", []),
        "greetings": greetings,
        "lorebook_ids": CANONICAL_LOREBOOK_IDS,
        "gallery": local_data.get("gallery", [])
    }
    
    # 6. Issue PUT request
    put_url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
    resp_put = requests.put(put_url, headers=headers, json=put_payload)
    if resp_put.status_code != 200:
        raise RuntimeError(f"PUT failed for {sc_id}: HTTP {resp_put.status_code} - {resp_put.text}")
    
    put_res = resp_put.json()
    new_rev = put_res.get("revision", live_rev + 1)
    print(f"  [PUT SUCCESS] HTTP 200! New revision: {new_rev}")
    
    # Pacing delay
    time.sleep(2.5)
    
    # 7. Post-PUT GET verification
    resp_verify = requests.get(get_url, headers=headers)
    if resp_verify.status_code != 200:
        raise RuntimeError(f"Post-PUT GET failed for {sc_id}: HTTP {resp_verify.status_code} - {resp_verify.text}")
    
    verify_data = resp_verify.json()
    ver_rev = verify_data.get("revision")
    ver_lbs = verify_data.get("lorebook_ids", [])
    ver_greetings = verify_data.get("greetings", [])
    
    assert len(ver_lbs) == 15, f"Expected 15 lorebook IDs, got {len(ver_lbs)}"
    assert ver_lbs == CANONICAL_LOREBOOK_IDS, "Lorebook IDs do not match canonical order!"
    
    for idx, vg in enumerate(ver_greetings):
        vg_pids = vg.get("linked_persona_ids", [])
        vg_name = vg.get("name", "")
        if mode == "dual":
            assert set(vg_pids) == set(DUAL_PERSONA_IDS), f"Greeting {idx} missing dual personas: {vg_pids}"
        elif mode == "alyssa":
            assert vg_pids == [ALYSSA_PERSONA_ID], f"Greeting {idx} expected Alyssa only: {vg_pids}"
        elif mode == "jasper":
            assert vg_pids == [JASPER_PERSONA_ID], f"Greeting {idx} expected Jasper only: {vg_pids}"
        elif mode == "master":
            if "[FemPOV]" in vg_name:
                assert vg_pids == [ALYSSA_PERSONA_ID], f"Master FemPOV greeting {idx} failed: {vg_pids}"
            elif "[MalePOV]" in vg_name:
                assert vg_pids == [JASPER_PERSONA_ID], f"Master MalePOV greeting {idx} failed: {vg_pids}"
            else:
                assert set(vg_pids) == set(DUAL_PERSONA_IDS), f"Master dual greeting {idx} failed: {vg_pids}"
    
    print(f"  [VERIFY OK] Remote state confirmed: {len(ver_lbs)} LBs, {len(ver_greetings)} greetings, Rev {ver_rev}")
    
    # 8. Update local JSON file with verified state
    # Update local file revision and ensured fields
    local_data["revision"] = ver_rev
    local_data["lorebook_ids"] = list(CANONICAL_LOREBOOK_IDS)
    local_data["greetings"] = greetings
    local_data["visibility"] = "private"
    
    with open(local_path, "w", encoding="utf-8") as f:
        json.dump(local_data, f, indent=2, ensure_ascii=False)
    
    print(f"  [LOCAL SAVED] Updated {local_path.name} (Rev: {ver_rev})")
    
    return {
        "scenario_id": sc_id,
        "name": name,
        "mode": mode,
        "old_rev": live_rev,
        "new_rev": ver_rev,
        "lorebook_count": len(ver_lbs),
        "greetings_count": len(ver_greetings),
        "status": "SUCCESS"
    }

def main():
    results = []
    print("Starting Svartúlfr Character Scenarios 15-Lorebook & Persona Update...")
    for cfg in SCENARIO_CONFIGS:
        res = update_scenario(cfg)
        results.append(res)
    
    summary_path = ROOT / "scratch" / "scenarios_15lb_update_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("ALL 7 SCENARIOS SUCCESSFULLY UPDATED AND VERIFIED!")
    print(f"Summary written to {summary_path}")
    print("="*70)

if __name__ == "__main__":
    main()
