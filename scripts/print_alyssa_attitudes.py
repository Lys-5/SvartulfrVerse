import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = {c['id']: c['display_name'] for c in d['world_characters']}
alyssa = [x for x in d['world_characters'] if x['id'] == '_MXcEC8Y6B3BNm3b1ttHj6'][0]

for a in alyssa.get('attitudes', []):
    tid = a.get('target_id')
    tname = chars.get(tid, tid)
    tier = a.get('tier')
    intensity = a.get('intensity')
    reasoning = a.get('reasoning')
    print(f"Target: {tname} ({tier}, intensity: {intensity})")
    print(f"  {reasoning}\n")
