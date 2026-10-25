import requests, json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

r_chars = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
chars = r_chars.json().get('characters', []) if r_chars.status_code == 200 else []
print(f"=== MINE CHARACTERS ({len(chars)}) ===")
for c in chars:
    print(f"  {c.get('id')} | {c.get('name')}")

r_scen = requests.get('https://app.wyvern.chat/api/character-scenarios/mine', headers=headers)
if r_scen.status_code == 200:
    res = r_scen.json()
    scens = res.get('scenarios', res if isinstance(res, list) else [])
    print(f"\n=== MINE CHARACTER SCENARIOS ({len(scens)}) ===")
    for s in scens:
        print(f"  {s.get('id')} | {s.get('name')}")
else:
    print('Scenarios mine status:', r_scen.status_code, r_scen.text[:100])
