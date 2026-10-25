import urllib.request
import re

chunk_url = "https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-d94d4a36163d1b0d.js"
req = urllib.request.Request(chunk_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    code = resp.read().decode('utf-8', errors='ignore')

idx = code.find('function eE(')
if idx == -1: idx = code.find('let eE=')
if idx == -1: idx = code.find('eE=e=>')
if idx == -1: idx = code.find('eE=function(')
print("Found eE at", idx)
print(code[idx:idx+2500])
