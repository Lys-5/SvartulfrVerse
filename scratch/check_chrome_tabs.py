import requests
import json

try:
    r = requests.get('http://127.0.0.1:9222/json/version')
    print('Version:', r.json())
    r2 = requests.get('http://127.0.0.1:9222/json/list')
    tabs = r2.json()
    print(f"Found {len(tabs)} tabs:")
    for t in tabs:
        print(f"  [{t.get('type')}] {t.get('title')} -> {t.get('url')} (id: {t.get('id')})")
except Exception as e:
    print('Error:', e)
