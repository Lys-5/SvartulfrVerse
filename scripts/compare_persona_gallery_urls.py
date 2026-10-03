import json

p = json.load(open(r'C:\Users\mande\.gemini\antigravity\brain\0d89b0ab-f901-4d1c-afad-d3e640b70dd7\scratch\alyssa_persona_raw.json', encoding='utf-8'))
gallery = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8')) # wait, let's load live gallery from script or api

import sys
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
import urllib.request

token = get_auth_token()
req = urllib.request.Request('https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7/gallery', headers={'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0'})
gal = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
gal_map = {item['title']: item['imageURL'] for item in gal}

print(f"{'Outfit':25s} | {'Persona image_url':35s} | {'Gallery imageURL':35s} | Match")
print("-" * 110)
for o in p['outfits']:
    oname = o['name']
    p_img = o.get('image_url') or ''
    g_key = f"alyssa_{oname.lower()}"
    if oname.lower() == 'naked':
        g_key = 'alyssa_nude'
    g_img = gal_map.get(g_key, '')
    match = (p_img == g_img)
    print(f"{oname:25s} | {p_img[-30:]:35s} | {g_img[-30:]:35s} | {match}")
