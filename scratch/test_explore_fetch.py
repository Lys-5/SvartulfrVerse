import urllib.request
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text().strip()

for q in ['Neon', 'Purr', 'Russ', 'Cocketeers']:
    url = f'https://app.wyvern.chat/explore?tab=characters&rating=all&search={q}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            print(f"Query '{q}': status={resp.status}, len={len(content)}")
            # check if q is anywhere in content
            count = content.lower().count(q.lower())
            print(f"  Count of '{q}': {count}")
    except Exception as e:
        print(f"Query '{q}' error: {e}")
