import requests, json, re, pathlib

root = pathlib.Path('.')
token = (root / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

r = requests.get('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
print('Status:', r.status_code, 'len:', len(r.text))
scripts = re.findall(r'src=["\']([^"\']+\.js[^"\']*)["\']', r.text)
print('Scripts count:', len(scripts))

matched = []
for s in scripts:
    url = 'https://app.wyvern.chat' + s
    try:
        res = requests.get(url, headers=headers, timeout=10)
        t = res.text
        if any(term in t for term in ['Skip this entry entirely', 'redundant duplicate', 'DON\'T ACTIVATE', 'dont_activate', 'disable_when_active']):
            print('MATCH IN:', s)
            matched.append((s, t))
    except Exception as e:
        pass

if matched:
    for s, t in matched:
        for term in ['Skip this entry entirely', 'redundant duplicate', 'DON\'T ACTIVATE']:
            if term in t:
                idx = t.find(term)
                print(f'=== Found {term} in {s} ===')
                print(t[max(0, idx-300):min(len(t), idx+600)])
                (root / 'scratch' / 'matched_duplicate_feature.js').write_text(t, encoding='utf-8')
else:
    print('No match in HTML scripts, searching manifest/build chunks...')
