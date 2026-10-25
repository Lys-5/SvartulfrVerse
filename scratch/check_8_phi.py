import json
import pathlib

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
    phi = d.get('post_history_instructions', '')
    print(f"\n{'='*20} {fname} {'='*20}")
    print(phi)
