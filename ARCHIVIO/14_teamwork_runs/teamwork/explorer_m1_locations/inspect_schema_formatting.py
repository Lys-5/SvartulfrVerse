import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

off_ids = {
    "_p6WUaYcTJURrTXejecchk", "_RNU9Fx2pLD6PJ8LcKAdg6", "_J1B6d2DnNNyJhpnKWNcXz",
    "_94hRP4ywVYTHaUDDGfLqg", "_qe962a69a6PBbaHWCbP8r", "_BEnFGJPqBFJnTtrAHQQ9F",
    "_VMwRTPXdGTARktqnDLRTA", "_2rTUXXxAyYh8WYnGNtV2M"
}
active_188 = [l for l in snap_locs if (l.get("id") or l.get("_id")) not in off_ids]

print("=== CHECKING FIELD PRESENCE ACROSS 188 LOCATIONS ===")
field_counts = Counter()
for l in active_188:
    for k in l.keys():
        if l[k] not in [None, "", []]:
            field_counts[k] += 1

for k, c in field_counts.most_common():
    print(f"  {k}: {c} / 188 populated")

print("\n=== SAMPLE AMBIENT TEXT & CONTEXT DESCRIPTION ===")
sample_locs = ["The Verve", "Villa Douglas", "Basilica Library", "Camp Mystic", "Bloodmoon Longhouse"]
for l in active_188:
    name = l.get("name")
    if name in sample_locs:
        print(f"\n--- LOCATION: {name} [{l.get('id') or l.get('_id')}] ---")
        print("keys:", l.get("keys"))
        print("secondary_keys:", l.get("secondary_keys"))
        print("key_logic:", l.get("key_logic"))
        print("context_description (len %d):" % len(l.get("context_description", "")))
        print(l.get("context_description", "")[:300] + ("..." if len(l.get("context_description", "")) > 300 else ""))
        print("description (len %d):" % len(l.get("description", "")))
        print(l.get("description", "")[:300] + ("..." if len(l.get("description", "")) > 300 else ""))
        print("brief_context_description:", l.get("brief_context_description"))
        print("environment_config:", l.get("environment_config"))
        print("included_lexicon_entries:", l.get("included_lexicon_entries"))
        print("excluded_lexicon_entries:", l.get("excluded_lexicon_entries"))
        print("final_instructions:", l.get("final_instructions"))

print("\n=== CHECKING INCLUDED_LEXICON_ENTRIES ACROSS ALL 188 LOCATIONS ===")
locs_with_lex = [l for l in active_188 if l.get("included_lexicon_entries")]
print(f"Locations with included_lexicon_entries: {len(locs_with_lex)}")
for l in locs_with_lex:
    print(f"  - {l.get('name')}: {l.get('included_lexicon_entries')}")
