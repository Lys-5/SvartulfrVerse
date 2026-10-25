import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary = json.load(f)

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    secondary = json.load(f)

print("=== CHECKING APPROVED CARDS IN PRIMARY ===")
approved_primary_cards = {
    'Erik': '_QPea6g4Q1QfeYCVHCLMPR',
    'Malachia': '_RDfz7XzTpM23LpPALVXHM',
    'Noah': '_zFLUjV8aVxQRAfQxGcAcY',
    'Logan': '_T8Ywcr9FEqNf9JxbK6eHP',
    'Wulfnic': '_HEQQbbRFwKdG8QE2Fh1z1',
    'Mackenzie': '_zn24784jfcchQ7EwCyAnm'
}

for name, card_id in approved_primary_cards.items():
    found = False
    for e in primary['entries']:
        if card_id in e.get('ignored_characters', []):
            found = True
            print(f"Found {name}: entry_id={e.get('entry_id')}, name={e.get('name')}, ignored_characters={e.get('ignored_characters')}")
            break
    if not found:
        print(f"WARNING: Card ID {card_id} for {name} not found in any ignored_characters in Primary!")

print("\n=== CHECKING EDRIC IN SECONDARY ===")
edric_card_id = '_TbRM3EdxDjHFgqztTbCpL'
found_edric = False
for e in secondary['entries']:
    if edric_card_id in e.get('ignored_characters', []):
        found_edric = True
        print(f"Found Edric: entry_id={e.get('entry_id')}, name={e.get('name')}, ignored_characters={e.get('ignored_characters')}")
        break
if not found_edric:
    print(f"WARNING: Edric card ID {edric_card_id} not found in Secondary!")

print("\n=== BROAD KEYS & AGE MACROS CHECK (PRIMARY & SECONDARY) ===")
BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

def scan_lorebook(lb_name, lb_data):
    broad_count = 0
    age_count = 0
    em_dash_count = 0
    npc_count = 0
    non_npc_with_npc_info = 0
    npc_missing_avatar = 0
    for i, e in enumerate(lb_data['entries']):
        keys = [k.lower() for k in e.get('keys', [])]
        for bk in BROAD_KEYS:
            if bk in keys:
                print(f"[{lb_name}] Entry {i} ({e.get('name')}) has broad key: {bk}")
                broad_count += 1
        content = e.get('content', '')
        if '{{age}}' in content:
            print(f"[{lb_name}] Entry {i} ({e.get('name')}) has {{age}} macro!")
            age_count += 1
        if '—' in content:
            em_dash_count += 1
        if e.get('type') == 'npc':
            npc_count += 1
            if not e.get('avatar'):
                print(f"[{lb_name}] NPC {i} ({e.get('name')}) missing avatar!")
                npc_missing_avatar += 1
        else:
            if e.get('npc_info') or e.get('custom_avatar_regex') or e.get('lines_parsed'):
                print(f"[{lb_name}] Non-NPC {i} ({e.get('name')}) has spurious NPC info!")
                non_npc_with_npc_info += 1
    print(f"[{lb_name}] Summary: NPCs={npc_count}, BroadKeys={broad_count}, AgeMacros={age_count}, EmDashes={em_dash_count}, SpuriousNonNPC={non_npc_with_npc_info}, NPCMissingAvatar={npc_missing_avatar}")

scan_lorebook("PRIMARY", primary)
scan_lorebook("SECONDARY", secondary)
