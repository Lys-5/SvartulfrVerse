import json
import pathlib

s1_path = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\fa5c149a-3193-41b6-a44f-45396c7b7227\.system_generated\steps\116\output.txt')
s2_path = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\fa5c149a-3193-41b6-a44f-45396c7b7227\.system_generated\steps\117\output.txt')

def parse_step_json(p: pathlib.Path):
    txt = p.read_text(encoding='utf-8')
    lines = txt.splitlines()
    # find line starting with { or [ or "
    for line in lines:
        s = line.strip()
        if s.startswith('{') or s.startswith('[') or s.startswith('"'):
            obj = json.loads(s)
            if isinstance(obj, str):
                obj = json.loads(obj)
            return obj
    raise ValueError(f'No JSON found in {p}')

d1 = parse_step_json(s1_path)
d2 = parse_step_json(s2_path)

md = ['# Catalogo Completo Prompt Argon / Gemini — SvartúlfrVerse\n']
md.append('Estratto integrale dalle due sessioni ufficiali di riferimento:\n- **Sessione 1 (Famiglia Douglas & Outfits):** `https://gemini.google.com/app/699ca946550ec63b`\n- **Sessione 2 (Wulfnic Bloodmoon & Varianti):** `https://gemini.google.com/app/cacb36df583d0db9`\n\n---\n')

for label, d in [('Sessione 1 — Famiglia Douglas (53 Turni)', d1), ('Sessione 2 — Wulfnic Bloodmoon (33 Turni)', d2)]:
    md.append(f'## {label}\n')
    for t in d.get('turns', []):
        md.append(f'### Turno {t.get("turn")}')
        if t.get('user'):
            md.append(f'**User Prompt / Istruzione:**\n```text\n{t.get("user").strip()}\n```')
        if t.get('imgs'):
            for img in t.get('imgs'):
                ia = img.get('alt', '') if isinstance(img, dict) else str(img)
                if ia and ia.strip() and ia.strip() != ", generata con l'AI" and ia.strip() != "Anteprima dell'immagine caricata":
                    md.append(f'**Generated Image Prompt (`img.alt`):**\n```text\n{ia.strip()}\n```')
        md.append('')

out_md = pathlib.Path(r'e:\repository\SvartulfrVerse\database\assets\argon_gemini_prompts_reference.md')
out_md.write_text('\n'.join(md), encoding='utf-8')
print(f'Wrote {out_md} ({out_md.stat().st_size} bytes)')

# 2. Extract live Personas from step 107 and save to scratch/live_wyvern_snapshot_oct16/personas_live.json
p107 = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\fa5c149a-3193-41b6-a44f-45396c7b7227\.system_generated\steps\107\output.txt')
d107 = parse_step_json(p107)
personas_out = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\live_wyvern_snapshot_oct16\personas_live.json')
personas_out.write_text(json.dumps(d107.get('personas', d107), indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Saved personas_live.json ({personas_out.stat().st_size} bytes)')

# 3. Inspect backup_consolidated_snapshot for Zeera, Jared, Mackenzie, Marek, Kaladin, Elizabeth, Magnus
snap_dir = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\backup_consolidated_snapshot')
for f in sorted(snap_dir.glob('*.json')):
    print('Snapshot file:', f.name, f.stat().st_size)

mine_snap = json.loads((snap_dir / 'mine_standalone_characters.json').read_text(encoding='utf-8'))
print('mine_standalone_characters keys/names:')
if isinstance(mine_snap, list):
    for c in mine_snap:
        print(' -', c.get('_id') or c.get('id'), c.get('name'), 'outfits:', len(c.get('outfits', [])))
elif isinstance(mine_snap, dict):
    for k, c in mine_snap.items():
        if isinstance(c, dict):
            print(' -', k, c.get('name'), 'outfits:', len(c.get('outfits', [])))

wc_snap = json.loads((snap_dir / 'world_characters.json').read_text(encoding='utf-8'))
targets = ['zeera', 'jared', 'mackenzie', 'marek', 'kaladin', 'elizabeth', 'magnus']
print('\nSearching world_characters.json for targets:')
wc_list = wc_snap if isinstance(wc_snap, list) else wc_snap.get('characters', wc_snap.get('world_characters', []))
for c in wc_list:
    nm = (c.get('name') or '').lower()
    if any(t in nm for t in targets):
        print(' * WC:', c.get('id'), c.get('name'), 'avatar:', bool(c.get('avatar')), 'outfits:', len(c.get('outfits', [])))
