import urllib.request
import re

with open('scripts/fetch_wyvern_scripts.py') as f:
    pass

req = urllib.request.Request('https://app.wyvern.chat', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)

for s in scripts:
    if not s.endswith('.js') or 'cloudflare' in s:
        continue
    url = 'https://app.wyvern.chat' + s
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        # Check if it has /gallery
        if '/gallery' in content:
            print(f"Found /gallery in {s}")
            # Find snippets with /gallery
            matches = [m.start() for m in re.finditer(r'/gallery', content)]
            for pos in matches[:5]:
                snippet = content[max(0, pos-100):min(len(content), pos+150)]
                print(f"  Snippet: {snippet}")
    except Exception as e:
        pass
