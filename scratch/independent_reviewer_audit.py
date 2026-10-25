import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
token_path = ROOT / 'scratch' / 'wyvern_token.txt'
token = token_path.read_text(encoding='utf-8').strip()

TARGET_WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
url = f'https://app.wyvern.chat/api/worlds/characters/world/{TARGET_WORLD_ID}'
req = urllib.request.Request(
    url,
    headers={
        'Authorization': f'Bearer {token}',
        'User-Agent': 'IndependentAuditorCritic/1.0'
    }
)

with urllib.request.urlopen(req) as resp:
    chars = json.loads(resp.read().decode('utf-8'))

print(f"=== INDEPENDENT ADVERSARIAL AUDIT ===")
print(f"Total live characters fetched: {len(chars)}")

expected_names = [
    'Erik Ulfr Douglas',
    'Logan Járn Douglas',
    'Edric Douglas',
    'Noah Loki Douglas Bloodmoon',
    'Malachia Björn Douglas Bloodmoon',
    'Jasper Svartr Douglas Bloodmoon',
    'Alyssa Hvit Douglas Bloodmoon',
    'Wulfnic Báleygr Bloodmoon',
    'Zefir Hvitskog',
    'Mackenzie Sanchez-Rogers',
    'Finnegan Novak',
    'Sierra Cruz',
    'Scarlett Rose'
]

by_name = {c.get('display_name'): c for c in chars}

findings = []

for name in expected_names:
    if name not in by_name:
        findings.append(f"CRITICAL: {name} not found in live API response!")
        continue
    c = by_name[name]
    cid = c.get('_id') or c.get('id')
    bdate = c.get('birthdate')
    tl = c.get('start_timeline_position')
    avatar = c.get('avatar')
    rpg = c.get('rpg_stats') or {}
    lvl = rpg.get('level')
    bs = rpg.get('base_stats') or {}
    desc = c.get('long_summary') or ''
    em_dashes = desc.count('\u2014')
    
    stat_nums = [bs.get(f'stat_{i}', 0) for i in range(1, 7)]
    stat_named = [bs.get(k, 0) for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']]
    
    # 1. Timeline check
    if bdate != tl:
        findings.append(f"TIMELINE MISMATCH: {name} bdate ({bdate}) != tl ({tl})")
    if not isinstance(bdate, int) or bdate < 0 or bdate > 10489902:
        findings.append(f"INVALID BDATE: {name} bdate {bdate} outside range [0, 10489902]")
        
    # 2. Avatar check
    if not avatar or not avatar.startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'):
        findings.append(f"INVALID AVATAR: {name} avatar {avatar}")
        
    # 3. Level cap check
    if lvl > 99:
        findings.append(f"LEVEL EXCEEDS 99: {name} level {lvl}")
        
    # 4. RPG stats check
    if sum(stat_nums) != 31:
        findings.append(f"STAT NUM SUM ERROR: {name} sum={sum(stat_nums)} != 31")
    if sum(stat_named) != 31:
        findings.append(f"STAT NAMED SUM ERROR: {name} sum={sum(stat_named)} != 31")
    for idx, (num, named) in enumerate(zip(stat_nums, stat_named), 1):
        if num != named:
            findings.append(f"STAT DUAL-KEY MISMATCH: {name} stat_{idx}={num} != named={named}")
        if num < 1:
            findings.append(f"STAT UNDERFLOW: {name} stat_{idx}={num} < 1")
            
    # 5. JED+ and Formatting
    if em_dashes > 0:
        findings.append(f"EM-DASH VIOLATION: {name} has {em_dashes} em-dashes")
    if not desc.startswith('['):
        findings.append(f"JED+ FORMAT VIOLATION: {name} does not start with bracket block")
    if 'BACKSTORY:' not in desc:
        findings.append(f"JED+ MISSING BACKSTORY: {name}")
    if 'VOICE & BEHAVIOR:' not in desc and 'VOICE AND BEHAVIOR:' not in desc:
        findings.append(f"JED+ MISSING VOICE: {name}")
    if len(desc) < 4000:
        findings.append(f"JED+ SHORT DESC: {name} length {len(desc)} < 4000")

    print(f"CHECKED: {name:32} | ID: {cid:22} | Lvl: {lvl:2} | Sum: {sum(stat_nums)} | BDate: {bdate:8} | CDN: OK | Em-dash: {em_dashes}")

print("\n--- AUDIT FINDINGS ---")
if not findings:
    print("ZERO FINDINGS: All 13 World Characters conform 100% to live requirements!")
else:
    for f in findings:
        print(f"Finding: {f}")
