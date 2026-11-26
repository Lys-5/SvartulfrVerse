import glob
import re

for p in glob.glob(r'e:\repository\SvartulfrVerse\scratch\*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
        if 'lorebook_ids' in t:
            print(f"=== FOUND 'lorebook_ids' in {p} ===")
            for m in re.finditer(r'lorebook_ids', t):
                start = max(0, m.start() - 200)
                end = min(len(t), m.end() + 350)
                print(f"--- Pos {m.start()} ---")
                print(t[start:end])
                print()
