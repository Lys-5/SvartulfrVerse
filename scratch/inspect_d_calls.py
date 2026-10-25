import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# Find all occurrences of "params:"
for m in re.finditer(r'params:', code):
    idx = m.start()
    print(code[max(0, idx - 150):min(len(code), idx + 250)])
    print("-" * 50)
