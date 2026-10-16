import os, json, re

for fname in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    path = os.path.join('FINAL', fname)
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"\n==========================================")
    print(f"Testing {fname}")
    print(f"==========================================")
    
    strict_case_name_fails = []
    ignorecase_name_fails = []
    
    for idx, e in enumerate(d['lexicon']):
        name = e.get('name', '')
        rg = e.get('avatar_activation_regex', '')
        info = e.get('npc_info', {})
        
        # Test 1: Full name header
        pat_strict = re.compile(rg, re.M)
        pat_ignore = re.compile(rg, re.M | re.I)
        
        # Full name test
        if not pat_strict.search(f"{name}:"):
            strict_case_name_fails.append((name, f"{name}:", rg))
        if not pat_ignore.search(f"{name}:"):
            ignorecase_name_fails.append((name, f"{name}:", rg))

    print(f"Full name '{name}:' strict case fails: {len(strict_case_name_fails)}")
    print(f"Full name '{name}:' ignorecase fails: {len(ignorecase_name_fails)}")
    if strict_case_name_fails:
        for item in strict_case_name_fails:
            print(f"  Strict fail: NPC '{item[0]}' header '{item[1]}' regex: {item[2]}")
