import requests, json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

scenarios = [
    ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'SUCC Alyssa'),
    ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'SUCC Jasper'),
    ('char_scenario_K9fVjM37B9x2hNRL4QTe2', 'Camp Mystic'),
    ('char_scenario_eP4nLMWzYgK8VpQJ7N3rC', 'DMHA Dungeons'),
    ('char_scenario_rM8tPKVxYnB3WjL94QFe2', 'Underworld Sindacato'),
    ('char_scenario_bN3xQWLzYgM8VpK7JR5tD', 'Villa Douglas')
]

# Let's check IDs from FINAL/scenarios
import glob
for p in glob.glob('FINAL/scenarios/*.json'):
    try:
        data = json.load(open(p, encoding='utf-8'))
        sc_id = data.get('id')
        name = data.get('name')
        r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
        print(f"Scenario {name} ({sc_id}): Status {r.status_code}")
    except Exception as e:
        print(f"Error {p}: {e}")
