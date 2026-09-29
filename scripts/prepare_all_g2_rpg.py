import urllib.request
import json
import sys
import re

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def prepare_g2_rpg():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    url = f'https://app.wyvern.chat/api/worlds/characters/world/{world_id}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chars = json.loads(resp.read().decode('utf-8'))

    missing = [c for c in chars if not c.get('rpg_stats')]
    print(f"Total G2 characters to configure: {len(missing)}")

    configs = []
    for c in missing:
        cid = c['id']
        name = c.get('display_name') or c.get('name')
        ls = c.get('long_summary') or ''
        sm = c.get('summary') or ''

        # 1. Species
        m_sp = re.findall(r'SPECIES:\s*([^;\]\n]+)', ls)
        sp = m_sp[0].strip() if m_sp else "Supernatural"
        # clean sp
        sp = re.sub(r'[\(\[].*?[\)\]]', '', sp).strip()
        if not sp:
            sp = "Supernatural"

        # 2. Occupation
        m_occ = re.findall(r'OCCUPATION:\s*([^;\]\n]+)', ls) or re.findall(r'ROLE:\s*([^;\]\n]+)', ls)
        occ = m_occ[0].strip() if m_occ else "Citizen"
        occ = re.sub(r'[\(\[].*?[\)\]]', '', occ).strip()
        if not occ:
            occ = "Citizen"

        # 3. Age / Level
        bd = c.get('birthdate')
        if bd is not None and bd > 0:
            age = max(1, min(99, int((10486470 - bd) / (24 * 365.25))))
        else:
            m_age = re.findall(r'AGE:\s*([0-9]{1,3})', ls)
            if m_age:
                age = max(1, min(99, int(m_age[0])))
            else:
                age = 25

        # 4. Archetype-based stat distribution (budget 25 points, sum 31)
        # Check text keywords for role archetype
        desc_lower = (ls + ' ' + sm + ' ' + occ).lower()
        if any(w in desc_lower for w in ['tank', 'brawler', 'enforcer', 'guard', 'muscle', 'berserker', 'warrior', 'heavy']):
            stats = {'stat_1': 8, 'stat_2': 7, 'stat_3': 5, 'stat_4': 4, 'stat_5': 5, 'stat_6': 2}
        elif any(w in desc_lower for w in ['rogue', 'infiltrator', 'scout', 'thief', 'assassin', 'hitman', 'hacker', 'speed']):
            stats = {'stat_1': 4, 'stat_2': 3, 'stat_3': 8, 'stat_4': 7, 'stat_5': 4, 'stat_6': 5}
        elif any(w in desc_lower for w in ['mage', 'witch', 'researcher', 'doctor', 'healer', 'medic', 'scholar', 'scientist', 'alchemy']):
            stats = {'stat_1': 2, 'stat_2': 4, 'stat_3': 4, 'stat_4': 9, 'stat_5': 6, 'stat_6': 6}
        elif any(w in desc_lower for w in ['leader', 'ceo', 'underboss', 'head', 'diplomat', 'council', 'politician', 'matriarch', 'patriarch', 'boss']):
            stats = {'stat_1': 5, 'stat_2': 5, 'stat_3': 4, 'stat_4': 6, 'stat_5': 8, 'stat_6': 3}
        elif any(w in desc_lower for w in ['guitarist', 'drummer', 'artist', 'dj', 'musician', 'singer', 'performer']):
            stats = {'stat_1': 4, 'stat_2': 4, 'stat_3': 6, 'stat_4': 5, 'stat_5': 8, 'stat_6': 4}
        else:
            # Balanced versatile
            stats = {'stat_1': 5, 'stat_2': 5, 'stat_3': 5, 'stat_4': 6, 'stat_5': 6, 'stat_6': 4}

        assert sum(stats.values()) == 31, f"Stat sum error for {name}: {sum(stats.values())}"

        # 5. Traits
        traits = []
        if sp and sp != "Supernatural":
            traits.append(sp[:30])
        if occ and occ != "Citizen":
            traits.append(occ[:30])
        # Extract traits from summary if available
        m_tr = re.findall(r'TRAITS:\s*([^;\]\n]+)', sm)
        if m_tr:
            tr_items = [t.strip() for t in m_tr[0].split(',') if t.strip()]
            traits.extend(tr_items[:2])
        if len(traits) < 3:
            traits.append("Solarton Resident")
        traits = traits[:4]

        configs.append({
            'id': cid,
            'name': name,
            'level': age,
            'species': sp[:40],
            'occupation': occ[:40],
            'stats': stats,
            'traits': traits
        })

    print(f"Successfully prepared {len(configs)} configurations!")
    for c in configs[:5]:
        print(f"  {c['name']:25} | Lv {c['level']:2} | Sp: {c['species']:18} | Occ: {c['occupation']:22} | Traits: {c['traits']}")

    return configs

if __name__ == '__main__':
    prepare_g2_rpg()
