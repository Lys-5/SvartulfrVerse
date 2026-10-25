import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
d = json.loads((ROOT / 'FINAL' / 'Noah_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))
print("=== NOAH DESCRIPTION ===")
print(d['description'])
print("=== NOAH PERSONALITY ===")
print(d['personality'])
