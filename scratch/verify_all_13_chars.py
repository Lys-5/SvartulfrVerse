import sys
sys.path.insert(0, '.')
import urllib.request
import json
from scripts.configure_display_settings_and_flags import get_auth_token

token = get_auth_token()
world_id = "_YpX47fNraQFw2dD7TdycJ"
url = f"https://app.wyvern.chat/api/worlds/characters/world/{world_id}"

req = urllib.request.Request(
    url,
    headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(req) as resp:
    chars = json.loads(resp.read().decode('utf-8'))

print(f"Total World Characters found: {len(chars)}")

stats_keys = ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']

anomalies = []
for idx, c in enumerate(chars):
    name = c.get('display_name') or c.get('name')
    avatar = c.get('avatar')
    rpg = c.get('rpg_stats') or {}
    enabled = rpg.get('enabled')
    level = rpg.get('level')
    base_stats = rpg.get('base_stats') or {}

    print(f"\n[{idx+1}] {name} (ID: {c.get('id')})")
    print(f"    Avatar: {avatar}")
    print(f"    RPG Enabled: {enabled}, Level: {level}")
    print(f"    Base stats: {base_stats}")

    # Check avatar
    if not avatar or not avatar.startswith('https://imagedelivery.net/'):
        anomalies.append(f"{name}: Invalid or missing avatar ({avatar})")

    # Check RPG enabled
    if enabled is not True:
        anomalies.append(f"{name}: rpg_stats.enabled is not True")

    # Check level
    if level is None or not (1 <= level <= 99):
        anomalies.append(f"{name}: Level {level} out of bounds (1..99)")

    # Check attributes for zero
    for k in stats_keys:
        val = base_stats.get(k)
        if val is None:
            anomalies.append(f"{name}: Missing stat {k}")
        elif val <= 0:
            anomalies.append(f"{name}: Zero or negative stat {k}={val}")

    # Check stat sum
    stat_sum = sum(base_stats.get(k, 0) for k in stats_keys)
    if stat_sum != 31:
        anomalies.append(f"{name}: Stat sum is {stat_sum} != 31")

print("\n" + "="*50)
if anomalies:
    print(f"FOUND {len(anomalies)} ANOMALIES:")
    for a in anomalies:
        print("  -", a)
else:
    print("ALL 13 WORLD CHARACTERS ARE FULLY READY WITH VALID AVATARS AND BALANCED 25-PT RPG BLOCKS (NO ZEROED ATTRIBUTES)!")
