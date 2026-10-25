import glob, re

content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()

# Look for exports of 98043: Bn, at, fN, pO, vK
for export_name in ['pO', 'vK', 'fN', 'Bn', 'at']:
    matches = list(re.finditer(r'\b[a-zA-Z0-9_\$]+\.' + export_name + r'\b', content))
    print(f"Export {export_name} usages: {len(matches)}")
    for m in matches[:5]:
        idx = m.start()
        print(f"  {content[max(0, idx-100):min(len(content), idx+200)]}")
        print("  " + "-"*40)
