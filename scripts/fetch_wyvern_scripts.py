import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
for m in re.finditer(r'<script[^>]+src=["\']([^"\']+)["\']', html):
    print("Script:", m.group(1))
