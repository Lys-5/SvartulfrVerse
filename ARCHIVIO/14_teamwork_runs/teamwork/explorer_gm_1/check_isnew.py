import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/assistants/%5Bid%5D/page-cbe4530944bdffb9.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

for kw in ['"new"', 'new:', 'isNew', 'create:', 'onCreate', 'router.push', 'title', 'kind']:
    for m in re.finditer(re.escape(kw), content):
        idx = m.start()
        print(f"[{kw}] ->", content[max(0, idx-60):min(len(content), idx+140)])
