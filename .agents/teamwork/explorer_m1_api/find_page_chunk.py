import urllib.request
import re

url = "https://app.wyvern.chat/worlds/create"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

scripts = re.findall(r'src="(/_next/static/chunks/[^"]+)"', html)
print(f"Total scripts: {len(scripts)}")
for s in scripts:
    if any(k in s for k in ['create', 'world', 'page', 'app']):
        print("Relevant script:", s)

# Let's inspect the last 15 scripts (which usually include page components in Next.js)
print("\nLast 15 scripts:")
for s in scripts[-15:]:
    print(" ", s)
