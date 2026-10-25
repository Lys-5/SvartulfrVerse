import json

for p in ["FINAL/Svartulfr_NPC_Primary.json", "FINAL/Svartulfr_Lorebook_I.json", "FINAL/Svartulfr_Lorebook_II.json"]:
    d = json.load(open(p, encoding="utf-8"))["entries"]
    for e in d:
        c = e.get("content", "")
        if any(k in c for k in ["Zefir", "Ut Berg", "Firstborn", "827", "824", "1005", "823"]):
            print(f"=== {p} | {e.get('name')} ===")
            print(c)
