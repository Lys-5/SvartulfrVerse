import os, json

target_names = ['GREED - Roxie', 'GLUTTONY - Kevin', 'ENVY - Siobhan', 'Andrew Campbell', 'Nicole O\'Connor']

for fname in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    path = os.path.join('FINAL', fname)
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for idx, e in enumerate(d['lexicon']):
        name = e.get('name', '')
        if any(t in name for t in target_names):
            print(f"File: {fname} [#{idx}] Name: {name}")
            print(f"  avatar_activation_regex: {e.get('avatar_activation_regex')}")
            print(f"  npc_info: {e.get('npc_info')}")
            print(f"  keys: {e.get('keys')}")
