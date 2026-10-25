import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}

scenarios = [
    ('char_scenario_88N1eQXqkbydKX9q9XQzp', 'Villa Douglas'),
    ('char_scenario_rrUCdBPH6WTNyBnQkMAKR', 'Underworld'),
    ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'SUCC Jasper'),
    ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'SUCC Alyssa'),
    ('char_scenario_eqtRNnDpKbxDp7dmJmq6E', 'DMHA Dungeons'),
    ('char_scenario_nLC84wrHdrbB6P3DEhwKb', 'Camp Mystic')
]

for sid, sname in scenarios:
    req = urllib.request.Request(f'https://app.wyvern.chat/api/character-scenarios/{sid}', headers=headers)
    with urllib.request.urlopen(req) as resp:
        d = json.loads(resp.read().decode('utf-8'))
    slots = [s.get('key') for s in d.get('slots', [])]
    has_script = bool(d.get('startup_script'))
    print(f"{sname}: slots={slots} | has_startup_script={has_script}")
