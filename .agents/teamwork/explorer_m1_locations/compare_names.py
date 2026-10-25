import json

with open("exports/Svartulfr_Export.json", "r", encoding="utf-8") as f:
    exp = json.load(f)
locs = exp["world_locations"]

print("Total export locations:", len(locs))
names = [l.get("name") for l in locs]

mystic = [n for n in names if "mystic" in n.lower() or "camp" in n.lower() or "erie" in n.lower()]
print("Camp/Mystic in export:", mystic)

with open("FINAL/Svartulfr_Location.json", "r", encoding="utf-8") as f:
    lb = json.load(f)
lb_names = [e.get("name") for e in lb["entries"]]

# Compare names
in_exp_not_lb = set(names) - set(lb_names)
in_lb_not_exp = set(lb_names) - set(names)
print(f"In export but not in Lorebook: {len(in_exp_not_lb)} -> {in_exp_not_lb}")
print(f"In Lorebook but not in export: {len(in_lb_not_exp)} -> {in_lb_not_exp}")
