import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
text = f.read_text(encoding='utf-8')

# Search for regex generation patterns or functions that take npc_info
# Look for matches of first_name or middle_names in 66353-44918b7fd11ff8ae.js
matches = [m.start() for m in re.finditer(r'npc_info', text)]
print(f"Total npc_info occurrences in 66353-44918b7fd11ff8ae.js: {len(matches)}")

for pos in matches:
    snippet = text[max(0, pos-150):min(len(text), pos+300)]
    print(f"Pos {pos}:")
    print(' '.join(snippet.split()))
    print("-" * 50)
