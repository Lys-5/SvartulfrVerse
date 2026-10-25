import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

chunks = set(re.findall(r'/_next/static/chunks/[^"\']+\.js', html))
print('Found chunks:', len(chunks))

for c in sorted(chunks):
    try:
        r = urllib.request.Request('https://app.wyvern.chat' + c, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as cr:
            code = cr.read().decode('utf-8', errors='ignore')
            if 'parent_location' in code:
                print('Found parent_location in:', c)
                for m in re.finditer(r'parent_location', code):
                    s = max(0, m.start() - 100)
                    e = min(len(code), m.end() + 200)
                    print(code[s:e])
                    print('-'*40)
                    break
    except Exception as ex:
        pass
