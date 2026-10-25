import requests
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

cid = '_TbRM3EdxDjHFgqztTbCpL'

# Test 1: Only description & personality
payload = {
    'name': 'Edric Douglas',
    'description': 'test'
}
r = requests.put(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers, json=payload)
print("PUT minimal payload status:", r.status_code, r.text[:200])

# Test 2: What if the endpoint is PATCH?
r_patch = requests.patch(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers, json=payload)
print("PATCH minimal payload status:", r_patch.status_code, r_patch.text[:200])
