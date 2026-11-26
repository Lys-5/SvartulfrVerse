import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
live_data = json.load(open(ROOT / '.agents' / 'teamwork' / 'explorer_scenarios_15lb_2' / 'live_scenarios_inspection.json', encoding='utf-8'))

UNIFIED_15_LOREBOOKS = [
    "_gwwCxCfQ6PQaLEjAQVpJL", # Lorebook I
    "_HfG7TeV6MJyj6bxMwxkpt", # Lorebook II
    "_9zWTGqYJNJ4BCDMj8gfcD", # Lorebook III
    "_EjXxkmPVhpCXg8xABpFkK", # Location
    "_Uht3Ckz44JBDrPnUHq7LV", # NPC Secondary
    "_zwEqgEEzh12X6gHVmMKKC", # NPC Primary
    "_GV1KyHVY1RMbCnWgLkzDG", # A0 Behavioral Realism
    "_GbWJbkhgLzWexMHrjyUUc", # A1 Physics
    "_FaVcHfmrqcaJq8pa3WmRw", # A2 Social Realism
    "_BbrRgrcdGPMLEbBU2b6xk", # A3 Medical Realism
    "_gchmML4Q478zdFjhXf8rN", # A4 Cultural Realism
    "_brNyzEdhzNAyxK8xC8hhm", # A5 Sex Position
    "_YtKLMTwyMxNf1DNYqBx1t", # A5.5 Scene Tone
    "_b9HgpUXtAW8VmTy82BPDV", # A6 World Realism
    "_c8bEm1bWphwqFBXWRPrV8"  # A7 Queer Realism
]

ALYSSA_PERSONA = "persona_1786335754946"
JASPER_PERSONA = "1792155173728"
DUAL_PERSONAS = [ALYSSA_PERSONA, JASPER_PERSONA]

print(f"Unified Lorebooks count: {len(UNIFIED_15_LOREBOOKS)}")

# Simulate payload generation for each scenario
scenarios_cfg = {
    "char_scenario_88N1eQXqkbydKX9q9XQzp": {
        "file": "FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json",
        "name": "Villa Douglas",
        "mode": "dual",
        "expected_greetings": 5
    },
    "char_scenario_nLC84wrHdrbB6P3DEhwKb": {
        "file": "FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json",
        "name": "Camp Mystic",
        "mode": "dual",
        "expected_greetings": 4
    },
    "char_scenario_eqtRNnDpKbxDp7dmJmq6E": {
        "file": "FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json",
        "name": "DMHA Dungeons",
        "mode": "dual",
        "expected_greetings": 4
    },
    "char_scenario_rrUCdBPH6WTNyBnQkMAKR": {
        "file": "FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json",
        "name": "Underworld Sindacato",
        "mode": "dual",
        "expected_greetings": 4
    },
    "char_scenario_CKgwq246DyCj1NNTBV9rt": {
        "file": "FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json",
        "name": "SUCC Route Alyssa",
        "mode": "alyssa",
        "expected_greetings": 6
    },
    "char_scenario_Kq4mJEBH83j7Q7DdVfFnF": {
        "file": "FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json",
        "name": "SUCC Route Jasper",
        "mode": "jasper",
        "expected_greetings": 5
    },
    "char_scenario_1DC43ggb6mB8YLJDJKrU4": {
        "file": "FINAL/Svartulfr_Master_Scenario.json",
        "name": "Master Scenario",
        "mode": "master",
        "expected_greetings": 29
    }
}

payload_validation_report = {}

for sc_id, cfg in scenarios_cfg.items():
    fpath = ROOT / cfg["file"]
    data = json.loads(fpath.read_text(encoding='utf-8'))
    
    # Check greetings
    greetings = data.get('greetings', [])
    assert len(greetings) == cfg["expected_greetings"], f"Expected {cfg['expected_greetings']} greetings, found {len(greetings)}"
    
    updated_greetings = []
    for idx, g in enumerate(greetings):
        new_g = dict(g)
        if cfg["mode"] == "dual":
            target_personas = DUAL_PERSONAS
        elif cfg["mode"] == "alyssa":
            target_personas = [ALYSSA_PERSONA]
        elif cfg["mode"] == "jasper":
            target_personas = [JASPER_PERSONA]
        elif cfg["mode"] == "master":
            gname = g.get('name', '')
            gdesc = g.get('description', '')
            content = g.get('content', '')
            txt = f"{gname} {gdesc} {content[:80]}"
            if '[FemPOV]' in txt:
                target_personas = [ALYSSA_PERSONA]
            elif '[MalePOV]' in txt or 'Jasper in meta' in txt: # check exact logic
                target_personas = [JASPER_PERSONA]
            else:
                target_personas = DUAL_PERSONAS
        
        new_g['linked_persona_ids'] = target_personas
        updated_greetings.append(new_g)
        
    payload = {
        "name": data.get("name"),
        "display_description": data.get("display_description", ""),
        "avatar": data.get("avatar", ""),
        "tags": data.get("tags", []),
        "visibility": "private",
        "rating": data.get("rating", "explicit"),
        "scenario": data.get("scenario", ""),
        "startup_script": data.get("startup_script", ""),
        "slots": data.get("slots", []),
        "greetings": updated_greetings,
        "lorebook_ids": UNIFIED_15_LOREBOOKS,
        "gallery": data.get("gallery", []),
        "linked_world_id": data.get("linked_world_id", "")
    }
    
    payload_validation_report[cfg["name"]] = {
        "scenario_id": sc_id,
        "local_file": cfg["file"],
        "name": payload["name"],
        "visibility": payload["visibility"],
        "lorebook_ids_count": len(payload["lorebook_ids"]),
        "greetings_count": len(payload["greetings"]),
        "slots_count": len(payload["slots"]),
        "sample_greeting_lp": [g["linked_persona_ids"] for g in payload["greetings"]]
    }

out_path = ROOT / '.agents' / 'teamwork' / 'explorer_scenarios_15lb_2' / 'payload_validation_test.json'
out_path.write_text(json.dumps(payload_validation_report, indent=2), encoding='utf-8')
print("Payload validation report written to", out_path)
