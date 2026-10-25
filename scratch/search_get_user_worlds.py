import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# find all calls to getUserWorlds
matches = [m.start() for m in re.finditer(r'getUserWorlds', code)]
print(f"Found {len(matches)} occurrences of getUserWorlds in 77818")

for idx in matches:
    print(code[max(0, idx - 150):min(len(code), idx + 250)])
    print("-" * 50)
