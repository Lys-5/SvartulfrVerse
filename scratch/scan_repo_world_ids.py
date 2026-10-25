import os
import re
import urllib.request
import urllib.error
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

found_ids = set()

# Scan only current repo
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.json', '.py', '.txt', '.md', '.js')):
            p = os.path.join(root, f)
            try:
                txt = open(p, 'r', encoding='utf-8', errors='ignore').read()
                for m in re.findall(r'_([A-Za-z0-9_\-]{21})', txt):
                    found_ids.add('_' + m)
            except Exception:
                pass

print(f"Total candidate IDs found in repo: {len(found_ids)}")

for wid in sorted(found_ids):
    url = f"https://app.wyvern.chat/api/worlds/{wid}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            creator = data.get('creator') or {}
            c_uid = creator.get('uid') if isinstance(creator, dict) else ''
            print(f"FOUND WORLD: {wid} | Name: '{data.get('name')}' | Creator: {c_uid} | Created: {data.get('created_at')} | Locations: {data.get('locations_count')}")
    except urllib.error.HTTPError as e:
        pass
    except Exception as e:
        pass

print("Done scanning.")
