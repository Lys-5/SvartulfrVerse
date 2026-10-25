import json

for lb_path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(lb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    em_count = 0
    asterisk_count = 0
    age_macro_count = 0
    broad_key_count = 0
    for e in data.get('lexicon', []):
        c = e.get('content', '')
        if '—' in c:
            em_count += 1
        if '**' in c:
            asterisk_count += 1
        if '{{age' in c:
            age_macro_count += 1
    print(f'{lb_path}:')
    print(f'   Em-dashes: {em_count} entries')
    print(f'   Bold asterisks (**): {asterisk_count} entries')
    print(f'   Age macro: {age_macro_count} entries')
