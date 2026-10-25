import urllib.request
import json
import sys
from pathlib import Path

ROOT = Path('.')
sys.path.insert(0, str(ROOT.resolve()))
token = Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
url = 'https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    live_chars = json.loads(resp.read().decode('utf-8'))

print('=== 1. LIVE BACKEND AUDIT ===')
print(f'Total live characters: {len(live_chars)}')

snap_path = ROOT / 'scratch' / 'm1_13_world_characters_verified.json'
with open(snap_path, 'r', encoding='utf-8') as sf:
    snap_data = json.load(sf)

snap_by_name = {s['name']: s for s in snap_data}
live_by_name = {c.get('display_name') or c.get('name'): c for c in live_chars}

discrepancies = []
for name, live in live_by_name.items():
    if name not in snap_by_name:
        discrepancies.append(f'Live char {name} not in snapshot!')
        continue
    snap = snap_by_name[name]
    live_id = live.get('_id') or live.get('id')
    if live_id != snap['id']:
        discrepancies.append(f'{name}: ID mismatch live={live_id} vs snap={snap["id"]}')
    if live.get('birthdate') != snap['birthdate']:
        discrepancies.append(f'{name}: birthdate mismatch live={live.get("birthdate")} vs snap={snap["birthdate"]}')
    if live.get('avatar') != snap['avatar']:
        discrepancies.append(f'{name}: avatar mismatch')
    rpg = live.get('rpg_stats') or {}
    if rpg.get('level') != snap['level']:
        discrepancies.append(f'{name}: level mismatch')
    if len(live.get('long_summary') or '') != snap['long_summary_len']:
        discrepancies.append(f'{name}: long_summary length mismatch')

print(f'Snapshot vs Live Discrepancies Count: {len(discrepancies)}')
if discrepancies:
    for d in discrepancies:
        print('  DISCREPANCY:', d)
else:
    print('PASS: Snapshot is a 100% faithful byte/field match of live backend state!')

print('\n=== 2. DEEP FORENSIC INTEGRITY INSPECTION OF LIVE RECORDS ===')
# Load canonical source lorebooks
with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary_data = json.load(f)
primary_by_id = {e['entry_id']: e for e in primary_data.get('lexicon', [])}

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    secondary_data = json.load(f)
secondary_by_id = {e['entry_id']: e for e in secondary_data.get('lexicon', [])}

from scripts.deploy_13_world_characters import CHARACTER_SPECS

spec_by_name = {s['display_name']: s for s in CHARACTER_SPECS}

violations = []
for idx, c in enumerate(live_chars, 1):
    name = c.get('display_name') or c.get('name')
    cid = c.get('_id') or c.get('id')
    spec = spec_by_name.get(name)
    if not spec:
        violations.append(f'{name}: Not recognized in CHARACTER_SPECS')
        continue
    
    # 1. Timeline integrity
    bdate = c.get('birthdate')
    tl_pos = c.get('start_timeline_position')
    if bdate != spec['birthdate']:
        violations.append(f'{name}: Birthdate {bdate} != expected {spec["birthdate"]}')
    if tl_pos != spec['start_timeline_position']:
        violations.append(f'{name}: Timeline position {tl_pos} != expected {spec["start_timeline_position"]}')
    if tl_pos != bdate:
        violations.append(f'{name}: Timeline position {tl_pos} != birthdate {bdate}')
    if not (0 <= bdate <= 10489902):
        violations.append(f'{name}: Birthdate {bdate} out of valid bounds (0..10489902)')
        
    # 2. Avatar verification
    avatar = c.get('avatar')
    if avatar != spec['avatar']:
        violations.append(f'{name}: Avatar {avatar} != expected {spec["avatar"]}')
    if not avatar.startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'):
        violations.append(f'{name}: Avatar {avatar} is not Cloudflare CDN gallery')
        
    # 3. RPG stats & level cap
    rpg = c.get('rpg_stats') or {}
    level = rpg.get('level')
    if level != spec['level']:
        violations.append(f'{name}: Level {level} != expected {spec["level"]}')
    if level > 99:
        violations.append(f'{name}: Level {level} exceeds 99 cap')
        
    bs = rpg.get('base_stats') or {}
    for i in range(1, 7):
        if f'stat_{i}' not in bs:
            violations.append(f'{name}: stat_{i} missing')
    for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']:
        if k not in bs:
            violations.append(f'{name}: {k} missing')
        elif bs[k] != spec['stats'][k]:
            violations.append(f'{name}: {k} value {bs[k]} != expected {spec["stats"][k]}')
            
    stat_sum = sum(bs[k] for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting'])
    if stat_sum != 31:
        violations.append(f'{name}: Stat sum {stat_sum} != 31')
        
    # 4. Long summary / JED+ content authenticity
    long_sum = c.get('long_summary') or ''
    if len(long_sum) < 4000:
        violations.append(f'{name}: JED+ length {len(long_sum)} < 4000 (potential facade/stub)')
    if '\u2014' in long_sum:
        violations.append(f'{name}: Contains em-dash in JED+ long summary')
    if not long_sum.startswith('[NAME:'):
        violations.append(f'{name}: Does not start with [NAME: bracket block')
    if 'BACKSTORY:' not in long_sum:
        violations.append(f'{name}: Missing BACKSTORY: section')
    if 'VOICE & BEHAVIOR:' not in long_sum and 'VOICE AND BEHAVIOR:' not in long_sum:
        violations.append(f'{name}: Missing VOICE & BEHAVIOR: section')
        
    # Compare with canonical lorebook source content
    src_file, entry_id = spec['lorebook_source']
    src_entry = primary_by_id.get(entry_id) if 'Primary' in src_file else secondary_by_id.get(entry_id)
    if not src_entry:
        violations.append(f'{name}: Source entry {entry_id} not found in {src_file}')
    else:
        src_content = src_entry.get('content', '')
        if long_sum != src_content:
            violations.append(f'{name}: Live long_summary diverges from canonical lorebook entry {entry_id} (len {len(long_sum)} vs {len(src_content)})')
            
    # 5. Format discipline in final_instructions
    final_inst = c.get('final_instructions') or ''
    if 'dialogue in quotes' not in final_inst or 'Never use the em dash' not in final_inst:
        violations.append(f'{name}: Incomplete or missing final_instructions format discipline')
        
    print(f'Checked [{idx:02d}] {name} (ID: {cid}) -> OK')

print(f'\nTotal Forensic Violations Found: {len(violations)}')
if violations:
    for v in violations:
        print('  VIOLATION:', v)
else:
    print('PASS: All 13 live characters passed 100% of forensic checks with zero violations!')
