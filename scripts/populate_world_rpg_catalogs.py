"""
Script to populate RPG Species (24), Occupations (28), and Traits (46)
on Wyvern World _YpX47fNraQFw2dD7TdycJ.
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def populate_collection(name, file_path, endpoint):
    print(f"\n--- Populating {name} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        catalog = json.load(f)
    print(f"Loaded {len(catalog)} items from {os.path.basename(file_path)}")

    created_items = []
    for i, item in enumerate(catalog):
        payload = {
            "world_id": WORLD_ID,
            "name": item.get("name"),
            "description": item.get("description", ""),
            "stat_modifiers": item.get("stat_modifiers", {}),
            "player_selectable": item.get("player_selectable", True),
            "tags": item.get("tags", []),
            "display_order": item.get("display_order", i)
        }
        
        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode('utf-8'),
            headers=get_headers(),
            method='POST'
        )
        
        retries = 3
        while retries > 0:
            try:
                with urllib.request.urlopen(req) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    created_items.append(data)
                    print(f"  [{i+1}/{len(catalog)}] Created: {item.get('name')} (id: {data.get('id')})")
                    break
            except urllib.error.HTTPError as e:
                err_text = e.read().decode('utf-8', errors='ignore')
                print(f"  [ERROR] Attempt failed for {item.get('name')}: {e.code} {err_text}")
                retries -= 1
                if retries > 0:
                    time.sleep(1)
                else:
                    raise RuntimeError(f"Failed to create {item.get('name')}: {e.code} {err_text}")
        time.sleep(0.15)
        
    print(f"Successfully created {len(created_items)} items for {name}!")
    return created_items

def main():
    print(f"=== Populating RPG Systems on World {WORLD_ID} ===")

    species_path = os.path.join(ROOT_DIR, 'scratch', 'rpg_species_catalog.json')
    occupations_path = os.path.join(ROOT_DIR, 'scratch', 'rpg_occupations_catalog.json')
    traits_path = os.path.join(ROOT_DIR, 'scratch', 'rpg_traits_catalog.json')

    # 1. Species (24)
    populate_collection(
        "Species",
        species_path,
        "https://app.wyvern.chat/api/worlds/rpg/species"
    )

    # 2. Occupations (28)
    populate_collection(
        "Occupations",
        occupations_path,
        "https://app.wyvern.chat/api/worlds/rpg/occupations"
    )

    # 3. Traits (46)
    populate_collection(
        "Traits",
        traits_path,
        "https://app.wyvern.chat/api/worlds/rpg/traits"
    )

    # Verification
    print("\n=== Verifying Total Counts on World ===")
    for sub in ['species', 'occupations', 'traits']:
        url = f"https://app.wyvern.chat/api/worlds/rpg/{sub}/{WORLD_ID}"
        req = urllib.request.Request(url, headers=get_headers())
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  {sub.capitalize()} on World: {len(data)}")

if __name__ == '__main__':
    main()
