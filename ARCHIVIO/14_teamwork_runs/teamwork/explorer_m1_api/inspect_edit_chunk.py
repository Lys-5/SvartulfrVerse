import urllib.request
import re
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

chunk_url = "https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js"
req = urllib.request.Request(chunk_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        code = resp.read().decode('utf-8', errors='ignore')
        print(f"Downloaded chunk len: {len(code)}")
        
        # Search for endpoints or mutation functions
        endpoints = set(re.findall(r'[\'"`]/api/[^\'"`]+[\'"`]', code))
        print("API endpoints in chunk:")
        for ep in sorted(endpoints):
            print("  ", ep)
            
        # Search for method: 'POST', 'PUT', 'DELETE'
        methods = re.findall(r'method:\s*[\'"`]([A-Z]+)[\'"`]', code)
        print("HTTP methods found:", set(methods))
        
        # Search for fetch calls
        for m in re.finditer(r'fetch\([^)]+\)', code):
            print("Fetch call snippet:", m.group(0)[:120])
except Exception as e:
    print("Error:", e)
