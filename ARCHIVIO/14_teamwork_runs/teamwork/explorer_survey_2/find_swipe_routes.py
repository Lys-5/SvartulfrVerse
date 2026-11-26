import re
import glob

for f in glob.glob('scratch/*.js'):
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'/(?:swipes|messages)/', content):
            start = max(0, m.start() - 100)
            end = min(len(content), m.end() + 100)
            print(f"File {f}: {content[start:end]}")
    except Exception as e:
        pass
