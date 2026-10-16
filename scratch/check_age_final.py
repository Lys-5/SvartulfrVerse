import pathlib
import json

root = pathlib.Path('.')
for p in (root / 'FINAL').glob('*.json'):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    if '{{age}}' in txt:
        print(f"{p.name}: {txt.count('{{age}}')} matches")
