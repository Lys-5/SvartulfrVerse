import json
import re

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

print("=== CHECKING ENTRIES VS LEXICON ARRAYS ===")
print("Primary top-level keys:", list(prim.keys()))
print("Primary entries len:", len(prim.get('entries', [])))
print("Primary lexicon len:", len(prim.get('lexicon', [])))

print("Secondary top-level keys:", list(sec.keys()))
print("Secondary entries len:", len(sec.get('entries', [])))
print("Secondary lexicon len:", len(sec.get('lexicon', [])))

# Check if entries and lexicon are identical
def compare_arrays(a1, a2, name):
    if len(a1) != len(a2):
        print(f"{name}: Different lengths! {len(a1)} vs {len(a2)}")
        return
    diffs = 0
    for idx, (e1, e2) in enumerate(zip(a1, a2)):
        id1 = e1.get('entry_id') or e1.get('id')
        id2 = e2.get('entry_id') or e2.get('id')
        if id1 != id2:
            diffs += 1
    print(f"{name}: Compared {len(a1)} items. ID mismatches: {diffs}")

compare_arrays(prim.get('entries', []), prim.get('lexicon', []), "Primary")
compare_arrays(sec.get('entries', []), sec.get('lexicon', []), "Secondary")

# Check BROAD_KEYS in labels and secondary_keys
BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

def check_broad_in_all_fields(data, name):
    lex = data.get('lexicon', [])
    in_keys = []
    in_sec_keys = []
    in_labels = []
    for e in lex:
        eid = e.get('entry_id')
        ename = e.get('name')
        for k in e.get('keys', []):
            if k.lower().strip() in BROAD_KEYS:
                in_keys.append((eid, ename, k))
        for k in e.get('secondary_keys', []):
            if k.lower().strip() in BROAD_KEYS:
                in_sec_keys.append((eid, ename, k))
        for l in e.get('labels', []):
            if l.lower().strip() in BROAD_KEYS:
                in_labels.append((eid, ename, l))
    print(f"\n{name} BROAD_KEYS check:")
    print(f"  In keys: {len(in_keys)}")
    print(f"  In secondary_keys: {len(in_sec_keys)}")
    print(f"  In labels: {len(in_labels)}")
    if in_labels:
        print(f"  Sample in labels: {in_labels[:5]}")

check_broad_in_all_fields(prim, "Primary")
check_broad_in_all_fields(sec, "Secondary")
