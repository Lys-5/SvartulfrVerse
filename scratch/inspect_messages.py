import json

for fname in ['Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'Svartulfr_Scenario_SUCC_Route_Jasper.json']:
    print('=== ' + fname + ' ===')
    with open('FINAL/scenarios/' + fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for gi, g in enumerate(data.get('greetings', [])):
        title = g.get('name') or g.get('title')
        print(f"G{gi} ({title}) [speaker_slot: {g.get('speaker_slot')}]:")
        for mi, m in enumerate(g.get('messages', [])):
            text = m.get('content', '')
            snippet = text[:90].replace('\n', ' ')
            print(f"  M{mi} [slot: {m.get('speaker_slot')}] -> {snippet}...")
