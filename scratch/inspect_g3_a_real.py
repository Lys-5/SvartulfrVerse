import json

with open('exports/entities/Svartulfr_Lexicon_NPCs_G3_A_Real.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])
print(f"Total entries in G3_A_Real: {len(entries)}")

done = [
    'adrian locke', 'finn', 'alistair deville', 'cato', 'vasile ionescu',
    'garrett locke', 'roger', 'harlow macgregor', 'bram beaumont',
    'atlas teague', 'arthur grey', 'jake thompson', 'kîwêtin', 'kiwetin', 'vargus', 'sawyer shephard'
]

remaining_entries = []
for e in entries:
    name = e.get('name', '')
    is_done = False
    for d in done:
        if d in name.lower():
            is_done = True
            break
    if not is_done:
        remaining_entries.append(e)

print(f"Remaining in G3_A_Real: {len(remaining_entries)}")
print("\nNext 15 in G3_A_Real:")
for i, e in enumerate(remaining_entries[:15]):
    print(f"{i+1:2d}. {e.get('name'):30s} | ID: {e.get('id'):22s} | Keys: {e.get('keys')}")
