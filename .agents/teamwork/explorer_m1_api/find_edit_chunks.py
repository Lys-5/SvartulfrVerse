import urllib.request
import re

url = "https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

scripts = re.findall(r'src="(/_next/static/chunks/[^"]+)"', html)
print(f"Total scripts: {len(scripts)}")
for s in scripts:
    if any(k in s for k in ['edit', 'world', 'page']):
        print("Relevant script:", s)

print("\nLast 15 scripts:")
for s in scripts[-15:]:
    print(" ", s)
