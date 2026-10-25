import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/parsed_modernfantasy.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split('============================== SECTION: ')
for s in sections[1:]:
    lines = s.strip().split('\n')
    sec_name = lines[0].replace(' ==============================', '').strip()
    print(f"--- {sec_name} ---")
    for l in lines[1:6]:
        if l.strip():
            print(f"  {l[:110]}")
