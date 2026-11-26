import json

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

# Filter out the 8 OFF locations
off_ids = {
    "_p6WUaYcTJURrTXejecchk", "_RNU9Fx2pLD6PJ8LcKAdg6", "_J1B6d2DnNNyJhpnKWNcXz",
    "_94hRP4ywVYTHaUDDGfLqg", "_qe962a69a6PBbaHWCbP8r", "_BEnFGJPqBFJnTtrAHQQ9F",
    "_VMwRTPXdGTARktqnDLRTA", "_2rTUXXxAyYh8WYnGNtV2M"
}
active_188 = [l for l in snap_locs if (l.get("id") or l.get("_id")) not in off_ids]
print(f"Active locations count: {len(active_188)}")

# Build lookup by id and name
loc_by_id = {}
for l in active_188:
    lid = l.get("id") or l.get("_id")
    loc_by_id[lid] = l

# Check parent_location field format
parents = {}
for lid, l in loc_by_id.items():
    pl = l.get("parent_location")
    if pl:
        if isinstance(pl, dict):
            pid = pl.get("id") or pl.get("_id")
            pname = pl.get("name")
        else:
            pid = pl
            pname = loc_by_id.get(pid, {}).get("name", "UNKNOWN")
        parents[lid] = (pid, pname)
    else:
        parents[lid] = (None, None)

print("\n--- ROOT LOCATIONS (parent_location is None) ---")
roots = [lid for lid, (pid, pname) in parents.items() if pid is None]
print(f"Root count: {len(roots)}")
for r in roots:
    print(f"- {loc_by_id[r].get('name')} (ID: {r})")
