import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/54866-5b1f01a517163780.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

pos = content.find('simple-assistant-config:create')
print("Position:", pos)
print("Snippet around modal definition:")
print(content[max(0, pos-1500):min(len(content), pos+3000)])
