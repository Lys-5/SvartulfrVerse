import urllib.request
import re
import sys

with open('scripts/search_chunks.py', 'r', encoding='utf-8') as f:
    text = f.read()

chunks = re.findall(r'"(/_next/static/chunks/[^"]+)"', text)
print(f"Checking {len(chunks)} chunks...")
for c in chunks:
    try:
        url = 'https://app.wyvern.chat' + c
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=5).read().decode('utf-8', errors='ignore')
        if 'property_config' in data or 'rent_price' in data or 'rentable' in data:
            print(f"Match in {c}:")
            for m in re.finditer(r'(.{0,100}(?:property_config|rent_price|rentable).{0,100})', data):
                print("   ", m.group(1).replace('\n', ' '))
    except Exception as e:
        pass
