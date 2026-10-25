import json

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
p_lex = prim.get('lexicon', [])

target_names = ["Echo", "Dominic Rogers", "Daniel \"Danny\" Boone", "Scarlett Rose", "Sierra Cruz", "Russell 'Russ' Sinclair"]

for e in p_lex:
    if e.get('name') in target_names:
        print("="*60)
        print(f"Name: {e.get('name')} | ID: {e.get('entry_id')}")
        print(e.get('content')[:1000])
        print("...\n" + e.get('content')[-400:])
