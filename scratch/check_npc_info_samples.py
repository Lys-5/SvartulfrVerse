import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    pdata = json.load(f)

print("=== NPC INFO SAMPLES (PRIMARY) ===")
count = 0
for item in pdata['lexicon']:
    if item.get('npc_info'):
        info = item['npc_info']
        print(f"Name: {item.get('name')}")
        print(f"  Regex: {item.get('avatar_activation_regex')}")
        print(f"  first_name: {info.get('first_name')}")
        print(f"  last_name: {info.get('last_name')}")
        print(f"  nicknames: {info.get('nicknames')}")
        print(f"  titles: {info.get('titles')}")
        count += 1
        if count >= 8:
            break
