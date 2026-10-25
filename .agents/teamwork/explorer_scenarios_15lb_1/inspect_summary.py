import json
import os

target_15_lbs = [
    "_gwwCxCfQ6PQaLEjAQVpJL", # Lorebook I
    "_HfG7TeV6MJyj6bxMwxkpt", # Lorebook II
    "_9zWTGqYJNJ4BCDMj8gfcD", # Lorebook III
    "_EjXxkmPVhpCXg8xABpFkK", # Location
    "_Uht3Ckz44JBDrPnUHq7LV", # NPC Secondary
    "_zwEqgEEzh12X6gHVmMKKC", # NPC Primary
    "_GV1KyHVY1RMbCnWgLkzDG", # A0 Behavioral Realism
    "_GbWJbkhgLzWexMHrjyUUc", # A1 Physics
    "_FaVcHfmrqcaJq8pa3WmRw", # A2 Social Realism
    "_BbrRgrcdGPMLEbBU2b6xk", # A3 Medical Realism
    "_gchmML4Q478zdFjhXf8rN", # A4 Cultural Realism
    "_brNyzEdhzNAyxK8xC8hhm", # A5 Sex Position
    "_YtKLMTwyMxNf1DNYqBx1t", # A5.5 Scene Tone
    "_b9HgpUXtAW8VmTy82BPDV", # A6 World Realism
    "_c8bEm1bWphwqFBXWRPrV8", # A7 Queer Realism
]

files = [
    "FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json",
    "FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json",
    "FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json",
    "FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json",
    "FINAL/Svartulfr_Master_Scenario.json"
]

base_dir = r"e:\repository\SvartulfrVerse"

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n=======================================================")
    print(f"FILE: {fpath}")
    print(f"ID: {data.get('id')}")
    print(f"TITLE: {data.get('title') or data.get('name')}")
    current_lbs = data.get("lorebook_ids", [])
    print(f"Current lorebook_ids count: {len(current_lbs)}")
    print(f"Current lorebook_ids: {current_lbs}")
    missing_lbs = [lb for lb in target_15_lbs if lb not in current_lbs]
    extra_lbs = [lb for lb in current_lbs if lb not in target_15_lbs]
    print(f"Missing from 15 target: {missing_lbs}")
    print(f"Extra not in 15 target: {extra_lbs}")
    
    greetings = data.get("greetings", [])
    print(f"Total greetings: {len(greetings)}")
    for i, g in enumerate(greetings):
        gid = g.get("id")
        gname = g.get("name") or g.get("title") or g.get("label")
        lpi = g.get("linked_persona_ids")
        lp = g.get("linked_personas")
        msgs = g.get("messages", [])
        print(f"  [{i}] ID: {gid} | Name: '{gname}' | linked_persona_ids: {lpi} | linked_personas: {lp} | msgs: {len(msgs)}")
