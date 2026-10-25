import json

for lb_path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(lb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    no_avatar = 0
    no_regex = 0
    no_npc_info = 0
    no_ignored_chars = 0
    selective_true_count = 0
    for e in data.get('lexicon', []):
        if not e.get('avatar'):
            no_avatar += 1
        if not e.get('custom_avatar_regex') or not e.get('avatar_activation_regex'):
            no_regex += 1
        if not e.get('npc_info'):
            no_npc_info += 1
        if not e.get('ignored_characters'):
            no_ignored_chars += 1
        if e.get('selective') is True:
            selective_true_count += 1
    print(f'{lb_path}:')
    print(f'   Missing avatar: {no_avatar}')
    print(f'   Missing regex: {no_regex}')
    print(f'   Missing npc_info: {no_npc_info}')
    print(f'   Empty ignored_characters: {no_ignored_chars}')
    print(f'   Selective true: {selective_true_count}')
