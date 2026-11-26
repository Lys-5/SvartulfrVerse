import json

data = json.load(open('FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json', encoding='utf-8'))
for i, s in enumerate(data.get('premade_scenes', [])):
    print(f"==================== SCENE {i}: {s.get('id')} ====================")
    print(f"Description: {s.get('description')}")
    lines = s.get('scene_text', '').split('\n')
    for line_idx, line in enumerate(lines):
        if line.strip():
            print(f"[{line_idx:02d}] {line[:140]}")
    print()
