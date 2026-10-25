import json

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for idx, e in enumerate(d["lexicon"]):
    info = e.get("npc_info", {})
    titles = info.get("titles")
    if titles:
        print(f"[{idx}] {info.get('first_name')} {info.get('last_name')}: titles = {titles}")
