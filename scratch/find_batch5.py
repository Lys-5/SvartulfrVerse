import json

with open('exports/entities/Svartulfr_Lexicon_NPCs_G3_A_Real.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])

done_names = [
    # Batch 1
    'adrian locke', 'finn', 'alistair deville', 'cato', 'vasile ionescu',
    # Batch 2
    'garrett locke', 'roger', 'harlow macgregor', 'bram beaumont',
    'atlas teague', 'arthur grey', 'jake thompson', 'kîwêtin', 'kiwetin', 'vargus', 'sawyer shephard',
    # Batch 3
    'ashton crowley', 'amerian de vian', 'aeril royen', 'caien vaelion',
    'lestat oreven', 'xaiden nershatar', 'zaire ziisis', 'wren lark', 'angui', 'madge',
    # Batch 4
    'bartholomew', 'marek', 'warg', 'vero walker', 'venera dolce',
    'vale roberts', 'talia grimwood', 'siebren dijkstra', 'rue', 'romeo "gray" dean', 'gray dean'
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
print("\nNext 12 candidates:")
for i, e in enumerate(remaining[:12]):
    print(f"{i+1:2d}. {e.get('name'):30s} | ID: {e.get('id'):22s}")
