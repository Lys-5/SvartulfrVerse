import json
import glob

# Load all NPCs in repository
all_npcs = set()
for p in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for e in d['entries']:
        name = e.get('name', '').lower()
        all_npcs.add(name)
        # also add tokens
        for token in name.replace('(', ' ').replace(')', ' ').replace('"', ' ').split():
            if len(token) > 3:
                all_npcs.add(token)

print(f"Total NPC names/tokens indexed: {len(all_npcs)}")

# Check Modern Fantasy characters
mf_names = [
    'Abel Vilas', 'Adrian Locke', 'Alistair', 'Angui', 'Arthur Gray', 'Atlas Teague',
    'Cato', 'Cyrus Camden', 'Damien Bishop', 'Emil', 'Everett Rottmore', 'Emlyn Danes',
    'Garrett Locke', 'Gianni Luciano', 'Graham Purcell', 'Ilya Volkov', 'Julian Bieri',
    'Kade Leavis', 'Kai Monroe', 'Levi Graham', 'Miles Airhardt', 'Milo Grayson',
    'Nic Lucero', 'Park Jae-sung', 'Rafael Callaway', 'Rhett and Jayce', 'Romeo Dean',
    'Ruaraidh Ballantine', 'Sullivan', 'Vale Roberts', 'Vasile Ionescu'
]

print("\n=== MODERN FANTASY ROSTER AUDIT ===")
for m in mf_names:
    first = m.split()[0].lower()
    in_repo = any(first in n for n in all_npcs)
    status = "PRESENT" if in_repo else "MISSING"
    print(f"[{status:7}] {m}")

# Check SUCC characters
succ_names = [
    'Andrew Campbell', 'Bailey Rogers', 'Casey Williams', 'Chase Anderson',
    'Fade Greymoor', 'Finnegan Novak', 'Iordan Vess', 'Janice Thompson',
    'Jared Thompson', 'Mackenzie Sanchez-Rogers', 'Nikolaj Jökull', 'Roland Vickers',
    'Santiago Herrera', 'Tate', 'Tomas Matthews', 'Vincent Campbell',
    'Richard Loewe', 'Ariadne Cirillo', 'Dullahan', 'Barkley Rover',
    'Hank Thompson', 'Stanley Davies Sr.', 'Eris Davies', 'Jasmin Thompson',
    'Oskar', 'Stan Davies Jr.'
]

print("\n=== SUCC CHARACTERS ROSTER AUDIT ===")
for s in succ_names:
    first = s.split()[0].lower()
    in_repo = any(first in n for n in all_npcs)
    status = "PRESENT" if in_repo else "MISSING"
    print(f"[{status:7}] {s}")
