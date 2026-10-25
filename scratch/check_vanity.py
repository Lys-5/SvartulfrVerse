import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

for u in ['lys', 'Lys', '2r4fVpvImte5dbljedLkZJxre2d2']:
    url = f"https://app.wyvern.chat/api/worlds/user/{u}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"URL: {url} -> {data}")
    except Exception as e:
        print(f"URL: {url} -> Error: {e}")
