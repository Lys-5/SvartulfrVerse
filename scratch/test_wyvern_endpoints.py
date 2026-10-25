import urllib.request
import json

with open('scratch/wyvern_token.txt', 'r') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

for ep in [
    'https://app.wyvern.chat/api/connections',
    'https://app.wyvern.chat/api/user/connections',
    'https://app.wyvern.chat/api/settings',
    'https://app.wyvern.chat/api/auth/session',
    'https://app.wyvern.chat/api/user'
]:
    try:
        req = urllib.request.Request(ep, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            print(f"SUCCESS {ep} -> {r.status}")
            data = json.loads(r.read().decode())
            print(str(data)[:200])
    except urllib.error.HTTPError as e:
        print(f"FAIL {ep} -> {e.code}")
    except Exception as e:
        print(f"ERROR {ep} -> {e}")
