import requests
import json
import os
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
BACKUP_DIR = ROOT / 'scratch' / 'backup_deleted_scenarios_20261021'
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

with open(ROOT / 'scratch' / 'wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

to_delete = [
    ('Master Scenario', 'char_scenario_1DC43ggb6mB8YLJDJKrU4'),
    ('Camp Mystic', 'char_scenario_nLC84wrHdrbB6P3DEhwKb'),
    ('DMHA Dungeons', 'char_scenario_eqtRNnDpKbxDp7dmJmq6E'),
    ('Underworld Sindacato', 'char_scenario_rrUCdBPH6WTNyBnQkMAKR'),
    ('Villa Douglas', 'char_scenario_88N1eQXqkbydKX9q9XQzp'),
]

to_keep = [
    ('SUCC Route Alyssa', 'char_scenario_CKgwq246DyCj1NNTBV9rt'),
    ('SUCC Route Jasper', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF'),
]

print("--- STEP 1: Backing up live data before deletion ---", flush=True)
for name, sc_id in to_delete:
    url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        backup_file = BACKUP_DIR / f"{sc_id}_{name.replace(' ', '_')}.json"
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Backed up {name} ({sc_id}) to {backup_file.name}", flush=True)
    else:
        print(f"Warning: Could not fetch {name} ({sc_id}) - HTTP {resp.status_code}", flush=True)

print("\n--- STEP 2: Executing DELETE for 5 scenarios ---", flush=True)
delete_results = {}
for name, sc_id in to_delete:
    url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
    resp = requests.delete(url, headers=headers, timeout=10)
    print(f"DELETE {name} ({sc_id}) -> HTTP {resp.status_code} | Body: {resp.text}", flush=True)
    delete_results[sc_id] = resp.status_code

print("\n--- STEP 3: Verifying deleted scenarios (expecting 404) ---", flush=True)
for name, sc_id in to_delete:
    url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
    resp = requests.get(url, headers=headers, timeout=10)
    print(f"VERIFY DELETED {name} ({sc_id}) -> HTTP {resp.status_code}", flush=True)

print("\n--- STEP 4: Verifying remaining scenarios (expecting 200) ---", flush=True)
for name, sc_id in to_keep:
    url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
    resp = requests.get(url, headers=headers, timeout=10)
    print(f"VERIFY ACTIVE {name} ({sc_id}) -> HTTP {resp.status_code}", flush=True)
