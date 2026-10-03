import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

SCENARIO_TARGETS = [
    {
        'id': '_Kn2DFVwyUgkVGz9UWUnBF',
        'location_id': '_DJxYBCM7rNrXMj1WracGM',  # Club House Ironhorn Nomads
        'name': 'Fumo di Gomma, Birra e Cloro: Il Branco dei Nomads'
    },
    {
        'id': '_7X4UXynjEUKbQhPDHxVRr',
        'location_id': '_RVRf9PtEdwhGt3rGGFjMC',  # The Cable District (HSK Consulting HQ)
        'name': 'Stage Formativo HSK: Il Colloquio e la Selezione'
    },
    {
        'id': '_X86JF72TG4p2DYqw7LzRp',
        'location_id': '_p1JatqFwBPeKPQrh6CmGe',  # Beta Rho Omega (BRO Frat House)
        'name': 'Halloween dei BRO: La Festa di Beta Rho Omega'
    },
    {
        'id': '_nMaPEAzNA8rQc82NFgXRU',
        'location_id': '_VbjcwqJnc7BaED9A9t2Dq',  # Sidewinders Bar & Nightclub
        'name': 'Basso Distorto e Sguardi da Lupo: Sabato Sera al Sidewinders'
    },
    {
        'id': '_XWFqGmaTPkbpbFQzargbf',
        'location_id': '_Bx2U1xzg1D3wpFRe39L7y',  # Bulls Stadium
        'name': 'Impatto sul Campo dei Bulls: Lo Scontro con Jared'
    },
    {
        'id': '_p1Ffq22CTwVywz1CFQBfF',
        'location_id': '_9H2EmzRm92QxBpkmJUR1z',  # Villa Douglas
        'name': 'Oltre i Cancelli della Villa: Il Primo Passo a Solarton'
    },
    {
        'id': '_h7N17PhK4ag3GxM8Bgr8g',
        'location_id': '_hfm1W4nYnXfQEqcNGwNxr',  # The Verve
        'name': 'Overclock Notturno: Il Rave Clandestino di DJ Frequency'
    },
    {
        'id': '_h7UQKNmxNJP8e7Jq1mEVL',
        'location_id': '_FrXnp2CALTP44CP3KVAhb',  # Ventura / Route 101
        'name': 'Asfalto e Liberta: Due Settimane On the Road con Logan'
    },
    {
        'id': '_F3AKNnAjh2UwUaJe9kc6A',
        'location_id': '_RXULtwFjxCBUcxBbTfWrh',  # Bloodmoon Longhouse
        'name': "L'Ombra del Primo Padre: La Grande Veglia con Wulfnic"
    },
    {
        'id': '_XwKb3hg1wG7gNgAdfGETr',
        'location_id': '_j67Dp2PVwFCpdrfWRYV2M',  # Supernatural University of Central California
        'name': 'Reclute sotto Scorta: Visita Tattica al Campus SUCC'
    },
    {
        'id': '_RL8HD1PbxLzNARyrHqqAn',
        'location_id': '_P78yNW43E1fayK9cXzGpd',  # Villa Douglas: Noah's Gourmet Kitchen
        'name': 'Il Bivio del Patriarca: Incontro in Cucina con Erik'
    }
]

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print("--- PUNTO 1: ALLINEAMENTO LOCATION INIZIALE SCENARI ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    for sc in SCENARIO_TARGETS:
        sid = sc['id']
        lid = sc['location_id']
        sname = sc['name']
        url = f"{API_BASE}/scenarios/{sid}"
        payload = {'location_id': lid}
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
            cur_loc = res.get('location_id') or (res.get('location', {}).get('id') if isinstance(res.get('location'), dict) else res.get('location'))
            print(f"  [SCENARIO OK] {sname[:40]:40} -> Location: {cur_loc}")
        except Exception as e:
            print(f"  [SCENARIO ERR] {sname[:40]:40}: {e}")
        time.sleep(0.2)

    print("\n--- PUNTO 1 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
