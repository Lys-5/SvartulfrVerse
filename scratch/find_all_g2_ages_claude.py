import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('drive/claude_export/extracted/projects/projects/01a03cfa-cebb-74ef-be69-f24d0ae96ed0.json', encoding='utf-8') as f:
    claude_proj = json.load(f)

docs = {d['filename']: d['content'] for d in claude_proj.get('docs', [])}

results = {}

for c in g2_list:
    name = c['name']
    cid = c['id']
    results[name] = {
        'id': cid,
        'ages_found': set(),
        'bdays_found': set(),
        'docs_matched': set()
    }
    
    clean_name = name.split('(')[0].split('"')[0].strip()
    
    for fname, content in docs.items():
        if clean_name.lower() in content.lower():
            results[name]['docs_matched'].add(fname)
            
            # Search for age patterns near name or in tables
            # e.g. | Name | Age | or Name ... 24 years old / age 24
            lines = content.split('\n')
            for line in lines:
                if clean_name.lower() in line.lower():
                    # check table: | Name | ... | Age | ...
                    table_parts = [p.strip() for p in line.split('|')]
                    for p in table_parts:
                        if re.match(r'^\d{1,4}$', p):
                            results[name]['ages_found'].add(p)
                    # check regex in line
                    m_age = re.findall(r'(?:age|anni|aged)\s*[:=]?\s*(\d{1,4})', line, re.I)
                    if m_age:
                        results[name]['ages_found'].update(m_age)
                    m_yo = re.findall(r'(\d{1,4})\s*(?:anni|-year-old|years old|yo\b)', line, re.I)
                    if m_yo:
                        results[name]['ages_found'].update(m_yo)
                    m_bday = re.findall(r'birth(?:day|date)\s*[:=]?\s*([A-Za-z]+\s+\d{1,2}(?:,\s*\d{4})?|\d{4})', line, re.I)
                    if m_bday:
                        results[name]['bdays_found'].update(m_bday)

# Convert sets to lists
output_data = {}
for name, data in results.items():
    output_data[name] = {
        'id': data['id'],
        'ages_found': sorted(list(data['ages_found']), key=lambda x: int(x) if x.isdigit() else 999),
        'bdays_found': list(data['bdays_found']),
        'docs_count': len(data['docs_matched']),
        'top_docs': list(data['docs_matched'])[:3]
    }

with open('scratch/g2_ages_from_claude_docs.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Processed {len(output_data)} characters.")
count_with_age = sum(1 for d in output_data.values() if d['ages_found'])
print(f"Characters with age found in Claude docs: {count_with_age} / {len(output_data)}")

for name, d in output_data.items():
    print(f"{name:30s} | Ages: {str(d['ages_found']):25s} | Bdays: {str(d['bdays_found']):25s} | Docs: {d['docs_count']}")
