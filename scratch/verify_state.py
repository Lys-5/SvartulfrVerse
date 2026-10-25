import sys, os, json, re, requests
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.getcwd())
from scripts.sync_from_wyvern_web import get_auth_token
H = {'Authorization': f'Bearer {get_auth_token()}'}
B = 'https://app.wyvern.chat/api'

chars = requests.get(f'{B}/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ', headers=H).json()
print('WORLD CHARS:', len(chars))
for c in chars:
    r = c.get('rpg_stats') or {}
    print(f"  {c.get('display_name')[:34]:34} av={bool(c.get('avatar'))} bd={c.get('birthdate')} lv={r.get('level')} stats={r.get('base_stats')} outfits={len(c.get('outfits') or [])}")

sc = requests.get(f'{B}/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H', headers=H).json()
for s in sc.get('premade_scenes', []):
    t = s['scene_text']
    bad = [l[:50] for l in t.splitlines() if re.match(r'^[A-Z][\w\u00C0-\u017F ]+: "', l)]
    print('SCENE', s['id'], 'speakers=', sorted(set(re.findall(r'^=>([^:\n]+):', t, re.M))), 'unprefixed=', len(bad), 'emdash=', t.count('\u2014'))
