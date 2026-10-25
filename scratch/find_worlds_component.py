import urllib.request
import re

html = open("scratch/wyvern_index.html", "r", encoding="utf-8").read()
# Let's read the html from /worlds
req = urllib.request.Request('https://app.wyvern.chat/worlds', headers={
    'User-Agent': 'Mozilla/5.0',
    'Authorization': f'Bearer {open("scratch/wyvern_token.txt").read().strip()}'
})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

chunks = set(re.findall(r'/_next/static/chunks/[^"\']+\.js', html))
print(f"Scanning {len(chunks)} chunks...")

for c in sorted(chunks):
    url = 'https://app.wyvern.chat' + c
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as cr:
            code = cr.read().decode('utf-8', errors='ignore')
            # Look for api calls to /api/worlds or world list
            if '/api/worlds' in code:
                # find the specific fetch or axios or api call
                for m in re.finditer(r'/api/worlds[a-zA-Z0-9_\-/${}?=&]*', code):
                    print(f"In {c}: {m.group(0)}")
            if 'Create World' in code or 'create-world' in code or 'Create a World' in code:
                print(f"WORLD UI COMPONENT IN: {c}")
    except Exception as e:
        pass
