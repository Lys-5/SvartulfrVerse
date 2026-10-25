import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

for lb_file in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    for idx, e in enumerate(lb.get('entries', [])):
        if idx == 97 and lb_file == 'Svartulfr_NPC_Primary.json':
            continue
        c = e.get('content', '')
        ks = json.dumps(e.get('keys', []))
        if '{{user}}' in c or '{{pronoun' in c or '{{user}}' in ks or '{{user}}' in e.get('name', ''):
            out.append(f"=== {lb_file} #{idx} | name={e.get('name')} | keys={e.get('keys')} ===")
            for line in c.splitlines():
                if '{{user}}' in line or '{{pronoun' in line:
                    out.append(f"  {line}")

(ROOT / 'scratch' / 'full_user_lines_lorebooks.txt').write_text('\n'.join(out), encoding='utf-8')
print(f"Written {len(out)} lines")
