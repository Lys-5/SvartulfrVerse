import requests, json, re

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

for sc_id, name in [
    ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'SUCC Alyssa'),
    ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'SUCC Jasper')
]:
    r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    if r.status_code == 200:
        data = r.json()
        print(f"=== Scenario {name} ===")
        greetings = data.get('greetings', [])
        for g in greetings:
            txt = g.get('content', '')
            for m in g.get('messages', []):
                txt += " " + m.get('content', '')
            macro_matches = set(re.findall(r'\{\{scenarioChar\s+[^}]+\}\}', txt))
            print(f"  Greeting: {g.get('name')} | speaker_slot: {g.get('speaker_slot')} | macros: {macro_matches}")
