import json

cards = [
    ('Erik', 'FINAL/Erik_Douglas_card.json'),
    ('Malachia', 'FINAL/Malachia_Douglas_Bloodmoon_card.json'),
    ('Noah', 'FINAL/Noah_Douglas_Bloodmoon_card.json'),
    ('Logan', 'FINAL/Logan_Douglas_card.json'),
    ('Wulfnic', 'FINAL/Wulfnic_Bloodmoon_card.json'),
    ('Mackenzie', 'FINAL/Mackenzie_Sanchez_Rogers_card.json'),
    ('Edric', 'FINAL/Edric_Douglas_card.json')
]

for label, path in cards:
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    desc = d.get('description', '')
    em_dash = desc.count('\u2014')
    asterisks = desc.count('*')
    has_age = '{{age' in desc.lower()
    print(f"{label:10} | id={d.get('id')} | len={len(desc):5} | em_dash={em_dash} | ast={asterisks} | age={has_age} | avatar={d.get('avatar')}")
