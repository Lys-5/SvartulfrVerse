import requests
import pathlib
import json

root = pathlib.Path('.')
token = (root / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}

for sc_id, name in [('char_scenario_CKgwq246DyCj1NNTBV9rt', 'Alyssa'), ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'Jasper')]:
    r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    print(f"=== {name} ({sc_id}) ===")
    if r.status_code == 200:
        data = r.json()
        print('Revision:', data.get('revision'))
        greetings = data.get('greetings', [])
        print('Greetings count:', len(greetings))
        for idx, g in enumerate(greetings):
            print(f"  [{idx}] {g.get('name')} | slot: {g.get('speaker_slot')} | msgs: {len(g.get('messages', []))}")
            if idx == 0:
                print("      description:", g.get('description'))
                for midx, m in enumerate(g.get('messages', [])):
                    print(f"      m[{midx}] slot: {m.get('speaker_slot')} | id: {m.get('id')} | content: {m.get('content')[:60]}...")
    else:
        print('Status:', r.status_code, r.text[:200])
