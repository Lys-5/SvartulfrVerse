import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Search for calls to `.in()` or `useCreate`
matches = list(re.finditer(r'\.in\(\)', content))
print(f"Total .in() matches: {len(matches)}")
for m in matches:
    idx = m.start()
    print("Match at", idx)
    print(content[max(0, idx-100):min(len(content), idx+400)])
    print("-" * 50)
