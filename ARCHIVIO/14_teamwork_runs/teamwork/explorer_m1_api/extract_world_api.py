import urllib.request

url = "https://app.wyvern.chat/_next/static/chunks/77818-c9463c8edce6c041.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

# print where worldApi is defined and print everything in p = { ... }
idx = code.find('worldApi:function(){return p}')
print("Found worldApi return at", idx)
idx_p = code.find('p={', idx)
print("p={ found at", idx_p)
# print 5000 chars of p
print(code[idx_p:idx_p+6000])
