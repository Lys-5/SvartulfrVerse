import json
import os
import re

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary_data = json.load(f)

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    secondary_data = json.load(f)

print("=== DETAILED NPC AVATAR & REGEX AUDIT ===")

all_npcs = []
for idx, e in enumerate(primary_data['entries']):
    all_npcs.append(('Primary', idx, e))
for idx, e in enumerate(secondary_data['entries']):
    all_npcs.append(('Secondary', idx, e))

print(f"Total NPCs across Primary and Secondary: {len(all_npcs)}")

# 1. Avatar values analysis
avatar_values = {}
missing_by_file = {'Primary': [], 'Secondary': []}
valid_by_file = {'Primary': [], 'Secondary': []}

for file_src, idx, e in all_npcs:
    eid = e.get('entry_id')
    name = e.get('name')
    avatar = e.get('avatar')
    
    val_type = type(avatar).__name__
    avatar_values[val_type] = avatar_values.get(val_type, 0) + 1
    
    is_valid = bool(avatar and isinstance(avatar, str) and avatar.strip() and avatar.strip().startswith(('http://', 'https://')))
    if is_valid:
        valid_by_file[file_src].append((eid, name, avatar))
    else:
        missing_by_file[file_src].append((eid, name, avatar))

print("\n--- Avatar field types ---")
for t, cnt in avatar_values.items():
    print(f"  {t}: {cnt}")

print(f"\nMissing Avatars in Primary: {len(missing_by_file['Primary'])}")
print(f"Missing Avatars in Secondary: {len(missing_by_file['Secondary'])}")
print(f"Total Missing Avatars: {len(missing_by_file['Primary']) + len(missing_by_file['Secondary'])}")

# Check what the missing values actually are (e.g. None, "", etc.)
missing_types = {}
for src in ['Primary', 'Secondary']:
    for eid, name, av in missing_by_file[src]:
        rep = repr(av)
        missing_types[rep] = missing_types.get(rep, 0) + 1
print("\nRepresentation of missing avatar values:", missing_types)

# 2. Check avatar domains for valid avatars
domains = {}
for src in ['Primary', 'Secondary']:
    for eid, name, av in valid_by_file[src]:
        # extract domain
        m = re.match(r'https?://([^/]+)', av)
        dom = m.group(1) if m else 'unknown'
        domains[dom] = domains.get(dom, 0) + 1

print("\nDomains of valid avatars (114 total):")
for dom, cnt in sorted(domains.items(), key=lambda x: -x[1]):
    print(f"  {dom}: {cnt}")

# 3. Check custom_avatar_regex
non_true_custom_regex = [(src, eid, name, e.get('custom_avatar_regex')) 
                         for src, idx, e in all_npcs if e.get('custom_avatar_regex') is not True]
print(f"\nNPCs with custom_avatar_regex != True: {len(non_true_custom_regex)}")

# 4. Check lines_parsed
non_one_lines_parsed = [(src, eid, name, e.get('lines_parsed')) 
                        for src, idx, e in all_npcs if e.get('lines_parsed') != 1]
print(f"NPCs with lines_parsed != 1: {len(non_one_lines_parsed)}")

# 5. Check avatar_activation_regex patterns
# Pattern should be: (?:^|\n)\s*(?:...)\s*:
regex_pattern = re.compile(r'^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$')
non_conforming_regex = []
missing_regex = []

for src, idx, e in all_npcs:
    eid = e.get('entry_id')
    name = e.get('name')
    reg = e.get('avatar_activation_regex')
    if not reg:
        missing_regex.append((src, eid, name))
    elif not regex_pattern.match(reg):
        non_conforming_regex.append((src, eid, name, reg))

print(f"\nNPCs with missing avatar_activation_regex: {len(missing_regex)}")
print(f"NPCs with non-conforming avatar_activation_regex: {len(non_conforming_regex)}")
if non_conforming_regex:
    print("Samples of non-conforming regex:")
    for item in non_conforming_regex[:10]:
        print(f"  [{item[0]}] {item[2]}: {item[3]}")

# 6. Check npc_info structure
npc_info_issues = []
for src, idx, e in all_npcs:
    eid = e.get('entry_id')
    name = e.get('name')
    info = e.get('npc_info')
    if not isinstance(info, dict):
        npc_info_issues.append((src, eid, name, "Not a dict"))
    else:
        req_keys = ['first_name', 'last_name', 'nicknames', 'titles']
        missing_keys = [k for k in req_keys if k not in info]
        if missing_keys:
            npc_info_issues.append((src, eid, name, f"Missing keys: {missing_keys}"))

print(f"\nNPCs with npc_info issues: {len(npc_info_issues)}")
