import json

cards = [
    'FINAL/Erik_Douglas_card.json',
    'FINAL/Malachia_Douglas_Bloodmoon_card.json',
    'FINAL/Jasper_Douglas_Bloodmoon_card.json',
    'FINAL/Noah_Douglas_Bloodmoon_card.json',
    'FINAL/Logan_Douglas_card.json',
    'FINAL/Wulfnic_Bloodmoon_card.json',
    'FINAL/Mackenzie_Sanchez_Rogers_card.json',
    'FINAL/Edric_Douglas_card.json'
]

for cpath in cards:
    with open(cpath, 'r', encoding='utf-8') as f:
        c = json.load(f)
    name = c.get('name')
    desc = c.get('description', '')
    print(f'{name}: len {len(desc)} chars')
    lines = desc.splitlines()
    sections = [l for l in lines if l.isupper() and ':' in l]
    print('   Sections:', sections[:6])
