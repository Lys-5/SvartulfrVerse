import re
import json

with open('scratch/campmystic_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Look for character json or script tags containing character data
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f'Total script tags: {len(scripts)}')

for i, s in enumerate(scripts):
    if 'campmystic' in s or 'Camp Mystic' in s or 'Shadowgamer' in s:
        print(f'Script {i} contains keywords, len: {len(s)}')
        # check if it contains JSON
        m = re.findall(r'(\{"id":"[^"]+",.*?"name":"[^"]+".*?\})', s)
        if m:
            print(f'  Found {len(m)} json objects in script {i}')
            for item in m[:3]:
                print('    Preview:', item[:200])

# Also check for window.__INITIAL_STATE__ or similar
for line in html.split('\n'):
    if any(k in line for k in ['"character":', '"scenario":', '"description":', 'campmystic']):
        if len(line) < 500:
            print('Line:', line.strip())
