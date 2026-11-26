import urllib.request
import re
import json

url = 'https://app.wyvern.chat/mine'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Find all script src
chunks = re.findall(r'src="([^"]+\.js)"', html)
print(f"Direct script tags on /mine: {len(chunks)}")
for c in chunks:
    print(" ", c)

# Also find buildId or chunk manifest
build_id = re.findall(r'/_next/data/([^/]+)/', html)
if build_id:
    print("Build ID:", build_id[0])

# Let's inspect the HTML itself for tab labels
tabs = re.findall(r'>([^<]*(?:Character|Assistant|Scenario|Lorebook|Story|Engine|Prompt)[^<]*)<', html, re.I)
print("Tabs/text matched in HTML:", set(tabs))
