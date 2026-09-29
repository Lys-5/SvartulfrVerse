import json

with open('exports/entities/Svartulfr_Lexicon_NPCs_G3_A_Real.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])

done_names = [
    # Batch 1 (5)
    'adrian locke', 'finn', 'alistair deville', 'cato', 'vasile ionescu',
    # Batch 2 (10)
    'garrett locke', 'roger', 'harlow macgregor', 'bram beaumont',
    'atlas teague', 'arthur grey', 'jake thompson', 'kîwêtin', 'kiwetin', 'vargus', 'sawyer shephard',
    # Batch 3 (10)
    'ashton crowley', 'amerian de vian', 'aeril royen', 'caien vaelion',
    'lestat oreven', 'xaiden nershatar', 'zaire ziisis', 'wren lark', 'angui', 'madge',
    # Batch 4 (10)
    'bartholomew', 'marek', 'warg', 'vero walker', 'venera dolce',
    'vale roberts', 'talia grimwood', 'siebren dijkstra', 'rue', 'romeo "gray" dean', 'gray dean',
    # Batch 5 (10)
    'rifle maddox', 'rhett moore', 'rafael callaway', 'persephone', 'park jae-sung',
    'nickolas wolffe', 'nic lucero', 'neon purr', 'milo grayson', 'miles airhardt',
    # Batch 6 (10)
    'levi graham', 'lennox mckay', 'kai monroe', 'kai mitchell', 'kade leavis',
    'julian bieri', 'jayce collins', 'ignis', 'graham purcell', 'gianni luciano'
]

remaining = []
for e in entries:
    name = e.get('name', '').lower()
    is_done = False
    for d in done_names:
        if d in name:
            is_done = True
            break
    if not is_done:
        remaining.append(e)

print(f"Total entries in G3_A_Real: {len(entries)}")
print(f"Total remaining: {len(remaining)}")
print("\nFinal candidates (all remaining):")
for i, e in enumerate(remaining):
    print(f"{i+1:2d}. {e.get('name'):30s} | ID: {e.get('id'):22s}")
