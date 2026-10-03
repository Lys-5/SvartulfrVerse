import os
import sys
import json
import requests
import uuid

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def get_world(token, wid):
    url = f"{API_BASE}/worlds/{wid}"
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"GET world failed: {resp.status_code} {resp.text}")
    return resp.json()

def put_world(token, wid, body):
    url = f"{API_BASE}/worlds/{wid}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.put(url, headers=headers, json=body)
    if resp.status_code != 200:
        raise Exception(f"PUT world failed: {resp.status_code} {resp.text}")
    return resp.json()

def main():
    token = get_auth_token()
    print("Fetching world...")
    world = get_world(token, WORLD_ID)
    
    # 1. Update relationship_config
    rel_config = world.get('relationship_config', {})
    moodlets = rel_config.get('custom_moodlets', [])
    
    new_moods = [
        {"id": "m_pre_heat", "label": "Pre-Heat", "delta": 15, "duration_hours": 72},
        {"id": "m_heat", "label": "In Heat", "delta": 40, "duration_hours": 168},
        {"id": "m_rut", "label": "In Rut", "delta": 40, "duration_hours": 168}
    ]
    
    existing_ids = [m.get('id') for m in moodlets]
    for nm in new_moods:
        if nm['id'] not in existing_ids:
            moodlets.append(nm)
            
    rel_config['custom_moodlets'] = moodlets
    
    # 2. Update stat_config
    stat_config = world.get('stat_config', {})
    
    # Replace default stats with MGT, RES, AGI, WIT, PRS, SCT
    stats = [
        {"id": "stat_1", "label": "Might", "abbreviation": "MGT", "enabled": True},
        {"id": "stat_2", "label": "Resilience", "abbreviation": "RES", "enabled": True},
        {"id": "stat_3", "label": "Agility", "abbreviation": "AGI", "enabled": True},
        {"id": "stat_4", "label": "Wits", "abbreviation": "WIT", "enabled": True},
        {"id": "stat_5", "label": "Presence", "abbreviation": "PRS", "enabled": True},
        {"id": "stat_6", "label": "Scouting", "abbreviation": "SCT", "enabled": True}
    ]
    stat_config['stats'] = stats
    stat_config['base_value'] = 1
    stat_config['point_budget'] = 25
    stat_config['max_traits'] = 10
    # Map stat_roles to the new ids
    stat_config['stat_roles'] = {
        "hp": "stat_2",
        "physical_attack": "stat_1",
        "physical_defense": "stat_2",
        "special_attack": "stat_4",
        "special_defense": "stat_4",
        "mp_stat": "stat_4",
        "speed": "stat_3",
        "accuracy": "stat_3",
        "evasion": "stat_3",
        "flee": "stat_3",
        "luck": "stat_6"
    }
    
    body = {
        "relationship_config": rel_config,
        "stat_config": stat_config
    }
    
    print("Updating world...")
    put_world(token, WORLD_ID, body)
    print("Update successful!")

if __name__ == '__main__':
    main()
