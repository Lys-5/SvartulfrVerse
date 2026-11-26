import re
import glob

for chunk in glob.glob('scratch/*-*.js'):
    content = open(chunk, encoding='utf-8', errors='ignore').read()
    if 'deleteMessage' in content:
        matches = re.finditer(r'deleteMessage\s*[:=]\s*(?:function|\([^)]*\)\s*=>|[a-zA-Z0-9_\$]+)', content)
        for m in matches:
            start = max(0, m.start() - 100)
            end = min(len(content), m.end() + 300)
            print(f"=== {chunk} at {m.start()} ===")
            print(content[start:end])
            print()
