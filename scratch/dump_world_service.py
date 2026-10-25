import urllib.request

url = 'https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

idx = code.find('getLimit:')
start = max(0, idx - 1000)
end = min(len(code), idx + 2000)
print(code[start:end])
