import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

idx = code.find('p={executeLua:')
# Look after the end of p
end_p = code.find('};', idx)
print("After p:")
print(code[end_p:end_p+500])
