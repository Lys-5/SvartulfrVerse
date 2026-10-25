import os
import json
import urllib.request
import urllib.error

print("=== CHECK 3: JARED THOMPSON DELETION & SNAPSHOT AUDIT ===")

# 1. Inspect snapshot files
snapshot_files = [
    'scratch/backup_deleted_cards_20261021/DELETED_Jared_Thompson__xJVPtBLL3dxy69RLKL9X9.json',
    'scratch/jared_pre_delete_snapshot__xJVPtBLL3dxy69RLKL9X9.json'
]

snapshots_valid = True
for sf in snapshot_files:
    if not os.path.exists(sf):
        print(f"FAILED: Snapshot file {sf} does not exist!")
        snapshots_valid = False
        continue
    size = os.path.getsize(sf)
    print(f"Snapshot file: {sf} (Size: {size} bytes)")
    try:
        with open(sf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        c_id = data.get('id')
        c_name = data.get('name')
        print(f"  Parsed JSON successfully: id={c_id}, name={c_name}")
        if c_id != '_xJVPtBLL3dxy69RLKL9X9':
            print(f"  ERROR: Snapshot id {c_id} != _xJVPtBLL3dxy69RLKL9X9")
            snapshots_valid = False
        if not c_name or 'Jared' not in c_name:
            print(f"  ERROR: Character name {c_name} does not match Jared!")
            snapshots_valid = False
        # Check presence of detailed character fields
        desc = data.get('description', '')
        print(f"  Character description length: {len(desc)} characters")
        if len(desc) < 2000:
            print(f"  ERROR: Character description suspiciously short ({len(desc)})")
            snapshots_valid = False
    except Exception as e:
        print(f"  FAILED to parse {sf}: {e}")
        snapshots_valid = False

# 2. Check live API deletion
token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ForensicAuditor/1.0',
    'Content-Type': 'application/json'
}

# GET /characters/mine
req_mine = urllib.request.Request('https://app.wyvern.chat/api/characters/mine', headers=headers)
with urllib.request.urlopen(req_mine) as resp:
    mine_data = json.loads(resp.read().decode('utf-8'))

chars = mine_data.get('characters', [])
jared_in_mine = [c for c in chars if c.get('id') == '_xJVPtBLL3dxy69RLKL9X9' or 'Jared' in c.get('name', '')]

print(f"\nLive /characters/mine check:")
print(f"  Total characters in mine: {len(chars)}")
print(f"  Jared present in mine: {len(jared_in_mine) > 0}")
if len(jared_in_mine) > 0:
    print(f"  ERROR: Jared found in mine: {jared_in_mine}")

# Direct GET /characters/_xJVPtBLL3dxy69RLKL9X9
req_jared = urllib.request.Request('https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9', headers=headers)
jared_status = None
jared_body = None
try:
    with urllib.request.urlopen(req_jared) as resp:
        jared_status = resp.status
        jared_body = resp.read().decode('utf-8')
except urllib.error.HTTPError as e:
    jared_status = e.code
    jared_body = e.read().decode('utf-8')

print(f"\nDirect GET /api/characters/_xJVPtBLL3dxy69RLKL9X9:")
print(f"  HTTP Status: {jared_status}")
print(f"  Response Body: {jared_body}")

# Final assessment
is_deleted = (jared_status == 404 and len(jared_in_mine) == 0 and len(chars) == 8)
print(f"\nFinal Check 3 Result: {'CLEAN - GENUINE DELETION & SNAPSHOT VERIFIED' if (snapshots_valid and is_deleted) else 'INTEGRITY VIOLATION'}")
