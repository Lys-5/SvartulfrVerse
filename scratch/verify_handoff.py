import json
import re
import glob

print("--- Running Verification 5.1 (Pillar 3) ---")
files = glob.glob('FINAL/*.json')
matches = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    found = re.findall(r'\{\{\s*age\s*\}\}', txt, re.I)
    if found:
        print(f'{f}: {len(found)} occurrences')
        matches += len(found)
print(f'Total {{age}} occurrences across FINAL/: {matches}')
assert matches == 0, 'Pillar 3 verification failed: residual {{age}} found!'
print('Pillar 3 PASS: Exactly 0 residual {{age}} macros in FINAL/')

print("\n--- Running Verification 5.2 (Pillar 4) ---")
prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))['entries']
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))['entries']
all_npcs = prim + sec
assert len(all_npcs) == 416, f'Expected 416 NPCs, got {len(all_npcs)}'

missing_av = [e for e in all_npcs if not (e.get('avatar') and e['avatar'].startswith('http'))]
assert len(missing_av) == 302, f'Expected 302 missing avatars, got {len(missing_av)}'

prim_missing = [e for e in prim if not (e.get('avatar') and e['avatar'].startswith('http'))]
sec_missing = [e for e in sec if not (e.get('avatar') and e['avatar'].startswith('http'))]
assert len(prim_missing) == 44, f'Expected 44 Primary missing, got {len(prim_missing)}'
assert len(sec_missing) == 258, f'Expected 258 Secondary missing, got {len(sec_missing)}'

non_cust_regex = [e for e in all_npcs if e.get('custom_avatar_regex') is not True]
assert len(non_cust_regex) == 0, f'Found {len(non_cust_regex)} non-true custom_avatar_regex'

non_line_1 = [e for e in all_npcs if e.get('lines_parsed') != 1]
assert len(non_line_1) == 0, f'Found {len(non_line_1)} lines_parsed != 1'

reg_pat = re.compile(r'^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$')
bad_reg = [e for e in all_npcs if not reg_pat.match(e.get('avatar_activation_regex', ''))]
assert len(bad_reg) == 0, f'Found {len(bad_reg)} bad avatar_activation_regex'

print('Pillar 4 PASS: 416 NPCs verified. 302 missing avatars (44 Prim, 258 Sec). 100% regex compliance.')
