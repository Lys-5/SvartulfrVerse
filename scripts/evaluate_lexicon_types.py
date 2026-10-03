import json
from collections import defaultdict

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
lexicon = d.get('world_lexicon_entries', [])

categories = {
    'to_organization_faction': [],
    'to_item': [],
    'to_creature': [],
    'to_ability_move': [],
    'to_memory': [],
    'keep_lore_concept': []
}

for l in lexicon:
    lid = l['id']
    name = l.get('name', '')
    name_l = name.lower()
    curr_type = l.get('type')
    content = l.get('content', '')
    content_l = content.lower()
    keys = [k.lower() for k in l.get('keys', [])]

    # Check 1: Should be organization/faction
    # Look for explicit faction names, houses, packs, clans, guilds, corporations
    org_markers = [
        'pack', 'house ', 'clan', 'guild', 'syndicate', 'cartel', 'brotherhood',
        'corporation', 'inc.', 'department', 'police', 'mc', 'nomads', 'pmc',
        'coalition', 'dynasty', 'federation', 'order of', 'family', 'alliance'
    ]
    is_org = False
    if curr_type != 'organization/faction':
        if any(m in name_l for m in ['dcc', 'dcc ', 'vanguard security', 'house douglas', 'house bloodmoon', 'seven hills pack', 'blackwood police', 'ironhorn nomads', 'dmha', 'k-sec', 'succ bears', 'succ bulls', 'clams', 'adventurers guild', 'monster fuckers']):
            is_org = True
        elif any(name_l.startswith(p) for p in ['house ', 'clan ', 'the ']) and any(m in name_l for m in ['pack', 'clan', 'house', 'family', 'cartel', 'syndicate']):
            is_org = True

    # Check 2: Should be creature
    is_creature = False
    if curr_type != 'creature':
        if any(c in name_l for c in ['beast', 'asag', 'dungeon boss', 'chimera', 'golem', 'aberration', 'fiend', 'satyr']) and 'satyr pheromones' not in name_l:
            if 'species' not in name_l and 'reproduction' not in name_l and 'anatomy' not in name_l:
                is_creature = True

    # Check 3: Should be item
    is_item = False
    if curr_type != 'item':
        if any(w in name_l for w in ['katana', 'dagger', 'sword', 'armor', 'tome', 'amulet', 'ring of', 'potion', 'field bag', 'pass di gilda', 'porsche', 'rolls-royce', 'harley', 'beetle']):
            if 'theory' not in name_l and 'lore' not in name_l:
                is_item = True

    # Check 4: Should be ability / move
    is_ability = False
    if curr_type not in ('ability', 'move'):
        if any(a in name_l for a in ['spell:', 'rite of', 'incantation', 'technique:', 'vow:']) or name_l in ['absolute pacifist vow', 'the absolute pacifist vow & boundless vital conduit']:
            is_ability = True

    # Check 5: Should be memory
    is_memory = False
    if curr_type != 'memory':
        if 'intimacy' in name_l or 'intimacy profile' in content_l or 'chat log' in name_l:
            is_memory = True

    if is_org:
        categories['to_organization_faction'].append((name, lid, curr_type))
    elif is_item:
        categories['to_item'].append((name, lid, curr_type))
    elif is_creature:
        categories['to_creature'].append((name, lid, curr_type))
    elif is_ability:
        categories['to_ability_move'].append((name, lid, curr_type))
    elif is_memory:
        categories['to_memory'].append((name, lid, curr_type))
    else:
        categories['keep_lore_concept'].append((name, lid, curr_type))

print("=== RECLASSIFICATION EVALUATION ===")
print(f"Candidates for organization/faction: {len(categories['to_organization_faction'])}")
for n, i, c in categories['to_organization_faction']:
    print(f"  * {n} ({i}) [current: {c}]")

print(f"\nCandidates for item: {len(categories['to_item'])}")
for n, i, c in categories['to_item']:
    print(f"  * {n} ({i}) [current: {c}]")

print(f"\nCandidates for creature: {len(categories['to_creature'])}")
for n, i, c in categories['to_creature']:
    print(f"  * {n} ({i}) [current: {c}]")

print(f"\nCandidates for ability: {len(categories['to_ability_move'])}")
for n, i, c in categories['to_ability_move']:
    print(f"  * {n} ({i}) [current: {c}]")

print(f"\nCandidates for memory: {len(categories['to_memory'])}")
for n, i, c in categories['to_memory']:
    print(f"  * {n} ({i}) [current: {c}]")

print(f"\nRemaining in current/lore/concept: {len(categories['keep_lore_concept'])}")
