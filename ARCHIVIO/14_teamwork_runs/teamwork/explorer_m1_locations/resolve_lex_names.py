import json

with open("ARCHIVIO/05_Snapshots_and_Extractions/raw_db_dumps/raw_lexicon.json", "r", encoding="utf-8") as f:
    raw_lex = json.load(f)

lex_lookup = {e.get("id") or e.get("_id"): e.get("name") for e in raw_lex}

with open("scratch/backup_consolidated_snapshot/world_locations.json", "r", encoding="utf-8") as f:
    snap_locs = json.load(f)

off_ids = {
    "_p6WUaYcTJURrTXejecchk", "_RNU9Fx2pLD6PJ8LcKAdg6", "_J1B6d2DnNNyJhpnKWNcXz",
    "_94hRP4ywVYTHaUDDGfLqg", "_qe962a69a6PBbaHWCbP8r", "_BEnFGJPqBFJnTtrAHQQ9F",
    "_VMwRTPXdGTARktqnDLRTA", "_2rTUXXxAyYh8WYnGNtV2M"
}
active_188 = [l for l in snap_locs if (l.get("id") or l.get("_id")) not in off_ids]

for l in active_188:
    inc = l.get("included_lexicon_entries")
    if inc:
        print(f"Location: {l.get('name')} [{l.get('id') or l.get('_id')}]")
        for x in inc:
            name = lex_lookup.get(x, "UNKNOWN")
            print(f"    - {x}: {name}")
