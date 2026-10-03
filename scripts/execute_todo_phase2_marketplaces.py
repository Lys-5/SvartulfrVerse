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

    print("--- FASE 2: ATTIVAZIONE DEI MARKETPLACE E INVENTARI VENDITA ---")

    markets = [
        # 1. THE VERVE
        {
            'location_id': '_hfm1W4nYnXfQEqcNGwNxr',
            'name': 'The Verve Bar & Pro Shop',
            'config': {
                'enabled': True,
                'name': 'The Verve Bar & Pro Shop',
                'description': 'Cocktail artigianali, accendini incisi, auricolari ad alta fedelta e drink speciali.',
                'buy_rate': 0.5,
                'inventory': [
                    {'lexicon_entry_id': '_YxGJRFDkjdVyeH1mJNM1T', 'stock': 50, 'price_override': {CURRENCY_USD: 15}},
                    {'lexicon_entry_id': '_UVX1RAqE8CWz8ywYkT4Fm', 'stock': 25, 'price_override': {CURRENCY_USD: 75}},
                    {'lexicon_entry_id': '_BRjbkk8JM3Jw1xyJGgzDH', 'stock': 30, 'price_override': {CURRENCY_USD: 25}},
                    {'lexicon_entry_id': '_mQ4wm3ED9192HEEKJ8pzb', 'stock': 10, 'price_override': {CURRENCY_USD: 120}}
                ]
            }
        },
        # 2. SIDEWINDERS BAR & NIGHTCLUB
        {
            'location_id': '_VbjcwqJnc7BaED9A9t2Dq',
            'name': 'Sidewinders Bar & Nightclub',
            'config': {
                'enabled': True,
                'name': 'Sidewinders Club Counter',
                'description': 'Bevande, accendini e accessori da festa per studenti di Solarton.',
                'buy_rate': 0.4,
                'inventory': [
                    {'lexicon_entry_id': '_YxGJRFDkjdVyeH1mJNM1T', 'stock': 40, 'price_override': {CURRENCY_USD: 10}},
                    {'lexicon_entry_id': '_UVX1RAqE8CWz8ywYkT4Fm', 'stock': 15, 'price_override': {CURRENCY_USD: 60}},
                    {'lexicon_entry_id': '_mQ4wm3ED9192HEEKJ8pzb', 'stock': 8, 'price_override': {CURRENCY_USD: 100}}
                ]
            }
        },
        # 3. BRICKLANE MALL
        {
            'location_id': '_hGpPMY77NaH4j6AxNGLVe',
            'name': 'Bricklane Mall',
            'config': {
                'enabled': True,
                'name': 'Bricklane Electronics & Department Store',
                'description': 'Smartphone, tecnologia, portafogli e accessori quotidiani.',
                'buy_rate': 0.6,
                'inventory': [
                    {'lexicon_entry_id': '_zhejTy83qc3bg6MNGU6ak', 'stock': 15, 'price_override': {CURRENCY_USD: 800}},
                    {'lexicon_entry_id': '_UVX1RAqE8CWz8ywYkT4Fm', 'stock': 40, 'price_override': {CURRENCY_USD: 80}},
                    {'lexicon_entry_id': '_bPh4kGmBQWczPJW2yf7G6', 'stock': 30, 'price_override': {CURRENCY_USD: 45}},
                    {'lexicon_entry_id': '_YxGJRFDkjdVyeH1mJNM1T', 'stock': 60, 'price_override': {CURRENCY_USD: 12}}
                ]
            }
        },
        # 4. STUDENT ASSOCIATION BUILDING
        {
            'location_id': '_aLqMW6UHHj1D9M4xxENF7',
            'name': 'Student Association Building',
            'config': {
                'enabled': True,
                'name': 'SUCC Student Store & Sundries',
                'description': 'Badge accademici, auricolari da studio e portachiavi per dormitori.',
                'buy_rate': 0.5,
                'inventory': [
                    {'lexicon_entry_id': '_N3UKUdUwaWeKnD3EEXrUU', 'stock': 100, 'price_override': {CURRENCY_USD: 30}},
                    {'lexicon_entry_id': '_UVX1RAqE8CWz8ywYkT4Fm', 'stock': 30, 'price_override': {CURRENCY_USD: 65}},
                    {'lexicon_entry_id': '_BRjbkk8JM3Jw1xyJGgzDH', 'stock': 50, 'price_override': {CURRENCY_USD: 15}}
                ]
            }
        },
        # 5. TEAM UKIYO OPERATIONAL BASE
        {
            'location_id': '_erHMcydnPVEyk7NY3K9wf',
            'name': 'Team Ukiyo Operational Base (Warehouse & Black Vault)',
            'config': {
                'enabled': True,
                'name': 'Ukiyo Tactical Depot & Quartermaster',
                'description': 'Equipaggiamento tattico, lame da dungeon, kit medici e nuclei abissali.',
                'buy_rate': 0.65,
                'inventory': [
                    {'lexicon_entry_id': '_XyPQbcYGhh7FbQTN4Py2p', 'stock': 10, 'price_override': {CURRENCY_USD: 250}},
                    {'lexicon_entry_id': '_9TydMzqz7TAyggeMyVjnW', 'stock': 15, 'price_override': {CURRENCY_USD: 120}},
                    {'lexicon_entry_id': '_H6xyd4Wf8UnDhH62yhLb2', 'stock': 20, 'price_override': {CURRENCY_USD: 95}},
                    {'lexicon_entry_id': '_NXGxXRm4eEpNrGk1tjjNH', 'stock': 10, 'price_override': {CURRENCY_USD: 80}},
                    {'lexicon_entry_id': '_yX62N9dALqk3AYrmkd67H', 'stock': 3, 'price_override': {CURRENCY_USD: 1500}},
                    {'lexicon_entry_id': '_gQga39XbehpJa2YLjKBN4', 'stock': 5, 'price_override': {CURRENCY_USD: 600}}
                ]
            }
        },
        # 6. THE DEAD DOG MOTEL
        {
            'location_id': '_qBt3jf1kppwrmMwTBbYJB',
            'name': 'The Dead Dog Motel',
            'config': {
                'enabled': True,
                'name': 'Dead Dog Vending & Supplies',
                'description': 'Distributori automatici, accendini e rifornimenti essenziali ai confini del void.',
                'buy_rate': 0.4,
                'inventory': [
                    {'lexicon_entry_id': '_YxGJRFDkjdVyeH1mJNM1T', 'stock': 25, 'price_override': {CURRENCY_USD: 8}},
                    {'lexicon_entry_id': '_BRjbkk8JM3Jw1xyJGgzDH', 'stock': 20, 'price_override': {CURRENCY_USD: 20}},
                    {'lexicon_entry_id': '_H6xyd4Wf8UnDhH62yhLb2', 'stock': 5, 'price_override': {CURRENCY_USD: 110}}
                ]
            }
        }
    ]

    for m in markets:
        try:
            lid = m['location_id']
            res = api_put_location(lid, {'marketplace_config': m['config']}, token)
            inv = res.get('marketplace_config', {}).get('inventory', [])
            print(f"  [OK] Marketplace '{m['name']}' ({lid}): {len(inv)} item a catalogo")
        except Exception as e:
            print(f"  [ERRORE] Marketplace '{m['name']}': {e}")
        time.sleep(0.3)

    print("\n--- FASE 2 COMPLETATA CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
