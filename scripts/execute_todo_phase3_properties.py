import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'
CURRENCY_USD = 'fbecc738-f9f7-4426-b8a1-a237b8ad922c'

def api_put_location(location_id, payload, token):
    url = f"{API_BASE}/locations/{location_id}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print("--- FASE 3: ATTIVAZIONE DI PROPERTY CONFIG SU ALLOGGI E DORMITORI ---")

    properties = [
        # 1. Wyrm Dormitories
        {
            'location_id': '_xfz8yrt2RjqHyTa8MXG3W',
            'name': 'Wyrm Dormitories',
            'rent': 650,
            'hours': 168
        },
        # 2. Apollo Dorms
        {
            'location_id': '_wEkzHgpxfetQr16bTWNUP',
            'name': 'Apollo Dorms',
            'rent': 600,
            'hours': 168
        },
        # 3. Artemis Dorms
        {
            'location_id': '_9YKj9HxFkRWnNJUJk84Tr',
            'name': 'Artemis Dorms',
            'rent': 600,
            'hours': 168
        },
        # 4. Apartment C (The Horns)
        {
            'location_id': '_CPWKPYwWeDY7ktNgBLWAy',
            'name': 'Apartment C',
            'rent': 550,
            'hours': 168
        },
        # 5. Coastal Residential (Blackwood City)
        {
            'location_id': '_UeKEhHTnCP6yQk7mhMVU1',
            'name': 'Coastal Residential',
            'rent': 1200,
            'hours': 168
        },
        # 6. Villa Douglas: Guest Wing
        {
            'location_id': '_mUHCbXLjDAy8YqraaR7jf',
            'name': 'Villa Douglas: Guest Wing',
            'rent': 1,
            'hours': 168
        },
        # 7. The Dead Dog Motel
        {
            'location_id': '_qBt3jf1kppwrmMwTBbYJB',
            'name': 'The Dead Dog Motel',
            'rent': 150,
            'hours': 168
        },
        # 8. Eidolon Creative Private Suites
        {
            'location_id': '_RTxCmM7pKQGx8VVA83B7Q',
            'name': 'Eidolon Creative Private Suites',
            'rent': 1800,
            'hours': 168
        }
    ]

    for p in properties:
        lid = p['location_id']
        name = p['name']
        prop_config = {
            'enabled': True,
            'rentable': True,
            'rent_price': {
                CURRENCY_USD: p['rent']
            },
            'rent_interval_hours': p['hours']
        }
        try:
            res = api_put_location(lid, {'property_config': prop_config}, token)
            cfg = res.get('property_config', {})
            print(f"  [OK] Property '{name}' ({lid}): rentable={cfg.get('rentable')}, rent=${p['rent']}/{p['hours']}h")
        except Exception as e:
            print(f"  [ERRORE] Property '{name}' ({lid}): {e}")
        time.sleep(0.3)

    print("\n--- FASE 3 COMPLETATA CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
