import json
from collections import Counter

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))

print("==================================================================")
print("             DEEP SYSTEM SCAN — WORLD SVARTULFR                   ")
print("==================================================================")

w = data['world']
chars = data['world_characters']
locs = data['world_locations']
envs = data['world_environments']
lex = data['world_lexicon_entries']
scens = data['world_scenarios']
maps = data['world_maps']
eras = data['world_eras']
parties = data['world_parties']
timeline = data['world_timeline_events']
trees = data['world_gedcom_trees']

print(f"World: {w.get('name')} (ID: {w.get('id')})")
print(f"World Clock: {w.get('world_age')} | Free Travel: {w.get('free_travel')}")
print(f"Entities: Chars={len(chars)}, Locs={len(locs)}, Envs={len(envs)}, Lex={len(lex)}, Scens={len(scens)}, Maps={len(maps)}, Eras={len(eras)}, Parties={len(parties)}, Events={len(timeline)}, Trees={len(trees)}")

print("\n--- 1. ANALISI WORLD SETTINGS & FEATURES ---")
print(f"World Features: {w.get('world_features')}")
print(f"World Tags ({len(w.get('tags', []))}): {w.get('tags')}")
print(f"Community Tags: {w.get('community_tags')}")
print(f"Avatar: {bool(w.get('avatar'))} | Banner: {bool(w.get('banner'))}")
print(f"Travel Routes: {len(w.get('travel_routes', []))}")
print(f"World Prompt length: {len(w.get('world_prompt', ''))} chars")

print("\n--- 2. ANALISI ENVIRONMENTS (2) ---")
for env in envs:
    print(f"  * {env['name']} (ID: {env['id']}): desc={bool(env.get('description'))}, tags={env.get('tags')}")

print("\n--- 3. ANALISI PARTIES (1) ---")
for p in parties:
    p_chars = p.get('party_members', []) or p.get('characters', [])
    print(f"  * Party '{p.get('name')}' (ID: {p.get('id')}): {len(p_chars)} membri")

print("\n--- 4. ANALISI ERAS (8) vs TIMELINE EVENTS (7) ---")
for era in eras:
    print(f"  * Era: {era.get('name')} | Start: {era.get('start_position')} | End: {era.get('end_position')}")

print("\n--- 5. ANALISI MAPS (4) & PINS ---")
for m in maps:
    pins = m.get('pins', [])
    print(f"  * Map: {m.get('name')} | Pins: {len(pins)} | Image: {bool(m.get('image'))}")

print("\n--- 6. ANALISI CREATURES NEL LEXICON ---")
creatures = [e for e in lex if e.get('type') == 'creature']
print(f"Voci di tipo 'creature': {len(creatures)}")
for c in creatures[:10]:
    cfg = c.get('creature_config')
    print(f"  * {c.get('name')}: creature_config={bool(cfg)}")

print("\n--- 7. ANALISI MEMORIE & INTIMACY PROFILES ---")
memories = [e for e in lex if e.get('type') == 'memory']
mem_with_char = [e for e in memories if e.get('attached_world_character_id')]
print(f"Voci di tipo 'memory': {len(memories)}")
print(f"Memorie con attached_world_character_id: {len(mem_with_char)} / {len(memories)}")

print("\n--- 8. ANALISI SCENARI & PREMADE SCENES ---")
for s in scens:
    scenes = s.get('premade_scenes', [])
    instructions = bool(s.get('scene_instructions'))
    print(f"  * {s.get('name')[:35]:35}: premade_scenes={len(scenes)}, instructions={instructions}")

print("\n--- 9. ANALISI AVATAR PERSONAGGI ---")
chars_no_avatar = [c for c in chars if not c.get('avatar')]
print(f"Personaggi senza avatar principale: {len(chars_no_avatar)}")

print("\n==================================================================")
