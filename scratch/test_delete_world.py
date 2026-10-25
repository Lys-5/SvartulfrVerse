import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

world_id = "_qWLGbk24Dm3JzydjXx7mQ"

req = urllib.request.Request(
    f'https://app.wyvern.chat/api/worlds/{world_id}',
    headers=headers,
    method='DELETE'
)

try:
    with urllib.request.urlopen(req) as resp:
        print("Delete World Status:", resp.status)
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error:", e)
