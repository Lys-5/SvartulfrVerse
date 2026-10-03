import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))

w = data.get('world', {})
print("=== VERIFICA COMPLETA DEI 5 PUNTI TODO ===")
print("1. Rotte di Viaggio e Navigazione:")
routes = w.get('travel_routes', [])
print(f"   - Rotte attive collegate: {len(routes)}")
print(f"   - free_travel abilitato: {w.get('free_travel')}")

print("\n2. Marketplaces e Inventari:")
markets = [l for l in data['world_locations'] if l.get('marketplace_config', {}).get('enabled')]
print(f"   - Location commerciali attive: {len(markets)}")
for m in markets:
    cfg = m.get('marketplace_config', {})
    inv = cfg.get('inventory', [])
    print(f"     * {m['name']}: {len(inv)} item in stock, buy_rate={cfg.get('buy_rate')}")

print("\n3. Proprietà e Alloggi Affittabili:")
props = [l for l in data['world_locations'] if l.get('property_config', {}).get('enabled')]
print(f"   - Alloggi/dormitori configurati: {len(props)}")
for p in props:
    cfg = p.get('property_config', {})
    rent = cfg.get('rent_price', {})
    hours = cfg.get('rent_interval_hours')
    print(f"     * {p['name']}: {rent} ogni {hours}h (rentable={cfg.get('rentable')})")

print("\n4. Home Location dei Personaggi:")
homes = [c for c in data['world_characters'] if c.get('home_location_id')]
print(f"   - Personaggi con home_location_id formalizzata: {len(homes)} / {len(data['world_characters'])}")

print("\n5. Character Pools e Toggles is_global:")
pools = [l for l in data['world_locations'] if l.get('included_character_pool')]
print(f"   - Location con character pool dedicato: {len(pools)}")
globals_true = [c for c in data['world_characters'] if c.get('is_global')]
globals_false = [c for c in data['world_characters'] if not c.get('is_global')]
print(f"   - Personaggi con is_global=True (G1 Core Cast): {len(globals_true)}")
for c in globals_true:
    name = c.get('display_name') or c.get('first_name')
    print(f"     * [G1] {name}")
print(f"   - Personaggi con is_global=False (NPC Locali / Pool): {len(globals_false)}")
