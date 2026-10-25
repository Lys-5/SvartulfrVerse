import glob
import re

for p in glob.glob('scratch/[0-9]*.js'):
    txt = open(p, encoding='utf-8', errors='ignore').read()
    # search for /api/
    api_calls = set(re.findall(r'[\'"`]/api/[^\'"`]+[\'"`]', txt))
    print(f"=== {p} (len {len(txt)}) ===")
    for a in sorted(api_calls):
        if any(term in a.lower() for term in ['world', 'mine', 'character', 'scenario']):
            print("  ", a)
