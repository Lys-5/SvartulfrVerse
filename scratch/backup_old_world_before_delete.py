import urllib.request
import json
import os

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

wid = '_CgYT8fHXpDC4crjmegQF7'
backup_dir = 'scratch/backup_old_world_CgYT8fHXpDC4crjmegQF7'
os.makedirs(backup_dir, exist_ok=True)

endpoints = {
    'world.json': f'/api/worlds/{wid}',
    'environments.json': f'/api/worlds/environments/world/{wid}',
    'locations.json': f'/api/worlds/locations/world/{wid}',
    'lexicon.json': f'/api/worlds/lexicon/world/{wid}',
    'linked_characters.json': f'/api/worlds/linked-characters/{wid}',
}

for fname, ep in endpoints.items():
    url = f"https://app.wyvern.chat{ep}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            with open(os.path.join(backup_dir, fname), 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Saved {fname} (count/type: {len(data) if isinstance(data, (list, dict)) else 'scalar'})")
    except Exception as e:
        print(f"Failed {fname}: {e}")
