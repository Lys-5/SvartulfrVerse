import urllib.request
import json
import sys
import os
import re
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from prepare_all_g2_rpg import prepare_g2_rpg

def apply_g2_rpg_batches():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    configs = prepare_g2_rpg()
    total = len(configs)
    print(f"\nApplying RPG Stats to {total} characters in batches of 25...")
    
    snapshot_dir = os.path.join('scratch', 'g2_rpg_snapshots')
    os.makedirs(snapshot_dir, exist_ok=True)
    
    batch_size = 25
    success_count = 0
    
    for i in range(0, total, batch_size):
        batch = configs[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (total + batch_size - 1) // batch_size
        print(f"\n=== Processing Batch {batch_num}/{total_batches} ({len(batch)} characters) ===")
        
        for c in batch:
            cid = c['id']
            name = c['name']
            c_url = f'https://app.wyvern.chat/api/worlds/characters/{cid}'
            
            # 1. Snapshot
            try:
                req = urllib.request.Request(c_url, headers=headers)
                with urllib.request.urlopen(req) as resp:
                    prev = json.loads(resp.read().decode('utf-8'))
                with open(os.path.join(snapshot_dir, f'{cid}.json'), 'w', encoding='utf-8') as sf:
                    json.dump(prev, sf, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"Warning: snapshot failed for {name}: {e}")
                
            # 2. Build payload
            st = c['stats']
            payload = {
                'rpg_stats': {
                    'enabled': True,
                    'level': c['level'],
                    'experience': 0,
                    'species_id': c['species'],
                    'occupation_id': c['occupation'],
                    'base_stats': {
                        'stat_1': st['stat_1'],
                        'stat_2': st['stat_2'],
                        'stat_3': st['stat_3'],
                        'stat_4': st['stat_4'],
                        'stat_5': st['stat_5'],
                        'stat_6': st['stat_6'],
                        'strength': st['stat_1'],
                        'endurance': st['stat_2'],
                        'agility': st['stat_3'],
                        'intelligence': st['stat_4'],
                        'charisma': st['stat_5'],
                        'luck': st['stat_6'],
                        'perception': st['stat_6']
                    }
                },
                'character_traits': c['traits']
            }
            
            # 3. PUT
            try:
                put_req = urllib.request.Request(
                    c_url,
                    data=json.dumps(payload).encode('utf-8'),
                    headers={**headers, 'Content-Type': 'application/json'},
                    method='PUT'
                )
                with urllib.request.urlopen(put_req) as resp:
                    pass
                success_count += 1
                print(f"  [OK] {name:25} | Lv {c['level']:2} | {c['species'][:15]:15} | {c['occupation'][:20]:20}")
            except Exception as e:
                print(f"  [FAIL] {name}: {e}")
                
        # Brief pause between batches
        time.sleep(1)
        
    print(f"\nAll batches processed! Updated {success_count} / {total} characters.")

if __name__ == '__main__':
    apply_g2_rpg_batches()
