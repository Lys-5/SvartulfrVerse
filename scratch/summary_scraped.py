import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_dates_scraped.json', encoding='utf-8') as f:
    scraped = json.load(f)

matched = []
unmatched = []

for name, data in scraped.items():
    cur_bd = data['current_bd']
    hours = data['found_hours']
    dates = data['found_dates']
    
    if cur_bd is not None:
        matched.append((name, f"EXISTING: {cur_bd}"))
    elif hours:
        matched.append((name, f"HOURS: {hours[0][0]} ({hours[0][1][:60]})"))
    elif any(d[1] is not None for d in dates):
        valid_d = [d for d in dates if d[1] is not None]
        matched.append((name, f"DATE: {valid_d[0][0]} -> {valid_d[0][1]} ({valid_d[0][2][:60]})"))
    else:
        unmatched.append(name)

print(f"Matched with exact hours/dates: {len(matched)} / {len(scraped)}")
print(f"Unmatched: {len(unmatched)} / {len(scraped)}")

print("\n--- MATCHED EXAMPLES ---")
for name, info in matched[:20]:
    print(f"{name:30s} | {info}")

print("\n--- UNMATCHED CHARACTERS ---")
for name in unmatched:
    print(f" - {name}")
