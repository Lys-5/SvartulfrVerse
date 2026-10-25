import json

data = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
print('Keys in lorebook JSON:', list(data.keys()))
has_entries = 'entries' in data
has_lexicon = 'lexicon' in data
print(f'has entries: {has_entries}, len: {len(data.get("entries", [])) if has_entries else 0}')
print(f'has lexicon: {has_lexicon}, len: {len(data.get("lexicon", [])) if has_lexicon else 0}')

# Check Jasper (Vcj4h2TL4Usola2A4OOl6)
jasper = next(e for e in data['lexicon'] if e.get('entry_id') == 'Vcj4h2TL4Usola2A4OOl6')
print('\nJasper keys:', list(jasper.keys()))
print('Jasper entry:', json.dumps({k: jasper[k] for k in ['name', 'type', 'selective', 'secondary_keys', 'key_logic', 'keys', 'avatar', 'custom_avatar_regex', 'lines_parsed', 'avatar_activation_regex', 'npc_info'] if k in jasper}, indent=2))

# Check another standard NPC like index 0 or Finn
standard_npc = next(e for e in data['lexicon'] if e.get('type') == 'npc')
print('\nSample standard NPC:', json.dumps({k: standard_npc[k] for k in standard_npc if k != 'content'}, indent=2))

for eid in ['4NzXF4_0hYxmN7Idltzpw', 'alyssa_world_dossier_2b54a223']:
    item = next(e for e in data['lexicon'] if e.get('entry_id') == eid)
    print(f'\nCurrent {eid} ({item.get("name")}):', json.dumps({k: item[k] for k in item if k != 'content'}, indent=2))
