import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request
import json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
wid = '_YpX47fNraQFw2dD7TdycJ'

# 1. World features & stat_config
req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{wid}', headers=headers)
with urllib.request.urlopen(req) as resp:
    wdata = json.loads(resp.read().decode('utf-8'))
    print('=== WORLD ===')
    print('World features:', wdata.get('world_features'))
    print('Stat config:', json.dumps(wdata.get('stat_config'), indent=2))

# 2. Check linked characters
req2 = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/linked-characters/{wid}', headers=headers)
with urllib.request.urlopen(req2) as resp:
    lchars = json.loads(resp.read().decode('utf-8'))
    print(f'\n=== LINKED CHARACTERS ({len(lchars)}) ===')
    for c in lchars:
        has_rpg = bool(c.get('rpg_stats'))
        enabled = c.get('has_rpg_stats') or (c.get('rpg_stats') or {}).get('enabled')
        print(f"  - {c.get('name')}: has_rpg={has_rpg}, enabled={enabled}")
        if has_rpg:
            print('    rpg_stats:', json.dumps(c.get('rpg_stats'), indent=4)[:300])

# 3. Check /characters/mine directly
req_mine = urllib.request.Request('https://app.wyvern.chat/api/characters/mine', headers=headers)
with urllib.request.urlopen(req_mine) as resp:
    mine_data = json.loads(resp.read().decode('utf-8'))
    print(f"\n=== /characters/mine ===")
    for c in mine_data.get('characters', []):
        print(f"  - {c.get('name')}: rpg_stats={bool(c.get('rpg_stats'))}, has_rpg_stats={c.get('has_rpg_stats')}")

# 4. Check Persona Alyssa
persona_id = "persona_1786335754946"
req3 = urllib.request.Request(f'https://app.wyvern.chat/api/user-personas/{persona_id}', headers=headers)
with urllib.request.urlopen(req3) as resp:
    pdata = json.loads(resp.read().decode('utf-8'))
    print(f'\n=== PERSONA ALYSSA ({persona_id}) ===')
    print('Keys:', list(pdata.keys()))
    print('has_rpg_stats:', pdata.get('has_rpg_stats'))
    print('rpg_stats:', json.dumps(pdata.get('rpg_stats'), indent=2))
