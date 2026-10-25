import json
import urllib.request
import urllib.error
import pathlib
import time
import base64

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

token = WT_PATH.read_text(encoding='utf-8').strip() if WT_PATH.exists() else ''
print(f"Token length: {len(token)}")

# Check token expiry
if token:
    try:
        parts = token.split('.')
        if len(parts) == 3:
            payload = parts[1]
            padded = payload + '=' * (-len(payload) % 4)
            data = json.loads(base64.urlsafe_b64decode(padded).decode('utf-8'))
            exp = data.get('exp', 0)
            now = time.time()
            print(f"Token exp: {exp}, now: {now}, diff: {exp - now:.1f}s")
            if exp < now:
                print("Token is EXPIRED!")
            else:
                print(f"Token is valid for {int(exp - now)} more seconds.")
    except Exception as e:
        print("Error decoding token payload:", e)

# Test GET request on first scenario with proper headers
scenario_id = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'
url = f'https://app.wyvern.chat/api/character-scenarios/{scenario_id}'
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        print(f"GET {scenario_id} HTTP Status: {resp.status}")
        data = json.loads(resp.read().decode())
        print(f"Retrieved keys: {list(data.keys())}")
        print(f"Title: {data.get('title')}")
        print(f"Revision: {data.get('revision')}")
        print(f"Lorebook IDs count: {len(data.get('lorebook_ids', []))}")
        print(f"Lorebook IDs: {data.get('lorebook_ids')}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} {e.reason}")
    body = e.read().decode()
    print(f"Body: {body[:300]}")
except Exception as e:
    print(f"General Error: {e}")
