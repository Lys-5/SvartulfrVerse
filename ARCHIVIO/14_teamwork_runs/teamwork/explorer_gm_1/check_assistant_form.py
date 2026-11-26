import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/assistants/%5Bid%5D/page-cbe4530944bdffb9.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Find FormLabel texts
labels = re.findall(r'FormLabel,\{[^}]*children:"([^"]+)"', content)
print("FormLabels found:", labels)

# Also find all string literals that look like UI labels or field names
for kw in ['Title', 'Description', 'Kind', 'System Prompt', 'Final Instructions', 'Avatar', 'Visibility', 'Rating', 'Tags']:
    matches = [m.start() for m in re.finditer(re.escape(kw), content, re.I)]
    print(f"Label '{kw}': {len(matches)} occurrences")
    for idx in matches[:3]:
        print(f"  Snippet for {kw}:", content[max(0, idx-60):min(len(content), idx+140)])

# Find Zod schema or object validation
for m in re.finditer(r'z\.(?:object|string|enum)', content):
    idx = m.start()
    print("\nZod schema snippet:", content[max(0, idx-20):min(len(content), idx+300)])
