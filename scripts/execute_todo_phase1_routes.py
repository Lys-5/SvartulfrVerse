import os
import sys
import json
import uuid
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def api_get_world(token):
    url = f"{API_BASE}/{WORLD_ID}"
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def api_put_world(payload, token):
    url = f"{API_BASE}/{WORLD_ID}"
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

    print("--- FASE 1: AGGIORNAMENTO GRAFO ROTTE DI VIAGGIO (TRAVEL ROUTES) & FREE TRAVEL ---")

    world = api_get_world(token)
    existing_routes = world.get('travel_routes', [])
    print(f"Rotte esistenti attuali: {len(existing_routes)}")

    existing_pairs = set()
    for r in existing_routes:
        f = r.get('from_location_id')
        t = r.get('to_location_id')
        existing_pairs.add((f, t))
        if r.get('bidirectional', True):
            existing_pairs.add((t, f))

    new_routes_defs = [
        # Regional & City Districts
        ('_9H2EmzRm92QxBpkmJUR1z', '_EwMMJ7KEg9ATJ3mTXBaha', 0, ['land'], 'Seven Hills residential approach to Villa Douglas gates.'),
        ('_EwMMJ7KEg9ATJ3mTXBaha', '_Gnm9WMQNjhUWJLhrkpqQk', 0, ['land'], 'Seven Hills descending road into historic Oldtown.'),
        ('_EwMMJ7KEg9ATJ3mTXBaha', '_8fRJTJVkd7VjkQ3jfJWQ1', 0, ['land'], 'Seven Hills ridge drive into financial Uptown district.'),
        ('_EwMMJ7KEg9ATJ3mTXBaha', '_hfm1W4nYnXfQEqcNGwNxr', 1, ['land'], 'Seven Hills bypass road down to Bluemoon and The Verve.'),
        ('_EwMMJ7KEg9ATJ3mTXBaha', '_H6PUHPMMUEmM2wJbfd8et', 1, ['land'], 'Boulevard connection to Paradise nightlife district.'),
        ('_Gnm9WMQNjhUWJLhrkpqQk', '_H6PUHPMMUEmM2wJbfd8et', 1, ['land'], 'Avenue connecting Oldtown to Paradise District.'),
        ('_Gnm9WMQNjhUWJLhrkpqQk', '_B7Eq8K8CUXrCe9NKATXGE', 0, ['land'], 'Oldtown cobblestone streets leading to riverfront Dockside.'),
        ('_Gnm9WMQNjhUWJLhrkpqQk', '_fyC1LJ8CAK8rP7k8Dr2a2', 0, ['land'], 'Transit line between colonial Oldtown and industrial Ironworks.'),
        ('_Gnm9WMQNjhUWJLhrkpqQk', '_X6R6dKTzkjdFk6cqdt2we', 0, ['land'], 'Oldtown boulevard leading into quiet residential Arcadia.'),
        ('_Gnm9WMQNjhUWJLhrkpqQk', '_xEB9X8wUGwQrELYzKX7gt', 1, ['land'], 'Forest highway into Bloodmoon Pack Territory.'),
        ('_xEB9X8wUGwQrELYzKX7gt', '_RXULtwFjxCBUcxBbTfWrh', 0, ['land'], 'Sacred pine trail leading to Bloodmoon Longhouse.'),
        ('_RXULtwFjxCBUcxBbTfWrh', '_qUkFeCX37Agez4XtPhtqp', 0, ['land'], 'Stone path to natural geothermal Longhouse Baths.'),
        ('_Gnm9WMQNjhUWJLhrkpqQk', '_761mFFeCcQyR9JxhLCWcy', 2, ['land'], 'Route 101 corridor connecting Blackwood and Solarton.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_Mq1DYmKdnkR83YBjNRyXr', 0, ['land'], 'Central thoroughfare to Solarton Square.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_hGpPMY77NaH4j6AxNGLVe', 0, ['land'], 'Shopping avenue to Bricklane Mall.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_VbjcwqJnc7BaED9A9t2Dq', 0, ['land'], 'Entertainment strip to Sidewinders Bar.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_UeKEhHTnCP6yQk7mhMVU1', 0, ['land'], 'Coastal road to Coastal Residential apartments.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_rnNnjzcmDkgg2xbHYFftH', 0, ['land'], 'Pier drive to Solarton Pier and ferry terminal.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_a2pRKBjYnQ1Q1LaN6xdeh', 0, ['land'], 'Boardwalk down to Solarton Public Beach.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_j67Dp2PVwFCpdrfWRYV2M', 0, ['land'], 'University Avenue into SUCC Campus Academic Core.'),
        ('_j67Dp2PVwFCpdrfWRYV2M', '_WrymW8qTETkm7r1QXQGaT', 0, ['land'], 'Main promenade opening into Lunar Quad.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_FrXnp2CALTP44CP3KVAhb', 1, ['land'], 'Route 101 coastal highway south toward Ventura.'),
        ('_FrXnp2CALTP44CP3KVAhb', '_qBt3jf1kppwrmMwTBbYJB', 1, ['land'], 'Highway pull-off to The Dead Dog Motel.'),
        ('_FrXnp2CALTP44CP3KVAhb', '_82cNpDwVJwVd8qGRUgFw8', 1, ['land'], 'Inland route to Simi Valley Infopoint.'),
        ('_FrXnp2CALTP44CP3KVAhb', '_6JEr2rqCjJa9tWzgbDcrb', 1, ['land'], 'Mountain pass connecting Ventura to Hex Valley.'),
        ('_FrXnp2CALTP44CP3KVAhb', '_X4A8gWVr43a7dRr9TbJ4m', 2, ['land'], 'Route 101 south into Los Angeles metropolitan area.'),
        ('_X4A8gWVr43a7dRr9TbJ4m', '_XD2gWgyhTYmDEXWkxMLer', 0, ['land'], 'Financial district street leading to DCC Tower.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_Caw9nRwKf4Gx9VzW21QJj', 2, ['land'], 'Interstate route connecting Solarton to CUMS.'),
        ('_761mFFeCcQyR9JxhLCWcy', '_fekTA9NRygQ49q7cxRz8A', 3, ['land'], 'Highway 99 northeast across the valley to Bakersfield.'),
        ('_fyC1LJ8CAK8rP7k8Dr2a2', '_erHMcydnPVEyk7NY3K9wf', 0, ['land'], 'Industrial alleyway to Team Ukiyo Operational Base.'),

        # SUCC Campus Internal Routes (Hub: Lunar Quad _WrymW8qTETkm7r1QXQGaT)
        ('_WrymW8qTETkm7r1QXQGaT', '_jYJxF7fte2Gz1F2HGXpUR', 0, ['land'], 'Gothic archway path to Basilica Library.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_ptpGD1VeVep7YknRmhFXM', 0, ['land'], 'Brick walkway to Griffin Clocktower.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_Bx2U1xzg1D3wpFRe39L7y', 0, ['land'], 'Athletic concourse to Bulls Stadium.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_ndMkLAHyKgBDyeMpjwhBt', 0, ['land'], 'Promenade to St. Neptune Aquatic Complex.'),
        ('_ndMkLAHyKgBDyeMpjwhBt', '_GnNYqapde8TGQtemCwJHT', 0, ['land'], 'Locker room breezeway to Main Pool.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_WRBThTNK3wJawVdLRhA1e', 0, ['land'], 'Pathway to outdoor Sports Fields.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_EmJg3zdjTT8kwteJJkyUR', 0, ['land'], 'Fitness corridor to Gym and Changing Facilities.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_xfz8yrt2RjqHyTa8MXG3W', 0, ['land'], 'Residential quad path to Wyrm Dormitories.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_wEkzHgpxfetQr16bTWNUP', 0, ['land'], 'Walkway to Apollo Dorms.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_9YKj9HxFkRWnNJUJk84Tr', 0, ['land'], 'Tree-lined path to Artemis Dorms.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_xLd2GzGayGJXUhjAdTPye', 0, ['land'], 'Perimeter sidewalk to Additional Student Housing.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_yXApVAkzqLrFkLkhW7fdU', 0, ['land'], 'Greek Row avenue to Fraternity and Sorority Row.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_DA14L9eU8wdcfFR1acpbn', 0, ['land'], 'Laboratory promenade into Science Quarter.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_Dw9VQxmgEDGTyQdJzwJgG', 0, ['land'], 'Sculpture garden path to Arts Building.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_aLqMW6UHHj1D9M4xxENF7', 0, ['land'], 'Central concourse to Student Association Building.'),
        ('_WrymW8qTETkm7r1QXQGaT', '_G33ABhpFceN7HanHwp8rr', 0, ['land'], 'Wellness lane to Supernatural Support Center.'),
        ('_jYJxF7fte2Gz1F2HGXpUR', '_4FMaQm3xQCUVHeRf3AWYk', 0, ['land'], 'Wrought-iron spiral stairs down to Basement Meeting Room 005.'),

        # Villa Douglas Internal Estate Routes (Hub: Villa Douglas _9H2EmzRm92QxBpkmJUR1z)
        ('_9H2EmzRm92QxBpkmJUR1z', '_cU3JC9R4VJJrcEJ8GtAFt', 0, ['land'], 'Heavy oak entrance into Main Atrium.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_xDrAxmgeq3tfgwxYKJwkq', 0, ['land'], 'Executive corridor to Council Room.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_gKQqD84T3ymHd3XKVBjFF', 0, ['land'], 'Arched formal hall to Throne Room.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_kfXfwkXrzPTRetcBmUt9T', 0, ['land'], 'Private guarded hallway to Alyssa Sanctuary and Omega Nest.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_hcmcH3jKtU82P8Bh11mF1', 0, ['land'], 'West wing basement stair to Jasper Cavern.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_P78yNW43E1fayK9cXzGpd', 0, ['land'], 'Ground floor passage to Noah Gourmet Kitchen.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_Uqpphc8B1L86DVjRAaJxR', 0, ['land'], 'Reinforced security wing to Malachia East Wing and Den.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_rpBxnqzbc2EPg4eUdhrhx', 0, ['land'], 'Private upper gallery to Erik Alpha Sanctuary.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_EYXqbQkgmU98JBfc8agjF', 0, ['land'], 'Marble corridor to Pack Bathhouse.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_mUHCbXLjDAy8YqraaR7jf', 0, ['land'], 'East corridor to Guest Wing.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_4X1A2UgJkcjhYHMXcL4Xh', 0, ['land'], 'French terrace doors to Gardens and Pools.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_gUjcJKTyq3K3LFF3BbVzd', 0, ['land'], 'Concealed spiral steps to The Attic Sanctuary.'),
        ('_9H2EmzRm92QxBpkmJUR1z', '_LVkMH48tkbdC41T7kCFFV', 0, ['land'], 'Subterranean ramp to Garage and Security Perimeter.')
    ]

    added_count = 0
    for frm, to, tm, med, desc in new_routes_defs:
        if (frm, to) not in existing_pairs:
            existing_routes.append({
                'id': str(uuid.uuid4()),
                'from_location_id': frm,
                'to_location_id': to,
                'bidirectional': True,
                'travel_time': tm,
                'required_mediums': med,
                'description': desc
            })
            existing_pairs.add((frm, to))
            existing_pairs.add((to, frm))
            added_count += 1

    print(f"Nuove rotte strutturate aggiunte: {added_count}")
    print(f"Totale rotte risultante: {len(existing_routes)}")

    # Abilita free_travel per garantire comunque la navigabilità totale ovunque
    payload = {
        'travel_routes': existing_routes,
        'free_travel': True
    }

    res = api_put_world(payload, token)
    print(f"  [OK] Aggiornato World travel: {len(res.get('travel_routes', []))} rotte, free_travel={res.get('free_travel')}")
    print("\n--- FASE 1 COMPLETATA CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
