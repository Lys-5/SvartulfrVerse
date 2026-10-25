import re
import glob

for chunk in glob.glob('scratch/*-*.js'):
    content = open(chunk, encoding='utf-8', errors='ignore').read()
    if 'editSwipe' in content:
        matches = re.finditer(r'editSwipe.{0,150}', content)
        for m in matches:
            print(f"=== {chunk} ===")
            print(m.group(0))
