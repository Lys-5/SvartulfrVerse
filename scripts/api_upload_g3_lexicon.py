import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def load_g3_a_entries():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, 'exports', 'entities', 'Svartulfr_Lexicon_NPCs_G3_A_Real.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('entries', [])

def get_live_lexicon(token):
    url = f"{API_BASE}/lexicon/world/{WORLD_ID}"
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return data if isinstance(data, list) else data.get('items', [])

def upload_entry(entry, token):
    url = f"{API_BASE}/lexicon"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Ensure zero em-dashes and proper types
    content = entry['content'].replace('—', ', ').replace('–', ', ')
    
    payload = {
        "world_id": WORLD_ID,
        "name": entry["name"].strip(),
        "keys": entry.get("keys", [entry["name"].strip()]),
        "secondary_keys": entry.get("secondary_keys", []),
        "key_logic": entry.get("key_logic", "AND_ANY"),
        "case_sensitive": entry.get("case_sensitive", False),
        "whole_words_only": entry.get("whole_words_only", True),
        "content": content,
        "type": "lore/concept",
        "is_global": True,
        "constant": False,
        "priority": entry.get("priority", 15),
        "position": "before_char",
        "scan_persona": False,
        "enabled": True,
        "comment": entry.get("comment", ""),
        "insertion_order": entry.get("insertion_order", 100),
        "extensions": {},
        "labels": [],
        "custom_fields": {},
        "related_entries": []
    }
    
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    with urllib.request.urlopen(req) as resp:
        res_data = json.loads(resp.read().decode('utf-8'))
        return res_data

def run_upload(batch_size=25, dry_run=False):
    token = get_auth_token()
    live_items = get_live_lexicon(token)
    existing_names = {item.get('name', '').strip().lower() for item in live_items if item.get('name')}
    
    entries = load_g3_a_entries()
    to_upload = [e for e in entries if e.get('name', '').strip().lower() not in existing_names]
    
    print(f"Total G3-A entries: {len(entries)}")
    print(f"Already on server: {len(entries) - len(to_upload)}")
    print(f"Pending upload: {len(to_upload)}")
    
    if dry_run:
        print("DRY RUN: No modifications made.")
        return
        
    total_uploaded = 0
    batches = [to_upload[i:i + batch_size] for i in range(0, len(to_upload), batch_size)]
    
    for b_idx, batch in enumerate(batches, 1):
        print(f"\n--- Processing Batch {b_idx}/{len(batches)} ({len(batch)} entries) ---")
        for e in batch:
            name = e.get('name', 'Unknown')
            try:
                res = upload_entry(e, token)
                new_id = res.get('id') or res.get('_id')
                print(f"  [OK] Uploaded: {name} (ID: {new_id})")
                total_uploaded += 1
                time.sleep(0.3)
            except Exception as err:
                print(f"  [ERROR] Failed to upload {name}: {err}")
                
        # Verification GET after batch
        print(f"Verifying batch {b_idx} with fresh GET...")
        token = get_auth_token() # refresh if needed
        live_after = get_live_lexicon(token)
        print(f"Live Lexicon entries on server now: {len(live_after)}")

    print(f"\nFinished! Total new entries uploaded: {total_uploaded}")

if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    run_upload(dry_run=dry)
