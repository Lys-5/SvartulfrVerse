import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

final_cards = [
    'Edric_Douglas_card.json',
    'Erik_Douglas_card.json',
    'Jasper_Douglas_Bloodmoon_card.json',
    'Logan_Douglas_card.json',
    'Mackenzie_Sanchez_Rogers_card.json',
    'Malachia_Douglas_Bloodmoon_card.json',
    'Noah_Douglas_Bloodmoon_card.json',
    'Wulfnic_Bloodmoon_card.json'
]

for fname in final_cards:
    p = ROOT / 'FINAL' / fname
    d = json.loads(p.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    print(f"\n{'='*20} {fname} {'='*20}")
    lines = desc.split('\n')
    for i, line in enumerate(lines):
        m = re.match(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', line)
        if m:
            print(f"  Line {i:03d}: {line[:70]}")
