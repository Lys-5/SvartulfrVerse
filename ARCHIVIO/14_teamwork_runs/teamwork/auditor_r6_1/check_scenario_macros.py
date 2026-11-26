import json
import re

npc_slots = [
    'best_friend', 'roommate', 'quarterback', 'sports_rival', 
    'friend', 'childhood_friend', 'male_roommate', 'ai_companion'
]

files = [
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json'
]

print("=== CHECK SCENARIO MACROS REPLACEMENT ===")
all_clean = True
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    text = json.dumps(data)
    print(f"\nChecking {fpath}:")
    for s in npc_slots:
        pattern = r'\{\{scenarioChar\s*\"' + s + r'\"\}\}'
        found = re.findall(pattern, text)
        print(f"  Slot '{s}' macro occurrences: {len(found)}")
        if len(found) > 0:
            all_clean = False
            print(f"    ERROR: Unreplaced macro for slot '{s}'!")

print(f"\nAll NPC macros successfully replaced: {all_clean}")
