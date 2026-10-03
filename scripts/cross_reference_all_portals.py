import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

world_characters = { (c.get('name') or c.get('display_name') or '').lower(): c for c in world_data['world_characters'] }
world_lexicon = { (l.get('name') or '').lower(): l for l in world_data['world_lexicon_entries'] }
world_locations = { (loc.get('name') or '').lower(): loc for loc in world_data['world_locations'] }

print("=== CHECK PORTALE SUCC ===")
with open('exports/portal_succ_extracted.json', 'r', encoding='utf-8') as f:
    succ_data = json.load(f)

succ_names = [
    'Finn Novak', 'Rick Howell', 'Andy', 'Tomas Matthews', 'Fade Greymoor',
    'Viola Carter', 'Roland Vickers', 'Coach Mack', 'Dullahan', 'Coach D',
    'Santiago Herrera', 'Vincent Campbell', 'Griffin Clocktower', 'Wyrm Dormitories',
    'Lunar Quad', 'Basilica Library', 'St. Neptune Stadium', 'Unicorn Hall',
    'CUMS', 'Hex Valley', 'Beta Rho Omega', 'Mu Omega Omega', 'SUCC Bulls', 'SUCC Bears', 'SUCC Kelpies'
]

for name in succ_names:
    k = name.lower()
    in_char = [c for ck, c in world_characters.items() if k in ck]
    in_lex = [l for lk, l in world_lexicon.items() if k in lk]
    in_loc = [loc for lock, loc in world_locations.items() if k in lock]
    status = []
    if in_char: status.append(f"Char: {in_char[0].get('name') or in_char[0].get('display_name')}")
    if in_lex: status.append(f"Lex: {in_lex[0].get('name')}")
    if in_loc: status.append(f"Loc: {in_loc[0].get('name')}")
    print(f"  {name:25} -> {', '.join(status) if status else 'MANCANTE'}")

print("\n=== CHECK PORTALE DDM ===")
with open('exports/portal_ddm_extracted.json', 'r', encoding='utf-8') as f:
    ddm_data = json.load(f)

ddm_names = [
    'Dead Dog Motel', 'Direct Dimensional Management', 'DDM Inc.', 'Richard Whitlock',
    'Hana & Adam Valencia', 'Luka Sutter', 'Johan Jakobsen', 'Fenrir', 'Aria Xenthon',
    'Elias Carter', 'Corrin Snow', 'Catharis Eight', 'Orion Kovač', 'SERAPHIM', 'Reality Tears'
]

for name in ddm_names:
    k = name.lower()
    in_char = [c for ck, c in world_characters.items() if k in ck]
    in_lex = [l for lk, l in world_lexicon.items() if k in lk]
    in_loc = [loc for lock, loc in world_locations.items() if k in lock]
    status = []
    if in_char: status.append(f"Char: {in_char[0].get('name') or in_char[0].get('display_name')}")
    if in_lex: status.append(f"Lex: {in_lex[0].get('name')}")
    if in_loc: status.append(f"Loc: {in_loc[0].get('name')}")
    print(f"  {name:25} -> {', '.join(status) if status else 'MANCANTE'}")

print("\n=== CHECK PORTALE ASTRAL ===")
with open('exports/portal_astral_extracted.json', 'r', encoding='utf-8') as f:
    astral_data = json.load(f)

astral_names = [
    'Astra Industries', 'Leo Sullivan', 'G.A.I.A', 'Nikolai Sutter', 'Ryan Coore',
    'Calhoun Rourke', 'Noah Kōhere', 'CA1N', 'Synthism', 'Rie\'al', 'The Sturgeon'
]

for name in astral_names:
    k = name.lower()
    in_char = [c for ck, c in world_characters.items() if k in ck]
    in_lex = [l for lk, l in world_lexicon.items() if k in lk]
    in_loc = [loc for lock, loc in world_locations.items() if k in lock]
    status = []
    if in_char: status.append(f"Char: {in_char[0].get('name') or in_char[0].get('display_name')}")
    if in_lex: status.append(f"Lex: {in_lex[0].get('name')}")
    if in_loc: status.append(f"Loc: {in_loc[0].get('name')}")
    print(f"  {name:25} -> {', '.join(status) if status else 'MANCANTE'}")
