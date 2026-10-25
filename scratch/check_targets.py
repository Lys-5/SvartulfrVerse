import json

targets = ['Barrow', 'Marek', 'Radek', 'Goran', 'Kian', 'Rory', 'Sully', 'Jean-Luc', 'Alicia', 'Arthur Sinclair', 'Ilya', 'Vasile']
for path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    d = json.load(open(path, 'r', encoding='utf-8'))
    for e in d.get('entries', []):
        name = e.get('name', '')
        for t in targets:
            if t.lower() in name.lower():
                print(f"{path} | {e.get('entry_id')} | {name} | keys: {e.get('keys')} | avatar: {e.get('avatar')}")
