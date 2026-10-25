import urllib.request
import re
import json

url = 'https://app.wyvern.chat/profiles/Shadowgamer0828/characters/campmystic'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        print('Fetched HTML length:', len(html))
        with open('scratch/campmystic_page.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Search for JSON data or next data or character payload
        matches = re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html, re.DOTALL)
        if matches:
            data = json.loads(matches[0])
            print('Next data keys:', list(data.keys()))
            props = data.get('props', {}).get('pageProps', {})
            print('PageProps keys:', list(props.keys()))
            char = props.get('character') or props.get('initialCharacter')
            if char:
                print('Character ID:', char.get('id'))
                print('Character Name:', char.get('name'))
                print('Tagline:', char.get('tagline'))
                with open('scratch/campmystic_extracted.json', 'w', encoding='utf-8') as f:
                    json.dump(char, f, indent=2, ensure_ascii=False)
            else:
                print('Props preview:', str(props)[:500])
        else:
            print('No __NEXT_DATA__ found. Searching for character strings...')
            m2 = re.findall(r'(\{[^{}]*"name"[^{}]*"Camp Mystic"[^{}]*\})', html)
            print('Matches m2:', len(m2))
except Exception as e:
    print('Error:', e)
