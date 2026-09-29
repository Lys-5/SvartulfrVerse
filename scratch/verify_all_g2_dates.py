import json
import sys
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

EP = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc)

def d_to_h(y, m, d, h=0):
    dt = datetime(y, m, d, h, 0, 0, tzinfo=timezone.utc)
    return int((dt - EP).total_seconds() // 3600)

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

# Import known_dates from resolve_g2_all.py
from resolve_g2_all import known_dates

WORLD_AGE = 10486470 # 2024-04-05 06:00 UTC

print(f"{'NAME':30s} | {'ID':22s} | {'Y-M-D':12s} | {'HOURS':10s} | {'AGE IN 2024':12s}")
print("-" * 95)

all_valid = True
for item in g2_list:
    name = item['name']
    cid = item['id']
    if name not in known_dates:
        print(f"ERROR: {name} not in known_dates!")
        all_valid = False
        continue
    y, m, d = known_dates[name]
    hours = d_to_h(y, m, d)
    
    # Calculate age in 2024
    age = 2024 - y
    if (m, d) > (4, 5):
        age -= 1
        
    if hours > WORLD_AGE:
        print(f"ERROR: {name} hours {hours} > WORLD_AGE {WORLD_AGE}!")
        all_valid = False
    elif hours < 0:
        print(f"WARNING: {name} hours {hours} < 0 (before 827 AD)")
    else:
        print(f"{name:30s} | {cid:22s} | {f'{y}-{m:02d}-{d:02d}':12s} | {hours:<10d} | {age} years")

print(f"\nAll 83 G2 characters validated: {all_valid}")
