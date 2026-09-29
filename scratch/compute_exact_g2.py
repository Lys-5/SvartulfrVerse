import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

with open('exports/entities/Svartulfr_Lexicon_NPCs_G3_A_Real.json', 'r', encoding='utf-8') as f:
    g3_data = json.load(f)

g3_ids = set(e['id'] for e in g3_data.get('entries', []))

chars = world_data.get('world_characters', [])
real_chars = [c for c in chars if len(c.get('long_summary') or '') > 100]

g1_names = [
    'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
    'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
    'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
    'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
    'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
]

g1_chars = []
g2_chars = []
g3_found = []

for c in real_chars:
    cid = c.get('id')
    dn = (c.get('display_name') or '').strip().lower()
    if dn in g1_names:
        g1_chars.append(c)
    elif cid in g3_ids:
        g3_found.append(c)
    else:
        g2_chars.append(c)

print(f"Total real characters in World: {len(real_chars)}")
print(f"G1 characters: {len(g1_chars)}")
print(f"G3-A characters found: {len(g3_found)}")
print(f"G2 characters: {len(g2_chars)}")

# Audit G2
print("\n--- G2 AUDIT BREAKDOWN ---")
is_global_false = [c for c in g2_chars if not c.get('is_global')]
final_inst_missing = [c for c in g2_chars if not c.get('final_instructions') or len(c.get('final_instructions').strip()) < 10]
birthdate_missing = [c for c in g2_chars if c.get('birthdate') is None]
timeline_missing = [c for c in g2_chars if c.get('start_timeline_position') is None]
outfits_missing = [c for c in g2_chars if len(c.get('outfits') or []) < 5]
attitudes_missing = [c for c in g2_chars if len(c.get('attitudes') or []) == 0]
speech_missing = [c for c in g2_chars if len(c.get('speech_examples') or []) < 5]

print(f"is_global == False: {len(is_global_false)} / {len(g2_chars)}")
print(f"final_instructions missing: {len(final_inst_missing)} / {len(g2_chars)}")
print(f"birthdate missing: {len(birthdate_missing)} / {len(g2_chars)}")
print(f"start_timeline_position missing: {len(timeline_missing)} / {len(g2_chars)}")
print(f"outfits < 5: {len(outfits_missing)} / {len(g2_chars)}")
print(f"attitudes == 0: {len(attitudes_missing)} / {len(g2_chars)}")
print(f"speech_examples < 5: {len(speech_missing)} / {len(g2_chars)}")

# Save list of G2
with open('scratch/g2_canonical_list.json', 'w', encoding='utf-8') as out:
    json.dump([{'id': c['id'], 'name': c.get('display_name')} for c in g2_chars], out, indent=2)
print("Saved G2 list to scratch/g2_canonical_list.json")
