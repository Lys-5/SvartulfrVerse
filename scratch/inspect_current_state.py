import sys
import json
import pathlib
import urllib.request

root = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(root / 'scratch'))
import refresh_token

token = refresh_token.refresh()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'AuditorBot/1.0'
}

print("=== CHECKING /api/characters/mine ===")
req = urllib.request.Request('https://app.wyvern.chat/api/characters/mine', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    chars = data.get('characters', [])
    print(f"Characters in /mine: {len(chars)}")
    for c in chars:
        cid = c.get('_id', c.get('id'))
        print(f"  {cid}: {c.get('name')}")

print("\n=== CHECKING /api/user-personas ===")
try:
    req_p = urllib.request.Request('https://app.wyvern.chat/api/user-personas', headers=headers)
    with urllib.request.urlopen(req_p) as resp_p:
        personas = json.loads(resp_p.read().decode())
        print(f"Personas retrieved: {len(personas) if isinstance(personas, list) else type(personas)}")
        if isinstance(personas, list):
            for p in personas:
                pid = p.get('_id', p.get('id'))
                print(f"  {pid}: {p.get('name')}")
        elif isinstance(personas, dict):
            for pid, p in personas.items():
                if isinstance(p, dict):
                    print(f"  {pid}: {p.get('name')}")
except Exception as e:
    print(f"Error checking user-personas: {e}")

print("\n=== CHECKING LOREBOOKS API ===")
for lid in ['_zwEqgEEzh12X6gHVmMKKC', '_Uht3Ckz44JBDrPnUHq7LV']:
    for base in ['https://app.wyvern.chat/api/lorebooks/', 'https://api.wyvern.chat/lorebooks/']:
        try:
            req_l = urllib.request.Request(f'{base}{lid}', headers=headers)
            with urllib.request.urlopen(req_l) as resp_l:
                lb = json.loads(resp_l.read().decode())
                print(f"Success GET {base}{lid} -> name: {lb.get('name')}, entries: {len(lb.get('lexicon', []))}")
                break
        except Exception as e:
            print(f"Failed {base}{lid}: {e}")
