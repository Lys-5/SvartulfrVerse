import re

for chunk in ['scratch/19010-2f567930ecf4f745.js', 'scratch/81904-87bfa0aca229c4ac.js']:
    content = open(chunk, encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'\.(?:put|patch)\(["\'`]\s*(?:\+?\s*\.concat\([^)]+\)|[^)]+)\)', content):
        start = max(0, m.start() - 200)
        end = min(len(content), m.end() + 200)
        snippet = content[start:end]
        if 'chat-log' in snippet:
            print(f"=== {chunk} at {m.start()} ===")
            print(snippet)
            print()
