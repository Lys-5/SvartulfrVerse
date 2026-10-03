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

def api_get(resource, entity_id, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

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

    print("--- STEP 4: AGGIORNAMENTO DEI PIN SULLE 4 MAPPE INTERATTIVE ---")

    # =========================================================================
    # 1. MAPPA SUCC (_jgbKVct94DLCynDdR9Gm9)
    # =========================================================================
    succ_map_id = '_jgbKVct94DLCynDdR9Gm9'
    succ_map = api_get('maps', succ_map_id, token)
    pins_succ = succ_map.get('pins', [])

    # Aggiorna pin Basilica Library
    for p in pins_succ:
        if p.get('label') == 'Basilisk Library' or p.get('location_id') == '_VGJ1w83h4Da3TxPEYbj1R':
            p['label'] = 'Basilica Library'
            p['location_id'] = '_jYJxF7fte2Gz1F2HGXpUR'
            p['color'] = '#9b59b6'

    # Aggiungi Meeting Room 005 se non presente
    if not any(p.get('id') == 'succ_room_005' for p in pins_succ):
        pins_succ.append({
            'id': 'succ_room_005',
            'location_id': '_4FMaQm3xQCUVHeRf3AWYk',
            'label': 'Library Meeting Room 005',
            'x_percent': 46.0,
            'y_percent': 49.0,
            'color': '#8e44ad',
            'visible': True
        })

    api_put('maps', succ_map_id, {'pins': pins_succ}, token)
    res_succ = api_get('maps', succ_map_id, token)
    print(f"  [OK] Mappa SUCC ({succ_map_id}): {len(res_succ.get('pins', []))} pin totali salvati")

    # =========================================================================
    # 2. MAPPA CALIFORNIA COAST (_RXLz9h2xtnzD8VgR9qUCz)
    # =========================================================================
    cal_map_id = '_RXLz9h2xtnzD8VgR9qUCz'
    cal_map = api_get('maps', cal_map_id, token)
    pins_cal = cal_map.get('pins', [])

    # Correggi il pin con label vuota (Los Angeles)
    for p in pins_cal:
        if p.get('location_id') == '_X4A8gWVr43a7dRr9TbJ4m' and not p.get('label'):
            p['label'] = 'Los Angeles'
            p['color'] = '#3498db'

    # Aggiungi Dead Dog Motel
    if not any(p.get('id') == 'cal_dead_dog_motel' for p in pins_cal):
        pins_cal.append({
            'id': 'cal_dead_dog_motel',
            'location_id': '_qBt3jf1kppwrmMwTBbYJB',
            'label': 'The Dead Dog Motel',
            'x_percent': 34.0,
            'y_percent': 65.0,
            'color': '#c0392b',
            'visible': True
        })

    # Aggiungi Dockside Ferry Landing
    if not any(p.get('id') == 'cal_dockside_ferry' for p in pins_cal):
        pins_cal.append({
            'id': 'cal_dockside_ferry',
            'location_id': '_AWyPeCP8QWhD4D1M6hfzT',
            'label': 'Dockside Ferry Landing',
            'x_percent': 39.0,
            'y_percent': 44.0,
            'color': '#2980b9',
            'visible': True
        })

    api_put('maps', cal_map_id, {'pins': pins_cal}, token)
    res_cal = api_get('maps', cal_map_id, token)
    print(f"  [OK] Mappa California Coast ({cal_map_id}): {len(res_cal.get('pins', []))} pin totali salvati")

    # =========================================================================
    # 3. MAPPA BLACKWOOD (_tUtyKpzKzzeVCGyxQBkQD)
    # =========================================================================
    bw_map_id = '_tUtyKpzKzzeVCGyxQBkQD'
    bw_map = api_get('maps', bw_map_id, token)
    pins_bw = bw_map.get('pins', [])

    # Aggiungi Bloodmoon Longhouse
    if not any(p.get('id') == 'bw_bloodmoon_longhouse' for p in pins_bw):
        pins_bw.append({
            'id': 'bw_bloodmoon_longhouse',
            'location_id': '_RXULtwFjxCBUcxBbTfWrh',
            'label': 'Bloodmoon Longhouse & Sacred Yew',
            'x_percent': 82.0,
            'y_percent': 24.0,
            'color': '#c0392b',
            'visible': True
        })

    # Aggiungi Bloodmoon Longhouse Baths
    if not any(p.get('id') == 'bw_longhouse_baths' for p in pins_bw):
        pins_bw.append({
            'id': 'bw_longhouse_baths',
            'location_id': '_qUkFeCX37Agez4XtPhtqp',
            'label': 'Bloodmoon Longhouse Baths',
            'x_percent': 84.5,
            'y_percent': 26.5,
            'color': '#16a085',
            'visible': True
        })

    api_put('maps', bw_map_id, {'pins': pins_bw}, token)
    res_bw = api_get('maps', bw_map_id, token)
    print(f"  [OK] Mappa Blackwood ({bw_map_id}): {len(res_bw.get('pins', []))} pin totali salvati")

    print("\n--- STEP 4 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
