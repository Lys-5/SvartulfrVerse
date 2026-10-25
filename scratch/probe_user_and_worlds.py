import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

# Probe various user profile endpoints
endpoints = [
    '/api/me',
    '/api/user',
    '/api/users/me',
    '/api/user/profile',
    '/api/user/me',
    '/api/auth/me',
    '/api/settings/profile',
    '/api/user/settings',
    '/api/gallery/user',
]

for ep in endpoints:
    try:
        req = urllib.request.Request(f'https://app.wyvern.chat{ep}', headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"SUCCESS {ep} -> {data[:120]}")
    except urllib.error.HTTPError as e:
        print(f"FAILED {ep} -> {e.code}")
    except Exception as e:
        print(f"ERROR {ep} -> {e}")
