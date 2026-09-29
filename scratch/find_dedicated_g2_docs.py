import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

doc_dir = 'docs/claude_project_docs'

# Read all files
all_files = {}
for fname in os.listdir(doc_dir):
    with open(os.path.join(doc_dir, fname), encoding='utf-8', errors='ignore') as f:
        all_files[fname] = f.read()

def find_dedicated_doc(name):
    # Try finding files dedicated to this character
    first = name.split()[0].replace('"', '')
    last = name.split()[-1].replace('"', '')
    
    candidates = []
    for fname, content in all_files.items():
        fn_lower = fname.lower()
        if (first.lower() in fn_lower and last.lower() in fn_lower) or (f"{first}_{last}".lower() in fn_lower):
            candidates.append((fname, content))
        elif len(name.split()) == 1 and first.lower() in fn_lower:
            candidates.append((fname, content))
    return candidates

char_data = {}

for item in g2_list:
    name = item['name']
    cid = item['id']
    docs = find_dedicated_doc(name)
    
    char_data[name] = {
        'id': cid,
        'dedicated_docs': [d[0] for d in docs]
    }
    
    print(f"=== {name} ({len(docs)} docs) ===")
    for fname, content in docs:
        print(f"  Doc: {fname}")
        # Search for birthdate, start position, age, timeline in content
        for line in content.split('\n'):
            line_str = line.strip()
            if any(k in line_str.lower() for k in ['birthdate', 'start position', 'timeline', 'start_timeline_position', 'data di nascita', 'età anagrafica']):
                print(f"    {line_str[:100]}")

with open('scratch/g2_dedicated_docs.json', 'w', encoding='utf-8') as f:
    json.dump(char_data, f, indent=2, ensure_ascii=False)
