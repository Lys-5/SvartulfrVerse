import json

print("=== CHECK 4: NATIVE SUPPRESSION ARRAYS AUDIT ===")

primary_file = 'FINAL/Svartulfr_NPC_Primary.json'
secondary_file = 'FINAL/Svartulfr_NPC_Secondary.json'

with open(primary_file, 'r', encoding='utf-8') as f:
    primary = json.load(f)

with open(secondary_file, 'r', encoding='utf-8') as f:
    secondary = json.load(f)

# Required suppression mappings
suppression_checks = [
    {
        'lorebook': 'Primary',
        'id': 'alyssa_world_dossier_2b54a223',
        'name': 'Alyssa Hvit Douglas Bloodmoon',
        'expected_characters': ['_6exg3yPfe2eCDK4hTftkh'],
        'expected_personas': ['persona_1786335754946'],
        'expected_selective': False
    },
    {
        'lorebook': 'Primary',
        'id': 'Vcj4h2TL4Usola2A4OOl6',
        'name': 'Jasper Svartr Douglas Bloodmoon',
        'expected_characters': ['_t4J9aQNJM36cUKAP4wB4U'],
        'expected_personas': ['1792155173728'],
        'expected_selective': False
    },
    {
        'lorebook': 'Primary',
        'id': '4NzXF4_0hYxmN7Idltzpw',
        'name': 'Scarlett Rose',
        'expected_characters': ['_qXgBMbFYJfc84hbLHhe92'],
        'expected_personas': [],
        'expected_selective': False
    },
    {
        'lorebook': 'Primary',
        'id': 'ijy8vrlphNv19-p-gbYuY',
        'name': 'Sierra Cruz',
        'expected_characters': ['_pnrXbkWqcgmFAf3meRWFY'],
        'expected_personas': [],
        'expected_selective': False
    },
    {
        'lorebook': 'Primary',
        'id': 'YCxAqNoShpefVvk0_Pc7i',
        'name': "Russell 'Russ' Sinclair",
        'expected_characters': ['_wn6DkCcg3Xqa2Xpx9ttnT'],
        'expected_personas': [],
        'expected_selective': False
    },
    {
        'lorebook': 'Primary',
        'id': 'ekdQjq63xP7HtNuaPQJQE',
        'name': 'Stanley Davies Jr.',
        'expected_characters': ['_Xd3NhKnRJByMTtdb6PjxJ'],
        'expected_personas': [],
        'expected_selective': False
    },
    {
        'lorebook': 'Primary',
        'id': 'RM6rcwv8MlY1XWaCTQp0M',
        'name': 'Jared Thompson',
        'expected_characters': ['_xJVPtBLL3dxy69RLKL9X9'],
        'expected_personas': [],
        'expected_selective': False
    },
    {
        'lorebook': 'Secondary',
        'id': 'h-ttmlgJYeRXqyDvQjSX7',
        'name': 'Edric Douglas',
        'expected_characters': ['_TbRM3EdxDjHFgqztTbCpL'],
        'expected_personas': [],
        'expected_selective': False
    }
]

all_passed = True

def audit_lorebook_entries(lb_data, lb_name, expected_list):
    global all_passed
    entries_map = {e.get('id') or e.get('entry_id'): e for e in lb_data.get('entries', [])}
    lexicon_map = {e.get('id') or e.get('entry_id'): e for e in lb_data.get('lexicon', [])}
    
    print(f"\nAuditing Lorebook: {lb_name}")
    print(f"  Total entries: {len(entries_map)} | Total lexicon: {len(lexicon_map)}")
    
    # Verify entries and lexicon match in count
    if len(entries_map) != len(lexicon_map):
        print(f"  ERROR: Count mismatch between entries ({len(entries_map)}) and lexicon ({len(lexicon_map)})")
        all_passed = False
        
    for item in expected_list:
        eid = item['id']
        name = item['name']
        
        e_ent = entries_map.get(eid)
        e_lex = lexicon_map.get(eid)
        
        if not e_ent or not e_lex:
            print(f"  ERROR: Entry {name} (ID: {eid}) missing in {lb_name}")
            all_passed = False
            continue
            
        for loc_name, e in [('entries', e_ent), ('lexicon', e_lex)]:
            ig_chars = e.get('ignored_characters')
            ig_pers = e.get('ignored_personas')
            selective = e.get('selective', False)
            e_type = e.get('type')
            
            if ig_chars != item['expected_characters']:
                print(f"  ERROR: {name} in {loc_name} ignored_characters mismatch! Got {ig_chars}, expected {item['expected_characters']}")
                all_passed = False
            if ig_pers != item['expected_personas']:
                print(f"  ERROR: {name} in {loc_name} ignored_personas mismatch! Got {ig_pers}, expected {item['expected_personas']}")
                all_passed = False
            if selective != item['expected_selective']:
                print(f"  ERROR: {name} in {loc_name} selective mismatch! Got {selective}, expected {item['expected_selective']}")
                all_passed = False
            if e_type != 'npc':
                print(f"  ERROR: {name} in {loc_name} type mismatch! Got {e_type}, expected 'npc'")
                all_passed = False
                
        print(f"  PASSED: {name} (ID: {eid}) — verified in entries and lexicon: ignored_characters={item['expected_characters']}, ignored_personas={item['expected_personas']}, selective={item['expected_selective']}")

primary_targets = [x for x in suppression_checks if x['lorebook'] == 'Primary']
secondary_targets = [x for x in suppression_checks if x['lorebook'] == 'Secondary']

audit_lorebook_entries(primary, 'FINAL/Svartulfr_NPC_Primary.json', primary_targets)
audit_lorebook_entries(secondary, 'FINAL/Svartulfr_NPC_Secondary.json', secondary_targets)

# Also check optimized directory mirroring
with open('lorebooks/optimized/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    opt_primary = json.load(f)
with open('lorebooks/optimized/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    opt_secondary = json.load(f)

audit_lorebook_entries(opt_primary, 'lorebooks/optimized/Svartulfr_NPC_Primary.json', primary_targets)
audit_lorebook_entries(opt_secondary, 'lorebooks/optimized/Svartulfr_NPC_Secondary.json', secondary_targets)

print(f"\nFinal Check 4 Result: {'ALL NATIVE SUPPRESSION CHECKS PASSED' if all_passed else 'INTEGRITY VIOLATION FOUND'}")
