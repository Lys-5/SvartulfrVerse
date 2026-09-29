import json
import re

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('drive/claude_export/extracted/projects/projects/01a03cfa-cebb-74ef-be69-f24d0ae96ed0.json', encoding='utf-8') as f:
    claude_proj = json.load(f)

docs = claude_proj.get('docs', [])

print(f"Loaded {len(docs)} documents from Claude Project.")

# Search each doc for character mentions, ages, birthdays, outfits
char_hits = {c['name']: [] for c in g2_list}

for doc in docs:
    fname = doc.get('filename', '')
    content = doc.get('content', '')
    
    for c in g2_list:
        name = c['name']
        first_name = name.split()[0].replace('"', '')
        if len(first_name) < 4:
            first_name = name # avoid short match like "Dan" or "Rev"
            
        if name.lower() in content.lower() or (len(name.split()) > 1 and first_name.lower() in content.lower()):
            # Find paragraphs or lines mentioning name
            lines = content.split('\n')
            matched_snippets = []
            for line in lines:
                if name.lower() in line.lower():
                    matched_snippets.append(line.strip())
            if matched_snippets:
                char_hits[name].append({
                    'doc': fname,
                    'snippets': matched_snippets[:5]
                })

# Print summary of findings
found_count = 0
for name, hits in char_hits.items():
    if hits:
        found_count += 1
        print(f"=== {name} ({len(hits)} docs) ===")
        for h in hits[:2]:
            print(f"  [{h['doc']}]: {h['snippets'][0][:120]}")

print(f"\nCharacters with documentation hits: {found_count} / {len(g2_list)}")

with open('scratch/g2_claude_docs_hits.json', 'w', encoding='utf-8') as f:
    json.dump(char_hits, f, indent=2, ensure_ascii=False)
