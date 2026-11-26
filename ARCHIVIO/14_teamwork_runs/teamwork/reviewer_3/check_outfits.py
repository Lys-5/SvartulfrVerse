import json

cards = [
    ('Edric', 'FINAL/Edric_Douglas_card.json'),
    ('Erik', 'FINAL/Erik_Douglas_card.json'),
    ('Jasper', 'FINAL/Jasper_Douglas_Bloodmoon_card.json'),
    ('Logan', 'FINAL/Logan_Douglas_card.json'),
    ('Mackenzie', 'FINAL/Mackenzie_Sanchez_Rogers_card.json'),
    ('Malachia', 'FINAL/Malachia_Douglas_Bloodmoon_card.json'),
    ('Noah', 'FINAL/Noah_Douglas_Bloodmoon_card.json'),
    ('Wulfnic', 'FINAL/Wulfnic_Bloodmoon_card.json'),
]

for name, path in cards:
    d = json.load(open(path, encoding='utf-8'))
    outfits = d.get('outfits', [])
    print(f"{name:15} | outfits count: {len(outfits) if isinstance(outfits, list) else outfits}")
