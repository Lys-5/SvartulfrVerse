import json

lorebooks = {
    'Lore_I': 'FINAL/Svartulfr_Lorebook_I.json',
    'Lore_II': 'FINAL/Svartulfr_Lorebook_II.json',
    'Lore_III': 'FINAL/Svartulfr_Lorebook_III.json',
    'Location': 'lorebooks/optimized/Svartulfr_Location.json',
    'NPC_Primary': 'FINAL/Svartulfr_NPC_Primary.json',
    'NPC_Secondary': 'FINAL/Svartulfr_NPC_Secondary.json'
}

schema_summary = {}

for name, path in lorebooks.items():
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    entries = d.get('entries', [])
    all_keys = set()
    key_frequency = {}
    for e in entries:
        for k in e.keys():
            all_keys.add(k)
            key_frequency[k] = key_frequency.get(k, 0) + 1
    
    schema_summary[name] = {
        'id': d.get('id'),
        'name': d.get('name'),
        'token_budget': d.get('token_budget'),
        'total_entries': len(entries),
        'top_level_keys': list(d.keys()),
        'entry_keys': sorted(list(all_keys)),
        'key_counts': key_frequency
    }

with open('e:/repository/SvartulfrVerse/.agents/teamwork/explorer_survey_2/schema_survey_results.json', 'w', encoding='utf-8') as out:
    json.dump(schema_summary, out, indent=2)

print('Wrote schema summary to schema_survey_results.json')
