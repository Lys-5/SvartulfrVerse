import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("================ ADVERSARIAL STRESS TEST ================")

all_files = sorted(glob.glob('FINAL/scenarios/*.json'))

checks = {
    "total_scenarios": len(all_files),
    "null_field_checks": 0,
    "pool_weight_checks": 0,
    "slot_key_regex_checks": 0,
    "greeting_order_checks": 0,
    "lorebook_order_checks": 0,
}

stress_errors = []

for f in all_files:
    d = json.load(open(f, encoding='utf-8'))
    
    # 1. Null fields
    for k in ['name', 'display_description', 'avatar', 'visibility', 'rating', 'scenario', 'slots', 'greetings', 'lorebook_ids']:
        if d.get(k) is None:
            stress_errors.append(f"{f}: field '{k}' is None")
        checks["null_field_checks"] += 1
        
    # 2. Pool weights & formats
    for s in d.get('slots', []):
        for p in s.get('pool', []):
            w = p.get('weight')
            cid = p.get('character_id')
            if not isinstance(w, int) or w <= 0:
                stress_errors.append(f"{f} slot '{s.get('key')}': invalid weight {w}")
            if not isinstance(cid, str) or not cid.startswith('_'):
                stress_errors.append(f"{f} slot '{s.get('key')}': invalid character_id {cid}")
            checks["pool_weight_checks"] += 1
            
    # 3. Key regex: Wyvern requires ^[a-zA-Z][a-zA-Z0-9_-]{0,63}$
    for s in d.get('slots', []):
        k = s.get('key', '')
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{0,63}$', k):
            stress_errors.append(f"{f} slot '{k}': failed Wyvern key regex")
        checks["slot_key_regex_checks"] += 1
        
    # 4. Greeting naming order: e.g. "01. ...", "02. ..."
    for idx, g in enumerate(d.get('greetings', [])):
        expected_prefix = f"{idx+1:02d}."
        if not g.get('name', '').startswith(expected_prefix):
            stress_errors.append(f"{f} greeting[{idx}] name '{g.get('name')}' does not start with '{expected_prefix}'")
        checks["greeting_order_checks"] += 1
        
    # 5. Lorebook list strict matching
    canonical_lbs = [
        "_gwwCxCfQ6PQaLEjAQVpJL",
        "_HfG7TeV6MJyj6bxMwxkpt",
        "_9zWTGqYJNJ4BCDMj8gfcD",
        "_EjXxkmPVhpCXg8xABpFkK",
        "_zwEqgEEzh12X6gHVmMKKC",
        "_Uht3Ckz44JBDrPnUHq7LV",
    ]
    if d.get('lorebook_ids') != canonical_lbs:
        stress_errors.append(f"{f} lorebook_ids list is not in exact canonical order: {d.get('lorebook_ids')}")
    checks["lorebook_order_checks"] += 1

print(f"Checks completed: {checks}")
print(f"Stress errors found: {len(stress_errors)}")
for err in stress_errors:
    print(f"  ❌ {err}")

if not stress_errors:
    print(">>> ADVERSARIAL STRESS TEST: ALL ASSUMPTIONS, EDGE CASES, AND INVARIANTS PASSED! <<<")
