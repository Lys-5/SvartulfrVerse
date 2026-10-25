import json
import re

with open('FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

print(f"Scenario Name: {sc.get('name')}")
print(f"Total Scenes: {len(sc.get('premade_scenes', []))}")

for idx, scene in enumerate(sc.get('premade_scenes', [])):
    sid = scene.get('id')
    desc = scene.get('description')
    text = scene.get('scene_text', '')
    em_dashes = [c for c in text if c in '—\u2014\u2013']
    asterisks = [c for c in text if c == '*']
    speaker_tags = re.findall(r'(?:^|\n)\s*(=>[A-Za-z0-9_]+:)', text)
    invalid_prefixes = re.findall(r'(?:^|\n)\s*([A-Za-z0-9_ ]+:\s*")', text)
    print(f"\n--- Scene {idx}: {sid} ---")
    print(f"Description: {desc}")
    print(f"Char count: {len(text)}")
    print(f"Em-dashes: {len(em_dashes)} {em_dashes}")
    print(f"Asterisks: {len(asterisks)}")
    print(f"Speaker tags count: {len(speaker_tags)}")
    print(f"Speaker tags: {speaker_tags}")
    print(f"Non-arrow speaker prefixes found: {invalid_prefixes}")
