import re

chunk93 = open('scratch/match_chunk_93.js', 'r', encoding='utf-8').read()
chunk108 = open('scratch/match_chunk_108.js', 'r', encoding='utf-8').read()

print("Searching AI Connections / Prompts in Chunk 93 & 108...")

for name, content in [("Chunk 93", chunk93), ("Chunk 108", chunk108)]:
    print(f"\n--- {name} ---")
    for pattern in [r'AI Connections', r'prompt-assembly', r'Prompt Assembly', r'custom prompt', r'/connections']:
        matches = list(re.finditer(pattern, content, re.IGNORECASE))
        print(f"Pattern '{pattern}': {len(matches)} matches")
        for m in matches[:3]:
            start = max(0, m.start() - 100)
            end = min(len(content), m.end() + 150)
            print(f"  [{m.start()}]: ...{content[start:end]}...")
