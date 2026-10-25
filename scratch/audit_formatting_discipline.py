import json
import re
from collections import Counter

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

p_lex = prim.get('lexicon', [])
s_lex = sec.get('lexicon', [])

all_entries = [("Primary", e) for e in p_lex] + [("Secondary", e) for e in s_lex]

BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

em_dash_matches = []
asterisk_matches = []
age_macro_matches = []
broad_key_matches = []
recursion_status = Counter()
recursion_not_true = []

for origin, e in all_entries:
    eid = e.get('entry_id', '')
    name = e.get('name', '')
    content = e.get('content', '')
    keys = e.get('keys', [])
    efr = e.get('exclude_from_recursion')
    
    recursion_status[str(efr)] += 1
    if efr is not True:
        recursion_not_true.append((origin, eid, name, efr))
        
    # Em-dashes
    if '—' in content:
        cnt = content.count('—')
        # find examples
        lines_with_em = [line.strip() for line in content.split('\n') if '—' in line]
        em_dash_matches.append((origin, eid, name, cnt, lines_with_em[:2]))
        
    # Asterisks: check for markdown formatting (*italic* or **bold** or bullet * )
    if '*' in content:
        cnt = content.count('*')
        lines_with_ast = [line.strip() for line in content.split('\n') if '*' in line]
        asterisk_matches.append((origin, eid, name, cnt, lines_with_ast[:3]))
        
    # {{age}} macros in content, name, keys
    for field_name, field_val in [('content', content), ('name', name)]:
        if '{{age' in field_val.lower():
            age_macro_matches.append((origin, eid, name, field_name, field_val))
    for k in keys:
        if '{{age' in k.lower():
            age_macro_matches.append((origin, eid, name, 'keys', k))
            
    # BROAD_KEYS in keys
    matched_bks = [k for k in keys if k.lower().strip() in BROAD_KEYS]
    if matched_bks:
        broad_key_matches.append((origin, eid, name, matched_bks, keys))

print("==================================================")
print("FORMATTING DISCIPLINE AUDIT RESULTS")
print("==================================================")
print(f"\n1. EM-DASHES ('—'):")
print(f"Total entries containing em-dash: {len(em_dash_matches)}")
total_em_dashes = sum(x[3] for x in em_dash_matches)
print(f"Total em-dash occurrences: {total_em_dashes}")
if em_dash_matches:
    print("Entries with em-dash:")
    for origin, eid, name, cnt, samples in em_dash_matches:
        print(f"  [{origin}] {eid} ({name}): {cnt} em-dashes")
        for s in samples:
            print(f"      sample: {repr(s[:100])}")

print(f"\n2. ASTERISKS ('*'):")
print(f"Total entries containing asterisks: {len(asterisk_matches)}")
total_asterisks = sum(x[3] for x in asterisk_matches)
print(f"Total asterisk occurrences: {total_asterisks}")
if asterisk_matches:
    print(f"Sample entries with asterisks (first 10):")
    for origin, eid, name, cnt, samples in asterisk_matches[:10]:
        print(f"  [{origin}] {eid} ({name}): {cnt} asterisks")
        for s in samples:
            print(f"      sample: {repr(s[:100])}")

print(f"\n3. RESIDUAL {{{{age}}}} MACROS:")
print(f"Total occurrences: {len(age_macro_matches)}")
for x in age_macro_matches:
    print(f"  {x}")

print(f"\n4. BROAD_KEYS MATCHES:")
print(f"Total entries with broad keys: {len(broad_key_matches)}")
for origin, eid, name, matched, all_k in broad_key_matches:
    print(f"  [{origin}] {eid} ({name}): matched={matched} | all_keys={all_k}")

print(f"\n5. EXCLUDE_FROM_RECURSION STATUS:")
print(f"Status distribution: {dict(recursion_status)}")
print(f"Total where exclude_from_recursion is NOT True: {len(recursion_not_true)} / {len(all_entries)}")
