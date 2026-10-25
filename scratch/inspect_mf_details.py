import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/parsed_modernfantasy.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split('============================== SECTION: ')

mf_chars = []
mf_lore = {}

for s in sections[1:]:
    lines = [l.strip() for l in s.split('\n') if l.strip()]
    if not lines:
        continue
    # sec_name is before the first space or parenthesis
    header_line = lines[0].replace(' ==============================', '').strip()
    sec_name = re.sub(r'\s*\(\d+\s*lines\)', '', header_line).strip()
    content = lines[1:]
    
    if sec_name in ['GLOBAL', 'section06', 'faq', 'srf', 'underworld']:
        mf_lore[sec_name] = content
    else:
        mf_chars.append({'id': sec_name, 'content': content})

print(f"Total Modern Fantasy characters found: {len(mf_chars)}")
print(f"Lore sections: {list(mf_lore.keys())}")

print("\n=== MODERN FANTASY OVERVIEW (section06) ===")
for l in mf_lore.get('section06', []):
    print(f"  {l}")

print("\n=== SRF (Supernatural Reserve Forces) ===")
for l in mf_lore.get('srf', []):
    print(f"  {l}")

print("\n=== UNDERWORLD ===")
for l in mf_lore.get('underworld', []):
    print(f"  {l}")

print("\n=== FAQ ===")
for l in mf_lore.get('faq', []):
    print(f"  {l}")
