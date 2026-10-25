import json
import os

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

results = {}

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        continue
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Check top level keys
    keys = list(data.keys())
    lorebook_ids = data.get("lorebook_ids", [])
    greetings = data.get("greetings", [])
    
    greeting_info = []
    for idx, g in enumerate(greetings):
        g_info = {
            "index": idx,
            "id": g.get("id"),
            "label": g.get("label"),
            "title": g.get("title"),
            "has_linked_persona_ids": "linked_persona_ids" in g,
            "linked_persona_ids": g.get("linked_persona_ids"),
            "keys": list(g.keys()),
            "messages_count": len(g.get("messages", [])) if "messages" in g else 0,
            "content_preview": g.get("content", "")[:100] if "content" in g else None,
        }
        if "messages" in g and len(g["messages"]) > 0:
            first_msg = g["messages"][0]
            g_info["first_msg_preview"] = {
                "speaker": first_msg.get("speaker") or first_msg.get("name") or first_msg.get("role"),
                "text_snippet": (first_msg.get("text") or first_msg.get("content") or "")[:100]
            }
        greeting_info.append(g_info)
        
    results[fpath] = {
        "title": data.get("title") or data.get("name"),
        "id": data.get("id"),
        "top_level_keys": keys,
        "lorebook_ids_count": len(lorebook_ids),
        "lorebook_ids": lorebook_ids,
        "greetings_count": len(greetings),
        "greetings": greeting_info
    }

print(json.dumps(results, indent=2))
