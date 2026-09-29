import urllib.request
import json
import sys
import re

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def inspect_g2():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    url = f'https://app.wyvern.chat/api/worlds/characters/world/{world_id}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chars = json.loads(resp.read().decode('utf-8'))

    missing = [c for c in chars if not c.get('rpg_stats')]
    print(f"Checking {len(missing)} characters without rpg_stats...\n")
    for c in missing[:20]:
        ls = c.get('long_summary') or ''
        sm = c.get('summary') or ''
        m_sp = re.findall(r'SPECIES:\s*([^;\]\n]+)', ls)
        m_occ = re.findall(r'OCCUPATION:\s*([^;\]\n]+)', ls) or re.findall(r'ROLE:\s*([^;\]\n]+)', ls)
        m_age = re.findall(r'AGE:\s*([^;\]\n]+)', ls)
        sp = m_sp[0].strip() if m_sp else "None"
        occ = m_occ[0].strip() if m_occ else "None"
        age = m_age[0].strip() if m_age else "None"
        name = c.get('display_name')
        print(f"- {name:25} | Sp: {sp[:20]:20} | Occ: {occ[:25]:25} | Age: {age}")

if __name__ == '__main__':
    inspect_g2()
