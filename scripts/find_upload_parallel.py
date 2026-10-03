import urllib.request
import re
from concurrent.futures import ThreadPoolExecutor

req = urllib.request.Request('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
scripts = [s for s in re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html) if s.endswith('.js') and 'cloudflare' not in s]

def check(s):
    url = 'https://app.wyvern.chat' + s
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(r, timeout=10).read().decode('utf-8', errors='ignore')
        if '36234:' in data:
            pos = data.find('36234:')
            print(f"FOUND 36234 in {s}:\n" + data[pos:pos+3500])
            return True
        if 'uploadDirect' in data and 'uploadDirect:' not in data: # function definition
            print(f"Found uploadDirect definition in {s}")
    except Exception as e:
        pass
    return False

with ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(check, scripts))
