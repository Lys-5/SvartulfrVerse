import json

for fname in ['FINAL/Svartulfr_Lorebook_III.json', 'FINAL/Svartulfr_Lorebook_II.json', 'FINAL/Svartulfr_Location.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"{fname}: entries={len(d.get('entries', []))}, lexicon={len(d.get('lexicon', []))}, id={d.get('id')}")
