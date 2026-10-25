import sys
import os
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

def parse_char_site(filename, sitename):
    with open(f'scratch/sites_raw/{filename}', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    print(f"==================================================")
    print(f"          PARSING {sitename} ({filename})         ")
    print(f"==================================================")
    
    # In Carrd char sites, characters have sections like #andy, #casey, #dullahan, etc.
    # Find all section markers or containers
    all_elements = soup.find('div', id='main') or soup.body
    
    char_sections = {}
    current_sec = 'INTRO'
    char_sections[current_sec] = []
    
    for elem in all_elements.find_all(True, recursive=True):
        eid = elem.get('id', '')
        if eid.endswith('-section'):
            current_sec = eid.replace('-section', '')
            if current_sec not in char_sections:
                char_sections[current_sec] = []
        
        if elem.name in ['h1', 'h2', 'h3', 'h4', 'p', 'li', 'td', 'th']:
            txt = elem.get_text(separator=' ', strip=True)
            if txt and len(txt) > 5:
                if txt not in char_sections[current_sec]:
                    char_sections[current_sec].append(txt)
                    
    print(f"Found {len(char_sections)} sections in {sitename}")
    
    out_file = f'scratch/sites_raw/parsed_{filename}.txt'
    with open(out_file, 'w', encoding='utf-8') as out:
        for sec, lines in char_sections.items():
            out.write(f"\n{'='*30} SECTION: {sec} {'='*30}\n")
            for l in lines:
                out.write(f"{l}\n")
    print(f"Written to {out_file}")
    return char_sections

chars1 = parse_char_site('io_succ_char.html', 'SUCC CHARACTERS 1')
chars2 = parse_char_site('io_succc.html', 'SUCC CHARACTERS 2')
