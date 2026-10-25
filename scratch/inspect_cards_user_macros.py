import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

files = sorted(FINAL.glob('*_card.json')) + sorted((FINAL / 'personas').glob('*.json'))
for p in files:
    data = json.loads(p.read_text(encoding='utf-8'))
    out.append(f"=== {p.name} ===")
    for k, v in data.items():
        if isinstance(v, str) and ('{{user}}' in v or '{{pronoun' in v or 'Ascended Alpha' in v):
            out.append(f"  FIELD: {k}")
            for line in v.splitlines():
                if '{{user}}' in line or '{{pronoun' in line or 'Ascended Alpha' in line:
                    out.append(f"    {line[:220]}")

(ROOT / 'scratch' / 'cards_user_macros.txt').write_text('\n'.join(out), encoding='utf-8')
print("Done cards_user_macros")
