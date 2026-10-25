import urllib.request
import re

routes = [
    '/assistants',
    '/assistants/new',
    '/assistants/create',
    '/simple-assistant-config/new',
    '/mine'
]

for r in routes:
    url = f'https://app.wyvern.chat{r}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"[HTTP {resp.status}] GET {r}")
            html = resp.read().decode('utf-8')
            # Look for page chunks
            chunks = re.findall(r'/_next/static/chunks/(app/[^\"]+\.js)', html)
            if chunks:
                print(f"  App chunks in {r}: {chunks}")
    except urllib.error.HTTPError as e:
        print(f"[HTTP {e.code}] GET {r}")
    except Exception as e:
        print(f"[ERR] GET {r}: {e}")
