import sys
import os
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/io_modernfantasy.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("==================================================")
print("        PARSING IO-MODERNFANTASY.UWU.AI           ")
print("==================================================")

# Let's inspect sections
all_elements = soup.find('div', id='main') or soup.body

sections = {}
current_sec = 'GLOBAL'
sections[current_sec] = []

for elem in all_elements.find_all(True, recursive=True):
    eid = elem.get('id', '')
    if eid.endswith('-section'):
        current_sec = eid.replace('-section', '')
        if current_sec not in sections:
            sections[current_sec] = []
    
    if elem.name in ['h1', 'h2', 'h3', 'h4', 'p', 'li', 'td', 'th', 'blockquote']:
        txt = elem.get_text(separator=' ', strip=True)
        if txt and len(txt) > 5:
            if txt not in sections[current_sec]:
                sections_content = sections[current_sec]
                # Avoid inserting child if already included
                sections_content.append(txt)

print(f"Found {len(sections)} sections in io-modernfantasy")

with open('scratch/sites_raw/parsed_modernfantasy.txt', 'w', encoding='utf-8') as out:
    for sec, lines in sections.items():
        out.write(f"\n{'='*30} SECTION: {sec} ({len(lines)} lines) {'='*30}\n")
        for l in lines:
            out.write(f"{l}\n")

print("Wrote to scratch/sites_raw/parsed_modernfantasy.txt")
