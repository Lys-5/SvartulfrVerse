import json
import glob
import re

EXPECTED_LOREBOOKS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV"
]

files = glob.glob('FINAL/scenarios/*.json')
print(f"Total scenario files to verify: {len(files)}")

all_passed = True

for fpath in files:
    print("\n" + "="*60)
    print(f"VERIFYING: {fpath}")
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 1. Visibility
    vis = data.get('visibility')
    if vis != 'private':
        print(f"  [FAIL] visibility is '{vis}', expected 'private'")
        all_passed = False
    else:
        print(f"  [PASS] visibility: {vis}")
        
    # 2. Lorebook IDs
    lb_ids = data.get('lorebook_ids', [])
    missing_lbs = [lb for lb in EXPECTED_LOREBOOKS if lb not in lb_ids]
    if missing_lbs:
        print(f"  [FAIL] Missing lorebook IDs: {missing_lbs}")
        all_passed = False
    else:
        print(f"  [PASS] All 6 standalone lorebooks attached ({len(lb_ids)})")
        
    # 3. Slots
    slots = data.get('slots', [])
    print(f"  Slots count: {len(slots)}")
    slot_keys = set()
    for s in slots:
        k = s.get('key')
        lbl = s.get('label')
        pool = s.get('pool', [])
        unavail = s.get('unavailable_count')
        if not re.match(r'^[a-z0-9_]+$', k or ''):
            print(f"    [FAIL] Slot key '{k}' invalid regex")
            all_passed = False
        if unavail != 0:
            print(f"    [FAIL] Slot '{k}' unavailable_count is {unavail}, expected 0")
            all_passed = False
        slot_keys.add(k)
        print(f"    - Slot '{k}' ({lbl}): {len(pool)} candidates in pool")
        
    # 4. Greetings
    greetings = data.get('greetings', [])
    print(f"  Greetings count: {len(greetings)}")
    for i, g in enumerate(greetings):
        gname = g.get('name') or g.get('title')
        msgs = g.get('messages', [])
        gcontent = g.get('content', '')
        if not msgs:
            print(f"    [FAIL] Greeting {i+1} has no messages")
            all_passed = False
        elif gcontent != msgs[0].get('content'):
            print(f"    [WARN] Greeting {i+1} content != messages[0].content")
        for m in msgs:
            sp = m.get('speaker_slot')
            if sp and sp not in slot_keys:
                print(f"    [FAIL] Message speaker_slot '{sp}' not in slots")
                all_passed = False
        print(f"    - Greeting {i+1}: '{gname}' ({len(msgs)} messages)")
        
    # 5. Em-dash check
    raw_text = json.dumps(data, ensure_ascii=False)
    if '—' in raw_text:
        count = raw_text.count('—')
        print(f"  [FAIL] Found {count} em-dash ('—') characters!")
        all_passed = False
    else:
        print(f"  [PASS] Zero em-dash ('—') characters")

print("\n" + "="*60)
if all_passed:
    print("ALL 6 SCENARIOS PASSED VERIFICATION!")
else:
    print("SOME CHECKS FAILED! INSPECT OUTPUT ABOVE.")
