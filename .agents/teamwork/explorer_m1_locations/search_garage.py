import json

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

print("Locations with 'garage' or 'logan' in name or description:")
for l in snap_locs:
    name = l.get("name", "")
    desc = l.get("description", "")
    cdesc = l.get("context_description", "")
    if "garage" in name.lower() or "logan" in name.lower():
        print(f"Match in NAME: '{name}' [ID: {l.get('id') or l.get('_id')}]")
        print(f"  Parent: {l.get('parent_location')}")
    elif "garage" in desc.lower() or "logan" in desc.lower() or "garage" in cdesc.lower() or "logan" in cdesc.lower():
        print(f"Match in DESC/CDESC: '{name}' [ID: {l.get('id') or l.get('_id')}]")
