import urllib.request
import re

url = "https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

targets = ['createEnvironment:', 'createLocation:', 'createLexiconEntry:', 'bulkCreateLexiconEntries:', 'createWorldCharacter:', 'createScenario:']

for t in targets:
    idx = code.find(t)
    print(f"=== {t} ===")
    if idx != -1:
        print(code[idx:idx+400])
    else:
        print("Not found")
