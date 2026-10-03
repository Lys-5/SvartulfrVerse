import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/modernfantasy_portal_raw.json', 'r', encoding='utf-8') as f:
    portal_data = json.load(f)

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

chars_by_name = {}
for c in world_data['world_characters']:
    name = c.get('name') or c.get('display_name') or ''
    chars_by_name[name.lower()] = c

lex_by_name = {}
for l in world_data['world_lexicon_entries']:
    name = l.get('name') or ''
    lex_by_name[name.lower()] = l

report = []

for sec_id, sec in portal_data['characters'].items():
    text = sec['text']
    images = sec['images']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    title = lines[0] if lines else sec_id
    
    # Extract details
    info = {
        'id': sec_id,
        'title': title,
        'lines': lines,
        'images': images,
        'full_text': text
    }
    report.append(info)

# Write a comprehensive breakdown
output_path = 'exports/portal_comprehensive_breakdown.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Salvato breakdown completo in {output_path} ({len(report)} sezioni)")

for r in report:
    imgs_count = len(r['images'])
    print(f"\n=======================================================")
    print(f"SEZIONE: {r['id']} (Titolo: {r['title']}) | Immagini: {imgs_count}")
    print(f"-------------------------------------------------------")
    for l in r['lines'][:15]:
        print("  ", l)
    if imgs_count > 0:
        print("  --- IMMAGINI / AVATAR DISPONIBILI ---")
        for img in r['images']:
            print(f"    * [{img['alt']}] {img['url']}")
