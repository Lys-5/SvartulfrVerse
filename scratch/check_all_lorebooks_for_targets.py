import json

target_names = ['Edric', 'Erik', 'Jasper', 'Logan', 'Mackenzie', 'Malachia', 'Noah', 'Wulfnic']

lorebooks = [
    ('FINAL/Svartulfr_Lorebook_I.json', 'Lorebook I'),
    ('FINAL/Svartulfr_Lorebook_II.json', 'Lorebook II'),
    ('FINAL/Svartulfr_Lorebook_III.json', 'Lorebook III'),
    ('FINAL/Svartulfr_Location.json', 'Location'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'NPC Primary'),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'NPC Secondary'),
]

for path, title in lorebooks:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    lex = data.get('lexicon', [])
    for e in lex:
        ename = e.get('name', '')
        etype = e.get('type', '')
        for t in target_names:
            if t.lower() in ename.lower():
                print(f"[{title:13}] Name: {ename:40} | Type: {etype:10} | IgnoredChars: {e.get('ignored_characters', [])} | Keys: {e.get('keys', [])[:2]}")
