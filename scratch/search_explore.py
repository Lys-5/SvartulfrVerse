import urllib.request
import urllib.parse
import json
import re
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text().strip()

for query in ['Neon Purr', 'Neon', 'Russ', 'Cocketeers']:
    url = f'https://app.wyvern.chat/explore?tab=characters&rating=all&search={urllib.parse.quote(query)}'
    req = urllib.request.Request(url, headers={'authorization': f'Bearer {token}', 'user-agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
            if m:
                data = json.loads(m.group(1))
                props = data.get('props', {}).get('pageProps', {})
                # Try finding characters in props
                dump = json.dumps(props)
                matches = re.findall(rf'(?i)"name":\s*"([^"]*{query}[^"]*)"', dump)
                print(f'Search "{query}": {len(matches)} name matches found -> {matches[:5]}')
            else:
                print(f'Search "{query}": __NEXT_DATA__ not found')
    except Exception as e:
        print(f'Search "{query}" error: {e}')
