import json
import difflib

# Load FINAL/Svartulfr_NPC_Primary.json
primary_path = 'FINAL/Svartulfr_NPC_Primary.json'
with open(primary_path, 'r', encoding='utf-8') as f:
    primary = json.load(f)

# The lorebook might have entries under 'entries' and/or 'lexicon'
entries_by_id = {}
for e in primary.get('entries', []):
    entries_by_id[e.get('id') or e.get('entry_id')] = e

lexicon_by_id = {}
for e in primary.get('lexicon', []):
    lexicon_by_id[e.get('id') or e.get('entry_id')] = e

targets = [
    {
        'name': 'Scarlett Rose',
        'id': '4NzXF4_0hYxmN7Idltzpw',
        'card_file': 'ARCHIVIO/cards_legacy/Scarlett_Rose_card.json'
    },
    {
        'name': 'Sierra Cruz',
        'id': 'ijy8vrlphNv19-p-gbYuY',
        'card_file': 'ARCHIVIO/cards_legacy/Sierra_Cruz_card.json'
    },
    {
        'name': "Russell 'Russ' Sinclair",
        'id': 'YCxAqNoShpefVvk0_Pc7i',
        'card_file': 'ARCHIVIO/cards_legacy/Russ_card.json'
    },
    {
        'name': 'Stanley Davies Jr.',
        'id': 'ekdQjq63xP7HtNuaPQJQE',
        'card_file': 'ARCHIVIO/cards_legacy/Stan_Davies_Jr_card.json'
    },
    {
        'name': 'Jared Thompson',
        'id': 'RM6rcwv8MlY1XWaCTQp0M',
        'card_file': 'ARCHIVIO/cards_legacy/Jared_Thompson_card.json'
    },
    {
        'name': 'Alyssa Hvit Douglas Bloodmoon',
        'id': 'alyssa_world_dossier_2b54a223',
        'card_file': 'ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json'
    }
]

print("=== CHECK 2: DESCRIPTION FIDELITY AUDIT ===")
all_match = True

for t in targets:
    t_id = t['id']
    t_name = t['name']
    card_path = t['card_file']
    
    with open(card_path, 'r', encoding='utf-8') as f:
        card_data = json.load(f)
    
    card_desc = card_data.get('data', {}).get('description') or card_data.get('description', '')
    
    e_entry = entries_by_id.get(t_id)
    e_lexicon = lexicon_by_id.get(t_id)
    
    if not e_entry:
        print(f"FAILED: {t_name} (ID: {t_id}) not found in 'entries' of {primary_path}")
        all_match = False
        continue
    if not e_lexicon:
        print(f"FAILED: {t_name} (ID: {t_id}) not found in 'lexicon' of {primary_path}")
        all_match = False
        continue
        
    entry_desc = e_entry.get('description') or e_entry.get('content', '')
    lex_desc = e_lexicon.get('description') or e_lexicon.get('content', '')
    
    # Check entries vs lexicon synchronization
    if entry_desc != lex_desc:
        print(f"FAILED: {t_name} description mismatch between 'entries' and 'lexicon' ({len(entry_desc)} vs {len(lex_desc)})")
        all_match = False
        continue
        
    # Check card_desc vs entry_desc
    diff = list(difflib.unified_diff(
        card_desc.splitlines(keepends=True),
        entry_desc.splitlines(keepends=True),
        fromfile='source_card',
        tofile='lorebook_entry'
    ))
    
    match = (card_desc == entry_desc)
    print(f"\nTarget: {t_name}")
    print(f"  ID: {t_id}")
    print(f"  Card desc length: {len(card_desc)}")
    print(f"  Lorebook entry desc length: {len(entry_desc)}")
    print(f"  Exact character-for-character match: {match}")
    
    if not match:
        all_match = False
        print(f"  Diff lines count: {len(diff)}")
        print("  Diff preview:")
        for line in diff[:10]:
            print("   ", line.strip())
    else:
        print(f"  First 80 chars: {entry_desc[:80]!r}")
        print(f"  Last 80 chars:  {entry_desc[-80:]!r}")

print(f"\nFinal Check 2 Result: {'ALL MATCH 100%' if all_match else 'INTEGRITY VIOLATION / MISMATCH FOUND'}")
