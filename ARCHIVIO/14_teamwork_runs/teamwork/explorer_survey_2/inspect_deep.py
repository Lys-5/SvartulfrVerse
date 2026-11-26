import json

# 1. Inspect 'none' type entry in NPC Secondary
with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    npc_sec = json.load(f)

for idx, e in enumerate(npc_sec.get('entries', [])):
    if e.get('type') != 'npc':
        print(f"NPC Secondary non-npc entry: #{idx} id={e.get('entry_id') or e.get('id')} name={e.get('name')} type={e.get('type')}")

# 2. Inspect Magic entries in Lorebook I
with open('FINAL/Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
    lore1 = json.load(f)

print("\n--- Lorebook I Magic Entries ---")
for idx, e in enumerate(lore1.get('entries', [])):
    name = e.get('name', '')
    if 'magic' in name.lower() or 'necroman' in name.lower() or 'run' in name.lower() or 'catalizzat' in name.lower() or 'abiss' in name.lower() or 'abyss' in name.lower():
        print(f"Lore I #{idx} id={e.get('entry_id') or e.get('id')} name=\"{name}\" type={e.get('type')} keys={e.get('keys')[:3]}")

# 3. Inspect Item/Cylinder/Crystal entries in Lorebook II
with open('FINAL/Svartulfr_Lorebook_II.json', 'r', encoding='utf-8') as f:
    lore2 = json.load(f)

print("\n--- Lorebook II Item/Artifact Entries ---")
for idx, e in enumerate(lore2.get('entries', [])):
    name = e.get('name', '')
    t = e.get('type', '')
    if t in ['item', 'concept', 'lore/concept'] and any(w in name.lower() for w in ['core', 'crystal', 'cristall', 'cylinder', 'cilindr', 'dungeon', 'rift', 'squarcio', 'runic', 'runa']):
        print(f"Lore II #{idx} id={e.get('entry_id') or e.get('id')} name=\"{name}\" type={t} keys={e.get('keys')[:3]}")

# 4. Inspect all 46 entries in Lorebook III
with open('FINAL/Svartulfr_Lorebook_III.json', 'r', encoding='utf-8') as f:
    lore3 = json.load(f)

print(f"\n--- Lorebook III All {len(lore3.get('entries', []))} Entries ---")
for idx, e in enumerate(lore3.get('entries', [])):
    print(f"Lore III #{idx} id={e.get('entry_id') or e.get('id')} name=\"{e.get('name')}\" type={e.get('type')} keys={e.get('keys')[:2]}")
