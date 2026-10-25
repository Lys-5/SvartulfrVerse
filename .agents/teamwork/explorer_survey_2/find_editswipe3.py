import re
import glob

content = open('scratch/81904-87bfa0aca229c4ac.js', encoding='utf-8', errors='ignore').read()

matches = re.finditer(r'editSwipe\s*:\s*(?:function|[a-zA-Z0-9_\$]+|\([^)]*\))', content)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 200)
    print("MATCH editSwipe:", content[start:end])

# Also check other chunks
for chunk in glob.glob('scratch/*-*.js'):
    if chunk == 'scratch/81904-87bfa0aca229c4ac.js': continue
    c = open(chunk, encoding='utf-8', errors='ignore').read()
    if 'editSwipe' in c:
        print("Found in other chunk:", chunk)
        matches = re.finditer(r'editSwipe.{0,100}', c)
        for m in matches:
            print("  ", m.group(0))
