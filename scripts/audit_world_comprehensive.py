import json
import re

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

world = d.get('world', {})
chars = d.get('world_characters', [])
scens = d.get('world_scenarios', [])
locs = d.get('world_locations', [])
envs = d.get('world_environments', [])
lex = d.get('world_lexicon_entries', [])

print("==================================================================")
print("1. WORLD SETTINGS & WORLD CLOCK AUDIT")
print("==================================================================")
world_age = world.get('world_age')
print(f"World Name: {world.get('name')}")
print(f"World Age: {world_age}")
print(f"Human Start Date: {world.get('human_start_date')}")
print(f"Calendar: {world.get('calendar')}")
print(f"Rating: {world.get('rating')}")
print(f"Tags count: {len(world.get('tags', []))}")
features = world.get('features', {}) or world.get('world_features', {})
print(f"Features: RPG={features.get('rpg_stats')}, Economy={features.get('currency_economy')}, Inventory={features.get('inventory_items')}")

print("\n==================================================================")
print("2. WORLD SCENARIOS AUDIT (11 Scenarios)")
print("==================================================================")
print(f"Total scenarios: {len(scens)}")
scen_em_dashes = 0
for idx, s in enumerate(sorted(scens, key=lambda x: x.get('insertion_point') or 0)):
    sid = s.get('id')
    name = s.get('name') or s.get('title')
    ins = s.get('insertion_point')
    scenes = s.get('premade_scenes', [])
    scene_text = scenes[0].get('scene_text', '') if scenes else ''
    first_line = scene_text.split('\n')[1] if len(scene_text.split('\n')) > 1 else ''
    
    # check em-dash
    full_text = f"{name} {s.get('tagline', '')} {s.get('description', '')} {scene_text}"
    has_dash = '—' in full_text or '–' in full_text
    if has_dash:
        scen_em_dashes += 1
    dash_flag = "[!] EM-DASH FOUND" if has_dash else "[OK]"
    print(f"  [{idx+1:02d}] Ins: {ins} | {dash_flag} | {name} ({first_line[:40]})")

print(f"Scenarios with em-dashes: {scen_em_dashes}")

print("\n==================================================================")
print("3. CHARACTER CARDS AUDIT (116 Characters)")
print("==================================================================")
print(f"Total characters: {len(chars)}")
empty_long_summary = []
missing_name = []
birthdate_mismatches = []
birthdate_future = []
duplicate_names = {}
em_dashes_chars = []
outfits_count = {}

for c in chars:
    cid = c.get('id')
    disp = (c.get('display_name') or c.get('name') or '').strip()
    if not disp:
        missing_name.append(cid)
    else:
        duplicate_names[disp] = duplicate_names.get(disp, 0) + 1
        
    ls = c.get('long_summary') or ''
    if not ls.strip():
        empty_long_summary.append((cid, disp))
        
    bdate = c.get('birthdate')
    stime = c.get('start_timeline_position')
    if bdate is not None and stime is not None and bdate != stime:
        birthdate_mismatches.append((cid, disp, bdate, stime))
    if bdate is not None and world_age is not None and bdate > world_age:
        birthdate_future.append((cid, disp, bdate))
        
    if '—' in ls or '–' in ls:
        em_dashes_chars.append((cid, disp))
        
    outfits = len(c.get('appearance_outfits', []))
    if outfits > 0:
        outfits_count[disp] = outfits

print(f"Missing names: {len(missing_name)}")
print(f"Empty long_summary: {len(empty_long_summary)}")
for cid, disp in empty_long_summary:
    print(f"  - Empty: [{cid}] {disp}")

dups = {k: v for k, v in duplicate_names.items() if v > 1}
print(f"Duplicate character names: {len(dups)}")
for k, v in dups.items():
    print(f"  - Duplicate '{k}': {v} instances")

print(f"Birthdate != start_timeline_position: {len(birthdate_mismatches)}")
for item in birthdate_mismatches[:5]:
    print(f"  - [{item[0]}] {item[1]}: birth={item[2]} != start={item[3]}")

print(f"Birthdate > world_age ({world_age}): {len(birthdate_future)}")
for item in birthdate_future:
    print(f"  - Future birthdate: [{item[0]}] {item[1]}: {item[2]}")

print(f"Characters with defined Outfits: {len(outfits_count)}")
print(f"Characters with em-dashes in long_summary: {len(em_dashes_chars)}")

print("\n==================================================================")
print("4. LOCATIONS AUDIT (171 Locations)")
print("==================================================================")
loc_empty_desc = []
loc_em_dash = []
loc_markdown = []

for l in locs:
    lid = l.get('id')
    lname = l.get('name') or ''
    ldesc = l.get('description') or ''
    if not ldesc.strip():
        loc_empty_desc.append((lid, lname))
    if '—' in ldesc or '–' in ldesc:
        loc_em_dash.append((lid, lname))
    if '**' in ldesc or '*' in ldesc:
        loc_markdown.append((lid, lname))

print(f"Locations with empty description: {len(loc_empty_desc)}")
print(f"Locations with em-dashes: {len(loc_em_dash)}")
print(f"Locations with asterisks/markdown (**): {len(loc_markdown)}")

print("\n==================================================================")
print("5. LEXICON ENTRIES AUDIT (532 Entries)")
print("==================================================================")
lex_types = {}
lex_no_keys = []
lex_em_dash = []
lex_placeholders = []

for e in lex:
    eid = e.get('id')
    ename = e.get('name') or e.get('title') or ''
    etype = e.get('type') or 'none'
    lex_types[etype] = lex_types.get(etype, 0) + 1
    
    keys = e.get('keys', [])
    if not keys:
        lex_no_keys.append((eid, ename))
        
    cnt = e.get('content') or ''
    if '—' in cnt or '–' in cnt:
        lex_em_dash.append((eid, ename))
        
    if 'placeholder' in cnt.lower() or 'in attesa di fonte' in cnt.lower():
        lex_placeholders.append((eid, ename))

print(f"Lexicon Entry Types distribution:")
for t, cnt in sorted(lex_types.items(), key=lambda x: -x[1]):
    print(f"  - {t:22}: {cnt} entries")

print(f"Entries without trigger keys: {len(lex_no_keys)}")
print(f"Entries with em-dashes: {len(lex_em_dash)}")
print(f"Placeholder entries awaiting source lore: {len(lex_placeholders)}")
