import json

with open('scratch/g2_ages_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"{'NAME':30s} | {'ID':22s} | {'AGE_RAW':20s} | {'BDAY_RAW':25s} | {'EXISTING_BD'}")
print("-" * 115)
for d in data:
    name = d['name']
    cid = d['id']
    age = str(d['age_raw'])
    bday = str(d['bday_raw'])
    ebd = str(d['existing_bd'])
    print(f"{name:30s} | {cid:22s} | {age[:20]:20s} | {bday[:25]:25s} | {ebd}")
