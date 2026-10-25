with open('scratch/19010-2f567930ecf4f745.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

import re
matches = list(re.finditer(r'/api/new/chat-logs/[^\'\"]+', c))
print(f"Matches of /api/new/chat-logs/ in 19010: {len(matches)}")
for m in matches:
    print(c[max(0, m.start()-50):min(len(c), m.end()+100)])

with open('scratch/81904-87bfa0aca229c4ac.js', 'r', encoding='utf-8', errors='ignore') as f:
    c2 = f.read()

matches2 = list(re.finditer(r'/api/new/chat-logs/[^\'\"]+', c2))
print(f"Matches of /api/new/chat-logs/ in 81904: {len(matches2)}")
for m in matches2:
    print(c2[max(0, m.start()-50):min(len(c2), m.end()+100)])
