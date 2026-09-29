import urllib.request
import json
import sys
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def audit_all_characters():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    
    url = f'https://app.wyvern.chat/api/worlds/characters/world/{world_id}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chars_list = json.loads(resp.read().decode('utf-8'))
    
    print(f"Total characters to inspect: {len(chars_list)}")
    
    with_rpg = []
    with_species = []
    with_occ = []
    with_traits = []
    with_inv = []
    
    for i, c in enumerate(chars_list):
        cid = c['id']
        name = c.get('display_name') or c.get('name')
        c_url = f'https://app.wyvern.chat/api/worlds/characters/{cid}'
        try:
            req = urllib.request.Request(c_url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                detail = json.loads(resp.read().decode('utf-8'))
            
            rs = detail.get('rpg_stats')
            sp = detail.get('species_id') or (rs.get('species_id') if rs else None)
            occ = detail.get('occupation_id') or (rs.get('occupation_id') if rs else None)
            traits = detail.get('character_traits')
            inv = detail.get('default_inventory')
            
            if rs:
                with_rpg.append((name, cid, rs))
            if sp:
                with_species.append((name, cid, sp))
            if occ:
                with_occ.append((name, cid, occ))
            if traits:
                with_traits.append((name, cid, traits))
            if inv:
                with_inv.append((name, cid, inv))
                
        except Exception as e:
            print(f"Error on {name} ({cid}): {e}")
            
    print(f"\n--- AUDIT SUMMARY ---")
    print(f"Characters with rpg_stats: {len(with_rpg)}")
    for name, cid, rs in with_rpg:
        print(f"  {name} ({cid}): level={rs.get('level')}, species_id={rs.get('species_id')}, occ_id={rs.get('occupation_id')}, stats={rs.get('base_stats')}")
        
    print(f"\nCharacters with species: {len(with_species)}")
    for name, cid, sp in with_species:
        print(f"  {name}: {sp}")
        
    print(f"\nCharacters with occupation: {len(with_occ)}")
    for name, cid, occ in with_occ:
        print(f"  {name}: {occ}")
        
    print(f"\nCharacters with character_traits: {len(with_traits)}")
    for name, cid, traits in with_traits:
        print(f"  {name}: {traits}")
        
    print(f"\nCharacters with default_inventory: {len(with_inv)}")
    for name, cid, inv in with_inv:
        print(f"  {name}: {inv}")

if __name__ == '__main__':
    audit_all_characters()
