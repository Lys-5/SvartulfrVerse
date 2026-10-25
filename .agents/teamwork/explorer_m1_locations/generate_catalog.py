import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

off_ids = {
    "_p6WUaYcTJURrTXejecchk", "_RNU9Fx2pLD6PJ8LcKAdg6", "_J1B6d2DnNNyJhpnKWNcXz",
    "_94hRP4ywVYTHaUDDGfLqg", "_qe962a69a6PBbaHWCbP8r", "_BEnFGJPqBFJnTtrAHQQ9F",
    "_VMwRTPXdGTARktqnDLRTA", "_2rTUXXxAyYh8WYnGNtV2M"
}
active_188 = [l for l in snap_locs if (l.get("id") or l.get("_id")) not in off_ids]

loc_map = { (l.get("id") or l.get("_id")): l for l in active_188 }

def get_ancestors(lid):
    ancestors = []
    curr = lid
    while True:
        loc = loc_map.get(curr)
        if not loc:
            break
        pl = loc.get("parent_location")
        if not pl:
            break
        pid = pl.get("id") or pl.get("_id") if isinstance(pl, dict) else pl
        if not pid or pid not in loc_map:
            break
        ancestors.append((pid, loc_map[pid].get("name")))
        curr = pid
    return ancestors

def assign_environment(lid):
    loc = loc_map[lid]
    name = loc.get("name")
    ancestor_names = [a[1] for a in get_ancestors(lid)]
    all_names = [name] + ancestor_names
    
    if any(x in all_names for x in ["DDM Inc. // Voidspace", "The Otherworld", "Dead Dog Motel / Voidspace", "Trial Dungeon: Hive Apex Rift (Floors 1-18)"]):
        return "7. Voidspace/Otherworld"
    if any(x in all_names for x in ["Simi Valley", "Team Ukiyo Operational Base (Warehouse & Black Vault)"]):
        return "6. DMHA HQ & Guild District"
    if "Seven Hills" in all_names or "Villa Douglas" in all_names:
        return "5. Seven Hills"
    if "Supernatural University of Central California" in all_names:
        return "2. SUCC campus"
    if "Solarton" in all_names:
        return "3. Solarton"
    if "Blackwood City" in all_names:
        return "4. Blackwood"
    return "1. California Coast"

catalog = []
for lid, l in loc_map.items():
    name = l.get("name")
    ancestors = get_ancestors(lid)
    depth = len(ancestors)
    parent_id = ancestors[0][0] if depth > 0 else "None (Root)"
    parent_name = ancestors[0][1] if depth > 0 else "None (Root)"
    env = assign_environment(lid)
    keys = ", ".join(l.get("keys", []))
    inc_lex = l.get("included_lexicon_entries") or []
    has_context = bool(l.get("context_description"))
    
    catalog.append({
        "id": lid,
        "name": name,
        "depth": depth,
        "parent_id": parent_id,
        "parent_name": parent_name,
        "environment": env,
        "keys": keys,
        "inc_lex": inc_lex,
        "has_context": has_context
    })

# Save catalog to json for reference
with open(".agents/teamwork/explorer_m1_locations/catalog_188.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

print(f"Catalog of {len(catalog)} entries written to catalog_188.json")
