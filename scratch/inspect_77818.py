import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

print("Length of chunk:", len(code))

# Find worlds/limit and print context
pos = 0
while True:
    idx = code.find('worlds/limit', pos)
    if idx == -1:
        break
    print(f"--- Context around worlds/limit at {idx} ---")
    start = max(0, idx - 500)
    end = min(len(code), idx + 800)
    print(code[start:end])
    pos = idx + 1

# Also find all fetch / api calls in this chunk
print("\n--- All /api/ paths in this chunk ---")
api_paths = re.findall(r'(/api/[a-zA-Z0-9_\-/{}]*)', code)
for p in set(api_paths):
    print(" ", p)
