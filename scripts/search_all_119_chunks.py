import urllib.request
import re
import sys

with open('scripts/fetch_edit_page.py', 'r', encoding='utf-8') as f:
    pass

import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
chunks = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
chunks = [c for c in chunks if 'chunks' in c]

targets = ['timeline-events', 'gedcom', 'item_config', 'moon_phase', 'moon_cycle', 'user_inputs']
print(f"Scanning {len(chunks)} chunks for {targets}...")

for c in chunks:
    try:
        url = 'https://app.wyvern.chat' + c
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=5).read().decode('utf-8', errors='ignore')
        for t in targets:
            if t in data:
                print(f"Found '{t}' in {c}:")
                for m in re.finditer(rf'(.{{0,120}}{t}.{{0,120}})', data):
                    print("   ", m.group(1).replace('\n', ' '))
    except Exception as e:
        pass
