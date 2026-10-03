import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
chunks = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
chunks = [c for c in chunks if 'chunks' in c]

for c in chunks:
    try:
        url = 'https://app.wyvern.chat' + c
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=5).read().decode('utf-8', errors='ignore')
        if 'moon' in data.lower():
            for m in re.finditer(r'(.{0,100}moon.{0,100})', data, re.IGNORECASE):
                snippet = m.group(1).replace('\n', ' ')
                if any(w in snippet.lower() for w in ['phase', 'cycle', 'calendar', 'orbit']):
                    print(f"{c}: {snippet}")
    except Exception as e:
        pass
