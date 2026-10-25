import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Let's search where simple-assistant-config form schema is defined
for m in re.finditer(r'title:.*description:', content):
    idx = m.start()
    print("Schema snippet:", content[max(0, idx-50):min(len(content), idx+300)])

# Let's search for lorebook attachments across the chunk
for m in re.finditer(r'simple.*assistant.*lorebook|lorebook.*assistant|assistant.*lorebook', content, re.I):
    idx = m.start()
    print("Lorebook assistant match:", content[max(0, idx-100):min(len(content), idx+200)])
