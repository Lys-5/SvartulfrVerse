import json

data = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
entries = data.get('lexicon', data.get('entries', []))

target_ids = [
    '4NzXF4_0hYxmN7Idltzpw',  # Scarlett Rose
    'ijy8vrlphNv19-p-gbYuY',  # Sierra Cruz
    'YCxAqNoShpefVvk0_Pc7i',  # Russell 'Russ' Sinclair
    'ekdQjq63xP7HtNuaPQJQE',  # Stanley Davies Jr.
    'RM6rcwv8MlY1XWaCTQp0M',  # Jared Thompson
    'alyssa_world_dossier_2b54a223', # Alyssa
    'Vcj4h2TL4Usola2A4OOl6'   # Jasper
]

for idx, e in enumerate(entries):
    eid = e.get('entry_id')
    if eid in target_ids:
        print(f"Index: {idx}, Entry ID: {eid}, Name: {e.get('name')}")
