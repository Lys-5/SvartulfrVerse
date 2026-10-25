import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

chunks = [
    '/_next/static/chunks/36457-688d656b1534b9f0.js',
    '/_next/static/chunks/61929-5cc0e3b134146cf3.js',
    '/_next/static/chunks/69712-af83c29ebab813a8.js',
    '/_next/static/chunks/29079-b6a0d5e327fba37e.js',
    '/_next/static/chunks/54866-5b1f01a517163780.js'
]

data = {}

for c in chunks:
    url = f"https://app.wyvern.chat{c}"
    filename = c.split('/')[-1]
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
    data[filename] = content
    print(f"Downloaded {filename}, length={len(content)}")
    with open(f"e:/repository/SvartulfrVerse/scratch/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

print("Saved all chunks locally to scratch/")
