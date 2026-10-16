import urllib.request
import json
import re

token = open('scratch/wyvern_token.txt').read().strip()
url = 'https://app.wyvern.chat/explore?tab=characters&rating=all&search=Marek'
req = urllib.request.Request(url, headers={'authorization': f'Bearer {token}', 'user-agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
        if m:
            data = json.loads(m.group(1))
            props = data.get('props', {}).get('pageProps', {})
            print('pageProps keys:', list(props.keys()))
            dump = json.dumps(props)
            matches = list(re.finditer(r'(?i)marek', dump))
            print(f'Total matches for marek: {len(matches)}')
            if matches:
                hit = matches[0]
                s = max(0, hit.start() - 150)
                e = min(len(dump), hit.end() + 150)
                print('Context:', dump[s:e])
        else:
            print('__NEXT_DATA__ tag not found')
except Exception as e:
    print('Error:', e)
