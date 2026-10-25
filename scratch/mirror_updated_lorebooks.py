import shutil
import json

targets = [
    ('FINAL/Svartulfr_Lorebook_III.json', 'lorebooks/optimized/Svartulfr_Lorebook_III.json'),
    ('FINAL/Svartulfr_Location.json', 'lorebooks/optimized/Svartulfr_Location.json'),
    ('FINAL/Svartulfr_Lorebook_II.json', 'lorebooks/optimized/Svartulfr_Lorebook_II.json')
]

for src, dst in targets:
    shutil.copy2(src, dst)
    with open(dst, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"Mirrored {src} -> {dst} (entries: {len(d.get('entries', []))}, lexicon: {len(d.get('lexicon', []))})")
