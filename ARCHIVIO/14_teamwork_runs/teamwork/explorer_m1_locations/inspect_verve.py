import json

print("=== THE VERVE IN WORLD_LOCATIONS ===")
with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

for l in snap_locs:
    name = l.get("name", "")
    if "verve" in name.lower() or "logan" in name.lower() or "garage" in name.lower():
        print(f"Name: {name} | ID: {l.get('id') or l.get('_id')}")
        print("Parent:", l.get("parent_location"))
        print("Environment:", l.get("environment"))
        print("Context Description:", l.get("context_description"))
        print("Description (first 300 chars):", l.get("description", "")[:300])
        print("Keys:", l.get("keys"), "Secondary:", l.get("secondary_keys"))
        print("Included Lexicon:", l.get("included_lexicon_entries"))
        print("Excluded Lexicon:", l.get("excluded_lexicon_entries"))
        print("Tags:", l.get("tags"))
        print("-" * 50)

print("\n=== THE VERVE IN FINAL/Svartulfr_Location.json ===")
with open("FINAL/Svartulfr_Location.json", "r", encoding="utf-8") as f:
    lb = json.load(f)

for e in lb["entries"]:
    name = e.get("name", "")
    if "verve" in name.lower() or "logan" in name.lower() or "garage" in name.lower():
        print(f"Name: {name} | ID: {e.get('entry_id')}")
        print("Keys:", e.get("keys"))
        print("Secondary:", e.get("secondary_keys"))
        print("Content (first 400 chars):", e.get("content", "")[:400])
        print("-" * 50)
