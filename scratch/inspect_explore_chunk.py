import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/explore/page-ed5d69098b7e35ab.js'
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        code = resp.read().decode('utf-8', errors='ignore')
        print("Explore page chunk len:", len(code))
        matches = re.findall(r'(/api/[a-zA-Z0-9_\-/{}]*)', code)
        print("API endpoints in explore chunk:")
        for m in set(matches):
            print(" ", m)
except Exception as e:
    print("Error:", e)
