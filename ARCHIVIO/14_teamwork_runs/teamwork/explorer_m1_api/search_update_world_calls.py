import urllib.request
import re

chunk_url = "https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js"
req = urllib.request.Request(chunk_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

matches = [m.start() for m in re.finditer(r'worldApi\.updateWorld\(', code)]
print(f"Matches for worldApi.updateWorld: {len(matches)}")
for pos in matches:
    print("--- pos", pos)
    print(code[max(0, pos-150):min(len(code), pos+300)])
