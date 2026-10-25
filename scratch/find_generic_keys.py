import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

GENERIC = {'the compound', 'solarton pd', 'barista', 'bartender', 'professor', 'hex valley'}

for lb_file in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    for idx, e in enumerate(lb.get('entries', [])):
        ks = e.get('keys', [])
        bad = [k for k in ks if k.strip().lower() in GENERIC]
        if bad:
            out.append(f"{lb_file} #{idx} ({e.get('name')}): {bad} in {ks}")

(ROOT / 'scratch' / 'generic_keys_found.txt').write_text('\n'.join(out), encoding='utf-8')
print('\n'.join(out))
