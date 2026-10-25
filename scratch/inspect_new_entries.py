import json

live_npc = json.load(open('scratch/live_raw_npc_secondary.json', encoding='utf-8'))['lexicon']
local_npc = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))['lexicon']

local_npc_names = set(e.get('name') for e in local_npc)
new_npc = [e for e in live_npc if e.get('name') not in local_npc_names]

lines = []
lines.append(f'Live NPC Secondary total: {len(live_npc)}')
lines.append(f'Local NPC Secondary total: {len(local_npc)}')
lines.append(f'New NPCs in live ({len(new_npc)}):')
for idx, e in enumerate(new_npc):
    keys_str = ', '.join(e.get('keys', []))
    lines.append(f"{idx+1:3d}. {e.get('name')} | Type: {e.get('type')} | Keys: [{keys_str}]")

live_loc = json.load(open('scratch/live_raw_location.json', encoding='utf-8'))['lexicon']
local_loc = json.load(open('FINAL/Svartulfr_Location.json', encoding='utf-8'))['lexicon']

local_loc_names = set(e.get('name') for e in local_loc)
new_loc = [e for e in live_loc if e.get('name') not in local_loc_names]

lines.append(f'\nLive Location total: {len(live_loc)}')
lines.append(f'Local Location total: {len(local_loc)}')
lines.append(f'New Locations in live ({len(new_loc)}):')
for idx, e in enumerate(new_loc):
    keys_str = ', '.join(e.get('keys', []))
    lines.append(f"{idx+1:3d}. {e.get('name')} | Type: {e.get('type')} | Keys: [{keys_str}]")

with open('scratch/new_entries_summary.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Written to scratch/new_entries_summary.txt')
