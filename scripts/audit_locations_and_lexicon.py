import json
from collections import defaultdict

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
locs = d.get('world_locations', [])
lexicon = d.get('world_lexicon_entries', [])

print("==================================================")
print(f"1. AUDIT LOCATIONS (Total: {len(locs)})")
print("==================================================")

# 1. Exact Name Duplicates
by_name = defaultdict(list)
for l in locs:
    name = l.get('name', '').strip()
    by_name[name].append(l)

dupes_exact = {k: v for k, v in by_name.items() if len(v) > 1}
print(f"\n[A] Exact Name Duplicates: {len(dupes_exact)}")
for name, items in dupes_exact.items():
    print(f"  * \"{name}\" ({len(items)} entries):")
    for it in items:
        p = (it.get('parent_location') or {}).get('name') or it.get('parent_location_id')
        print(f"      ID: {it['id']} | Parent: {p} | Updated: {it.get('updated_at')}")

# Key collisions
key_map = {}
key_conflicts = []
for l in locs:
    for k in (l.get('keys') or []):
        kl = k.lower().strip()
        if kl in key_map:
            key_conflicts.append((k, key_map[kl], (l.get('name'), l.get('id'))))
        else:
            key_map[kl] = (l.get('name'), l.get('id'))

print(f"\n[A2] Exact Key Collisions across different locations: {len(key_conflicts)}")
for k, l1, l2 in key_conflicts:
    print(f"  * Key \"{k}\": \"{l1[0]}\" ({l1[1]}) <--> \"{l2[0]}\" ({l2[1]})")

# 2. Similar / Substring / Overlapping Names
print("\n[B] Potential Semantic / Naming Duplicates:")
seen_pairs = set()
for i, l1 in enumerate(locs):
    n1 = l1.get('name', '').lower().strip()
    for j, l2 in enumerate(locs):
        if i >= j:
            continue
        n2 = l2.get('name', '').lower().strip()
        # If one name contains another or very close
        if n1 == n2:
            continue
        if (n1 in n2 or n2 in n1) and len(min(n1, n2)) > 6:
            # exclude generic parent-child like "Seven Hills" vs "Seven Hills High"
            pair = tuple(sorted([l1['id'], l2['id']]))
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                print(f"  * \"{l1.get('name')}\" ({l1['id']}) <--> \"{l2.get('name')}\" ({l2['id']})")
                p1 = (l1.get('parent_location') or {}).get('name')
                p2 = (l2.get('parent_location') or {}).get('name')
                print(f"      Parent 1: {p1} | Parent 2: {p2}")

print("\n==================================================")
print(f"2. AUDIT LEXICON TYPES (Total: {len(lexicon)})")
print("==================================================")

type_counts = defaultdict(int)
for item in lexicon:
    t = item.get('type')
    type_counts[str(t)] += 1

print("\nCurrent Lexicon Type Distribution:")
for t, count in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  - {t}: {count}")

# Check invalid types according to GEMINI.md:
# Pure text: lore/concept, organization/faction, memory, null / ''
# Config panel: item, furniture, creature, move, nature, ability
valid_types = {
    'lore/concept', 'organization/faction', 'memory', 'None', '',
    'item', 'furniture', 'creature', 'move', 'nature', 'ability'
}

invalid_types = {k: v for k, v in type_counts.items() if k not in valid_types}
print(f"\nInvalid / Unknown Types: {invalid_types}")

# Audit single-character entries (Intimacy Profiles, specific personal memory/lore)
print("\n[C] Check Single Character entries / Attached Character rule:")
intimacy_wrong_type = []
memory_without_attached = []
attached_not_memory = []

for item in lexicon:
    name = item.get('name', '')
    t = str(item.get('type'))
    attached = item.get('attached_world_character_id')
    keys = item.get('keys', [])
    content = item.get('content', '')

    if 'intimacy' in name.lower() or 'intimacy profile' in content.lower():
        if t != 'memory' or not attached:
            intimacy_wrong_type.append((name, t, attached, item.get('id')))

    if attached and t != 'memory':
        attached_not_memory.append((name, t, attached, item.get('id')))

print(f"  - Intimacy profiles with wrong type or missing attached char: {len(intimacy_wrong_type)}")
for name, t, att, iid in intimacy_wrong_type[:10]:
    print(f"      * {name} ({iid}): type='{t}', attached='{att}'")

print(f"  - Entries with attached_world_character_id but type != 'memory': {len(attached_not_memory)}")
for name, t, att, iid in attached_not_memory[:10]:
    print(f"      * {name} ({iid}): type='{t}', attached='{att}'")

# Check entries named after factions or organizations that are typed as lore/concept
print("\n[D] Factions / Organizations categorized as lore/concept or None:")
org_candidates = []
org_keywords = ['pack', 'house', 'family', 'clan', 'guild', 'syndicate', 'cartel', 'inc.', 'corporation', 'club', 'brotherhood', 'department', 'police']
for item in lexicon:
    name = item.get('name', '')
    t = str(item.get('type'))
    if t in ('lore/concept', 'None', ''):
        name_lower = name.lower()
        if any(kw in name_lower for kw in ['house ', 'pack', 'clan', 'guild', 'brotherhood', 'corporation', 'syndicate', 'vanguard security']):
            # check if it really is an organization
            org_candidates.append((name, t, item.get('id')))

print(f"  - Candidates for organization/faction: {len(org_candidates)}")
for name, t, iid in org_candidates[:15]:
    print(f"      * {name} ({iid}): current='{t}'")

# Check creatures / species
print("\n[E] Species / Creatures categorization check:")
creature_candidates = []
for item in lexicon:
    name = item.get('name', '')
    t = str(item.get('type'))
    if t == 'creature':
        print(f"  - Currently 'creature': {name} ({item.get('id')})")
    elif t == 'mob':
        print(f"  - Found invalid type 'mob': {name} ({item.get('id')})")
