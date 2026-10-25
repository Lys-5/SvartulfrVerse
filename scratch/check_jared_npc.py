import json

sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))
for e in sec['lexicon']:
    if 'jared' in e.get('name', '').lower():
        print(f"Found entry in secondary: {e['name']}")
        print(e.get('content', '')[:500])
