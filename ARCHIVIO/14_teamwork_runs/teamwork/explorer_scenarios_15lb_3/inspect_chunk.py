import re

def search_in_file(path, patterns):
    print(f"=== SEARCHING IN {path} ===")
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for p in patterns:
        for m in re.finditer(p, content):
            start = max(0, m.start() - 250)
            end = min(len(content), m.end() + 350)
            print(f"\n--- MATCH '{p}' at pos {m.start()} ---")
            print(content[start:end])

search_in_file(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', ['linked_persona_ids', 'Offer a persona', 'lorebook_ids'])
