import re
import glob

for f in glob.glob('scratch/*.js'):
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'/messages/([^"\'`\s]+)', content):
            print(f"File {f}: {m.group(0)}")
            start = max(0, m.start() - 60)
            end = min(len(content), m.end() + 60)
            print("   context:", content[start:end])
    except Exception as e:
        pass
