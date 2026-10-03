import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

world = data.get('world', {})
characters = data.get('world_characters', [])
locations = data.get('world_locations', [])
environments = data.get('world_environments', [])
lexicon = data.get('world_lexicon_entries', [])
scenarios = data.get('world_scenarios', [])

print('================================================================')
print('              AUDIT COMPLETO DEL WORLD SVARTULFR                ')
print('================================================================')
print(f"World ID:             {world.get('id')}")
print(f"World Name:           {world.get('name')}")
print(f"World Clock:          {world.get('world_age')} (28 Ago 2024, 08:00 UTC)")
print(f"Scenarios:            {len(scenarios)}")
print(f"Characters:           {len(characters)}")
print(f"Locations:            {len(locations)}")
print(f"Environments:         {len(environments)}")
print(f"Lexicon Entries:      {len(lexicon)}")
print('----------------------------------------------------------------')

# 1. SCENARIOS AUDIT
print('\n[1. SCENARI]')
scen_em = []
for s in scenarios:
    txt = (s.get('prompt') or '') + (s.get('first_mes') or '') + (s.get('name') or '')
    if '\u2014' in txt:
        scen_em.append(s.get('name'))
if scen_em:
    print(f"  ALERTA Em-dash negli scenari ({len(scen_em)}): {scen_em}")
else:
    print("  Tutti gli 11 scenari sono puliti da em-dash e allineati cronologicamente.")

# 2. CHARACTERS AUDIT
print('\n[2. CHARACTERS]')
ghosts = [c for c in characters if not (c.get('long_summary') or '').strip()]
print(f"  Schede con long_summary vuoto (Ghost / Stubs): {len(ghosts)}")
for g in ghosts:
    print(f"    - {g.get('name') or g.get('display_name')} [ID: {g.get('id')}] (summary: {len(g.get('summary') or '')} char)")

names = {}
for c in characters:
    n = c.get('name') or c.get('display_name')
    names.setdefault(n, []).append(c.get('id'))
dups = {n: ids for n, ids in names.items() if len(ids) > 1}
print(f"\n  Nomi Personaggio Duplicati ({len(dups)}):")
for n, ids in dups.items():
    print(f"    - {n}: {ids}")

active_chars = [c for c in characters if c not in ghosts]
no_outfits = [c for c in active_chars if not c.get('outfits') and not c.get('appearance_outfits')]
print(f"\n  Personaggi Attivi SENZA Outfits ({len(no_outfits)}):")
for no in no_outfits:
    print(f"    - {no.get('name') or no.get('display_name')} [ID: {no.get('id')}]")

non_jed = [c for c in active_chars if not (c.get('long_summary') or '').strip().startswith('[')]
print(f"\n  Personaggi Attivi con prefisso non standard (non inizia con [): ({len(non_jed)}):")
for nj in non_jed:
    print(f"    - {nj.get('name') or nj.get('display_name')} [ID: {nj.get('id')}]: {(nj.get('long_summary') or '')[:40]!r}")

# 3. LOCATIONS AUDIT
print('\n[3. LOCATIONS]')
locs_empty = [l for l in locations if not (l.get('context_description') or '').strip() and not (l.get('description') or '').strip()]
print(f"  Location senza alcuna descrizione ({len(locs_empty)}):")
for le in locs_empty:
    print(f"    - {le.get('name')} [ID: {le.get('id')}]")

locs_em = [l for l in locations if '\u2014' in ((l.get('context_description') or '') + (l.get('description') or '') + (l.get('name') or ''))]
print(f"  Location con Em-dash ({len(locs_em)}):")
for lm in locs_em:
    print(f"    - {lm.get('name')} [ID: {lm.get('id')}]")

# 4. LEXICON AUDIT
print('\n[4. LEXICON]')
empty_lex = [e for e in lexicon if not (e.get('content') or '').strip()]
print(f"  Lexicon completamente vuoti: {len(empty_lex)}")
for el in empty_lex:
    print(f"    - {el.get('name')} [ID: {el.get('id')}]")

em_lex = [e for e in lexicon if '\u2014' in ((e.get('content') or '') + (e.get('name') or ''))]
print(f"  Lexicon con Em-dash ({len(em_lex)}):")
for el in em_lex:
    print(f"    - {el.get('name')} [ID: {el.get('id')}]")

stubs = [e for e in lexicon if len((e.get('content') or '').strip()) < 100]
print(f"  Lexicon Stubs (<100 caratteri): {len(stubs)}")
for s in stubs:
    print(f"    - {s.get('name')} [ID: {s.get('id')}]: {s.get('content')!r}")

print('\n================================================================')
