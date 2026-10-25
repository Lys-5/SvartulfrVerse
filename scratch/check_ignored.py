import json

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for idx, e in enumerate(d["lexicon"]):
    ics = e.get("ignored_characters")
    ips = e.get("ignored_personas")
    if ics or ips:
        print(f"[{idx}] {e.get('name')}: ignored_characters={ics}, ignored_personas={ips}")
