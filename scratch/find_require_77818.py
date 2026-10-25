import urllib.request
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

html = open("scratch/wyvern_index.html", "r", encoding="utf-8").read()
chunks = sorted(list(set(re.findall(r'/_next/static/chunks/[^"\']+\.js', html))))

def check_chunk(c):
    if '77818' in c:
        return None
    url = 'https://app.wyvern.chat' + c
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as cr:
            code = cr.read().decode('utf-8', errors='ignore')
            if '77818' in code:
                return (c, code)
    except Exception:
        pass
    return None

with ThreadPoolExecutor(max_workers=10) as ex:
    for res in ex.map(check_chunk, chunks):
        if res:
            c, code = res
            print(f"CHUNK IMPORTING 77818: {c}")
            for m in re.finditer(r'77818', code):
                idx = m.start()
                print(code[max(0, idx - 150):min(len(code), idx + 250)])
                print("="*60)
