with open('scratch/match_chunk_106.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
for m in re.finditer(r'/new/chat-logs/[^\"]+', c):
    print(c[max(0, m.start()-40):min(len(c), m.end()+60)])
