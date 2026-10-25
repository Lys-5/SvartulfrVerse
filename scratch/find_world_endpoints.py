import os
import re

endpoints = set()
for root, dirs, files in os.walk('scratch'):
    for f in files:
        if f.endswith('.js') or f.endswith('.py'):
            p = os.path.join(root, f)
            try:
                content = open(p, encoding='utf-8', errors='ignore').read()
                matches = re.findall(r'(/api/worlds[a-zA-Z0-9_\-/{}]*)', content)
                for m in matches:
                    endpoints.add(m)
            except Exception:
                pass

print("Discovered World endpoints:")
for ep in sorted(endpoints):
    print(" ", ep)
