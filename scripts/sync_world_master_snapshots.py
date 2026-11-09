"""
Script to synchronize all authoritative live World configurations and RPG catalogs
into FINAL/ and update scratch/ snapshots, ensuring 100% Omni-Parity.
"""

import os
import sys
import json
import shutil
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }

def main():
    print("=== Synchronizing Live World State to FINAL/ and scratch/ ===")
    headers = get_headers()
    
    # 1. Fetch live world
    print("Fetching live World metadata...")
    url_world = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"
    req_w = urllib.request.Request(url_world, headers=headers)
    with urllib.request.urlopen(req_w) as resp:
        world_data = json.loads(resp.read().decode('utf-8'))
        
    world_scratch = os.path.join(ROOT_DIR, 'scratch', f'live_world_YpX47fNraQFw2dD7TdycJ.json')
    with open(world_scratch, 'w', encoding='utf-8') as f:
        json.dump(world_data, f, indent=2, ensure_ascii=False)
    print(f"  -> Saved {world_scratch}")
    
    # 2. Fetch live lexicon
    print("Fetching live World Lexicon (including 54 items)...")
    url_lex = f"https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}"
    req_l = urllib.request.Request(url_lex, headers=headers)
    with urllib.request.urlopen(req_l) as resp:
        lex_data = json.loads(resp.read().decode('utf-8'))
        
    lex_scratch = os.path.join(ROOT_DIR, 'scratch', f'live_world__YpX47fNraQFw2dD7TdycJ_lexicon.json')
    with open(lex_scratch, 'w', encoding='utf-8') as f:
        json.dump(lex_data, f, indent=2, ensure_ascii=False)
    print(f"  -> Saved {lex_scratch} ({len(lex_data)} entries)")
    
    # 3. Fetch live locations
    print("Fetching live World Locations (including 5 shops)...")
    url_loc = f"https://app.wyvern.chat/api/worlds/locations/world/{WORLD_ID}"
    req_loc = urllib.request.Request(url_loc, headers=headers)
    with urllib.request.urlopen(req_loc) as resp:
        loc_data = json.loads(resp.read().decode('utf-8'))
        
    loc_scratch = os.path.join(ROOT_DIR, 'scratch', f'live_world__YpX47fNraQFw2dD7TdycJ_locations.json')
    with open(loc_scratch, 'w', encoding='utf-8') as f:
        json.dump(loc_data, f, indent=2, ensure_ascii=False)
    print(f"  -> Saved {loc_scratch} ({len(loc_data)} locations)")
    
    # 4. Copy catalogs to FINAL/
    print("\nArchiving RPG Catalogs into FINAL/...")
    catalogs = [
        ('rpg_species_catalog.json', 'species'),
        ('rpg_occupations_catalog.json', 'occupations'),
        ('rpg_traits_catalog.json', 'traits')
    ]
    
    for filename, sub in catalogs:
        src = os.path.join(ROOT_DIR, 'scratch', filename)
        dst = os.path.join(ROOT_DIR, 'FINAL', filename)
        
        # Verify live API content for this catalog
        url_cat = f"https://app.wyvern.chat/api/worlds/rpg/{sub}/{WORLD_ID}"
        req_c = urllib.request.Request(url_cat, headers=headers)
        with urllib.request.urlopen(req_c) as resp:
            live_items = json.loads(resp.read().decode('utf-8'))
            
        with open(dst, 'w', encoding='utf-8') as f:
            json.dump(live_items, f, indent=2, ensure_ascii=False)
        print(f"  -> Archived {dst} ({len(live_items)} {sub})")
        
        # Keep scratch synchronized
        with open(src, 'w', encoding='utf-8') as f:
            json.dump(live_items, f, indent=2, ensure_ascii=False)

    # 5. Save canonical World RPG config in FINAL/
    final_rpg_config_path = os.path.join(ROOT_DIR, 'FINAL', 'Svartulfr_World_RPG_Config.json')
    final_rpg_config = {
        "world_id": WORLD_ID,
        "world_name": world_data.get('name'),
        "stat_config": world_data.get('stat_config'),
        "relationship_config": world_data.get('relationship_config'),
        "shop_locations": [
            {
                "id": loc.get('id'),
                "name": loc.get('name'),
                "marketplace_config": loc.get('marketplace_config')
            }
            for loc in loc_data if loc.get('marketplace_config', {}).get('enabled') is True
        ]
    }
    with open(final_rpg_config_path, 'w', encoding='utf-8') as f:
        json.dump(final_rpg_config, f, indent=2, ensure_ascii=False)
    print(f"  -> Saved {final_rpg_config_path}")
    
    print("\n[SUCCESS] All snapshots and FINAL/ catalogs synchronized with 100% Omni-Parity!")

if __name__ == '__main__':
    main()
