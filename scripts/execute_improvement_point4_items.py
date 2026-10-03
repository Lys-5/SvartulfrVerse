import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'
CURRENCY_USD = 'fbecc738-f9f7-4426-b8a1-a237b8ad922c'

ITEMS_CONFIG = {
    # Weapons
    '_XyPQbcYGhh7FbQTN4Py2p': {'slot': 'main_hand', 'rarity': 'common', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 250},
    '_9TydMzqz7TAyggeMyVjnW': {'slot': 'main_hand', 'rarity': 'uncommon', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 120},
    '_746G8T2RVL2tRExw337cq': {'slot': 'main_hand', 'rarity': 'rare', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 1200},
    '_xbjVJJ3aNC4W9Uz4nNn4d': {'slot': 'main_hand', 'rarity': 'legendary', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 50000},
    '_XNkgRjKF6XRnKqgJjkUR3': {'slot': 'two_hand', 'rarity': 'legendary', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 65000},
    '_8WaPQUH42VgQz2xVXaJF7': {'slot': 'body', 'rarity': 'epic', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 8500},

    # Apparel / Gowns
    '_TwdTtK8VWNaUrBkLF8cj2': {'slot': 'body', 'rarity': 'rare', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 3500},
    '_9ETrKmarxnCG8qWp2V7bR': {'slot': 'body', 'rarity': 'rare', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 4200},

    # Accessories, Electronics & Everyday Tools
    '_UVX1RAqE8CWz8ywYkT4Fm': {'slot': 'head', 'rarity': 'common', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 75},
    '_YxGJRFDkjdVyeH1mJNM1T': {'slot': 'accessory', 'rarity': 'common', 'tradeable': True, 'stackable': True, 'consumable': False, 'val': 15},
    '_BRjbkk8JM3Jw1xyJGgzDH': {'slot': 'accessory', 'rarity': 'common', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 20},
    '_zhejTy83qc3bg6MNGU6ak': {'slot': 'accessory', 'rarity': 'common', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 800},
    '_bPh4kGmBQWczPJW2yf7G6': {'slot': 'accessory', 'rarity': 'common', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 45},
    '_N3UKUdUwaWeKnD3EEXrUU': {'slot': 'accessory', 'rarity': 'common', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 30},
    '_GNAP7tw8UWry76Dww36FR': {'slot': 'accessory', 'rarity': 'uncommon', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 150},
    '_NXGxXRm4eEpNrGk1tjjNH': {'slot': 'accessory', 'rarity': 'uncommon', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 80},
    '_aqUFagqQnjUUjynEmxXFM': {'slot': 'accessory', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 0},
    '_4XxeUWQBrBUJxH6JjQtNq': {'slot': 'neck', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 1500},
    '_eDhQ8NgT8eG9A67AEJbUH': {'slot': 'accessory', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 2500},
    '_gQga39XbehpJa2YLjKBN4': {'slot': 'back', 'rarity': 'epic', 'tradeable': True, 'stackable': False, 'consumable': False, 'val': 600},
    '_B3Y9cAUxJNbx266Ph1hCX': {'slot': 'back', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 850},
    '_NPnaqeH3xXpqL8Y3GnnHR': {'slot': 'accessory', 'rarity': 'legendary', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 10000},
    '_cyz7rXrhYxNUD61nfMVFf': {'slot': 'accessory', 'rarity': 'legendary', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 100000},

    # Consumables & Cores
    '_H6xyd4Wf8UnDhH62yhLb2': {'slot': 'accessory', 'rarity': 'uncommon', 'tradeable': True, 'stackable': True, 'consumable': True, 'val': 95},
    '_h4A1mMrYQy36kbY62ChdN': {'slot': 'accessory', 'rarity': 'rare', 'tradeable': False, 'stackable': True, 'consumable': True, 'val': 300},
    '_mQ4wm3ED9192HEEKJ8pzb': {'slot': 'accessory', 'rarity': 'rare', 'tradeable': True, 'stackable': True, 'consumable': True, 'val': 120},
    '_yX62N9dALqk3AYrmkd67H': {'slot': 'accessory', 'rarity': 'epic', 'tradeable': True, 'stackable': True, 'consumable': False, 'val': 1500},
    '_yePEEGFty3bfJ9zGhq3ew': {'slot': 'accessory', 'rarity': 'rare', 'tradeable': True, 'stackable': True, 'consumable': False, 'val': 450},

    # Vehicles & Keys
    '_NadEJefbKJ2fDMkWH2E1Y': {'slot': 'vehicle', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 18000},
    '_qm8mJaU7w1cPbEhyqqGLQ': {'slot': 'vehicle', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 22000},
    '_AnjFMMp2TXJebQWUHKMYW': {'slot': 'vehicle', 'rarity': 'epic', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 140000},
    '_daCL1ektYmVmxwDQyqqQ2': {'slot': 'vehicle', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 95000},
    '_43YpaDM3QxbHTNDgN4yAr': {'slot': 'vehicle', 'rarity': 'rare', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 65000},
    '_yqJhrzm6KWPtFy9F736rD': {'slot': 'vehicle', 'rarity': 'uncommon', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 12000},
    '_Btz9THKwAB4rJHadchgKJ': {'slot': 'vehicle', 'rarity': 'legendary', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 450000},
    '_mtny9zMQxyk6166R2ctDM': {'slot': 'accessory', 'rarity': 'common', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 10},
    '_XRYgVtcEUq7fEj7GaqERR': {'slot': 'accessory', 'rarity': 'common', 'tradeable': False, 'stackable': False, 'consumable': False, 'val': 10},
}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print(f"--- PUNTO 4: CONFIGURAZIONE ITEM_CONFIG SU {len(ITEMS_CONFIG)} ITEM ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    # Load master export for names
    data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    lex_map = {e['id']: e['name'] for e in data['world_lexicon_entries']}

    success_cnt = 0
    for eid, spec in ITEMS_CONFIG.items():
        ename = lex_map.get(eid, eid)
        safe_name = ename.encode('ascii', 'replace').decode('ascii')
        cfg = {
            'stackable': spec['stackable'],
            'tradeable': spec['tradeable'],
            'equip_slot': spec['slot'],
            'rarity': spec['rarity'],
            'consumable': spec['consumable'],
            'sellback_pct': 0.5,
            'value': {CURRENCY_USD: spec['val']} if spec['val'] > 0 else {}
        }
        url = f"{API_BASE}/lexicon/{eid}?world_id={WORLD_ID}"
        try:
            req = urllib.request.Request(url, data=json.dumps({'item_config': cfg}).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
            slot = res.get('item_config', {}).get('equip_slot')
            rarity = res.get('item_config', {}).get('rarity')
            print(f"  [ITEM OK] {safe_name[:35]:35} -> Slot: {slot}, Rarity: {rarity}, Val: ${spec['val']}")
            success_cnt += 1
        except Exception as e:
            print(f"  [ITEM ERR] {safe_name[:35]:35}: {e}")
        time.sleep(0.15)

    print(f"\n--- PUNTO 4 COMPLETATO: {success_cnt}/{len(ITEMS_CONFIG)} item configurati con successo! ---")

if __name__ == '__main__':
    main()
