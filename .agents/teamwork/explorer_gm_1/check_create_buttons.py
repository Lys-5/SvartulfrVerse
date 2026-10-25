import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Search for "Create" buttons in /mine
for m in re.finditer(r'Create (?:New|Assistant|Preset|Character|Scenario|Lorebook)', content):
    idx = m.start()
    print("Match at", idx, ":", content[max(0, idx-100):min(len(content), idx+200)])
