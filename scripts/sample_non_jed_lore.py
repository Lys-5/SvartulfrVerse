import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
lexicon = d.get('world_lexicon_entries', [])

non_jed_lore = [l for l in lexicon if l.get('type') == 'lore/concept' and not l.get('content', '').strip().startswith('[NAME:')]

print(f"Total lore/concept (non-JED): {len(non_jed_lore)}")
print("\nSample topics:")
for l in non_jed_lore[:40]:
    print(f"  - {l['name']} ({l['id']})")
