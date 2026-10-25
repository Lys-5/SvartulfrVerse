import urllib.request
import re

chunk_url = "https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js"
req = urllib.request.Request(chunk_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

keywords = ['createWorld', 'updateWorld', 'saveWorld', 'world_features', 'calendar', 'useWorld', 'world_age']
for kw in keywords:
    matches = [m.start() for m in re.finditer(re.escape(kw), code)]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for pos in matches[:3]:
        snippet = code[max(0, pos-100):min(len(code), pos+150)]
        print(f"   [pos {pos}]: {snippet}\n")
