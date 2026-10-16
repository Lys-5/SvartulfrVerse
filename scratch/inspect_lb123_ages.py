import json

for lb_name in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json']:
    src_path = f'lorebooks/source/{lb_name}'
    fin_path = f'FINAL/{lb_name}'
    with open(src_path, 'r', encoding='utf-8') as f:
        src_data = json.load(f)
    with open(fin_path, 'r', encoding='utf-8') as f:
        fin_data = json.load(f)
    
    src_entries = src_data['entries']
    src_list = src_entries.values() if isinstance(src_entries, dict) else src_entries
    
    age_in_src = [e for e in src_list if '{{age}}' in e.get('content', '')]
    print(f"\n=== {lb_name} ===")
    print(f"Occurrences of {{{{age}}}} in source: {len(age_in_src)}")
    for e in age_in_src[:3]:
        name = e.get('comment') or e.get('name') or (e.get('key', [''])[0] if isinstance(e.get('key'), list) else '')
        print(f"  Sample entry: {name}")
        for l in e.get('content', '').split('\n'):
            if '{{age}}' in l:
                print(f"    SOURCE: {l.strip()[:100]}")
