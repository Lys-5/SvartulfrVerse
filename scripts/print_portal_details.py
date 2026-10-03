import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/portal_comprehensive_breakdown.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

for r in report:
    print(f"*** {r['id']} ({r['title']}) ***")
    for l in r['lines'][:10]:
        print('  ', l)
    for img in r['images']:
        print('   IMG:', img['alt'], img['url'])
    print()
