import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
token = get_auth_token()

# 1. Fetch gallery
req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{WORLD_ID}/gallery', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
gallery = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
gallery_map = {item['title']: item['imageURL'] for item in gallery if item.get('type') == 'avatar'}

# 2. Load characters
d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = {c['id']: c for c in d['world_characters']}

g1_check = [
    ('wulfnic', '_W9PLYt9ERTBJBXqKQL2en', 'Wulfnic Bloodmoon'),
    ('noah', '_r42cVzMjcGTAx7bR1DQVt', 'Noah Douglas Bloodmoon'),
    ('malachia', '_rAcN9GXD1Le4WxY28e49W', 'Malachia Douglas Bloodmoon'),
    ('logan', '_JL37wK9PQMNDChULCDrWj', 'Logan Douglas'),
    ('jasper', '_x3VY2kcbaDbKyCqywGeET', 'Jasper Douglas Bloodmoon'),
    ('erik', '_d44gDc8N18kkbEhAcfUCG', 'Erik Douglas'),
    ('edric', '_YJQ4cjdrT7brm7HWVkf3K', 'Edric Douglas'),
    ('fenris-full', '_wpMTPQ2VVA2pWqJ3cMztJ', 'Fenris'),
    ('alyssa', '_MXcEC8Y6B3BNm3b1ttHj6', 'Alyssa Douglas Bloodmoon')
]

print("=== G1 Characters Avatar Comparison ===")
for g_title, cid, name in g1_check:
    c = chars[cid]
    curr_av = c.get('avatar') or 'NONE'
    g_av = gallery_map.get(g_title)
    is_same = (curr_av == g_av)
    print(f"\n{name} ({g_title}):")
    print(f"  Current: {curr_av}")
    print(f"  Gallery: {g_av}")
    print(f"  Match:   {is_same}")
