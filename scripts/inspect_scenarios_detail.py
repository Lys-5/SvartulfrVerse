import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
scens = data.get('world_scenarios', [])
print(f"Total scenarios: {len(scens)}")
s0 = scens[0]
print("Keys in scenario:", list(s0.keys()))
for s in scens:
    sid = s['id']
    sname = s['name']
    start_loc = s.get('starting_location')
    inputs = s.get('user_inputs', [])
    print(f"{sid} | {sname} | start_loc: {start_loc} | inputs: {len(inputs)}")
