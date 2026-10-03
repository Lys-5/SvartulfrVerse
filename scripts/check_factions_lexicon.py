import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
lexicon = d.get('world_lexicon_entries', [])

print("=== POTENTIAL ORGANIZATIONS / FACTIONS TYPED AS LORE/CONCEPT ===")
for item in lexicon:
    t = item.get('type')
    name = item.get('name', '')
    content = item.get('content', '')
    
    # Check if content has [FACTION: or [ORGANIZATION:
    if '[faction:' in content.lower() or '[organization:' in content.lower():
        print(f"  * HAS [FACTION:] tag: \"{name}\" ({item['id']}) - current type: {t}")
    elif t == 'lore/concept':
        name_l = name.lower()
        if any(w in name_l for w in ['confraternita', 'fraternity', 'sorority', 'police', 'squad', 'corps', 'commission', 'department', 'alliance', 'cartel', 'syndicate']):
            print(f"  * Faction name match: \"{name}\" ({item['id']})")
