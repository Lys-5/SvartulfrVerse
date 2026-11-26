import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

# Fetch full details of both configs in GET /simple-assistant-config
url = 'https://app.wyvern.chat/api/simple-assistant-config'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("Full list from /api/simple-assistant-config:")
    print(json.dumps(data, indent=2))

# Also fetch detail of each config
for c in data.get('configs', []):
    cid = c.get('id')
    detail_url = f'https://app.wyvern.chat/api/simple-assistant-config/{cid}'
    req = urllib.request.Request(detail_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        detail = json.loads(resp.read().decode('utf-8'))
        print(f"\n--- DETAIL FOR {cid} ---")
        print(json.dumps(detail, indent=2))
