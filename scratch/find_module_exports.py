import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# Find module definition and exports
idx = code.find('.d(t,{')
if idx != -1:
    print("Module exports definition:")
    print(code[idx:idx+1500])
else:
    print("No .d(t,{ found, searching for export")
    matches = re.findall(r'(\w+\.\w+\s*=\s*p)', code)
    print("Matches:", matches)
