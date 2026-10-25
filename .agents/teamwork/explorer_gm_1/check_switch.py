import urllib.request

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

pos = content.find('case"characters":')
print("Switch snippet:\n")
print(content[pos-200:pos+2500])
