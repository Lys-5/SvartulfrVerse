import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def show_card(fname):
    p = ROOT / 'FINAL' / fname
    d = json.loads(p.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    print(f"\n{'='*20} {fname} {'='*20}")
    # find lines that look like headers
    lines = desc.split('\n')
    for i, line in enumerate(lines):
        m = re.match(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', line)
        if m:
            print(f"Line {i:03d}: {line[:80]}")

if __name__ == '__main__':
    for f in ['Noah_Douglas_Bloodmoon_card.json', 'Malachia_Douglas_Bloodmoon_card.json']:
        show_card(f)
