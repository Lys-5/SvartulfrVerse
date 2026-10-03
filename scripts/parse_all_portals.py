import os
import sys
import json
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

portals = {
    'succ': {
        'file': r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2944\content.md',
        'base_url': 'https://io-succ.uwu.ai/'
    },
    'ddm': {
        'file': r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2946\content.md',
        'base_url': 'https://io-ddm.uwu.ai/'
    },
    'astral': {
        'file': r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2948\content.md',
        'base_url': 'https://io-astral.uwu.ai/'
    },
    'modernfantasy': {
        'file': r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2830\content.md',
        'base_url': 'https://io-modernfantasy.uwu.ai/'
    }
}

parsed_results = {}

for portal_name, pinfo in portals.items():
    fpath = pinfo['file']
    base_url = pinfo['base_url']
    if not os.path.exists(fpath):
        print(f"File non trovato per {portal_name}: {fpath}")
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        raw = f.read()
        
    soup = BeautifulSoup(raw, 'html.parser')
    
    title = soup.title.string.strip() if soup.title else portal_name
    print(f"\n=======================================================")
    print(f"PORTALE: {portal_name.upper()} ({title})")
    print(f"=======================================================")
    
    sections = soup.find_all('section')
    print(f"Totale sezioni: {len(sections)}")
    
    portal_data = {
        'portal': portal_name,
        'title': title,
        'base_url': base_url,
        'sections': {}
    }
    
    for s in sections:
        sec_id = s.get('id', '')
        if not sec_id:
            continue
            
        sec_imgs = []
        for img in s.find_all('img'):
            src = img.get('src')
            alt = img.get('alt', '')
            if src and not src.startswith('data:'):
                full_src = src if src.startswith('http') else base_url + src.lstrip('/')
                sec_imgs.append({'alt': alt, 'url': full_src})
                
        # Style urls
        for tag in s.find_all(style=True):
            style = tag.get('style', '')
            m = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', style)
            for url in m:
                if not url.startswith('data:'):
                    full_src = url if url.startswith('http') else base_url + url.lstrip('/')
                    sec_imgs.append({'alt': 'background', 'url': full_src})
                    
        full_text = s.get_text(separator='\n', strip=True)
        lines = [l.strip() for l in full_text.split('\n') if l.strip()]
        
        portal_data['sections'][sec_id] = {
            'id': sec_id,
            'title': lines[0] if lines else sec_id,
            'lines': lines,
            'text': full_text,
            'images': sec_imgs
        }
        
    parsed_results[portal_name] = portal_data
    
    # Save individual JSON
    out_file = f"exports/portal_{portal_name}_extracted.json"
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(portal_data, f, indent=2, ensure_ascii=False)
    print(f"Salvati dati estratti in {out_file} ({len(portal_data['sections'])} sezioni)")

print("\n--- Estrazione completata per tutti i portali! ---")
