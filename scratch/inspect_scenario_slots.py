import requests, json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

for sc_id, name in [
    ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'SUCC Alyssa'),
    ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'SUCC Jasper')
]:
    r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    if r.status_code == 200:
        data = r.json()
        print(f"=== Slots for {name} ===")
        slots = data.get('slots', [])
        for s in slots:
            print(f"Key: {s.get('key')} | Label: {s.get('label')}")
            for p in s.get('pool', []):
                print(f"   Pool char: {p.get('id')} (type: {type(p.get('id'))})")
