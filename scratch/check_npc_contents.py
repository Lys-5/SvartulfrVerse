import json

primary = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8')).get('lexicon', [])
secondary = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8')).get('lexicon', [])

all_npcs = primary + secondary

for name in ['Alyssa Hvit Douglas Bloodmoon', 'Jared Thompson', "Russell 'Russ' Sinclair", 'Scarlett Rose', 'Sierra Cruz', 'Stanley Davies Jr.']:
    for e in all_npcs:
        if e.get('name') == name:
            desc = e.get('description', '')
            print(f"=== {name} ===")
            print(f"Type: {e.get('type')}, Keys: {e.get('keys')}, Desc len: {len(desc)}")
            print("Description preview:\n", desc[:300], "\n...")
