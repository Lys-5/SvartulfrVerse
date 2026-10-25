import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
for cid in ['_YjmGAE9zPFgEQgYKaGXYq', '_e134BGYwKcRbteXnhAkLn']:
    url = f'https://app.wyvern.chat/api/connections/{cid}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"=== Connection {cid} ({data.get('name')}) ===")
            print(json.dumps(data, indent=2))
    except urllib.error.HTTPError as e:
        print(f"FAIL {cid}: {e.code} {e.read().decode()}")
