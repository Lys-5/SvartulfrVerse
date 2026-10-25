import requests, json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

for sc_id, name in [('char_scenario_CKgwq246DyCj1NNTBV9rt', 'Alyssa Route'), ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'Jasper Route')]:
    r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    print(f"{name} ({sc_id}): status {r.status_code}")
    if r.status_code == 200:
        d = r.json()
        print(f"  rev: {d.get('revision')} | slots: {len(d.get('slots', []))} | greetings: {len(d.get('greetings', []))}")
        for s in d.get('slots', []):
            pool_ids = [p.get('character_id') for p in s.get('pool', [])]
            print(f"    slot: {s.get('key'):18} | unavail: {s.get('unavailable_count')} | pool: {pool_ids}")
