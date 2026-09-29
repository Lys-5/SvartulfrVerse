import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        scripts = re.findall(r'src="([^"]+\.js)"', html)
        print('Scripts found:', len(scripts))
        for s in scripts:
            if not s.startswith('http'):
                s = 'https://app.wyvern.chat' + s
            print('Checking script:', s)
            s_req = urllib.request.Request(s, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(s_req) as s_resp:
                content = s_resp.read().decode('utf-8', errors='ignore')
                if 'Narrative Tiers' in content or 'crit_margin' in content or 'Base DC' in content or 'battle_instructions' in content:
                    print('MATCH in:', s)
                    matches = re.findall(r'[a-zA-Z0-9_]+_margin|[a-zA-Z0-9_]+_dc|combat_[a-zA-Z0-9_]+|battle_[a-zA-Z0-9_]+', content)
                    print('Tokens:', set(matches))
except Exception as e:
    print('Error:', e)
