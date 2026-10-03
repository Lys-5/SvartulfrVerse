import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/worlds/edit/%5Bid%5D/page-e1a3b390a8ec26db.js'
data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8', errors='ignore')

matches = re.finditer(r'(.{0,150}(?:gedcom-trees|createGedcom|gedcom_trees|newTree).{0,150})', data)
for m in list(matches)[:10]:
    print('Match:', m.group(1).replace('\n', ' '))
