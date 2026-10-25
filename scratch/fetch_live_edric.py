import requests
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': f'Bearer {token}'}
r = requests.get('https://app.wyvern.chat/api/characters/_TbRM3EdxDjHFgqztTbCpL', headers=headers)
live = r.json()

print("=== LIVE EDRIC CARD FIELDS ===")
for k in ['name', 'rating', 'description', 'personality', 'scenario', 'first_mes', 'post_history_instructions']:
    v = live.get(k, '')
    print(f"--- {k} ({len(v) if v else 0} chars) ---")
    if v:
        print(v[:400])

with open('scratch/live_edric_card_fetched.json', 'w', encoding='utf-8') as f:
    json.dump(live, f, indent=2, ensure_ascii=False)
