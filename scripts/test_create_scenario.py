import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

token = get_auth_token()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

test_scen = {
    'world_id': WORLD_ID,
    'name': 'Festa in Piscina agli Ironhorn Nomads con Marek',
    'description': "Marek porta Alyssa alla festa in piscina nel cortile fortificato del Club House degli Ironhorn Nomads.",
    'tags': ['Ironhorn Nomads', 'Marek', 'Pool Party', 'Alyssa'],
    'premade_scenes': [
        {
            'id': 'scene-ironhorn-pool-party',
            'description': 'Club House Ironhorn Nomads, Naperville',
            'scene_text': "=>Narrator:\nIl basso pulsante delle casse professionali fa tremare l'asfalto del cortile recintato del Club House degli Ironhorn Nomads.\n\n=>Marek:\n\"Nessuno si avvicina senza il mio permesso.\""
        }
    ]
}

req = urllib.request.Request(f"{API_BASE}/scenarios", data=json.dumps(test_scen).encode('utf-8'), headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print('SUCCESS creating scenario! ID:', res.get('id'), res.get('_id'))
except urllib.error.HTTPError as e:
    print('HTTP ERROR:', e.code, e.read().decode('utf-8'))
