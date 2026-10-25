import os
import re
import urllib.request
import urllib.error
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

brain_dir = r'C:\Users\mande\.gemini\antigravity\brain'
found_ids = set()

# Scan all logs in brain
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if f.endswith(('.jsonl', '.log', '.txt')):
            p = os.path.join(root, f)
            try:
                txt = open(p, 'r', encoding='utf-8', errors='ignore').read()
                # find /worlds/_... or worlds/_...
                for m in re.findall(r'worlds/(?:edit/)?(_[A-Za-z0-9_-]{21})', txt):
                    found_ids.add(m)
                for m in re.findall(r'api/worlds/(_[A-Za-z0-9_-]{21})', txt):
                    found_ids.add(m)
                for m in re.findall(r'\"world_id\":\s*\"(_[A-Za-z0-9_-]{21})\"', txt):
                    found_ids.add(m)
            except Exception:
                pass

print(f"Total candidate World IDs found across brain: {len(found_ids)}")

for wid in sorted(found_ids):
    url = f"https://app.wyvern.chat/api/worlds/{wid}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            creator = data.get('creator') or {}
            c_uid = creator.get('uid') if isinstance(creator, dict) else ''
            print(f"FOUND: {wid} | Name: '{data.get('name')}' | Creator: {c_uid} | Created: {data.get('created_at')} | Locations: {data.get('locations_count')}")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"ERROR {wid}: HTTP {e.code}")
    except Exception as e:
        pass
