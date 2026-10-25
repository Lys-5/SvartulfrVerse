import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# Search for WorldCard or world list components
for term in ['WorldCard', 'worldCard', 'WorldItem', 'WorldsPage', 'WorldList', 'MyWorlds', 'my-worlds', 'user-worlds']:
    for m in re.finditer(re.escape(term), code, re.IGNORECASE):
        idx = m.start()
        print(f"Match '{term}' at {idx}:")
        print(code[max(0, idx - 150):min(len(code), idx + 250)])
        print("-" * 50)
