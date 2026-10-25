import urllib.request
import re

url = 'https://app.wyvern.chat/mine'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
chunks = set(re.findall(r'/_next/static/chunks/[^\"]+\.js', html))

print(f"Scanning {len(chunks)} chunks for 'simple-assistant-config:create'...")

for c in chunks:
    cu = 'https://app.wyvern.chat' + c
    try:
        txt = urllib.request.urlopen(urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        if 'simple-assistant-config:create' in txt:
            print(f"Match in chunk: {c}")
            for m in re.finditer(r'simple-assistant-config:create', txt):
                idx = m.start()
                print(txt[max(0, idx-100):min(len(txt), idx+400)])
                print("-" * 50)
    except Exception:
        pass
