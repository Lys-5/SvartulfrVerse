import json
from collections import defaultdict

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
lexicon = d.get('world_lexicon_entries', [])

print(f"Total entries: {len(lexicon)}")

# Categorization analysis
reclassify_suggestions = []

for item in lexicon:
    iid = item.get('id')
    name = item.get('name', '')
    curr_type = item.get('type')
    content = item.get('content', '')
    keys = item.get('keys', [])
    attached = item.get('attached_world_character_id')
    
    # Check 1: Intimacy profile or personal digital interaction -> memory
    is_intimacy = 'intimacy' in name.lower() or 'intimacy profile' in content.lower()
    is_digital = 'digital interaction' in name.lower() or 'chat log' in name.lower()
    
    # Check 2: Organizations / Factions / Clans / Guilds
    org_terms = ['faction', 'syndicate', 'guild', 'brotherhood', 'cartel', 'corporation', 'inc.', 'department', 'police department', 'pd', 'security firm', 'dynasty', 'house ', 'pack ', 'clan ']
    is_org = False
    name_l = name.lower()
    # specifically check if this entry is about a specific faction/group rather than abstract theory
    if any(term in name_l for term in ['vanguard security', 'blackwood police', 'dcc ', 'ironhorn nomads', 'k-sec', 'succ ', 'guild of', 'adventurers guild', 'house douglas', 'house bloodmoon', 'seven hills pack', 'blackwood pack', 'fenris pack', 'clams']):
        is_org = True

    # Check 3: Items / Relics / Weapons / Devices
    item_terms = ['katana', 'dagger', 'sword', 'blade', 'armor', 'ring', 'amulet', 'key', 'bag', 'satchel', 'device', 'car', 'vehicle', 'potion', 'tome', 'scroll', 'relic']
    is_item = any(t in name_l for t in item_terms) and 'theory' not in name_l and 'lore' not in name_l

    # Check 4: Creature / Monsters / Beasts (non-playable enemy/beast)
    is_creature = any(t in name_l for t in ['beast', 'monster', 'aberration', 'fiend', 'golem', 'hound', 'swarm']) or curr_type == 'creature'

    # Check 5: Abilities / Spells / Moves / Techniques
    ability_terms = ['spell', 'technique', 'vow', 'form: ', 'shift: ', 'ability', 'stance', 'rite of']

    # Record current state
    if curr_type == 'npc':
        reclassify_suggestions.append((iid, name, curr_type, 'creature' if 'spirit' in content.lower() else 'lore/concept', 'Type npc is non-standard or candidate for lore/concept'))
    elif is_intimacy and curr_type != 'memory':
        reclassify_suggestions.append((iid, name, curr_type, 'memory', 'Intimacy Profile should be memory'))
    elif is_org and curr_type != 'organization/faction':
        reclassify_suggestions.append((iid, name, curr_type, 'organization/faction', 'Named faction/organization'))

print(f"Total potential reclassifications: {len(reclassify_suggestions)}")
for iid, name, old_t, new_t, reason in reclassify_suggestions:
    print(f"  * [{iid}] \"{name}\": {old_t} -> {new_t} ({reason})")
