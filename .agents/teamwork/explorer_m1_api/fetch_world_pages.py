import urllib.request
import re
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

urls = [
    "https://app.wyvern.chat/worlds",
    "https://app.wyvern.chat/worlds/create",
    "https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7",
]

for url in urls:
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    })
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"[{url}] -> {resp.status} (len {len(html)})")
            scripts = set(re.findall(r'/_next/static/chunks/[a-zA-Z0-9_\-\.]+\.js', html))
            print(f"   Scripts ({len(scripts)}):")
            for s in sorted(scripts)[:10]:
                print("     ", s)
    except urllib.error.HTTPError as e:
        print(f"[{url}] -> HTTP {e.code}: {e.reason}")
    except Exception as e:
        print(f"[{url}] -> Error: {e}")
