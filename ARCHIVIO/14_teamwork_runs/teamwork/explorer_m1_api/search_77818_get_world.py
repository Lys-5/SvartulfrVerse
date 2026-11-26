import urllib.request
import re

url = "https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

matches = [m.start() for m in re.finditer(r'getWorld', code)]
print(f"Matches for getWorld in 77818: {len(matches)}")
for pos in matches:
    print("--- pos", pos)
    print(code[max(0, pos-100):min(len(code), pos+200)])
