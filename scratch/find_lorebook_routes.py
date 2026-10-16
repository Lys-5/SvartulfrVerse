import pathlib
import re

for p in pathlib.Path('.').rglob('*.js'):
    if 'wv_chunk' in p.name:
        text = p.read_text(encoding='utf-8', errors='ignore')
        matches = set(re.findall(r'[\'"`]/api/([a-zA-Z0-9_\-/]+)[\'"`]', text))
        for m in sorted(matches):
            if 'lorebook' in m:
                print('  /api/' + m)
