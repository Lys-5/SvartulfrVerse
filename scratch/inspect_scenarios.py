import json
import requests

scenarios = [
    ('Master Scenario', 'char_scenario_1DC43ggb6mB8YLJDJKrU4', 'FINAL/Svartulfr_Master_Scenario.json', 'master'),
    ('Villa Douglas', 'char_scenario_88N1eQXqkbydKX9q9XQzp', 'FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json', 'dual'),
    ('Camp Mystic', 'char_scenario_nLC84wrHdrbB6P3DEhwKb', 'FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json', 'dual'),
    ('DMHA Dungeons', 'char_scenario_eqtRNnDpKbxDp7dmJmq6E', 'FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json', 'dual'),
    ('Underworld Sindacato', 'char_scenario_rrUCdBPH6WTNyBnQkMAKR', 'FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json', 'dual'),
    ('SUCC Route Alyssa', 'char_scenario_CKgwq246DyCj1NNTBV9rt', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'alyssa'),
    ('SUCC Route Jasper', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json', 'jasper'),
]

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

for name, sc_id, local_path, mode in scenarios:
    resp = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    print(f'=== {name} ({sc_id}) ===')
    if resp.status_code == 200:
        data = resp.json()
        rev = data.get("revision")
        lbs = data.get("lorebook_ids", [])
        greetings = data.get("greetings", [])
        persona_counts = [len(g.get("linked_persona_ids", [])) for g in greetings]
        print(f'  Live: HTTP 200, rev={rev}, LBs={len(lbs)}, greetings={len(greetings)}, personas per greeting={persona_counts}')
    else:
        print(f'  Live: HTTP {resp.status_code}')
    with open(local_path, 'r', encoding='utf-8') as f:
        loc = json.load(f)
    loc_rev = loc.get("revision")
    loc_lbs = loc.get("lorebook_ids", [])
    loc_greetings = loc.get("greetings", [])
    loc_persona_counts = [len(g.get("linked_persona_ids", [])) for g in loc_greetings]
    print(f'  Local: rev={loc_rev}, LBs={len(loc_lbs)}, greetings={len(loc_greetings)}, personas per greeting={loc_persona_counts}')
