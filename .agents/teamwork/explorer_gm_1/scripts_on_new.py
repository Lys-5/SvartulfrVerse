import urllib.request
import re

url = 'https://app.wyvern.chat/assistants/new'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

scripts = re.findall(r'src="([^"]+\.js)"', html)
print(f"Scripts on /assistants/new: {len(scripts)}")
for s in scripts:
    if 'chunks' in s:
        print(s)
