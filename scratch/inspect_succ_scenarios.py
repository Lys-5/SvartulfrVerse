import json
import pathlib

root = pathlib.Path('.')
for name, rel_path in [('Alyssa', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json'),
                       ('Jasper', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json')]:
    path = root / rel_path
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== {name} ({d.get('name')}) ===")
    print("Slots:", [(s['key'], s['label']) for s in d.get('slots', [])])
    greetings = d.get('greetings', [])
    print(f"Greetings Count: {len(greetings)}")
    for idx, g in enumerate(greetings):
        print(f"  [{idx}] {g.get('id')} | {g.get('name')} | speaker_slot: {g.get('speaker_slot')}")
        print(f"      description: {g.get('description')}")
        msgs = g.get('messages', [])
        print(f"      messages count: {len(msgs)}")
        for midx, m in enumerate(msgs):
            print(f"        m[{midx}] slot: {m.get('speaker_slot')} | id: {m.get('id')} | content: {m.get('content')[:60]}...")
