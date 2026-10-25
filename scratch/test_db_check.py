import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}

# 1. Update Free-Tier-Master with selected_provider as _x3jXXcbELnhK36PUTb8Te
url = 'https://app.wyvern.chat/api/connections/_e134BGYwKcRbteXnhAkLn'
payload = {
    "provider": "_x3jXXcbELnhK36PUTb8Te",
    "selected_provider": "_x3jXXcbELnhK36PUTb8Te",
    "use_browser_request": True,
    "custom_model_id": "free-tier-master"
}

req = urllib.request.Request(url, method='PUT', headers=headers, data=json.dumps(payload).encode('utf-8'))
with urllib.request.urlopen(req) as resp:
    print("PUT returned:", resp.status)

# 2. Now GET https://app.wyvern.chat/api/connections/user
req2 = urllib.request.Request('https://app.wyvern.chat/api/connections/user', headers=headers)
with urllib.request.urlopen(req2) as resp2:
    conns = json.loads(resp2.read().decode('utf-8'))
    for c in conns.get('connections', []):
        print(f"Conn {c.get('id')} ({c.get('name')}): model={c.get('custom_model_id')}, provider={c.get('selected_provider')}, use_browser={c.get('use_browser_request')}")
