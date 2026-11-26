import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Search for where create or createMutation is called
for kw in ['useCreateAssistant', 'createAssistant', 'Create Assistant', 'create_assistant', 'New Assistant', 'Add Assistant']:
    for m in re.finditer(re.escape(kw), content, re.I):
        idx = m.start()
        print(f"[{kw}] ->", content[max(0, idx-100):min(len(content), idx+200)])

# Find where /simple-assistant-config POST is invoked by looking for `.create(`
for m in re.finditer(r'\.create\(', content):
    idx = m.start()
    print("[.create(] ->", content[max(0, idx-100):min(len(content), idx+200)])
