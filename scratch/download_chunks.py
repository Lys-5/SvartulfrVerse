import urllib.request
import json
import re

headers = {"User-Agent": "Mozilla/5.0"}

urls = [
    "https://app.wyvern.chat/_next/static/chunks/66353-44918b7fd11ff8ae.js",
    "https://app.wyvern.chat/_next/static/chunks/53944-e2a3f3ea28ad0416.js",
    "https://app.wyvern.chat/_next/static/chunks/99424-7f608d672232ed88.js"
]

for url in urls:
    name = url.split('/')[-1]
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='replace')
        with open(f"scratch/{name}", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Downloaded {name}, size: {len(content)}")
