import json

for fname in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f'Checking {fname}...')
    age_macros = 0
    non_npc = 0
    not_custom_regex = 0
    lines_parsed_not_1 = 0
    ignored_chars_count = 0
    ignored_personas_count = 0
    selective_count = 0

    for idx, e in enumerate(d['entries']):
        name = e.get('name', 'UNKNOWN')
        c = e.get('content', '')
        if '{{age}}' in c:
            age_macros += 1
            print(f"  [FAIL] {name} has {{age}} macro!")
        if e.get('type') != 'npc':
            non_npc += 1
            print(f"  [FAIL] {name} type is {e.get('type')}")
        if e.get('custom_avatar_regex') is not True:
            not_custom_regex += 1
            print(f"  [FAIL] {name} custom_avatar_regex is not True")
        if e.get('lines_parsed') != 1:
            lines_parsed_not_1 += 1
            print(f"  [FAIL] {name} lines_parsed is not 1")
        if e.get('ignored_characters'):
            ignored_chars_count += 1
        if e.get('ignored_personas'):
            ignored_personas_count += 1
        if e.get('selective'):
            selective_count += 1
            print(f"  Selective entry: {name}, sec_keys: {e.get('secondary_keys')}")

    print(f"  age_macros: {age_macros}")
    print(f"  non_npc: {non_npc}")
    print(f"  not_custom_regex: {not_custom_regex}")
    print(f"  lines_parsed_not_1: {lines_parsed_not_1}")
    print(f"  entries with ignored_characters: {ignored_chars_count}")
    print(f"  entries with ignored_personas: {ignored_personas_count}")
    print(f"  entries with selective: true: {selective_count}")
