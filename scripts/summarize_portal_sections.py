import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/modernfantasy_portal_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"=== LISTA SEZIONI ESTRATTE ({len(data['characters'])}) ===")
for sec_id, sec_data in data['characters'].items():
    imgs = sec_data.get('images', [])
    text_preview = sec_data.get('text', '').replace('\n', ' ')[:120]
    print(f"\nID: {sec_id} | Immagini: {len(imgs)}")
    print(f"  Anteprima: {text_preview}...")
    for img in imgs:
        print(f"    - [{img['alt']}] {img['url']}")
