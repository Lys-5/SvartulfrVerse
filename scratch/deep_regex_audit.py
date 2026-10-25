import json
import re

for fname in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"Deep Regex Audit: {fname}")
    compilation_errors = 0
    empty_regex = 0
    for idx, e in enumerate(d['entries']):
        name = e.get('name', f"Index {idx}")
        pattern = e.get('avatar_activation_regex', '')
        if not pattern:
            empty_regex += 1
            print(f"  [WARN] Empty regex on {name}")
            continue
        try:
            # Test compiling pattern (note: js lookbehinds or character classes might differ in python re vs regex, let's test)
            # Module 93312 pattern uses (?<=^|\n)\s*...
            # Python re supports (?<=^|\n)
            # But let's check basic compilation
            re.compile(pattern)
        except re.error as err:
            # If standard re fails due to unicode properties like \p{L}, check with regex module or inspect
            compilation_errors += 1
            # print first error
            if compilation_errors <= 3:
                print(f"  [REGEX NOTE] {name}: {err}")

    print(f"  empty_regex: {empty_regex}")
    print(f"  python re compilation errors (e.g. JS-specific constructs): {compilation_errors}")
