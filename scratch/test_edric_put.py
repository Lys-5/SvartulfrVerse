import requests
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

with open('scratch/live_edric_card_fetched.json', 'r', encoding='utf-8') as f:
    live = json.load(f)

# Test sending live exactly as fetched
r = requests.put('https://app.wyvern.chat/api/characters/_TbRM3EdxDjHFgqztTbCpL', headers=headers, json=live)
print("PUT unmodified live status:", r.status_code, r.text[:200])

# If fails, test pruning metadata fields
test_payload = dict(live)
for field in ['creator', '_id', 'created_at', 'updated_at', 'equipped_badges', 'equipped_border']:
    if field in test_payload:
        del test_payload[field]

r2 = requests.put('https://app.wyvern.chat/api/characters/_TbRM3EdxDjHFgqztTbCpL', headers=headers, json=test_payload)
print("PUT pruned status:", r2.status_code, r2.text[:200])
