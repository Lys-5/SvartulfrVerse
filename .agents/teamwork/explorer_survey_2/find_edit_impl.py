import re

content = open('scratch/81904-87bfa0aca229c4ac.js', encoding='utf-8', errors='ignore').read()

matches = re.finditer(r'editMessage\s*[:=]', content)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 600)
    print(f"=== at {m.start()} ===")
    print(content[start:end])
    print()
