import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/portal_comprehensive_breakdown.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

sec06 = [r for r in report if r['id'] == 'section06-section'][0]
print("=== SECTION 06 - ALL LINES ===")
for l in sec06['lines']:
    print(l)

print("\n=== SECTION 06 - ALL IMAGES ===")
for img in sec06['images']:
    print(f"[{img['alt']}] {img['url']}")
