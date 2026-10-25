import sys
import os
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/io_succ.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("==================================================")
print("             ANALISI DI IO-SUCC.UWU.AI            ")
print("==================================================")

# Let's extract by sections
sections = [
    'home-section',
    'map-section',
    'solarton-section',
    'cums-section',
    'clubs-section',
    'sports-section',
    'degrees-section',
    'species-section',
    'faq-section'
]

# In Carrd, all siblings between one section marker and the next belong to that section
all_elements = soup.find('div', id='main') or soup.body

# Let's group all text elements by which section marker precedes them
sections_content = {}
current_sec = 'HEADER / GLOBAL'
sections_content[current_sec] = []

for elem in all_elements.find_all(True, recursive=True):
    eid = elem.get('id', '')
    if eid in sections:
        current_sec = eid
        if current_sec not in sections_content:
            sections_content[current_sec] = []
    
    # We only want text leaves or specific containers to avoid duplicate text
    if elem.name in ['p', 'h1', 'h2', 'h3', 'h4', 'li', 'td', 'th']:
        txt = elem.get_text(separator=' ', strip=True)
        if txt and len(txt) > 5:
            # check if not already in list
            if txt not in sections_content[current_sec]:
                sections_content[current_sec].append(txt)

with open('scratch/sites_raw/parsed_succ.txt', 'w', encoding='utf-8') as out:
    for sec, lines in sections_content.items():
        header = f"\n{'='*30} {sec} {'='*30}\n"
        out.write(header)
        print(f"Section {sec}: {len(lines)} items")
        for line in lines:
            out.write(f"- {line}\n")

print("Parsed SUCC written to scratch/sites_raw/parsed_succ.txt")
