import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
data = json.load(open('FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json', encoding='utf-8'))

for i, s in enumerate(data['premade_scenes']):
    print(f"============================== SCENE {i}: {s['id']} ==============================")
    print(f"Description: {s['description']}")
    text = s['scene_text']
    paragraphs = text.split('\n\n')
    for p_idx, p in enumerate(paragraphs):
        p_strip = p.strip()
        first_line = p_strip.split('\n')[0]
        print(f"P{p_idx:02d}: [{first_line[:70]}] (total lines: {len(p_strip.split(chr(10)))}, chars: {len(p_strip)})")
    print()
