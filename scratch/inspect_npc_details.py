import json
import pathlib

snap_dir = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\backup_consolidated_snapshot')
wc = json.loads((snap_dir / 'world_characters.json').read_text(encoding='utf-8'))
targets = ['zeera', 'jared', 'mackenzie', 'marek', 'kaladin', 'elizabeth', 'magnus', 'alyssa']

for v in wc:
    nm = f"{v.get('display_name','')} {v.get('first_name','')} {v.get('last_name','')}"
    if any(t in nm.lower() for t in targets):
        print('WC:', v.get('id'), '|', v.get('display_name'), '| avatar:', v.get('avatar'), '| outfits:', len(v.get('outfits', [])), '| gallery:', len(v.get('gallery_images', [])), '| long_summary len:', len(v.get('long_summary', '') or ''))

pa = json.loads((snap_dir / 'persona_alyssa.json').read_text(encoding='utf-8'))
pe = json.loads((snap_dir / 'persona_echo.json').read_text(encoding='utf-8'))
print('persona_alyssa keys:', list(pa.keys()))
print('persona_alyssa outfits:', len(pa.get('outfits', [])), 'appearances:', len(pa.get('appearances', [])))
print('persona_echo keys:', list(pe.keys()))
print('persona_echo outfits:', len(pe.get('outfits', [])), 'appearances:', len(pe.get('appearances', [])))

plive = json.loads(pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\live_wyvern_snapshot_oct16\personas_live.json').read_text(encoding='utf-8'))
for p in plive:
    print('plive:', p.get('_id'), p.get('persona_id'), p.get('name'), 'outfits:', len(p.get('outfits', [])), 'appearances:', len(p.get('appearances', [])))
