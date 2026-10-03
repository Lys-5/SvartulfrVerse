import os
import sys
import json
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

html_path = r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2830\content.md'
with open(html_path, 'r', encoding='utf-8') as f:
    raw = f.read()

soup = BeautifulSoup(raw, 'html.parser')

base_url = 'https://io-modernfantasy.uwu.ai/'

sections = soup.find_all('section')
extracted_data = {
    'characters': {},
    'settings': {},
    'galleries': {}
}

for s in sections:
    sec_id = s.get('id', '')
    if not sec_id:
        continue
    
    # Check if character section
    # Usually ending in -section or specific names
    text_blocks = []
    for el in s.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'span', 'div']):
        # If element has direct text
        t = el.get_text(separator=' ', strip=True)
        if t and t not in text_blocks and len(t) > 2:
            # avoid adding parent if identical to child
            text_blocks.append(t)
            
    # Find images in this section
    sec_imgs = []
    for img in s.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', '')
        if src and not src.startswith('data:'):
            full_src = src if src.startswith('http') else base_url + src.lstrip('/')
            sec_imgs.append({'alt': alt, 'url': full_src})
            
    # Also find background images or style URLs
    for tag in s.find_all(style=True):
        style = tag.get('style', '')
        m = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', style)
        for url in m:
            if not url.startswith('data:'):
                full_src = url if url.startswith('http') else base_url + url.lstrip('/')
                sec_imgs.append({'alt': 'background', 'url': full_src})

    full_text = s.get_text(separator='\n', strip=True)
    
    if sec_id.endswith('-section') or sec_id in ['srf-section', 'underworld-section', 'faq-section']:
        extracted_data['characters'][sec_id] = {
            'id': sec_id,
            'text': full_text,
            'images': sec_imgs
        }
    else:
        extracted_data['settings'][sec_id] = {
            'id': sec_id,
            'text': full_text,
            'images': sec_imgs
        }

output_path = 'exports/modernfantasy_portal_raw.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, indent=2, ensure_ascii=False)

print(f"Estratte {len(extracted_data['characters'])} sezioni principali/personaggi e {len(extracted_data['settings'])} altre sezioni.")
print(f"Salvate in {output_path}")
