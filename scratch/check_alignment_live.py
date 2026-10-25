import json
import requests

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
print('Status mine:', r.status_code)
live_chars = {}
if r.status_code == 200:
    chars = r.json().get('characters', [])
    print(f'Total active characters on Wyvern: {len(chars)}')
    for c in chars:
        cid = c.get('id')
        name = c.get('name')
        desc = c.get('description', '')
        avatar = c.get('avatar', '')
        live_chars[cid] = {'name': name, 'desc': desc, 'desc_len': len(desc), 'avatar': avatar}
        print(f"  {name:30} | ID: {cid} | Desc len: {len(desc)} | Avatar: {avatar}")
else:
    print('Failed:', r.text[:200])

# Check Lorebook Primary
r_lb_prim = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
print('Status LB Primary:', r_lb_prim.status_code)
lb_prim = r_lb_prim.json() if r_lb_prim.status_code == 200 else {}

# Check Lorebook Secondary
r_lb_sec = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
print('Status LB Secondary:', r_lb_sec.status_code)
lb_sec = r_lb_sec.json() if r_lb_sec.status_code == 200 else {}

target_cards = {
    'Edric Douglas': ('_TbRM3EdxDjHFgqztTbCpL', lb_sec, 'Secondary'),
    'Erik Ulfr Douglas': ('_QPea6g4Q1QfeYCVHCLMPR', lb_prim, 'Primary'),
    'Jasper Svartr Douglas Bloodmoon': ('_t4J9aQNJM36cUKAP4wB4U', lb_prim, 'Primary'),
    'Logan Járn Douglas': ('_T8Ywcr9FEqNf9JxbK6eHP', lb_prim, 'Primary'),
    'Mackenzie Sanchez-Rogers': ('_zn24784jfcchQ7EwCyAnm', lb_prim, 'Primary'),
    'Malachia Björn Douglas Bloodmoon': ('_RDfz7XzTpM23LpPALVXHM', lb_prim, 'Primary'),
    'Noah Loki Douglas Bloodmoon': ('_zFLUjV8aVxQRAfQxGcAcY', lb_prim, 'Primary'),
    'Wulfnic Bóleygr Bloodmoon': ('_HEQQbbRFwKdG8QE2Fh1z1', lb_prim, 'Primary'),
}

print('\n' + '='*80)
print('ALIGNMENT CHECK: LIVE CARDS vs LIVE LOREBOOKS (TEXTUAL, VISUAL, EXCLUSIONS)')
print('='*80)

all_desc_ok = True
all_avatar_ok = True
all_ignored_ok = True

for full_name, (cid, lb_data, lb_name) in target_cards.items():
    live_card = live_chars.get(cid)
    card_desc = live_card.get('desc', '') if live_card else ''
    card_avatar = live_card.get('avatar', '') if live_card else ''
    
    # find entry in lb
    found_entry = None
    for e in lb_data.get('lexicon', []):
        if cid in e.get('ignored_characters', []):
            found_entry = e
            break
        if e.get('name') == full_name:
            found_entry = e
            break
            
    if not found_entry:
        print(f"FAILED: Entry for {full_name} ({cid}) not found in {lb_name}!")
        all_desc_ok = False
        continue
        
    entry_desc = found_entry.get('content', '')
    entry_avatar = found_entry.get('avatar', '')
    ignored_chars = found_entry.get('ignored_characters', [])
    ignored_pers = found_entry.get('ignored_personas', [])
    
    desc_match = (card_desc == entry_desc)
    avatar_match = (card_avatar == entry_avatar and bool(card_avatar))
    id_in_ignored = (cid in ignored_chars)
    
    if not desc_match:
        all_desc_ok = False
    if not avatar_match:
        all_avatar_ok = False
    if not id_in_ignored:
        all_ignored_ok = False
    
    print(f"Character: {full_name:32}")
    print(f"  Live Card Exists: {bool(live_card)} (Len: {len(card_desc)})")
    print(f"  Lorebook Entry:   {found_entry.get('name')} in {lb_name} (Len: {len(entry_desc)})")
    print(f"  Desc Match:       {desc_match} (Diff: {len(entry_desc) - len(card_desc)})")
    print(f"  Avatar Match:     {avatar_match} -> {card_avatar}")
    print(f"  ignored_chars OK: {id_in_ignored} -> {ignored_chars}")
    print(f"  ignored_personas: {ignored_pers}")
    print('-'*80)

print(f"\nFINAL VERIFICATION SUMMARY:")
print(f"  Textual Parity (8/8):     {all_desc_ok}")
print(f"  Visual Parity (8/8):      {all_avatar_ok}")
print(f"  Exclusion Parity (8/8):   {all_ignored_ok}")

assert all_desc_ok, "Textual parity failure detected!"
assert all_avatar_ok, "Visual parity (avatar) failure detected!"
assert all_ignored_ok, "Exclusion parity (ignored_characters) failure detected!"
print("\n>>> ALL 8 CHARACTERS CERTIFIED 100% IN FULL TRIPARTITE PARITY <<<")
