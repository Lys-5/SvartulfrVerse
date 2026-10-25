import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat/worlds', headers={
    'User-Agent': 'Mozilla/5.0',
    'Authorization': f'Bearer {open("scratch/wyvern_token.txt").read().strip()}'
})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Status:", resp.status, "HTML len:", len(html))
        chunks = re.findall(r'/_next/static/chunks/[^"\']+\.js', html)
        print("Found chunks on /worlds:", len(chunks))
        for c in set(chunks):
            print(" ", c)
except Exception as e:
    print("Error:", e)
