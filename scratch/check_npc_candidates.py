import json

primary = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8')).get('lexicon', [])
secondary = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8')).get('lexicon', [])

all_npcs = primary + secondary

candidates = ['Alyssa', 'Jared', 'Russ', 'Scarlett', 'Sierra', 'Stanley', 'Davies', 'Thompson']

for cand in candidates:
    matches = [e for e in all_npcs if cand.lower() in e.get('name', '').lower() or any(cand.lower() in str(k).lower() for k in e.get('keys', []))]
    print(f"\n--- Matches for '{cand}': {len(matches)} ---")
    for m in matches:
        print(f"  ID: {m.get('id')} | Name: {m.get('name')} | Type: {m.get('type')} | Keys: {m.get('keys')}")
