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

def load_g3_candidates():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    export_path = os.path.join(base_dir, 'exports', 'Svartulfr_Export.json')
    g2_list_path = os.path.join(base_dir, 'scratch', 'g2_canonical_list.json')
    
    with open(export_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(g2_list_path, 'r', encoding='utf-8') as f:
        g2_list = json.load(f)
        
    chars = data.get('world_characters', [])
    g2_ids = {c['id'] for c in g2_list}
    
    g1_names = [
        'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
        'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
        'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
        'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
        'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
    ]
    
    def is_g1(char):
        name = (char.get('display_name') or f"{char.get('first_name', '')} {char.get('last_name', '')}").strip().lower()
        return any(g1 in name for g1 in g1_names)
        
    g3_chars = [c for c in chars if c['id'] not in g2_ids and not is_g1(c)]
    return g3_chars

def delete_character(char_id, token):
    url = f"{API_BASE}/characters/{char_id}"
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers, method='DELETE')
    with urllib.request.urlopen(req) as resp:
        return resp.status

def run_delete(batch_size=25, dry_run=False, limit=None):
    g3_chars = load_g3_candidates()
    print(f"Total G3 characters identified for removal: {len(g3_chars)}")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    backup_file = os.path.join(base_dir, 'exports', 'raw_db_dumps', 'g3_characters_pre_delete_backup.json')
    os.makedirs(os.path.dirname(backup_file), exist_ok=True)
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(g3_chars, f, indent=2, ensure_ascii=False)
    print(f"Pre-delete snapshot saved to: {backup_file}")
    
    state_file = os.path.join(base_dir, 'scratch', 'g3_delete_progress.json')
    deleted_ids = set()
    if os.path.exists(state_file):
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                deleted_ids = set(json.load(f))
        except Exception:
            pass
            
    to_delete = [c for c in g3_chars if c['id'] not in deleted_ids]
    if limit:
        to_delete = to_delete[:limit]
        
    print(f"Already deleted according to state: {len(deleted_ids)}")
    print(f"Remaining to delete in this run: {len(to_delete)}")
    
    if dry_run:
        print("DRY RUN: No deletions made.")
        return
        
    token = get_auth_token()
    batches = [to_delete[i:i + batch_size] for i in range(0, len(to_delete), batch_size)]
    
    for b_idx, batch in enumerate(batches, 1):
        print(f"\n--- Processing Delete Batch {b_idx}/{len(batches)} ({len(batch)} characters) ---")
        for c in batch:
            cid = c['id']
            name = c.get('display_name') or f"{c.get('first_name', '')} {c.get('last_name', '')}".strip()
            try:
                status = delete_character(cid, token)
                print(f"  [OK {status}] Deleted: {name} ({cid})")
                deleted_ids.add(cid)
                time.sleep(0.2)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"  [ALREADY DELETED 404] {name} ({cid})")
                    deleted_ids.add(cid)
                elif e.code == 401:
                    print("  [401] Refreshing token...")
                    token = get_auth_token()
                    status = delete_character(cid, token)
                    print(f"  [OK {status}] Deleted: {name} ({cid})")
                    deleted_ids.add(cid)
                else:
                    print(f"  [ERROR {e.code}] Failed to delete {name} ({cid}): {e}")
            except Exception as err:
                print(f"  [ERROR] {name} ({cid}): {err}")
                
        # Save progress
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(list(deleted_ids), f)
            
        # Post-batch verification GET
        token = get_auth_token()
        url = f"{API_BASE}/characters/world/{WORLD_ID}"
        req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            live_count = len(json.loads(resp.read().decode('utf-8')))
        print(f"Live Characters remaining on server after Batch {b_idx}: {live_count}")

    print(f"\nDeletions complete! Total deleted in state: {len(deleted_ids)}")

if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    limit_val = None
    if '--limit' in sys.argv:
        idx = sys.argv.index('--limit')
        if idx + 1 < len(sys.argv):
            limit_val = int(sys.argv[idx + 1])
    run_delete(dry_run=dry, limit=limit_val)
