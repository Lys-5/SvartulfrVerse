import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

for m in re.finditer(r'Attach/Remove Lorebooks', content):
    idx = m.start()
    print("Match at", idx)
    print(content[max(0, idx-200):min(len(content), idx+400)])
