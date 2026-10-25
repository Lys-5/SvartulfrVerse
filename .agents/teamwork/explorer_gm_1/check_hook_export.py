import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Find the exported name of that hook (e.g. `f` in module exports)
pos = content.find('Assistant config created successfully')
print("Position:", pos)
# Let's inspect 1000 characters around it to see what function or module exports it
snippet = content[max(0, pos-400):min(len(content), pos+1500)]
print("Snippet around create:\n", snippet)
