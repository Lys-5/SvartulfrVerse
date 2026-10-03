import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
locs = d.get('world_locations', [])
lexicon = d.get('world_lexicon_entries', [])

loc_names = {l.get('name', '').lower().strip(): l for l in locs}

print("=== CHECKING LOCATIONS DUPLICATED AS LEXICON ENTRIES ===")
duplicated_loc_in_lexicon = []

for item in lexicon:
    lname = item.get('name', '').lower().strip()
    if lname in loc_names:
        l_obj = loc_names[lname]
        duplicated_loc_in_lexicon.append((item.get('name'), item.get('id'), l_obj.get('id')))

print(f"Total direct name matches between Lexicon and Location: {len(duplicated_loc_in_lexicon)}")
for name, lex_id, loc_id in duplicated_loc_in_lexicon:
    print(f"  * \"{name}\": Lexicon ID: {lex_id} <--> Location ID: {loc_id}")
