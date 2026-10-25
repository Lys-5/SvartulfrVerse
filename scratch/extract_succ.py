import sys
import os
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/io_succ.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

print("=== SEARCHING FOR SECTIONS & NAV ===")
for a in soup.find_all('a', href=True):
    href = a['href']
    text = a.get_text(strip=True)
    if text:
        print(f"Link: {text:30} -> {href}")

print("\n=== EXTRACTING ALL TEXT BLOCKS ===")
# Carrd stores text in divs with id like text01, text02, etc.
text_elements = soup.find_all(True, id=re.compile(r'^(text|table|list|container)'))
print(f"Found {len(text_elements)} text-like elements")

output_lines = []
for elem in text_elements:
    eid = elem.get('id', '')
    txt = elem.get_text(separator='\n', strip=True)
    if txt and len(txt) > 10:
        output_lines.append(f"--- ID: {eid} ---\n{txt}\n")

with open('scratch/sites_raw/succ_all_text.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(output_lines))

print(f"Wrote {len(output_lines)} blocks to scratch/sites_raw/succ_all_text.txt")
