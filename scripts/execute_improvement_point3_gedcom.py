import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'
TREE_ID = '_yQRNHGTeqj6AWxtpaFtFK'

NODES = [
    # Gen 1
    {
        'id': 'node-cornelius',
        'label': 'Lord Cornelius Douglas',
        'description': 'Fondatore di House Douglas (1666), Pureblood Founding Ancestor.',
        'entity_type': 'character',
        'entity_id': '_rJKYcCt61hQa8XRamHEdM',
        'position': {'x': 450, 'y': 50}
    },
    # Gen 2
    {
        'id': 'node-magnus',
        'label': 'Magnus Douglas III',
        'description': 'Patriarca Pureblood, colonial governor posture.',
        'entity_type': 'character',
        'entity_id': '_jeJTbxLcrYWXNWYPDx4ph',
        'position': {'x': 340, 'y': 190}
    },
    {
        'id': 'node-elizabeth',
        'label': 'Lady Elizabeth Duskwood',
        'description': 'Pureblood Omega, Pack Mom di Seven Hills.',
        'entity_type': 'character',
        'entity_id': '_EwPN1te7qtUKYEx4NLgag',
        'position': {'x': 560, 'y': 190}
    },
    # Ancestor Bloodmoon
    {
        'id': 'node-wulfnic',
        'label': 'Wulfnic Bloodmoon',
        'description': 'Alpha of Alphas, Primo Nato millenario.',
        'entity_type': 'character',
        'entity_id': '_W9PLYt9ERTBJBXqKQL2en',
        'position': {'x': 50, 'y': 190}
    },
    # Gen 3
    {
        'id': 'node-nixara',
        'label': 'Nixara Bloodmoon',
        'description': 'White Moon, sposa di Erik e madre dei quattro fratelli.',
        'entity_type': 'character',
        'entity_id': '_fmzBDjDn3Gnq2hXKy7tY6',
        'position': {'x': 180, 'y': 360}
    },
    {
        'id': 'node-erik',
        'label': 'Erik Douglas',
        'description': 'Prime Alpha, CEO della DCC, Patriarca di Seven Hills.',
        'entity_type': 'character',
        'entity_id': '_d44gDc8N18kkbEhAcfUCG',
        'position': {'x': 390, 'y': 360}
    },
    {
        'id': 'node-logan',
        'label': 'Logan Douglas',
        'description': 'Fratello minore di Erik, proprietario di The Verve.',
        'entity_type': 'character',
        'entity_id': '_JL37wK9PQMNDChULCDrWj',
        'position': {'x': 680, 'y': 360}
    },
    # Gen 4
    {
        'id': 'node-malachia',
        'label': 'Malachia Douglas Bloodmoon',
        'description': 'Founding Alpha, primogenito, Tank dell\'avanguardia.',
        'entity_type': 'character',
        'entity_id': '_rAcN9GXD1Le4WxY28e49W',
        'position': {'x': 80, 'y': 540}
    },
    {
        'id': 'node-noah',
        'label': 'Noah Douglas Bloodmoon',
        'description': 'Founding Delta, diplomatico, KSA Golden Boy.',
        'entity_type': 'character',
        'entity_id': '_r42cVzMjcGTAx7bR1DQVt',
        'position': {'x': 230, 'y': 540}
    },
    {
        'id': 'node-jasper',
        'label': 'Jasper Douglas Bloodmoon',
        'description': 'Founding Beta, DJ Frequency, gemello di Alyssa.',
        'entity_type': 'character',
        'entity_id': '_x3VY2kcbaDbKyCqywGeET',
        'position': {'x': 380, 'y': 540}
    },
    {
        'id': 'node-alyssa',
        'label': 'Alyssa Douglas Bloodmoon',
        'description': 'Dominant Omega, White Moon erede, studentessa SUCC.',
        'entity_type': 'character',
        'entity_id': '_MXcEC8Y6B3BNm3b1ttHj6',
        'position': {'x': 530, 'y': 540}
    },
    {
        'id': 'node-edric',
        'label': 'Edric Douglas',
        'description': 'Figlio di Logan, nipote dodicenne pre-presentazione.',
        'entity_type': 'character',
        'entity_id': '_YJQ4cjdrT7brm7HWVkf3K',
        'position': {'x': 680, 'y': 540}
    }
]

CONNECTIONS = [
    # Cornelius -> Magnus
    {'id': 'edge-cor-mag', 'from_node_id': 'node-cornelius', 'to_node_id': 'node-magnus', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    # Magnus + Elizabeth
    {'id': 'edge-mag-eli', 'from_node_id': 'node-magnus', 'to_node_id': 'node-elizabeth', 'label': 'Sposi', 'style': {'color': '#e066ff', 'strokeWidth': 2}},
    # Magnus -> Erik & Logan
    {'id': 'edge-mag-erik', 'from_node_id': 'node-magnus', 'to_node_id': 'node-erik', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-eli-erik', 'from_node_id': 'node-elizabeth', 'to_node_id': 'node-erik', 'label': 'Madre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-mag-logan', 'from_node_id': 'node-magnus', 'to_node_id': 'node-logan', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-eli-logan', 'from_node_id': 'node-elizabeth', 'to_node_id': 'node-logan', 'label': 'Madre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    # Wulfnic -> Nixara (Bloodline)
    {'id': 'edge-wulf-nix', 'from_node_id': 'node-wulfnic', 'to_node_id': 'node-nixara', 'label': 'Antenato Firstborn', 'style': {'color': '#ff4444', 'strokeWidth': 2}},
    # Erik + Nixara
    {'id': 'edge-erik-nix', 'from_node_id': 'node-erik', 'to_node_id': 'node-nixara', 'label': 'Compagni d\'Anima', 'style': {'color': '#ff3366', 'strokeWidth': 2}},
    # Erik & Nixara -> Malachia
    {'id': 'edge-erik-mal', 'from_node_id': 'node-erik', 'to_node_id': 'node-malachia', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-nix-mal', 'from_node_id': 'node-nixara', 'to_node_id': 'node-malachia', 'label': 'Madre', 'style': {'color': '#ff3366', 'strokeWidth': 2}},
    # Erik & Nixara -> Noah
    {'id': 'edge-erik-noah', 'from_node_id': 'node-erik', 'to_node_id': 'node-noah', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-nix-noah', 'from_node_id': 'node-nixara', 'to_node_id': 'node-noah', 'label': 'Madre', 'style': {'color': '#ff3366', 'strokeWidth': 2}},
    # Erik & Nixara -> Jasper
    {'id': 'edge-erik-jas', 'from_node_id': 'node-erik', 'to_node_id': 'node-jasper', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-nix-jas', 'from_node_id': 'node-nixara', 'to_node_id': 'node-jasper', 'label': 'Madre', 'style': {'color': '#ff3366', 'strokeWidth': 2}},
    # Erik & Nixara -> Alyssa
    {'id': 'edge-erik-aly', 'from_node_id': 'node-erik', 'to_node_id': 'node-alyssa', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}},
    {'id': 'edge-nix-aly', 'from_node_id': 'node-nixara', 'to_node_id': 'node-alyssa', 'label': 'Madre', 'style': {'color': '#ff3366', 'strokeWidth': 2}},
    # Jasper <-> Alyssa (Twins)
    {'id': 'edge-jas-aly', 'from_node_id': 'node-jasper', 'to_node_id': 'node-alyssa', 'label': 'Gemelli', 'style': {'color': '#ffaa00', 'strokeWidth': 2}},
    # Logan -> Edric
    {'id': 'edge-logan-edr', 'from_node_id': 'node-logan', 'to_node_id': 'node-edric', 'label': 'Padre', 'style': {'color': '#00d9ff', 'strokeWidth': 2}}
]

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print(f"--- PUNTO 3: POPOLAMENTO ALBERO GENEALOGICO GEDCOM ({TREE_ID}) ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    url = f"{API_BASE}/gedcom-trees/{TREE_ID}?world_id={WORLD_ID}"
    payload = {
        'nodes': NODES,
        'connections': CONNECTIONS,
        'layout_settings': {'layout_type': 'manual', 'zoom': 0.85, 'pan': {'x': 0, 'y': 0}}
    }

    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
        nodes_cnt = len(res.get('nodes', []))
        conn_cnt = len(res.get('connections', []))
        print(f"  [GEDCOM OK] Albero '{res.get('name')}' aggiornato con {nodes_cnt} nodi e {conn_cnt} connessioni dinastiche!")
    except Exception as e:
        print(f"  [GEDCOM ERR] Errore salvataggio albero: {e}")
        sys.exit(1)

    print("\n--- PUNTO 3 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
