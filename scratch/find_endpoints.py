import pathlib
import re

text = pathlib.Path('scratch/inbox/wv_chunk.js').read_text(encoding='utf-8', errors='ignore')
matches = set(re.findall(r'/api/[a-zA-Z0-9_\-/]+', text))
for m in sorted(matches):
    if any(k in m for k in ['search', 'explore', 'characters']):
        print('  ' + m)
