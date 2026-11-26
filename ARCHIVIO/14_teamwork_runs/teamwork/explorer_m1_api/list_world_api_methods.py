import urllib.request
import re

url = "https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# Let's inspect a.BC
idx_bc = code.find('a.BC')
print("a.BC snippet:", code[max(0, idx_bc-100):min(len(code), idx_bc+100)])

# Find all keys in p
idx_p = code.find('p={')
end_p = code.find('};', idx_p)
if end_p == -1: end_p = idx_p + 25000
p_code = code[idx_p:end_p]

# Match method_name:
methods = re.findall(r'([a-zA-Z0-9_]+)\s*:\s*(?:function|\([^)]*\)\s*=>)', p_code)
print(f"Total methods in worldApi: {len(methods)}")
for m in methods:
    print("  ", m)
