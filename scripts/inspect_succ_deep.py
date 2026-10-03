import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

fname = 'exports/portal_succ_extracted.json'
with open(fname, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=======================================================")
print("             ISPEZIONE PORTALE SUCC                    ")
print("=======================================================")
for sec_id, s in data['sections'].items():
    print(f"\n--- SEZIONE: {sec_id} ({s['title']}) | Img: {len(s['images'])} ---")
    for l in s['lines'][:30]:
        print("  ", l)
    for img in s['images']:
        print(f"    * [{img['alt']}] {img['url']}")
