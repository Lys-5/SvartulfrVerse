import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('FINAL/scenarios/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    print(f"\n========================================================")
    print(f"DEEP LORE & STRING AUDIT: {f}")
    
    # 1. Macro check
    raw_str = json.dumps(d)
    macros = re.findall(r'\{\{[^}]+\}\}', raw_str)
    print(f"Macros found: {set(macros)}")
    
    # 2. Asterisk check
    asterisks_matches = []
    for g_i, g in enumerate(d.get('greetings', [])):
        for m_i, m in enumerate(g.get('messages', [])):
            c = m.get('content', '')
            if '*' in c:
                asterisks_matches.append((g_i, m_i, c))
    print(f"Messages with asterisks (*): {len(asterisks_matches)}")
    for g_i, m_i, c in asterisks_matches:
        print(f"  g[{g_i}] m[{m_i}] asterisk context: {c[:150]}")
        
    # 3. Double asterisks (markdown bold) check
    bold_matches = []
    for g_i, g in enumerate(d.get('greetings', [])):
        for m_i, m in enumerate(g.get('messages', [])):
            c = m.get('content', '')
            if '**' in c:
                bold_matches.append((g_i, m_i, c))
    if bold_matches:
        print(f"  WARNING: Messages with bold (**): {len(bold_matches)}")
    else:
        print(f"  PASS: Zero markdown bold (**) in messages.")
        
    # 4. Avatar verification
    avatar = d.get('avatar', '')
    print(f"Avatar URL: {avatar}")
    
    # 5. Pools character_id validation
    pools = []
    for s in d.get('slots', []):
        for p in s.get('pool', []):
            pools.append((s.get('key'), p.get('character_id'), p.get('weight')))
    print(f"Character pools ({len(pools)} total mapped cards):")
    for k, cid, w in pools:
        print(f"  slot '{k}' -> card_id '{cid}' (weight: {w})")

