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

def load_local_g2_characters():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    list_path = os.path.join(base_dir, 'scratch', 'g2_canonical_list.json')
    export_path = os.path.join(base_dir, 'exports', 'Svartulfr_Export.json')
    
    with open(list_path, 'r', encoding='utf-8') as f:
        g2_list = json.load(f)
    g2_ids = {c['id'] for c in g2_list}
    
    with open(export_path, 'r', encoding='utf-8') as f:
        export_data = json.load(f)
        
    chars = export_data.get('world_characters', [])
    return [c for c in chars if c.get('id') in g2_ids]

def get_live_character(char_id, token):
    url = f"{API_BASE}/characters/{char_id}"
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def update_character(char_id, partial_payload, token):
    url = f"{API_BASE}/characters/{char_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    body = json.dumps(partial_payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def run_update(batch_size=25, dry_run=False):
    token = get_auth_token()
    g2_chars = load_local_g2_characters()
    print(f"Total G2 characters to update: {len(g2_chars)}")
    
    if dry_run:
        print("DRY RUN: No modifications made.")
        return

    batches = [g2_chars[i:i + batch_size] for i in range(0, len(g2_chars), batch_size)]
    total_updated = 0
    
    for b_idx, batch in enumerate(batches, 1):
        print(f"\n--- Processing G2 Batch {b_idx}/{len(batches)} ({len(batch)} characters) ---")
        for char in batch:
            cid = char['id']
            name = char.get('display_name') or f"{char.get('first_name', '')} {char.get('last_name', '')}".strip()
            
            # Prepare strictly partial payload (Rule 11)
            speech_ex = []
            for ex in char.get('speech_examples', []):
                if isinstance(ex, dict):
                    clean_ex = dict(ex)
                    if 'prompt' in clean_ex and isinstance(clean_ex['prompt'], str):
                        clean_ex['prompt'] = clean_ex['prompt'].replace('—', ', ').replace('–', ', ')
                    if 'response' in clean_ex and isinstance(clean_ex['response'], str):
                        clean_ex['response'] = clean_ex['response'].replace('—', ', ').replace('–', ', ')
                    speech_ex.append(clean_ex)
                elif isinstance(ex, str):
                    speech_ex.append(ex.replace('—', ', ').replace('–', ', '))

            payload = {
                "is_global": True,
                "birthdate": char.get('birthdate'),
                "start_timeline_position": char.get('start_timeline_position'),
                "final_instructions": (char.get('final_instructions') or '').replace('—', ', ').replace('–', ', '),
                "outfits": char.get('outfits', []),
                "speech_examples": speech_ex,
                "attitudes": char.get('attitudes', [])
            }
            
            try:
                res = update_character(cid, payload, token)
                print(f"  [OK] Updated: {name} ({cid})")
                total_updated += 1
                time.sleep(0.3)
            except Exception as err:
                print(f"  [ERROR] Failed to update {name} ({cid}): {err}")
                
        # Verification GET after batch
        print(f"Verifying batch {b_idx} with verification GET...")
        token = get_auth_token() # Refresh token if needed
        verify_char = get_live_character(batch[0]['id'], token)
        print(f"Sample verification ({verify_char.get('display_name')}): is_global={verify_char.get('is_global')}, outfits={len(verify_char.get('outfits', []))}, birthdate={verify_char.get('birthdate')}")

    print(f"\nFinished G2 update! Total characters updated: {total_updated}")

if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    run_update(dry_run=dry)
