import re
import json

files = [
    'scratch/match_chunk_93.js',
    'scratch/match_chunk_100.js',
    'scratch/match_chunk_106.js',
    'scratch/match_chunk_108.js',
]

for fp in files:
    try:
        content = open(fp, 'r', encoding='utf-8').read()
        print(f"=== {fp} (len: {len(content)}) ===")
        
        # Check for assistant config
        for m in re.finditer(r'simple-assistant-config', content):
            start = max(0, m.start() - 100)
            end = min(len(content), m.end() + 200)
            print(f"Match simple-assistant-config at {m.start()}:\n{content[start:end]}\n---")
            
        # Check for prompt assembly
        for m in re.finditer(r'prompt-assembl', content):
            start = max(0, m.start() - 100)
            end = min(len(content), m.end() + 200)
            print(f"Match prompt-assembl at {m.start()}:\n{content[start:end]}\n---")
            
    except Exception as e:
        print(f"Error {fp}: {e}")
