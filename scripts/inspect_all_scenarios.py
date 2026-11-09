"""
Inspect standalone Character Scenarios and World Scenarios on Wyvern API and locally.
"""
import os
import sys
import json
import urllib.request

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token

def main():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    # 1. Standalone Character Scenarios
    req1 = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios', headers=headers)
    try:
        with urllib.request.urlopen(req1) as r:
            scenarios = json.loads(r.read().decode('utf-8'))
        print(f"=== Standalone Character Scenarios ({len(scenarios)}) ===")
        for s in scenarios:
            print(f"ID: {s.get('id')} | Title: {s.get('title')} | linked_world_id: {s.get('linked_world_id')}")
            print(f"   lorebook_ids: {s.get('lorebook_ids')}")
            print(f"   characters count: {len(s.get('characters', []))}")
            print(f"   has startup_script: {bool(s.get('startup_script'))}")
    except Exception as e:
        print(f"Error fetching character scenarios: {e}")

    # 2. World Scenarios
    world_id = '_YpX47fNraQFw2dD7TdycJ'
    req2 = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/scenarios/world/{world_id}', headers=headers)
    try:
        with urllib.request.urlopen(req2) as r:
            wscenarios = json.loads(r.read().decode('utf-8'))
        print(f"\n=== World Scenarios in {world_id} ({len(wscenarios)}) ===")
        for s in wscenarios:
            print(f"ID: {s.get('id')} | Title: {s.get('title') or s.get('name')} | Loc: {s.get('location_id')}")
            print(f"   slots count: {len(s.get('slots', s.get('characters', [])))}")
            print(f"   has startup_script: {bool(s.get('startup_script'))}")
    except Exception as e:
        print(f"Error fetching world scenarios: {e}")

if __name__ == '__main__':
    main()
