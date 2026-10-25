import re

with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's find e3 = a(XXXX) or similar webpack/next require
for m in re.finditer(r'e3\s*=\s*([a-zA-Z0-9_\$\.\(\)]+)', content):
    print("Match:", m.group(0))
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 200)
    print(content[start:end])
    break
