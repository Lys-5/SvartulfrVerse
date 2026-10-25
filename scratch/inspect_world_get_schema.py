import json
import urllib.request
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}

req = urllib.request.Request('https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print("Top keys:", list(data.keys()))
for k in list(data.keys())[:15]:
    val = data[k]
    val_type = type(val).__name__
    val_str = str(val)[:50] if not isinstance(val, (dict, list)) else f"{val_type} len={len(val)}"
    print(f"  {k}: {val_str}")

if 'world' in data:
    w = data['world']
    print("\nKeys in data['world']:", list(w.keys())[:20])
    print("world_features:", w.get('world_features'))
    print("world_age:", w.get('world_age'))
    print("stat_config:", w.get('stat_config'))
