import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/webpack-3693ac4f07a2c363.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        print("Webpack chunk length:", len(content))
        # Look for 41680
        pos = content.find('41680')
        if pos != -1:
            print("Found 41680 in webpack chunk map!")
            print(content[max(0, pos-100):min(len(content), pos+200)])
        else:
            print("41680 not in webpack chunk map, searching for chunk loader...")
except Exception as e:
    print("Error:", e)
