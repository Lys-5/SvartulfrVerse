import requests
import json

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

targets = [
    ('Master Scenario', 'char_scenario_1DC43ggb6mB8YLJDJKrU4'),
    ('Camp Mystic', 'char_scenario_nLC84wrHdrbB6P3DEhwKb'),
    ('DMHA Dungeons', 'char_scenario_eqtRNnDpKbxDp7dmJmq6E'),
    ('Underworld Sindacato', 'char_scenario_rrUCdBPH6WTNyBnQkMAKR'),
    ('Villa Douglas', 'char_scenario_88N1eQXqkbydKX9q9XQzp'),
    ('SUCC Route Alyssa (KEEP)', 'char_scenario_CKgwq246DyCj1NNTBV9rt'),
    ('SUCC Route Jasper (KEEP)', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF'),
]

for name, sc_id in targets:
    url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            print(f"FOUND: {name} ({sc_id}) -> title: '{data.get('title')}', revision: {data.get('revision')}")
        else:
            print(f"STATUS {resp.status_code}: {name} ({sc_id})")
    except Exception as e:
        print(f"ERROR: {name} ({sc_id}) -> {e}")
