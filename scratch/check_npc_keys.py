import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

for lb_file in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    out.append(f"=== {lb_file} ===")
    for idx, e in enumerate(lb.get('entries', [])):
        ks = e.get('keys', [])
        sks = e.get('secondary_keys', [])
        out.append(f"#{idx:03d} ({e.get('name')}): keys={ks} | sec={sks}")

(ROOT / 'scratch' / 'npc_all_keys.txt').write_text('\n'.join(out), encoding='utf-8')
print("Done npc_all_keys")
