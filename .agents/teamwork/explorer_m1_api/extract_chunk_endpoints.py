import urllib.request
import re

url = "https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

idx_p = code.find('p={')
# find all /worlds endpoints in chunk
endpoints = set(re.findall(r'/worlds[a-zA-Z0-9_\-\/]*', code))
print("All /worlds endpoints in chunk 77818:")
for ep in sorted(endpoints):
    print("  ", ep)

# Also let's check what a.BC is
idx_a = code.find('a=o(')
print("a=o snippet:", code[max(0, idx_a-50):min(len(code), idx_a+100)])
