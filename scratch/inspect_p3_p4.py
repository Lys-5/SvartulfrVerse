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

CANONICAL_CREST = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

print("==================================================")
print("           PILLAR 3 AUDIT RESULTS                 ")
print("==================================================")

p3_matches = []
all_macros = set()

for lb_path in lorebook_files:
    fname = os.path.basename(lb_path)
    with open(lb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = data.get('entries', [])
    lexicon = data.get('lexicon', [])
    
    for list_name, item_list in [('entries', entries), ('lexicon', lexicon)]:
        for idx, item in enumerate(item_list):
            item_str = json.dumps(item, ensure_ascii=False)
            macros = re.findall(r'\{\{[^}]+\}\}', item_str)
            all_macros.update(macros)
            
            age_found = re.findall(r'\{\{\s*age\s*\}\}', item_str, re.IGNORECASE)
            if age_found:
                p3_matches.append({
                    'file': fname,
                    'list': list_name,
                    'index': idx,
                    'id': item.get('id'),
                    'title': item.get('title') or item.get('name'),
                    'type': item.get('type'),
                    'matches': age_found,
                    'keys_with_age': [k for k, v in item.items() if isinstance(v, str) and re.search(r'\{\{\s*age\s*\}\}', v, re.IGNORECASE)]
                })

print(f"Total {{age}} occurrences found across all 6 lorebooks: {len(p3_matches)}")
if p3_matches:
    for m in p3_matches:
        print(f"  - {m['file']} [{m['list']} #{m['index']}]: id={m['id']}, title={m['title']}, keys={m['keys_with_age']}")
else:
    print("  => CONFIRMED: 0 residual {{age}} macros in FINAL/*.json standalone lorebooks!")

print(f"\nAll unique macros detected across all 6 lorebooks: {sorted(list(all_macros))}")

print("\n==================================================")
print("           PILLAR 4 AUDIT RESULTS                 ")
print("==================================================")

total_entries = 0
total_npc_entries = 0
npcs_by_file = {}

missing_avatar_npcs = []
non_matching_regex_npcs = []
missing_custom_regex_npcs = []
missing_lines_parsed_npcs = []
missing_npc_info = []

for lb_path in lorebook_files:
    fname = os.path.basename(lb_path)
    with open(lb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = data.get('entries', [])
    total_entries += len(entries)
    
    file_npcs = []
    for idx, item in enumerate(entries):
        # Check if type is npc
        is_npc_type = (item.get('type') == 'npc')
        has_npc_info = bool(item.get('npc_info'))
        has_avatar = bool(item.get('avatar'))
        
        if is_npc_type or has_npc_info:
            file_npcs.append((idx, item))
            total_npc_entries += 1
            
            item_id = item.get('id')
            item_title = item.get('title') or item.get('name')
            avatar = item.get('avatar')
            custom_avatar_regex = item.get('custom_avatar_regex')
            lines_parsed = item.get('lines_parsed')
            avatar_activation_regex = item.get('avatar_activation_regex')
            npc_info = item.get('npc_info')
            
            # Check avatar validity
            is_valid_avatar = bool(avatar and isinstance(avatar, str) and avatar.strip() and avatar.strip().startswith(('http://', 'https://')))
            if not is_valid_avatar:
                missing_avatar_npcs.append({
                    'file': fname,
                    'index': idx,
                    'id': item_id,
                    'title': item_title,
                    'avatar_current': avatar,
                    'reason': 'None/Empty' if not avatar else 'Invalid URL format'
                })
            
            # Check custom_avatar_regex: true
            if custom_avatar_regex is not True:
                missing_custom_regex_npcs.append({
                    'file': fname,
                    'index': idx,
                    'id': item_id,
                    'title': item_title,
                    'custom_avatar_regex': custom_avatar_regex
                })
                
            # Check lines_parsed: 1
            if lines_parsed != 1:
                missing_lines_parsed_npcs.append({
                    'file': fname,
                    'index': idx,
                    'id': item_id,
                    'title': item_title,
                    'lines_parsed': lines_parsed
                })
                
            # Check avatar_activation_regex multiline format: (?:^|\n)\s*(?:...)\s*:
            # Note: Multiline regex format per GEMINI.md §7:
            # (?:^|\n)\s*(?:Nome Completo|Nome|Nickname)\s*:
            if not avatar_activation_regex:
                non_matching_regex_npcs.append({
                    'file': fname,
                    'index': idx,
                    'id': item_id,
                    'title': item_title,
                    'regex': avatar_activation_regex,
                    'issue': 'missing'
                })
            else:
                # Check if it has (?:^|\n) or starts with multiline pattern
                is_multiline = '(?:^|\\n)' in avatar_activation_regex or '(?:^|\n)' in avatar_activation_regex or avatar_activation_regex.startswith('(?:^|\\n)')
                if not is_multiline:
                    non_matching_regex_npcs.append({
                        'file': fname,
                        'index': idx,
                        'id': item_id,
                        'title': item_title,
                        'regex': avatar_activation_regex,
                        'issue': 'not multiline (lacks (?:^|\\n))'
                    })
                    
            if not npc_info or not isinstance(npc_info, dict):
                missing_npc_info.append({
                    'file': fname,
                    'index': idx,
                    'id': item_id,
                    'title': item_title,
                    'npc_info': npc_info
                })
                
    npcs_by_file[fname] = len(file_npcs)

print(f"Total entries inspected across 6 lorebooks: {total_entries}")
print(f"Total NPC entries identified: {total_npc_entries}")
for fname, cnt in npcs_by_file.items():
    print(f"  - {fname}: {cnt} NPCs")

print(f"\nPillar 4 Findings Breakdown:")
print(f"1. NPCs with missing/empty/invalid avatar: {len(missing_avatar_npcs)}")
print(f"2. NPCs with custom_avatar_regex != True: {len(missing_custom_regex_npcs)}")
print(f"3. NPCs with lines_parsed != 1: {len(missing_lines_parsed_npcs)}")
print(f"4. NPCs with non-compliant / non-multiline regex: {len(non_matching_regex_npcs)}")
print(f"5. NPCs missing npc_info object: {len(missing_npc_info)}")



print("\n=== CHECKING LOREBOOKS DIR FOR {{age}} ===")
for root, dirs, files in os.walk('lorebooks'):
    for f in files:
        if f.endswith('.json'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                txt = fp.read()
            if '{{age}}' in txt:
                print(f"Found in {path}: {txt.count('{{age}}')}")
