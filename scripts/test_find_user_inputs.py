import urllib.request
import re

with open('scripts/search_chunks.py', 'r', encoding='utf-8') as f:
    text = f.read()

chunks = re.findall(r'"(/_next/static/chunks/[^"]+)"', text)
for c in chunks:
    try:
        url = 'https://app.wyvern.chat' + c
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=5).read().decode('utf-8', errors='ignore')
        if 'user_inputs' in data:
            print(f"Match in {c}:")
            for m in re.finditer(r'(.{0,150}user_inputs.{0,150})', data):
                print("   ", m.group(1).replace('\n', ' '))
    except Exception as e:
        pass
