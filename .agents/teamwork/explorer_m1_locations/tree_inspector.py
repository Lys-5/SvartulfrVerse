import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

off_ids = {
    "_p6WUaYcTJURrTXejecchk", "_RNU9Fx2pLD6PJ8LcKAdg6", "_J1B6d2DnNNyJhpnKWNcXz",
    "_94hRP4ywVYTHaUDDGfLqg", "_qe962a69a6PBbaHWCbP8r", "_BEnFGJPqBFJnTtrAHQQ9F",
    "_VMwRTPXdGTARktqnDLRTA", "_2rTUXXxAyYh8WYnGNtV2M"
}
active_188 = [l for l in snap_locs if (l.get("id") or l.get("_id")) not in off_ids]

loc_map = {}
for l in active_188:
    lid = l.get("id") or l.get("_id")
    loc_map[lid] = l

children = defaultdict(list)
parent_map = {}
orphans = []

for lid, l in loc_map.items():
    pl = l.get("parent_location")
    if pl:
        pid = pl.get("id") or pl.get("_id") if isinstance(pl, dict) else pl
        if pid in loc_map:
            children[pid].append(lid)
            parent_map[lid] = pid
        else:
            orphans.append((lid, l.get("name"), pid))
    else:
        children[None].append(lid)
        parent_map[lid] = None

out_lines = []
out_lines.append(f"Total active: {len(loc_map)}")
out_lines.append(f"Orphans (pointing to missing parent): {len(orphans)}")
for o in orphans:
    out_lines.append(f"  Orphan: {o}")

def format_tree(pid, indent=0):
    for cid in sorted(children[pid], key=lambda x: loc_map[x].get("name", "")):
        loc = loc_map[cid]
        cname = loc.get("name")
        sub_count = len(children[cid])
        sub_str = f" ({sub_count} children)" if sub_count > 0 else ""
        out_lines.append("  " * indent + f"- {cname} [ID: {cid}]{sub_str}")
        format_tree(cid, indent + 1)

out_lines.append("\n=== COMPLETE HIERARCHICAL TREE OF 188 LOCATIONS ===")
for root_id in sorted(children[None], key=lambda x: loc_map[x].get("name", "")):
    loc = loc_map[root_id]
    rname = loc.get("name")
    sub_count = len(children[root_id])
    out_lines.append(f"\nROOT: {rname} [ID: {root_id}] ({sub_count} children)")
    format_tree(root_id, 1)

def count_tree(pid):
    c = 1 if pid is not None else 0
    for child in children[pid]:
        c += count_tree(child)
    return c

out_lines.append(f"\nTotal tree node count: {count_tree(None)}")

with open(".agents/teamwork/explorer_m1_locations/tree_structure.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Tree structure written successfully. Total lines: {len(out_lines)}, total nodes: {count_tree(None)}")
