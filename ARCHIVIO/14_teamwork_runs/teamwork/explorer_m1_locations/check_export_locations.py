import json
import os

print("=== CHECKING exports/Svartulfr_Export.json ===")
if os.path.exists("exports/Svartulfr_Export.json"):
    with open("exports/Svartulfr_Export.json", "r", encoding="utf-8") as f:
        exp = json.load(f)
    print("Export keys:", list(exp.keys()) if isinstance(exp, dict) else type(exp))
    if isinstance(exp, dict) and "locations" in exp:
        print("locations in export:", len(exp["locations"]))
        locs = exp["locations"]
        print("sample location keys:", list(locs[0].keys()) if locs else [])

print("\n=== CHECKING scratch/backup_consolidated_snapshot/world_locations.json ===")
if os.path.exists("scratch/backup_consolidated_snapshot/world_locations.json"):
    with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
        wlocs = json.load(f)
    print("wlocs len:", len(wlocs))
    # Check enabled or status
    print("sample wloc keys:", list(wlocs[0].keys()) if wlocs else [])

print("\n=== CHECKING FINAL/Svartulfr_Location.json entries ===")
with open("FINAL/Svartulfr_Location.json", "r", encoding="utf-8") as f:
    lb = json.load(f)
lb_entries = lb.get("entries", [])
print("Lorebook entries len:", len(lb_entries))
# Check names with Camp Mystic
cm_entries = [e for e in lb_entries if "camp mystic" in e.get("name", "").lower() or "mystic" in e.get("name", "").lower() or "cabin" in e.get("name", "").lower() or "b-0" in e.get("name", "").lower() or "g-0" in e.get("name", "").lower()]
print("Camp Mystic related entries in Lorebook:", len(cm_entries))
