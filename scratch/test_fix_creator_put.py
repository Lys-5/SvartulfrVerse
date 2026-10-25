import urllib.request
import urllib.error
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

wid = '_CgYT8fHXpDC4crjmegQF7'
user_id = '2r4fVpvImte5dbljedLkZJxre2d2'

payload = {
    "creator": {
        "_id": user_id,
        "uid": user_id,
        "displayName": "Lys"
    }
}

url = f"https://app.wyvern.chat/api/worlds/{wid}"
req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')

try:
    with urllib.request.urlopen(req) as resp:
        print(f"PUT {wid} -> Status: {resp.status}")
        data = json.loads(resp.read().decode('utf-8'))
        print("Updated creator:", data.get('creator'))
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8', errors='ignore')
    print(f"PUT {wid} -> HTTP Error {e.code}: {err_body}")
except Exception as e:
    print(f"PUT {wid} -> Error: {e}")
