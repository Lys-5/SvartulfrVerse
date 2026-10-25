import json

files = [
    'FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json',
    'FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json'
]
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('FILE:', fpath)
    print('ID:', data.get('id'))
    print('TITLE:', data.get('title') or data.get('name'))
    print('lorebook_ids:', data.get('lorebook_ids'))
    print('greetings count:', len(data.get('greetings', [])))
    for i, g in enumerate(data.get('greetings', [])):
        print(f"  [{i}] ID: {g.get('id')} | Name: {g.get('name')} | linked_persona_ids: {g.get('linked_persona_ids')}")
