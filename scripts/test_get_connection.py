import urllib.request
import json

with open('scratch/wyvern_token.txt', 'r') as f:
    token = f.read().strip()

url = 'https://app.wyvern.chat/api/connections/_YjmGAE9zPFgEQgYKaGXYq'
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        print("GET Connection:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print(json.dumps(data, indent=2)[:500])
except urllib.error.HTTPError as e:
    print(f"GET Connection failed: {e.code} {e.reason}: {e.read().decode('utf-8')}")
