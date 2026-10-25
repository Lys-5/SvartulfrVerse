import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

idx = code.find('p={executeLua:')
end = code.find('export', idx)
snippet = code[idx:idx+8000]

# find all method names (key: or key(
keys = re.findall(r'([a-zA-Z0-9_]+):(?:function|\()', snippet)
print("Keys in p:", keys)
