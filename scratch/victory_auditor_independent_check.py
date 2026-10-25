"""
Victory Auditor Independent Script
Auditor: victory_auditor_6
Strictly independent verification of World _YpX47fNraQFw2dD7TdycJ
"""

import os
import sys
import json
import urllib.request
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

TOKEN_PATH = os.path.join(os.path.dirname(__file__), 'wyvern_token.txt')
SNAPSHOT_PATH = os.path.join(os.path.dirname(__file__), 'world_new_deployed.json')
BASE_URL = 'https://app.wyvern.chat/api'
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
    TOKEN = f.read().strip()

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'VictoryAuditor/6.0'
}

def get(endpoint):
    req = urllib.request.Request(f"{BASE_URL}{endpoint}", headers=HEADERS, method='GET')
    with urllib.request.urlopen(req) as r:
        return r.status, json.loads(r.read().decode('utf-8'))

print("=== VICTORY AUDITOR INDEPENDENT LIVE CHECK ===")

# 1. World endpoint
s, w = get(f'/worlds/{WORLD_ID}')
assert s == 200, f"Status: {s}"
print(f"World: '{w.get('name')}', age: {w.get('world_age')}, visibility: {w.get('visibility')}")
assert w.get('world_age') == 10489902
assert w.get('visibility') == 'private'
assert w.get('rating') == 'explicit'

# Temporal verification
epoch = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc)
computed_dt = epoch + timedelta(hours=w.get('world_age'))
print(f"Computed datetime: {computed_dt.strftime('%A, %d %B %Y %H:%M:%S UTC')}")
assert computed_dt.year == 2024
assert computed_dt.month == 8
assert computed_dt.day == 26
assert computed_dt.hour == 6
assert computed_dt.weekday() == 0 # Monday

# Features & Stats
wf = w.get('world_features', {})
assert wf.get('inventory') is True
assert wf.get('currency') is True
assert wf.get('combat') is True
assert wf.get('rpg_stats') is True
assert wf.get('relationships') is True
assert wf.get('show_party_stats') is False
assert wf.get('show_species_info') is False
assert wf.get('ships') is False
assert wf.get('creature_catcher') is False

sc = w.get('stat_config', {})
assert sc.get('base_value') == 1
assert sc.get('point_budget') == 25
stats = [s.get('abbreviation') for s in sc.get('stats', [])]
print(f"Stats: {stats}")
assert sorted(stats) == sorted(['MGT', 'RES', 'AGI', 'WIT', 'PRS', 'SCT'])

# 2. Environments
se, envs = get(f'/worlds/environments/world/{WORLD_ID}')
assert se == 200
print(f"Environments count: {len(envs)}")
assert len(envs) == 7

# 3. Locations
sl, locs = get(f'/worlds/locations/world/{WORLD_ID}')
assert sl == 200
print(f"Locations count: {len(locs)}")
assert len(locs) == 188

# Check orphans
loc_ids = set(l.get('id') or l.get('_id') for l in locs)
orphans = []
verve = None
for l in locs:
    if l.get('name') == 'The Verve':
        verve = l
    p = l.get('parent_location')
    if p:
        pid = p.get('id') or p.get('_id') if isinstance(p, dict) else p
        if pid not in loc_ids:
            orphans.append((l.get('name'), pid))
assert len(orphans) == 0, f"Orphans found: {orphans}"
print("Orphans count: 0 (verified)")

assert verve is not None
v_parent = verve.get('parent_location')
v_pid = v_parent.get('id') or v_parent.get('_id') if isinstance(v_parent, dict) else v_parent
parent_name = next(l.get('name') for l in locs if (l.get('id') or l.get('_id')) == v_pid)
print(f"The Verve parent: {parent_name}")
assert parent_name == 'Bluemoon'
print(f"The Verve included_lexicon_entries: {verve.get('included_lexicon_entries')}")
assert len(verve.get('included_lexicon_entries', [])) == 3

# 4. Lexicon
slex, lex = get(f'/worlds/lexicon/world/{WORLD_ID}')
assert slex == 200
print(f"Lexicon count: {len(lex)}")
assert len(lex) == 707
for item in lex:
    assert item.get('scan_persona') is True
    assert item.get('whole_words_only') is True

# 5. Linked characters
slc, lchars = get(f'/worlds/linked-characters/{WORLD_ID}')
assert slc == 200
print(f"Linked characters count: {len(lchars)}")
assert len(lchars) == 8

# 6. Snapshot parity
with open(SNAPSHOT_PATH, 'r', encoding='utf-8') as f:
    snap = json.load(f)
assert json.dumps(snap['entries'], sort_keys=True) == json.dumps(snap['lexicon'], sort_keys=True)
print("Snapshot entries == lexicon byte-for-byte parity: PASS")

print("=== ALL INDEPENDENT CHECKS PASSED WITH FLYING COLORS ===")
