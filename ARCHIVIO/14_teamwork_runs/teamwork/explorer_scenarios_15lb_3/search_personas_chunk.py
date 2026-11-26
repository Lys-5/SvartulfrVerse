import re

with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

for m in re.finditer(r'linkedPersonaIds', content):
    start = max(0, m.start() - 300)
    end = min(len(content), m.end() + 500)
    print(f"\n--- MATCH linkedPersonaIds at pos {m.start()} ---")
    print(content[start:end])
