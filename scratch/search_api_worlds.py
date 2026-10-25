import os
import re

for root, dirs, files in os.walk('scratch'):
    for f in files:
        if f.endswith('.js') or f.endswith('.txt') or f.endswith('.json') or f.endswith('.py'):
            p = os.path.join(root, f)
            try:
                txt = open(p, 'r', encoding='utf-8', errors='ignore').read()
                matches = re.findall(r'/api/worlds[^\s\"\'\`\)]*', txt)
                if matches:
                    print(f"{p}: {set(matches)}")
            except Exception:
                pass
