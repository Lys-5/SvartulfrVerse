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
    m = re.match(r'^\s*(\[[^\]]*\])', desc, flags=re.DOTALL)
    bracket = m.group(1) if m else desc.split('\n')[0]
    # find AGE:
    age_m = re.search(r'AGE:[^;\]]+[;\]]', bracket)
    print(f"{fname}:")
    print(f"  Current AGE match: {age_m.group(0) if age_m else 'NONE'}")
    print(f"  Bracket preview: {bracket[:140]}...")
