import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

# 1. Inspect 95148-b515b69ac26da978.js around npc_info
f1 = chunk_dir / '95148-b515b69ac26da978.js'
if f1.exists():
    c1 = f1.read_text(encoding='utf-8')
    print("=== 95148-b515b69ac26da978.js ===")
    for m in re.finditer(r'npc_info', c1):
        start = max(0, m.start() - 300)
        end = min(len(c1), m.end() + 600)
        print("--- MATCH at", m.start(), "---")
        print(c1[start:end])
        print("\n")

# 2. Inspect 66353-44918b7fd11ff8ae.js around npc_info, gallery, ignored_characters
f2 = chunk_dir / '66353-44918b7fd11ff8ae.js'
if f2.exists():
    c2 = f2.read_text(encoding='utf-8')
    print("=== 66353-44918b7fd11ff8ae.js ===")
    for term in ['npc_info', 'ignored_characters', 'galleryImages']:
        for m in re.finditer(re.escape(term), c2):
            start = max(0, m.start() - 300)
            end = min(len(c2), m.end() + 600)
            print(f"--- MATCH for {term} at {m.start()} ---")
            print(c2[start:end])
            print("\n")
            break
