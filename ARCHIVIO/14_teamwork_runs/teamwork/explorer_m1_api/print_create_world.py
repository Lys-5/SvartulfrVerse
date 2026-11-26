import urllib.request

chunk_url = "https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js"
req = urllib.request.Request(chunk_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

pos = 22865
print("=== Around createWorld (pos 22865) ===")
print(code[max(0, pos-400):min(len(code), pos+600)])
