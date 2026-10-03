import json
import sys
import requests

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

lexicon_entries = [
    {
        "name": "Dungeon Gates (Reality Tears)",
        "keys": ["Dungeon Gate", "Dungeon Gates", "Varchi", "Varco", "Reality Tear", "Squarcio", "Dungeon Tier", "Squarci nella realtà"],
        "content": "A Solarton e Blackwood, i cacciatori e le Gilde chiamano questi fenomeni 'Dungeon Gates' o 'Varchi', classificandoli per Tier di pericolosità (da F a S). Al loro interno, le leggi della fisica collassano e proliferano mostri e anomalie. In realtà, da una prospettiva cosmica (DDM/Voidspace), questi varchi sono 'Reality Tears', ovvero pericolosi squarci nel tessuto multiversale. Mentre i Contractor del Dead Dog Motel intervengono per sigillare queste fratture e prevenire il collasso della realtà, i cacciatori locali terrestri le vedono come opportunità per razziare loot e risorse magiche.",
        "is_global": True,
        "category": "Lore",
        "type": "lore/concept"
    }
]

def main():
    token = get_auth_token()
    url = f"{API_BASE}/worlds/{WORLD_ID}/lexicon"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    for entry in lexicon_entries:
        resp = requests.post(url, headers=headers, json=entry)
        if resp.status_code in [200, 201]:
            print(f"Created Lexicon: {entry['name']}")
        else:
            print(f"Failed {entry['name']}: {resp.status_code} {resp.text}")

if __name__ == '__main__':
    main()
