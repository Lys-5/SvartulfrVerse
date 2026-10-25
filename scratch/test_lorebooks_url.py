import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

variants = [
    '/api/lorebooks/user',
    '/api/lorebooks/user/2r4fVpvImte5dbljedLkZJxre2d2',
    '/api/lorebooks/my',
    '/api/lorebooks?creator=2r4fVpvImte5dbljedLkZJxre2d2',
    '/api/lorebooks/me',
    '/api/lorebooks/user/me',
    '/api/lorebooks',
]

for v in variants:
    try:
        req = urllib.request.Request(f"https://app.wyvern.chat{v}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"SUCCESS {v} -> {data[:80]}")
    except urllib.error.HTTPError as e:
        print(f"FAILED {v} -> {e.code}")
