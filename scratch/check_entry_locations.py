import json

primary = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8')).get('lexicon', [])
secondary = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8')).get('lexicon', [])

names = ['Alyssa Hvit Douglas Bloodmoon', 'Jared Thompson', "Russell 'Russ' Sinclair", 'Scarlett Rose', 'Sierra Cruz', 'Stanley Davies Jr.']

print("--- Location of entries ---")
for n in names:
    in_p = any(e.get('name') == n for e in primary)
    in_s = any(e.get('name') == n for e in secondary)
    print(f"{n}: Primary={in_p}, Secondary={in_s}")
