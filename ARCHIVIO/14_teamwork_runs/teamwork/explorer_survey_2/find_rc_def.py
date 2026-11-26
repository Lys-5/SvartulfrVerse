import re

content = open('scratch/81904-87bfa0aca229c4ac.js', encoding='utf-8', errors='ignore').read()

# Let's inspect between 245000 and 255000
for m in re.finditer(r'rC\s*=\s*(?:async\s*)?\([^)]*\)\s*=>', content):
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 500)
    print(f"=== rC at {m.start()} ===")
    print(content[start:end])
