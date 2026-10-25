import re

with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

for m in re.finditer(r'(?:var|let|const)\s+e3\s*=', content):
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 300)
    print(f"\n--- MATCH at {m.start()} ---")
    print(content[start:end])

# Also search for "Offer a persona" across ALL chunks or entire scratch
print("=== SEARCHING 'Offer a persona' in all scratch files ===")
import glob
for p in glob.glob(r'e:\repository\SvartulfrVerse\scratch\*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
        if 'Offer a persona' in t:
            print(f"Found in {p}")
            idx = t.find('Offer a persona')
            print(t[max(0, idx-200):min(len(t), idx+400)])
