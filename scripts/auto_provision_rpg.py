"""
RPG Auto-Provisioning Engine for Svartúlfr World (_YpX47fNraQFw2dD7TdycJ).
Ensures that any missing Species, Occupation, or Trait is automatically created
on the Wyvern World API and persisted to FINAL/ and scratch/ master catalogs.
"""

import os
import sys
import json
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
from scripts.sync_from_wyvern_web import get_auth_token

def get_headers(with_content_type=True):
    try:
        token = get_auth_token()
        with open(TOKEN_PATH, 'w', encoding='utf-8') as f:
            f.write(token)
    except Exception:
        with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
            token = f.read().strip()
            
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    if with_content_type:
        headers['Content-Type'] = 'application/json'
    return headers

def get_catalog(category):
    final_path = os.path.join(ROOT_DIR, 'FINAL', f'rpg_{category}_catalog.json')
    if os.path.exists(final_path):
        with open(final_path, 'r', encoding='utf-8') as f:
            return json.load(f)
            
    # Fallback to API if local file doesn't exist
    url = f"https://app.wyvern.chat/api/worlds/rpg/{category}/{WORLD_ID}"
    req = urllib.request.Request(url, headers=get_headers(with_content_type=False))
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def save_catalog(category, catalog):
    for folder in ['FINAL', 'scratch']:
        path = os.path.join(ROOT_DIR, folder, f'rpg_{category}_catalog.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(catalog, f, indent=2, ensure_ascii=False)

def check_and_provision_entity(category, name, description="", stat_modifiers=None, player_selectable=True, tags=None):
    """
    Checks if entity exists by name (case-insensitive) in category ('species', 'occupations', 'traits').
    If not, automatically provisions it via POST API and saves to local catalogs.
    Returns: (bool provisioned, dict entity_data)
    """
    assert category in ['species', 'occupations', 'traits'], f"Invalid category: {category}"
    catalog = get_catalog(category)
    
    # 1. Check existing
    norm_name = name.strip().lower()
    for item in catalog:
        if item.get('name', '').strip().lower() == norm_name:
            return False, item
            
    # 2. Auto-Provision via API
    print(f"[AUTO-PROVISION] Creating missing {category[:-1]}: '{name}' on World API...")
    url = f"https://app.wyvern.chat/api/worlds/rpg/{category}"
    payload = {
        "world_id": WORLD_ID,
        "name": name.strip(),
        "description": description or f"Auto-provisioned {category[:-1]} for Svartúlfr Verse.",
        "player_selectable": player_selectable,
        "stat_modifiers": stat_modifiers or {},
        "tags": tags or [],
        "display_order": len(catalog)
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers=get_headers(with_content_type=True),
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            created_item = json.loads(resp.read().decode('utf-8'))
            print(f"[AUTO-PROVISION SUCCESS] Created {name} with ID: {created_item.get('id')}")
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='ignore')
        raise RuntimeError(f"Auto-provisioning failed for {name} ({category}): HTTP {e.code} {err}")
        
    # 3. Synchronize local master catalogs
    catalog.append(created_item)
    save_catalog(category, catalog)
    
    return True, created_item

def delete_provisioned_entity(category, entity_id):
    """
    Deletes an entity by ID from Wyvern API and updates local catalogs.
    CRITICAL: Does NOT include Content-Type header to avoid Fastify FST_ERR_CTP_EMPTY_JSON_BODY.
    """
    assert category in ['species', 'occupations', 'traits'], f"Invalid category: {category}"
    url = f"https://app.wyvern.chat/api/worlds/rpg/{category}/{entity_id}"
    req = urllib.request.Request(url, headers=get_headers(with_content_type=False), method='DELETE')
    
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"[TEARDOWN SUCCESS] Deleted {category} entity {entity_id} (HTTP {resp.status})")
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='ignore')
        raise RuntimeError(f"Failed to delete {category} entity {entity_id}: HTTP {e.code} {err}")
        
    # Remove from local catalog
    catalog = get_catalog(category)
    new_catalog = [item for item in catalog if item.get('id') != entity_id]
    save_catalog(category, new_catalog)

if __name__ == '__main__':
    # Ad-hoc test CLI
    if len(sys.argv) > 2:
        cat = sys.argv[1]
        n = sys.argv[2]
        prov, it = check_and_provision_entity(cat, n)
        print(f"Result: provisioned={prov}, id={it.get('id')}")
    else:
        print("Usage: python auto_provision_rpg.py <species|occupations|traits> <name>")
