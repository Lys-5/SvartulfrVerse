import json

fpath = 'FINAL/Svartulfr_Master_Scenario.json'
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

greetings = data.get('greetings', [])

catalog = []
for i, g in enumerate(greetings):
    gid = g.get('id')
    name = g.get('name')
    desc = g.get('description')
    lpi = g.get('linked_persona_ids', [])
    content = g.get('content', '')
    first_msg = g.get('messages', [{}])[0]
    speaker_slot = first_msg.get('speaker_slot')
    
    # Classification
    if '[FemPOV]' in name:
        pov = 'FemPOV'
        target_ids = ['persona_1786335754946']
    elif '[MalePOV]' in name:
        pov = 'MalePOV'
        target_ids = ['1792155173728']
    else:
        pov = 'Shared/Neutral'
        target_ids = ['persona_1786335754946', '1792155173728']
        
    catalog.append({
        'index': i,
        'id': gid,
        'title': name,
        'description': desc,
        'speaker_slot': speaker_slot,
        'pov_class': pov,
        'current_lpi': lpi,
        'target_lpi': target_ids,
        'content_snippet': content.replace('\n', ' ')[:120]
    })

print(f"Total greetings: {len(catalog)}")
fem_count = sum(1 for c in catalog if c['pov_class'] == 'FemPOV')
male_count = sum(1 for c in catalog if c['pov_class'] == 'MalePOV')
shared_count = sum(1 for c in catalog if c['pov_class'] == 'Shared/Neutral')
print(f"FemPOV: {fem_count}, MalePOV: {male_count}, Shared/Neutral: {shared_count}")
