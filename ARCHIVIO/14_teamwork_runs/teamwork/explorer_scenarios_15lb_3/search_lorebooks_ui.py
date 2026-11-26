import re

with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for lorebook_ids in UI JSX
for m in re.finditer(r'lorebook_ids', content):
    start = max(0, m.start() - 200)
    end = min(len(content), m.end() + 400)
    print(f"\n--- MATCH lorebook_ids at pos {m.start()} ---")
    print(content[start:end])
