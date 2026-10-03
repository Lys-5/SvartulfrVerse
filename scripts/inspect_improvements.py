import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
w = data.get('world', {})

print("=== ANALISI POTENZIALI MIGLIORAMENTI ===")

# 1. Parent locations hierarchy
locs = data.get('world_locations', [])
sub_locs = [l for l in locs if ':' in l['name'] or ' - ' in l['name']]
sub_with_parent = [l for l in sub_locs if l.get('parent_location')]
print(f"1. Gerarchia Parent-Child Locations:")
print(f"   - Sub-location identificate (es. 'Villa Douglas: ...'): {len(sub_locs)}")
print(f"   - Sub-location con parent_location impostato: {len(sub_with_parent)} / {len(sub_locs)}")
if len(sub_with_parent) < len(sub_locs):
    print("   -> OPPORTUNITÀ: Collegare le stanze interne alla location madre (es. tutte le ali di Villa Douglas alla villa principale)!")

# 2. Timeline events
tl = data.get('world_timeline_events', [])
print(f"\n2. Timeline Events:")
print(f"   - Eventi storici registrati su Wyvern: {len(tl)}")
if len(tl) == 0:
    print("   -> OPPORTUNITÀ: Popolare gli eventi cardine della timeline ufficiale del Lore (Consacrazione 1005, Carta Coloniale 1666, Nascita Gemelli/Morte Nixara 2005, Incidente Gamma-7 2019, Present Day 2024)!")

# 3. GEDCOM Family Trees
gt = data.get('world_gedcom_trees', [])
print(f"\n3. GEDCOM Family Trees:")
print(f"   - Alberi genealogici caricati: {len(gt)}")
if len(gt) == 0:
    print("   -> OPPORTUNITÀ: Caricare l'albero genealogico ufficiale della dinastia Douglas / Bloodmoon per la visualizzazione grafica nell'UI!")

# 4. Item configurations in Lexicon
lex = data.get('world_lexicon_entries', [])
items = [e for e in lex if e.get('type') == 'item']
items_with_cfg = [e for e in items if e.get('item_config')]
print(f"\n4. Lexicon Items & Equipaggiamento:")
print(f"   - Voci di tipo item: {len(items)}")
print(f"   - Item con item_config (rarità, consumo, valore, slot): {len(items_with_cfg)}")

# 5. Attitudes network
chars = data.get('world_characters', [])
chars_with_att = [c for c in chars if c.get('attitudes')]
print(f"\n5. Attitudes Network (Relazioni interpersonali):")
print(f"   - Personaggi con attitudes configurate: {len(chars_with_att)} / {len(chars)}")
if len(chars_with_att) < len(chars):
    print("   -> OPPORTUNITÀ: Estendere la rete delle Attitudes ai fratelli Douglas (Malachia, Noah, Jasper, Edric), ai Firstborn, al clan Darkfire e alla band Grave Mistake!")

# 6. Scenari & User Inputs
scens = data.get('world_scenarios', [])
print(f"\n6. Scenari e User Inputs / Guided Setup:")
print(f"   - Scenari totali: {len(scens)}")
scens_with_inputs = [s for s in scens if s.get('user_inputs')]
print(f"   - Scenari con Guided Setup / User Inputs (scelta item, fazione, background): {len(scens_with_inputs)} / {len(scens)}")
for s in scens:
    inputs = s.get('user_inputs', [])
    start_loc = s.get('starting_location')
    print(f"     * {s['name'][:35]:35}: start_loc={bool(start_loc)}, inputs={len(inputs)}")

# 7. World Features & Calendario / Luna
print(f"\n7. World Features & Calendario:")
print(f"   - world_features: {w.get('world_features')}")
cal = w.get('calendar', {})
print(f"   - Calendario: mesi={len(cal.get('months', []))}, giorni_settimana={len(cal.get('days_of_the_week', []))}")
print(f"   - Fasi lunari / Moon cycles: {cal.get('moon_phases') or cal.get('moons')}")
