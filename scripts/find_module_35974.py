import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)

for s in scripts:
    if not s.endswith('.js') or 'cloudflare' in s:
        continue
    url = 'https://app.wyvern.chat' + s
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(r, timeout=5).read().decode('utf-8', errors='ignore')
        if '35974:' in data:
            print('MATCH IN SCRIPT (defines 35974):', s)
            pos = data.find('35974:')
            print(data[pos:pos+2500])
            break
    except Exception as e:
        pass
