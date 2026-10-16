import json
import os
import re

lorebook_files = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Lorebook_III.json',
    'FINAL/Svartulfr_Location.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'FINAL/Svartulfr_NPC_Secondary.json'
]

print("=== DEEP DIVE: PILLAR 3 - AGE PATTERNS IN NPC ENTRIES ===")

age_pattern = re.compile(r'\bAGE:\s*([^;\]\n]+)', re.IGNORECASE)
born_pattern = re.compile(r'\b(?:Born|Birth|Birthday):\s*([^;\]\n]+)', re.IGNORECASE)

entries_with_age_field = 0
entries_without_age_field = 0
sample_ages = []

for lb in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(lb, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for e in data['entries']:
        content = e.get('content') or e.get('text') or ''
        m_age = age_pattern.search(content)
        if m_age:
            entries_with_age_field += 1
            if len(sample_ages) < 10:
                sample_ages.append((e.get('id'), e.get('title') or e.get('name'), m_age.group(0)))
        else:
            entries_without_age_field += 1

print(f"NPC entries with 'AGE:' pattern: {entries_with_age_field}")
print(f"NPC entries without 'AGE:' pattern: {entries_without_age_field}")
print("Sample AGE patterns found:")
for s in sample_ages:
    print(f"  [{s[0]}] {s[1]}: {s[2]}")

print("\n=== DEEP DIVE: PILLAR 4 - AVATAR DETAILS ===")

primary_missing = []
secondary_missing = []
primary_has = []
secondary_has = []

regex_samples = []

for lb in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    is_primary = 'Primary' in lb
    with open(lb, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for idx, e in enumerate(data['entries']):
        eid = e.get('id')
        name = e.get('title') or e.get('name')
        avatar = e.get('avatar')
        regex = e.get('avatar_activation_regex')
        if len(regex_samples) < 5:
            regex_samples.append((name, regex))
            
        is_valid = bool(avatar and isinstance(avatar, str) and avatar.strip() and avatar.strip().startswith(('http://', 'https://')))
        record = {
            'id': eid,
            'name': name,
            'avatar': avatar,
            'index': idx
        }
        if is_primary:
            if is_valid:
                primary_has.append(record)
            else:
                primary_missing.append(record)
        else:
            if is_valid:
                secondary_has.append(record)
            else:
                secondary_missing.append(record)

print(f"Primary NPCs total: {len(primary_has) + len(primary_missing)}")
print(f"  - Valid Avatar: {len(primary_has)}")
print(f"  - Missing Avatar: {len(primary_missing)}")

print(f"Secondary NPCs total: {len(secondary_has) + len(secondary_missing)}")
print(f"  - Valid Avatar: {len(secondary_has)}")
print(f"  - Missing Avatar: {len(secondary_missing)}")

print("\nSample Regex Patterns:")
for r in regex_samples:
    print(f"  {r[0]}: {r[1]}")

print("\nSample Valid Avatars in Primary:")
for h in primary_has[:5]:
    print(f"  {h['name']}: {h['avatar']}")

if secondary_has:
    print("\nSample Valid Avatars in Secondary:")
    for h in secondary_has[:5]:
        print(f"  {h['name']}: {h['avatar']}")
else:
    print("\nSecondary NPCs: None have avatars!")

