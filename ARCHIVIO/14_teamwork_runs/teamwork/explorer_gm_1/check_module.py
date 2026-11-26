import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Search for the module definition enclosing `Assistant config created successfully`
pos = content.find('Assistant config created successfully')
# find module start before pos
mod_start = content.rfind('function(', 0, pos - 500)
mod_end = content.find('function(', pos + 500)
print("Module start:", mod_start, "Module end:", mod_end)
print(content[mod_start:mod_start+300])
print("...")
print(content[pos-100:pos+800])
