import json
import pathlib
from collections import defaultdict

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

LOREBOOKS = [
    'Svartulfr_Lorebook_I.json',
    'Svartulfr_Lorebook_II.json',
    'Svartulfr_Lorebook_III.json',
    'Svartulfr_Location.json',
    'Svartulfr_NPC_Primary.json',
    'Svartulfr_NPC_Secondary.json',
]

entries_by_name = defaultdict(list)

for fname in LOREBOOKS:
    fpath = FINAL_DIR / fname
    data = json.loads(fpath.read_text(encoding='utf-8'))
    entries = data.get('lexicon') or data.get('entries') or []
    for idx, e in enumerate(entries):
        name = e.get('name', '').strip()
        if name:
            entries_by_name[name.lower()].append((fname, idx, name, e.get('type')))

print("=== VERIFICA DUPLICATI CROSS-LOREBOOK ===")
duplicates = {k: v for k, v in entries_by_name.items() if len(v) > 1}
print(f"Totale nomi duplicati trovati: {len(duplicates)}")
for k, v in sorted(duplicates.items()):
    print(f"\nNome: '{k}' appare in {len(v)} posti:")
    for fname, idx, orig_name, etype in v:
        print(f"  - {fname} [idx={idx}] -> '{orig_name}' (type={etype})")
