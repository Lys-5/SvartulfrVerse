import sys, json, requests
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'
token = get_auth_token()
H = {'Authorization': f'Bearer {token}'}

names = ["Rozalia Tănase", "Ruby Valerius", "Vesna", "Mikan", "Ginger", "Orion and Sigrid Valois",
         "Henrey Cote", "Aria Xenthon", "Tori", "River", "Ailsa Hourie", "Silas", "Bramble Mossmere",
         "Evan", "Vespera Thorne", "Eira Elloway", "Darius Azadi", "Varg Darkfire", "Aras Darkfire",
         "Karshin Darkfire", "Boros Darkfire", "Zeera Darkfire"]

chars = requests.get(f'{API_BASE}/worlds/characters/world/{WORLD_ID}', headers=H).json()
by_name = {}
for c in chars:
    by_name.setdefault(c.get('display_name', ''), []).append(c.get('id'))

for n in names:
    ids = by_name.get(n, [])
    if not ids:
        print(f'{n}: NOT FOUND')
        continue
    for cid in ids:
        d = requests.get(f'{API_BASE}/worlds/characters/{cid}', headers=H).json()
        ls = d.get('long_summary') or ''
        lvl = (d.get('rpg_stats') or {}).get('level')
        print(f"{n} [{cid}] long_summary={len(ls)} chars, has_description_field={'description' in d}, "
              f"is_global={d.get('is_global')}, level={lvl}, start={d.get('start_timeline_position')}")

# Lexicon check
lex = requests.get(f'{API_BASE}/worlds/lexicon/world/{WORLD_ID}', headers=H)
print('LEXICON GET status', lex.status_code)
try:
    items = lex.json()
    if isinstance(items, dict):
        items = items.get('data') or items.get('entries') or []
    tgt = [e for e in items if str(e.get('name', e.get('title', ''))).startswith(('Kink:', 'Magic:', 'Species:'))]
    print('Kink/Magic/Species entries found:', len(tgt))
    if tgt:
        print('Sample keys:', list(tgt[0].keys()))
        s = tgt[0]
        print('Sample content len:', len(str(s.get('content') or s.get('description') or s.get('text') or '')))
except Exception as e:
    print('lexicon parse error', e, lex.text[:300])
