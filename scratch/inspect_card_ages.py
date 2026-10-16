import pathlib
import json

root = pathlib.Path('.')
for fname in [
    'Elizabeth_Duskwood_card.json',
    'Jared_Thompson_card.json',
    'Kaladin_Nargathon_card.json',
    'Mackenzie_Sanchez_Rogers_card.json',
    'Magnus_Douglas_III_card.json',
    'Zeera_Darkfire_card.json'
]:
    p = root / 'FINAL' / fname
    txt = p.read_text(encoding='utf-8')
    lines = txt.splitlines()
    print(f"=== {fname} ===")
    for i, line in enumerate(lines, 1):
        if '{{age}}' in line:
            print(f"  Line {i}: {line[:120]}")
