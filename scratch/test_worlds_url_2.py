import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

test_urls = [
    '/api/worlds/user/me',
    '/api/worlds/me',
    '/api/worlds/user/2r4fVpvImte5dbljedLkZJxre2d2',
    '/api/worlds?userId=2r4fVpvImte5dbljedLkZJxre2d2',
    '/api/worlds/list/2r4fVpvImte5dbljedLkZJxre2d2',
    '/api/worlds/created-by/2r4fVpvImte5dbljedLkZJxre2d2',
    '/api/user/2r4fVpvImte5dbljedLkZJxre2d2/worlds',
    '/api/worlds/parties/user',
]

for u in test_urls:
    try:
        req = urllib.request.Request(f"https://app.wyvern.chat{u}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"SUCCESS {u} -> {data[:120]}")
    except urllib.error.HTTPError as e:
        print(f"FAILED {u} -> {e.code}")
