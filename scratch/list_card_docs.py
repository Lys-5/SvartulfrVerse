import os
import re

doc_dir = 'docs/claude_project_docs'
files = os.listdir(doc_dir)

# Look for files with "Card", "Completamento", "Schede", "Batch"
card_docs = [f for f in files if any(w in f for w in ['Card', 'Completamento', 'Schede', 'Batch', 'Concilio', 'District', 'Sinners', 'Cocketeers', 'Grave'])]

print(f"Found {len(card_docs)} card/completion documents:")
for f in sorted(card_docs):
    print(" -", f)
