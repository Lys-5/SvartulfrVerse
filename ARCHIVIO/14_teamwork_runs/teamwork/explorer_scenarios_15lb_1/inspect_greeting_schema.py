import json

files = [
    'FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json',
    'FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json',
    'FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json',
    'FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json',
    'FINAL/Svartulfr_Master_Scenario.json'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    greetings = data.get('greetings', [])
    first_g = greetings[0] if greetings else {}
    print(f"=== {fpath} ===")
    print("Greeting keys:", list(first_g.keys()))
    print("linked_persona_ids in greeting:", "linked_persona_ids" in first_g, type(first_g.get("linked_persona_ids")))
    print("linked_personas in greeting:", "linked_personas" in first_g, type(first_g.get("linked_personas")))
    if "messages" in first_g and len(first_g["messages"]) > 0:
        print("Message[0] keys:", list(first_g["messages"][0].keys()))
        print("Sample message[0]:", first_g["messages"][0])
    print()
