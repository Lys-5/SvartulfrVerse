import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

# Check environments for existing world _CgYT8fHXpDC4crjmegQF7
url = 'https://app.wyvern.chat/api/worlds/environments/world/_CgYT8fHXpDC4crjmegQF7'
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print(f"Environments count for _CgYT8fHXpDC4crjmegQF7: {len(data)}")
        if data:
            print("Sample environment keys:", list(data[0].keys()))
            print(json.dumps(data[0], indent=2))
except Exception as e:
    print("Error:", e)
