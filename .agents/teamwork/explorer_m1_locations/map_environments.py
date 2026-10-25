import json
import sys
from collections import defaultdict, Counter

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

# Check existing environment property on each of the 188 locations
env_on_loc = {}
for lid, l in loc_map.items():
    env = l.get("environment")
    if env:
        ename = env.get("name") if isinstance(env, dict) else env
        eid = env.get("id") or env.get("_id") if isinstance(env, dict) else env
        env_on_loc[lid] = (eid, ename)
    else:
        env_on_loc[lid] = (None, None)

print("Existing environment distribution on location objects:")
env_counter = Counter(ename for eid, ename in env_on_loc.values())
for ename, count in env_counter.items():
    print(f"  {ename}: {count}")

# Now let's examine the 7 canonical Environments:
# 1. California Coast (Root: LA, Bakersfield, Ventura, Hex Valley, Route 101, Camp Mystic?)
# 2. SUCC campus (Parent: California Coast)
# 3. Solarton (Parent: California Coast)
# 4. Blackwood (Parent: California Coast)
# 5. Seven Hills (Parent: Blackwood)
# 6. DMHA HQ & Guild District (Parent: California Coast / Simi Valley)
# 7. Voidspace/Otherworld (DDM Inc., Dead Dog Motel, Trial Dungeons 1-18)

# Let's write a function that traces ancestors of any location
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

# Let's map each of the 188 locations to one of the 7 Environments
def assign_environment(lid):
    loc = loc_map[lid]
    name = loc.get("name")
    ancestor_names = [a[1] for a in get_ancestors(lid)]
    all_names = [name] + ancestor_names
    
    # Check 7. Voidspace/Otherworld
    # "Voidspace/Otherworld (DDM Inc., Dead Dog Motel, Trial Dungeons 1-18, fratture di realtà generate dalle faglie)"
    # Notice: DDM Inc. // Voidspace, The Otherworld (under Blackwood Forest), Dead Dog Motel / Voidspace, Trial Dungeon
    if any(x in all_names for x in ["DDM Inc. // Voidspace", "The Otherworld", "Dead Dog Motel / Voidspace", "Trial Dungeon: Hive Apex Rift (Floors 1-18)"]):
        return "7. Voidspace/Otherworld"
    
    # Check 6. DMHA HQ & Guild District
    # "(Parent: California Coast / Simi Valley — epicentro disturbi magici e apertura delle faglie dei dungeon, comando cacciatori DMHA, taglie, armerie runiche, CCD)"
    # Simi Valley and its children, or Team Ukiyo
    if any(x in all_names for x in ["Simi Valley", "Team Ukiyo Operational Base (Warehouse & Black Vault)"]):
        return "6. DMHA HQ & Guild District"
    
    # Check 5. Seven Hills
    # "(Parent: Blackwood — Quartiere residenziale del Branco, Villa Douglas, tenuta e campi di addestramento)"
    if "Seven Hills" in all_names or "Villa Douglas" in all_names:
        return "5. Seven Hills"
        
    # Check 2. SUCC campus
    # "(Parent: California Coast — 129 Hocus Way, aule, dormitori, laboratori, impianti sportivi)"
    if "Supernatural University of Central California" in all_names:
        return "2. SUCC campus"
        
    # Check 3. Solarton
    # "(Parent: California Coast — Solarton Square, Bricklane Mall, Sidewinders, residenziale)"
    # But NOT SUCC campus (which is a child of Solarton in parent_location, but designated as separate Environment #2)
    if "Solarton" in all_names:
        return "3. Solarton"
        
    # Check 4. Blackwood
    # "(Parent: California Coast — Uptown, Arcadia, Bluemoon, Oldtown, Dockside, Ironworks, Bloodmoon Forest)"
    # But NOT Seven Hills (which is Environment #5) and NOT The Otherworld (Environment #7)
    if "Blackwood City" in all_names:
        return "4. Blackwood"
        
    # Check 1. California Coast
    # "(Root: LA, Bakersfield, Ventura, Hex Valley, Route 101)"
    # Plus Camp Mystic, Zone di Transito e Confine (Ventura / Route 101)
    return "1. California Coast"

env_buckets = defaultdict(list)
for lid, l in loc_map.items():
    target_env = assign_environment(lid)
    env_buckets[target_env].append((lid, l.get("name")))

print("\n=== MAPPING OF 188 LOCATIONS ACROSS 7 CANONICAL ENVIRONMENTS ===")
total_mapped = 0
for env_name in sorted(env_buckets.keys()):
    locs = env_buckets[env_name]
    total_mapped += len(locs)
    print(f"\n{env_name}: {len(locs)} locations")
    for lid, name in sorted(locs, key=lambda x: x[1]):
        print(f"  - {name} [ID: {lid}]")

print(f"\nTotal mapped: {total_mapped} / 188")
