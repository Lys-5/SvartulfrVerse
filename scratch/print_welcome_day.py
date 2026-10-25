import json

with open('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    g = d['greetings'][0]
    print('=== ALYSSA GREETING 0 ===')
    print('Name:', g.get('name'))
    print('Description:', g.get('description'))
    for i, m in enumerate(g.get('messages', [])):
        print(f"\n--- MESSAGE {i} (slot: {m.get('speaker_slot')}) ---")
        print(m.get('content'))

with open('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    g = d['greetings'][0]
    print('\n' + '='*50)
    print('=== JASPER GREETING 0 ===')
    print('Name:', g.get('name'))
    print('Description:', g.get('description'))
    for i, m in enumerate(g.get('messages', [])):
        print(f"\n--- MESSAGE {i} (slot: {m.get('speaker_slot')}) ---")
        print(m.get('content'))
