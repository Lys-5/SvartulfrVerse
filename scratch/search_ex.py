import re

with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

matches = [m.start() for m in re.finditer(r'\beX\s*=', c66)]
print("eX= matches:", matches)
for idx in matches:
    print(c66[idx-50:idx+300])
