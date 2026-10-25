with open('scratch/14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
matches = list(re.finditer(r'(\d{4,6})\s*:\s*function', c))
for m in matches:
    print(f"Module {m.group(1)} at {m.start()}")
