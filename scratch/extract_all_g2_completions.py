import os
import re
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

g2_by_name = {c['name']: c['id'] for c in g2_list}

doc_dir = 'docs/claude_project_docs'

results = {}

for item in g2_list:
    name = item['name']
    cid = item['id']
    results[name] = {
        'id': cid,
        'doc_sources': [],
        'extracted_fields': {}
    }

for fname in os.listdir(doc_dir):
    fpath = os.path.join(doc_dir, fname)
    with open(fpath, encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    for name in g2_by_name:
        # Check if name is in title or content
        clean_name = name.split('(')[0].split('"')[0].strip()
        if clean_name.lower() in fname.lower() or (f"# {clean_name}".lower() in content.lower()) or (f"**{clean_name}**".lower() in content.lower()):
            results[name]['doc_sources'].append(fname)
            
            # Extract fields like Birthdate, Start Position, Age, Attitudes, Outfits
            for line in content.split('\n'):
                line_str = line.strip()
                if any(k in line_str.lower() for k in ['birthdate', 'start position', 'timeline', 'attitudes', 'outfits', 'età anagrafica', 'data di nascita']):
                    if clean_name.lower() in line_str.lower() or len(line_str) < 120:
                        results[name]['extracted_fields'][line_str[:50]] = line_str

with open('scratch/g2_completions_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

for name, d in results.items():
    docs_str = ", ".join(d['doc_sources'][:3])
    print(f"{name:30s} | Docs ({len(d['doc_sources'])}): {docs_str[:50]}")
    for k, v in list(d['extracted_fields'].items())[:3]:
        print(f"    -> {v}")
