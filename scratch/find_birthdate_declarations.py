import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc_dir = 'docs/claude_project_docs'
for f in os.listdir(doc_dir):
    with open(os.path.join(doc_dir, f), encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
    matches = re.findall(r'([A-Z][a-zA-Z\s\.\'\"]{2,30})\s*(?:—|-|\|)\s*(?:[Bb]irthdate|[Nn]ascita|[Nn]ato|[Nn]ata)\s*[:=]?\s*([^\n\|]+)', text)
    if matches:
        print(f"=== {f} ===")
        for m in matches[:10]:
            print(f"  {m[0].strip()} --> {m[1].strip()}")
