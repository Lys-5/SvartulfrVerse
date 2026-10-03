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
    
    currencies = world.get('currencies', [])
    
    # Check if DMHA Credits already exist
    exists = False
    for c in currencies:
        if c['name'] == 'DMHA Credits' or c['name'] == 'Guild Credits':
            exists = True
            break
            
    if not exists:
        currencies.append({
            "id": str(uuid.uuid4()),
            "name": "DMHA Guild Credits",
            "symbol": "Cr",
            "decimal_places": 0,
            "is_primary": False,
            "universal_credit_rate": 0.01  # 100 credits = 1 US Dollar
        })
        
        body = {
            "currencies": currencies
        }
        
        print("Updating currencies...")
        put_world(token, WORLD_ID, body)
        print("Update successful!")
    else:
        print("Currency already exists.")

if __name__ == '__main__':
    main()
