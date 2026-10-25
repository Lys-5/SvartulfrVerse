import json
import os

with open("exports/Svartulfr_Export.json", "r", encoding="utf-8") as f:
    exp = json.load(f)
export_locs = exp["world_locations"]

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

with open("FINAL/Svartulfr_Location.json", "r", encoding="utf-8") as f:
    lb = json.load(f)
lb_entries = lb["entries"]

print(f"Export locs count: {len(export_locs)}")
print(f"Snapshot locs count: {len(snap_locs)}")
print(f"Lorebook entries count: {len(lb_entries)}")

export_ids = {l.get("id") or l.get("_id"): l.get("name") for l in export_locs}
snap_ids = {l.get("id") or l.get("_id"): l.get("name") for l in snap_locs}
lb_ids = {e.get("entry_id"): e.get("name") for e in lb_entries}

print("\n--- IN SNAPSHOT BUT NOT IN EXPORT (The 8 removed/OFF locations?) ---")
diff_snap_exp = set(snap_ids.keys()) - set(export_ids.keys())
print(f"Count: {len(diff_snap_exp)}")
for did in diff_snap_exp:
    print(f"ID: {did} | Name: {snap_ids[did]}")

print("\n--- IN EXPORT BUT NOT IN SNAPSHOT ---")
diff_exp_snap = set(export_ids.keys()) - set(snap_ids.keys())
print(f"Count: {len(diff_exp_snap)}")
for did in diff_exp_snap:
    print(f"ID: {did} | Name: {export_ids[did]}")

print("\n--- CHECKING SNAPSHOT LOCATIONS ATTRIBUTES (parent_location, environment, etc.) ---")
# Check how many in snapshot have parent_location and environment populated
snap_by_id = {l.get("id") or l.get("_id"): l for l in snap_locs}
exp_by_id = {l.get("id") or l.get("_id"): l for l in export_locs}

# Let's inspect fields in snap vs exp for an overlapping location
overlap_id = list(set(export_ids.keys()) & set(snap_ids.keys()))[0]
print(f"Sample overlapping location: {export_ids[overlap_id]} ({overlap_id})")
print("In export:", exp_by_id[overlap_id])
print("\nIn snapshot:", {k: v for k, v in snap_by_id[overlap_id].items() if k not in ['description']})
