import json
import re
import sys

# Ensure utf-8 output or replace unprintable chars
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

d = json.load(open('scratch/mod93312_dump.json', encoding='utf-8'))
text = d['content'][0]['text']

# search for regex generation or speaker matching
matches = [m.start() for m in re.finditer(r'speaker|npc_info|first_name|regex', text, re.I)]
print(f"Total keyword matches: {len(matches)}")
for idx in matches[:10]:
    print("--- SNIPPET ---")
    print(text[max(0, idx - 150):min(len(text), idx + 250)])
