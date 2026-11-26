import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

pos = content.find('91650:function(')
if pos != -1:
    print("Found module 91650 at", pos)
    print(content[pos:pos+2500])
else:
    print("Module 91650 not in this chunk, searching for /simple-assistant-config string...")
    pos2 = content.find('/simple-assistant-config')
    print(content[pos2-100:pos2+1000])
