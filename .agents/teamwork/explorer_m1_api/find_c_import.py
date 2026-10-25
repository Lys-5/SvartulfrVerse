import urllib.request
import re

chunk_url = "https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js"
req = urllib.request.Request(chunk_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# Look near position 20000-23000 to see where c comes from
pos = 22856
sub = code[max(0, pos-3000):pos]
# find variable declarations like "c = ..." or imports like "(0, a.something)" or webpack require
print(sub[-1500:])
