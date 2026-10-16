import json

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as f:
    scen = json.load(f)

for g in scen.get('greetings', []):
    sp = g.get('speaker_slot')
    msp = [m.get('speaker_slot') for m in g.get('messages', [])]
    all_sp = set([sp] + msp)
    bad = all_sp.intersection({'paternal_grandfather', 'paternal_grandmother', 'boss', 'major'})
    if bad:
        print(f"Greeting '{g.get('id')}' ({g.get('name')}): uses {bad}")
