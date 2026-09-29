import json

with open('scratch/g2_full_analysis.json', encoding='utf-8') as f:
    report = json.load(f)

print(f"{'NAME':28s} | {'BDAY FIELD':22s} | {'AGE FIELD':32s} | {'EXISTING BD':12s} | {'AGE MENTIONS'}")
print("-" * 120)
for r in report:
    name = r['name']
    bday = r['bday_field']
    age = r['age_field']
    bd = str(r['birthdate'])
    mentions = str(r['age_mentions'])
    if bday or r['birthdate'] is not None or 'born' in age.lower() or r['age_mentions']:
        print(f"{name:28s} | {bday:22s} | {age:32s} | {bd:12s} | {mentions}")
