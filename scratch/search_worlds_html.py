import urllib.request
import re
import json

req = urllib.request.Request('https://app.wyvern.chat/worlds', headers={
    'User-Agent': 'Mozilla/5.0',
    'Authorization': f'Bearer {open("scratch/wyvern_token.txt").read().strip()}'
})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# find world IDs in html
wids = re.findall(r'(_[A-Za-z0-9_-]{21})', html)
print("World IDs found in /worlds HTML:", set(wids))

# find any mentions of Svartulfr
for m in re.finditer(r'Svart[uú]lfr', html, re.IGNORECASE):
    s = max(0, m.start() - 100)
    e = min(len(html), m.end() + 200)
    print("Match context:", html[s:e])
    print("-" * 50)
