import urllib.request
import urllib.error
import json
import os

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

user_id = '2r4fVpvImte5dbljedLkZJxre2d2'
endpoints = [
    f'/api/worlds/user/{user_id}',
    f'/api/worlds/creator/{user_id}',
    f'/api/worlds/author/{user_id}',
    f'/api/worlds/by-user/{user_id}',
    f'/api/user/worlds',
    f'/api/users/{user_id}/worlds',
    f'/api/worlds?creator={user_id}',
    f'/api/worlds?user_id={user_id}',
    f'/api/worlds/all',
    f'/api/worlds/search',
    f'/api/worlds',
]

for ep in endpoints:
    url = f'https://app.wyvern.chat{ep}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f'[SUCCESS {resp.status}] {ep} -> len: {len(data)}, snippet: {data[:200]}')
    except urllib.error.HTTPError as e:
        print(f'[{e.code}] {ep}')
