import json

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as f:
    scen = json.load(f)

for gid in ['scene-alyssa-story-2-1', 'scene-guild-1', 'scene-alyssa-story-8-1', 'scene-alyssa-story-9-1']:
    g = next(x for x in scen['greetings'] if x['id'] == gid)
    print(f"=== {g['id']} : {g['name']} ===")
    print("Main speaker_slot:", g.get('speaker_slot'))
    for idx, m in enumerate(g.get('messages', [])):
        print(f"  Msg {idx}: speaker_slot={m.get('speaker_slot')} | text={m.get('content')[:80]}...")
