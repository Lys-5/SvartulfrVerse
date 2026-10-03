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

def api_put(resource, entity_id, payload, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
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

    print("--- STEP 2: WIRING INCLUDED_LEXICON_ENTRIES PER LOCATION ED ENVIRONMENT ---")

    # Mappatura Location -> Lista di Lexicon IDs
    location_wiring = [
        {
            'name': 'Basilica Library',
            'id': '_jYJxF7fte2Gz1F2HGXpUR',
            'lex_ids': ['_xB6wzXC39XpCgVmD89Y2h', '_2JKA6UUf8DAzBFbADWAAJ', '_h1BaVYDMckXpgdaDCFNed']
        },
        {
            'name': 'Library Basement Meeting Room 005',
            'id': '_4FMaQm3xQCUVHeRf3AWYk',
            'lex_ids': ['_2JKA6UUf8DAzBFbADWAAJ', '_h1BaVYDMckXpgdaDCFNed']
        },
        {
            'name': 'Bulls Stadium',
            'id': '_Bx2U1xzg1D3wpFRe39L7y',
            'lex_ids': ['_HPQnf2PEMBKYVdYDBLejW', '_CrpErFXTTJBRLrCR4hTeX', '_eDhC6hY41n7VtjTMxReP4']
        },
        {
            'name': 'St. Neptune Stadium',
            'id': '_ndMkLAHyKgBDyeMpjwhBt',
            'lex_ids': ['_xB6wzXC39XpCgVmD89Y2h', '_4QX9aHTxU71gaHHWk7M4W', '_HPQnf2PEMBKYVdYDBLejW', '_CrpErFXTTJBRLrCR4hTeX']
        },
        {
            'name': 'Main Pool',
            'id': '_GnNYqapde8TGQtemCwJHT',
            'lex_ids': ['_xB6wzXC39XpCgVmD89Y2h']
        },
        {
            'name': 'The Verve',
            'id': '_hfm1W4nYnXfQEqcNGwNxr',
            'lex_ids': ['_YxGJRFDkjdVyeH1mJNM1T', '_UVX1RAqE8CWz8ywYkT4Fm', '_BRjbkk8JM3Jw1xyJGgzDH']
        },
        {
            'name': 'Bloodmoon Longhouse',
            'id': '_RXULtwFjxCBUcxBbTfWrh',
            'lex_ids': [
                '_DckKRHKgyptVFwNxwWUTR', # The Tear Beneath the Yew
                '_rrzaRw7kGFNNRBV8LRQhp', # La Guerra di Fenris e l'Esilio dei Firstborn
                '_ALr42Gp4YJGrBdEebpJ83', # LSE Sacred Calendar of Fenris
                '_4bg7BKpHbBwkW6nLArqB9', # LSE Pantheon & the Nine Precepts of Fenris
                '_TQCr6hNmBqRKnm8FLAFDF'  # LSE Faith of Fenris
            ]
        },
        {
            'name': 'Bloodmoon Longhouse Baths',
            'id': '_qUkFeCX37Agez4XtPhtqp',
            'lex_ids': ['_ALr42Gp4YJGrBdEebpJ83', '_TQCr6hNmBqRKnm8FLAFDF']
        },
        {
            'name': 'Paradise',
            'id': '_H6PUHPMMUEmM2wJbfd8et',
            'lex_ids': ['_X2qqf3HhhdMahnhFUW3j7', '_LyHK91bhWrej3K4XyWW6h', '_xYWFcMXnH7M8qac4rGmXW']
        },
        {
            'name': 'The Dead Dog Motel',
            'id': '_qBt3jf1kppwrmMwTBbYJB',
            'lex_ids': ['_7H2Ve9Y7f33rTxNN9Ep91', '_GaQ8B1wLA7NCM1zP8JW6q']
        },
        {
            'name': 'Ventura / Route 101',
            'id': '_FrXnp2CALTP44CP3KVAhb',
            'lex_ids': ['_C6JqdNxNgtqeneW1DxbrK']
        },
        {
            'name': 'Dockside',
            'id': '_B7Eq8K8CUXrCe9NKATXGE',
            'lex_ids': ['_LyHK91bhWrej3K4XyWW6h', '_xYWFcMXnH7M8qac4rGmXW']
        }
    ]

    for loc in location_wiring:
        try:
            res = api_put('locations', loc['id'], {'included_lexicon_entries': loc['lex_ids']}, token)
            print(f"  [OK] Location '{loc['name']}' ({loc['id']}): {len(res.get('included_lexicon_entries', []))} lexicon collegati")
        except Exception as e:
            print(f"  [ERRORE] Location '{loc['name']}': {e}")
        time.sleep(0.3)

    # Mappatura Environment Voidspace
    print("\n--- AGGIORNAMENTO ENVIRONMENT VOIDSPACE ---")
    void_id = '_gNmX2qncQ6m9E4fG223ge'
    try:
        void_res = api_put('environments', void_id, {'included_lexicon_entries': ['_7H2Ve9Y7f33rTxNN9Ep91', '_GaQ8B1wLA7NCM1zP8JW6q']}, token)
        print(f"  [OK] Environment Voidspace ({void_id}): {len(void_res.get('included_lexicon_entries', []))} lexicon collegati")
    except Exception as e:
        print(f"  [ERRORE] Environment Voidspace: {e}")

    print("\n--- STEP 2 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
