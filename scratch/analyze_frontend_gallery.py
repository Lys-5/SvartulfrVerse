import urllib.request
import re

url_page = 'https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC'
req = urllib.request.Request(url_page, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
except Exception as e:
    print('Failed to fetch html:', e)
    html = ''

chunks = re.findall(r'/_next/static/chunks/[^"\'\s]+\.js', html)
print(f'Found {len(chunks)} chunks')

found = []
for c in set(chunks):
    url = 'https://app.wyvern.chat' + c
    try:
        data = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore')
    except Exception:
        continue
    if 'select avatar from gallery' in data.lower() or 'unknown source' in data.lower() or 'select different avatar' in data.lower():
        print(f'*** MATCH IN CHUNK: {c} ***')
        found.append((c, data))

if not found:
    print('Trying broader search on all chunks...')
    for c in set(chunks):
        url = 'https://app.wyvern.chat' + c
        try:
            data = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore')
        except Exception:
            continue
        if 'gallery' in data.lower() and 'avatar' in data.lower():
            if 'cutout' in data.lower() or 'sprite' in data.lower():
                print(f'Relevant chunk: {c}')
                found.append((c, data))

for c, data in found:
    # Look for "Unknown source" or avatar matching
    pos = data.lower().find('unknown source')
    if pos != -1:
        print(f'\n--- Snippet near "Unknown source" in {c} ---')
        print(data[max(0, pos-200):min(len(data), pos+300)])
    pos2 = data.lower().find('select avatar from gallery')
    if pos2 != -1:
        print(f'\n--- Snippet near "Select avatar from gallery" in {c} ---')
        print(data[max(0, pos2-200):min(len(data), pos2+300)])
