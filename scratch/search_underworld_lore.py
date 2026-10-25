import re

with open('ARCHIVIO/01_Drafts/Core_Docs/Svartúlfr.md', 'r', encoding='utf-8') as f:
    text = f.read()

queries = [
    'Rory',
    'Ballantine',
    'Sully',
    'Sinners',
    'Jean-Luc',
    'Virtuoso',
    'Ambrosia',
    'Arthur Sinclair',
    'Ilya Volkov',
    'Vasile Ionescu',
    'Harbor',
    'Lab'
]

for q in ['Ambrosia', 'Rory\'s Estate', 'Sinners', 'Dr. Arthur Sinclair']:
    matches = [m.start() for m in re.finditer(re.escape(q), text, re.IGNORECASE)]
    print(f"Query '{q}': {len(matches)} occurrences")
    for idx in matches[:3]:
        start = max(0, idx - 100)
        end = min(len(text), idx + 400)
        print("--- SNIPPET ---")
        print(text[start:end].replace('\n', ' '))
