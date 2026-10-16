import pathlib
import json

root = pathlib.Path('.')
targets = ['FINAL', 'lorebooks']
found = []

for folder in targets:
    p_dir = root / folder
    if p_dir.exists():
        for p in p_dir.glob('**/*.json'):
            txt = p.read_text(encoding='utf-8', errors='ignore')
            if '{{age}}' in txt:
                found.append((str(p), txt.count('{{age}}')))

print(f"Total files in FINAL/lorebooks with {{{{age}}}}: {len(found)}")
for f, c in found:
    print(f"  {f}: {c}")
