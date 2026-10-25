import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    pdata = json.load(f)

check_names = ['Scarlett Rose', 'Sierra Cruz', 'Russell Sinclair', 'Stanley Davies', 'Jared Thompson', 'Alyssa', 'Jasper']

for item in pdata['lexicon']:
    for cn in check_names:
        if cn.lower() in item.get('name', '').lower():
            print(f"=== {item.get('name')} (entry_id: {item.get('entry_id')}) ===")
            for k in ['type', 'selective', 'keys', 'secondary_keys', 'avatar', 'custom_avatar_regex', 'avatar_activation_regex', 'lines_parsed', 'npc_info', 'ignored_characters', 'ignored_personas']:
                print(f"  {k}: {item.get(k)}")
            print(f"  desc length: {len(item.get('content', ''))}")
