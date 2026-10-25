import os
import sys
import json
import urllib.request
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from remediate_lorebook_npcs import build_compact_put_payload

token = get_auth_token()
lb_id = '_zwEqgEEzh12X6gHVmMKKC'

# 1. Fetch live gallery items
url_gal = f'https://app.wyvern.chat/api/gallery/lorebook/{lb_id}'
req_gal = urllib.request.Request(url_gal, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
gallery = json.loads(urllib.request.urlopen(req_gal).read().decode('utf-8'))
gal_map = {g['title'].lower(): g['imageURL'] for g in gallery}

print(f"Fetched {len(gallery)} gallery items from live server.")

# Exact mapping from character identification to gallery title
MAPPING = {
    'erik': 'erikmain',
    'logan': 'loganmain',
    'malachia': 'mailmain',
    'noah': 'noahmain',
    'wulfnic': 'mainwulfnic',
    'nixara': 'nixara',
    'scarlett': 'scarlettmain',
    'sierra': 'sierramain',
    'zefir': 'zefirmain',
    'kaladin': 'kaladin',
    'elizabeth': 'elizabeth'
}

# 2. Fetch live lorebook
url_lb = f'https://app.wyvern.chat/api/lorebooks/{lb_id}'
req_lb = urllib.request.Request(url_lb, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
lb = json.loads(urllib.request.urlopen(req_lb).read().decode('utf-8'))
entries = lb.get('lexicon') or lb.get('entries') or []

updated_count = 0
for entry in entries:
    name_lower = entry.get('name', '').lower()
    for key, gal_title in MAPPING.items():
        if key in name_lower:
            target_url = gal_map.get(gal_title)
            if target_url:
                old_avatar = entry.get('avatar')
                entry['avatar'] = target_url
                entry['type'] = 'npc'
                entry['scan_persona'] = True
                entry['whole_words_only'] = True
                entry['highlight_keys'] = True
                entry['enable_highlighting'] = True
                updated_count += 1
                print(f"  [RECONCILED] {entry['name']} -> {gal_title} ({target_url[:55]}...)")
            break

print(f"\nTotal entries reconciled with gallery: {updated_count}")

# 3. Save to local FINAL/Svartulfr_NPC_Primary.json
local_path = 'FINAL/Svartulfr_NPC_Primary.json'
with open(local_path, 'r', encoding='utf-8') as f:
    local_lb = json.load(f)

for local_entry in local_lb['entries']:
    matched = next((e for e in entries if e.get('entry_id') == local_entry.get('entry_id') or e.get('name') == local_entry.get('name')), None)
    if matched:
        local_entry['avatar'] = matched.get('avatar')
        local_entry['type'] = 'npc'
        local_entry['scan_persona'] = True
        local_entry['whole_words_only'] = True
        local_entry['highlight_keys'] = True
        local_entry['enable_highlighting'] = True

local_lb['lexicon'] = local_lb['entries']
with open(local_path, 'w', encoding='utf-8') as f:
    json.dump(local_lb, f, indent=2, ensure_ascii=False)
print(f"Saved reconciled entries to {local_path}")

# 4. Deploy to live server via API PUT
lb['entries'] = entries
lb['lexicon'] = entries
payload_bytes = build_compact_put_payload(lb)

put_req = urllib.request.Request(
    url_lb,
    data=payload_bytes,
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    method='PUT'
)

with urllib.request.urlopen(put_req) as resp:
    print(f"\nLive deployment successful: HTTP {resp.status}!")
