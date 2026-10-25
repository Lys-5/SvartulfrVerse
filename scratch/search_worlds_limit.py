import urllib.request
import re

# Fetch /worlds HTML again to get all script chunk paths
req = urllib.request.Request('https://app.wyvern.chat/worlds', headers={
    'User-Agent': 'Mozilla/5.0',
    'Authorization': f'Bearer {open("scratch/wyvern_token.txt").read().strip()}'
})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

chunks = set(re.findall(r'/_next/static/chunks/[^"\']+\.js', html))
print(f"Searching for 'worlds/limit' across {len(chunks)} chunks...")

for c in sorted(chunks):
    url = 'https://app.wyvern.chat' + c
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as cr:
            code = cr.read().decode('utf-8', errors='ignore')
            if 'worlds/limit' in code:
                print(f"FOUND 'worlds/limit' in chunk: {c}")
                # Print surrounding context
                idx = code.find('worlds/limit')
                snippet = code[max(0, idx-300):min(len(code), idx+400)]
                print("Context:", snippet)
                print("="*60)
    except Exception as e:
        pass
