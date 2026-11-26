import re
import glob

for chunk in glob.glob('scratch/*-*.js'):
    content = open(chunk, encoding='utf-8', errors='ignore').read()
    if 'editSwipe' in content:
        matches = re.finditer(r'editSwipe\s*[:=]\s*(?:async\s*)?\([^)]*\)\s*=>', content)
        for m in matches:
            start = max(0, m.start() - 50)
            end = min(len(content), m.end() + 300)
            print(f"=== {chunk} at {m.start()} ===")
            print(content[start:end])
