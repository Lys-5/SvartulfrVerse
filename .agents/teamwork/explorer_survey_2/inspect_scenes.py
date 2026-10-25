import json
import re

scenario = json.load(open('FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json', encoding='utf-8'))

print("Scenario ID:", scenario.get('id'), scenario.get('_id'))
print("Scenario Name:", scenario.get('name'))
print("Premade scenes count:", len(scenario.get('premade_scenes', [])))

for idx, sc in enumerate(scenario.get('premade_scenes', [])):
    print(f"\n================ Scene {idx}: {sc.get('id')} ================")
    print("Description:", sc.get('description'))
    text = sc.get('scene_text', '')
    lines = text.split('\n')
    print(f"Total lines: {len(lines)}, total chars: {len(text)}")
    
    # Find all speaker-like lines
    arrow_speakers = re.findall(r'^=>([^:\n]+):', text, flags=re.MULTILINE)
    colon_speakers = re.findall(r'^([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', text, flags=re.MULTILINE)
    
    print("Arrow speakers (=>Speaker:):", arrow_speakers)
    print("Plain colon speakers (Speaker:):", [s for s in colon_speakers if not s.startswith('=>')])
