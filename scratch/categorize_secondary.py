import json

sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

groups = {
    'camp_mystic': [],
    'has_backstory': [],
    'no_bracket': [],
    'other_format': []
}

for e in sec['lexicon']:
    eid = e.get('entry_id')
    name = e.get('name')
    content = e.get('content', '').strip()
    
    if not content.startswith('['):
        groups['no_bracket'].append((eid, name))
    elif 'CAMP MYSTIC BACKGROUND & ROLE:' in content:
        groups['camp_mystic'].append((eid, name))
    elif 'BACKSTORY:' in content:
        groups['has_backstory'].append((eid, name))
    else:
        groups['other_format'].append((eid, name))

print("=== SECONDARY BREAKDOWN ===")
print("No bracket start:", len(groups['no_bracket']))
for x in groups['no_bracket']:
    print(" ", x)

print("Camp Mystic format:", len(groups['camp_mystic']))
print("Standard BACKSTORY format:", len(groups['has_backstory']))
print("Other format:", len(groups['other_format']))
for x in groups['other_format']:
    print(" ", x)
