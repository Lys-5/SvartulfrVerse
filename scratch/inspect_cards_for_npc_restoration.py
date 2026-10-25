import json

card_files = {
    'Scarlett': 'FINAL/Scarlett_Rose_card.json',
    'Sierra': 'FINAL/Sierra_Cruz_card.json',
    'Russ': 'FINAL/Russ_card.json',
    'Stan': 'FINAL/Stan_Davies_Jr_card.json',
    'Jared': 'FINAL/Jared_Thompson_card.json',
    'Alyssa': 'FINAL/Alyssa_Douglas_Bloodmoon_card.json'
}

for name, path in card_files.items():
    data = json.load(open(path, encoding='utf-8'))
    desc = data.get('description', '')
    first_mes = data.get('first_mes', '')
    avatar = data.get('avatar', '')
    personality = data.get('personality', '')
    print(f"=== {name} ({path}) ===")
    print(f"  desc_len: {len(desc)}")
    print(f"  avatar: {avatar}")
    print(f"  first_mes_len: {len(first_mes)}")
    print(f"  desc preview: {desc[:120].strip()}...")
