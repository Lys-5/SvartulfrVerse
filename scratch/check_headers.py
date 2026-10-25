import json

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for idx, e in enumerate(d["lexicon"]):
    info = e.get("npc_info", {})
    content = e.get("content", "")
    first_line = content.split("\n")[0] if content else ""
    mn = info.get("middle_names")
    if mn:
        print(f"[{idx}] {info.get('first_name')} {mn} {info.get('last_name')}")
        print(f"   Header: {first_line[:130]}...")
