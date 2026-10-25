import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

files = sorted(FINAL.glob('*_card.json')) + sorted((FINAL / 'personas').glob('*.json'))
for p in files:
    data = json.loads(p.read_text(encoding='utf-8'))
    for k, v in data.items():
        if isinstance(v, str) and ('[INSTRUCTIONS:' in v or 'Ascended Alpha' in v):
            out.append(f"{p.name} -> {k}:")
            for m in re.finditer(r'(\[INSTRUCTIONS:.*?\]|Ascended Alpha)', v, re.S):
                out.append(f"  MATCH: {m.group(0)[:200]}")

print('\n'.join(out))
