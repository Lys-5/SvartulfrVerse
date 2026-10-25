import urllib.request
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

req = urllib.request.Request('https://app.wyvern.chat/worlds', headers={
    'User-Agent': 'Mozilla/5.0',
    'Authorization': f'Bearer {open("scratch/wyvern_token.txt").read().strip()}'
})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

chunks = sorted(list(set(re.findall(r'/_next/static/chunks/[^"\']+\.js', html))))
print(f"Total chunks: {len(chunks)}")

def check_chunk(c):
    url = 'https://app.wyvern.chat' + c
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as cr:
            code = cr.read().decode('utf-8', errors='ignore')
            res = []
            if 'worlds/limit' in code:
                res.append(f"worlds/limit in {c}")
            if '/api/worlds' in code:
                matches = re.findall(r'/api/worlds[a-zA-Z0-9_\-/${}?=&]*', code)
                res.append(f"/api/worlds in {c}: {set(matches)}")
            return res
    except Exception:
        return []

with ThreadPoolExecutor(max_workers=10) as ex:
    results = ex.map(check_chunk, chunks)
    for r in results:
        for line in r:
            print(line)

print("Scan complete.")
