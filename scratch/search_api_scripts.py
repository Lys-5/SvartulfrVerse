import pathlib
import re

for p in list(pathlib.Path('scripts').glob('*.py')) + list(pathlib.Path('scripts').glob('*.js')):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    matches = set(re.findall(r'/api/[a-zA-Z0-9_\-\/]+', txt))
    char_matches = [m for m in matches if 'char' in m]
    if char_matches:
        print(p.name, '->', char_matches)
