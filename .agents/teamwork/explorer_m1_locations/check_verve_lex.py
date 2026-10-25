import json

with open("exports/Svartulfr_Export.json", "r", encoding="utf-8") as f:
    exp = json.load(f)

lex = exp.get("world_lexicon_entries", [])
lex_map = {e.get("id") or e.get("_id"): e for e in lex}

v_lex_ids = ['_YxGJRFDkjdVyeH1mJNM1T', '_UVX1RAqE8CWz8ywYkT4Fm', '_BRjbkk8JM3Jw1xyJGgzDH']
print("Checking The Verve's included lexicon entries:")
for vid in v_lex_ids:
    e = lex_map.get(vid)
    if e:
        print(f"ID: {vid} | Name: {e.get('name')} | Type: {e.get('type')}")
    else:
        print(f"ID: {vid} | NOT FOUND in export lexicon")
