import urllib.request
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

html = open("scratch/wyvern_index.html", "r", encoding="utf-8").read()
chunks = sorted(list(set(re.findall(r'/_next/static/chunks/[^"\']+\.js', html))))

def search_chunk(c):
    url = 'https://app.wyvern.chat' + c
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as cr:
            code = cr.read().decode('utf-8', errors='ignore')
            if 'getUserWorlds' in code and '77818' not in c:
                return (c, code)
    except Exception:
        pass
    return None

with ThreadPoolExecutor(max_workers=10) as ex:
    for res in ex.map(search_chunk, chunks):
        if res:
            c, code = res
            print(f"CALLER IN {c}:")
            for m in re.finditer(r'getUserWorlds', code):
                idx = m.start()
                print(code[max(0, idx - 200):min(len(code), idx + 300)])
                print("="*50)
