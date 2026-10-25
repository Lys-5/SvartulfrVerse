import sys
import os
import json
import urllib.request
import urllib.error

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
BASE_URL = 'https://app.wyvern.chat/api'

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def main():
    endpoints = ['/worlds/mine', '/worlds/user', '/worlds']
    headers = get_headers()
    
    for ep in endpoints:
        url = f"{BASE_URL}{ep}"
        req = urllib.request.Request(url, headers=headers, method='GET')
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                print(f"Endpoint {ep} succeeded, count: {len(data) if isinstance(data, list) else type(data)}")
                if isinstance(data, list):
                    for idx, w in enumerate(data):
                        print(f"[{idx}] ID: {w.get('id')} | Name: '{w.get('name')}' | Visibility: {w.get('visibility')} | Created: {w.get('created_at')} | Locations: {len(w.get('locations', []))} | Environments: {len(w.get('environments', []))}")
                    return data
                elif isinstance(data, dict):
                    worlds = data.get('worlds', [])
                    for idx, w in enumerate(worlds):
                        print(f"[{idx}] ID: {w.get('id')} | Name: '{w.get('name')}' | Visibility: {w.get('visibility')} | Created: {w.get('created_at')}")
                    return worlds
        except urllib.error.HTTPError as e:
            print(f"Endpoint {ep} returned {e.code}")

if __name__ == '__main__':
    main()
