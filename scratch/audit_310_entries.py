import json, re

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

def analyze_lorebook(data, lb_name):
    lexicon = data.get('lexicon', [])
    print(f"\n==========================================")
    print(f"ANALYSIS OF {lb_name} (Total entries: {len(lexicon)})")
    print(f"==========================================")
    
    no_bracket_start = []
    types_count = {}
    selective_count = {}
    missing_avatar = []
    placeholder_avatar = []
    custom_avatar = []
    
    has_backstory = 0
    has_family_pack = 0
    has_clan_company = 0
    has_voice_behavior = 0
    has_voice_other = []
    
    exclude_from_recursion_true = 0
    exclude_from_recursion_other = 0
    
    priorities = {}
    
    for idx, e in enumerate(lexicon):
        eid = e.get('entry_id', f'idx_{idx}')
        name = e.get('name', 'UNKNOWN')
        content = e.get('content', '')
        etype = e.get('type')
        types_count[etype] = types_count.get(etype, 0) + 1
        
        sel = e.get('selective')
        selective_count[sel] = selective_count.get(sel, 0) + 1
        
        efr = e.get('exclude_from_recursion')
        if efr is True:
            exclude_from_recursion_true += 1
        else:
            exclude_from_recursion_other += 1
            
        pri = e.get('priority')
        priorities[pri] = priorities.get(pri, 0) + 1
        
        avatar = e.get('avatar')
        if not avatar:
            missing_avatar.append((eid, name))
        elif '99d10d9b-611c-45b7-566a-79c3ed2e9800' in avatar:
            placeholder_avatar.append((eid, name))
        else:
            custom_avatar.append((eid, name, avatar))
            
        # Check start bracket
        stripped = content.strip()
        if not stripped.startswith('['):
            no_bracket_start.append((eid, name, stripped[:60]))
            
        if 'BACKSTORY:' in content:
            has_backstory += 1
        if 'FAMILY & PACK:' in content:
            has_family_pack += 1
        if 'CLAN AND COMPANY:' in content or 'CLAN & COMPANY:' in content:
            has_clan_company += 1
        if 'VOICE & BEHAVIOR:' in content:
            has_voice_behavior += 1
        else:
            # check alternative voice headings
            vh = re.findall(r'^[A-Z0-9 &/\-\(\)]*VOICE[A-Z0-9 &/\-\(\)]*:', content, re.M)
            if vh:
                has_voice_other.append((eid, name, vh))

    print(f"Types breakdown: {types_count}")
    print(f"Selective breakdown: {selective_count}")
    print(f"exclude_from_recursion: True={exclude_from_recursion_true}, other={exclude_from_recursion_other}")
    print(f"Priorities breakdown: {priorities}")
    print(f"Avatars: Custom={len(custom_avatar)}, Placeholder={len(placeholder_avatar)}, Missing={len(missing_avatar)}")
    if missing_avatar:
        print(f"  Missing avatars: {missing_avatar[:10]} (total: {len(missing_avatar)})")
    print(f"Entries NOT starting with '[': {len(no_bracket_start)}")
    for x in no_bracket_start:
        print(f"  - {x[0]} ({x[1]}): {x[2]}")
    print(f"Section stats: BACKSTORY={has_backstory}/{len(lexicon)}, FAMILY & PACK={has_family_pack}/{len(lexicon)}, CLAN/COMPANY={has_clan_company}/{len(lexicon)}, VOICE & BEHAVIOR={has_voice_behavior}/{len(lexicon)}")
    if has_voice_other:
        print(f"Alternative voice headings ({len(has_voice_other)}):")
        for x in has_voice_other[:10]:
            print(f"  - {x[0]} ({x[1]}): {x[2]}")

analyze_lorebook(prim, "Svartúlfr - NPC Primary")
analyze_lorebook(sec, "Svartúlfr - NPC Secondary")
