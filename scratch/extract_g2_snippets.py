import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

doc_dir = 'docs/claude_project_docs'
docs = {}
for fname in os.listdir(doc_dir):
    with open(os.path.join(doc_dir, fname), encoding='utf-8', errors='ignore') as f:
        docs[fname] = f.read()

# We want to find exact age or birthdate mentions for all characters in g2_list
found_specs = {}

for item in g2_list:
    name = item['name']
    cid = item['id']
    
    clean_name = name.split('(')[0].split('"')[0].strip()
    # If name has multiple words, search for full clean name
    snippets = []
    for fname, content in docs.items():
        if clean_name.lower() in content.lower():
            for p in content.split('\n\n'):
                if clean_name.lower() in p.lower():
                    # check if paragraph has age, birthdate, or years
                    if any(w in p.lower() for w in ['birthdate', 'start position', 'anni', 'age', 'nato', 'nata', 'born', '19', '20']):
                        for l in p.split('\n'):
                            if any(w in l.lower() for w in ['birthdate', 'start position', 'anni', 'age', 'nato', 'nata', 'born']) and (clean_name.lower() in l.lower() or len(l) < 150):
                                snippets.append(f"{fname}: {l.strip()}")
                                
    found_specs[name] = snippets[:6]

with open('scratch/g2_all_extracted_snippets.json', 'w', encoding='utf-8') as f:
    json.dump(found_specs, f, indent=2, ensure_ascii=False)

for name, snips in found_specs.items():
    print(f"=== {name} ===")
    if not snips:
        print("   (NO SNIPPETS FOUND)")
    for s in snips[:3]:
        print(f"   {s[:110]}")
