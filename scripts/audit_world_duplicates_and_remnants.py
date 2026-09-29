import json
import re

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('=== SCANNING CHARACTERS ===')
chars = d.get('world_characters', [])
name_map = {}
for c in chars:
    name = (c.get('display_name') or c.get('name') or '').strip().lower()
    name_map.setdefault(name, []).append(c)
for name, clist in name_map.items():
    if len(clist) > 1:
        print(f'Duplicate Character: "{name}" -> {[c.get("id") for c in clist]}')

print('\n=== SCANNING LOCATIONS ===')
locs = d.get('world_locations', [])
loc_map = {}
for l in locs:
    name = (l.get('name') or '').strip().lower()
    loc_map.setdefault(name, []).append(l)
for name, llist in loc_map.items():
    if len(llist) > 1:
        print(f'Duplicate Location: "{name}" -> {[l.get("id") for l in llist]}')

print('\n=== SCANNING SCENARIOS ===')
scens = d.get('world_scenarios', [])
scen_map = {}
for s in scens:
    name = (s.get('name') or '').strip().lower()
    scen_map.setdefault(name, []).append(s)
for name, slist in scen_map.items():
    if len(slist) > 1:
        print(f'Duplicate Scenario: "{name}" -> {[s.get("id") for s in slist]}')

print('\n=== SCANNING LEXICON FOR DUPLICATES ===')
lex = d.get('world_lexicon_entries', [])
lex_map = {}
for lx in lex:
    name = (lx.get('name') or '').strip().lower()
    lex_map.setdefault(name, []).append(lx)
for name, lxlist in lex_map.items():
    if len(lxlist) > 1:
        print(f'Duplicate Lexicon: "{name}" -> {[x.get("id") for x in lxlist]}')

print('\n=== SCANNING LEXICON FOR RAW TAGS (<...>) ===')
raw_tag_entries = []
for lx in lex:
    content = lx.get('content') or ''
    m = re.findall(r'<[a-zA-Z0-9_-]+>', content)
    if m:
        raw_tag_entries.append((lx.get('id'), lx.get('name'), m[:3]))
print(f'Found {len(raw_tag_entries)} Lexicon entries with raw XML tags:')
for lid, lname, tags in raw_tag_entries:
    print(f'  - {lname} ({lid}): tags {tags}')
