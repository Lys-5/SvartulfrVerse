import os
import glob
import re

for root, dirs, files in os.walk('scratch'):
    for f in files:
        if f.endswith('.js') or f.endswith('.py') or f.endswith('.json'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    matches = re.findall(r'https?://[^\s"\']+/api/character-scenarios[^\s"\'`]*', content)
                    for m in set(matches):
                        print(f"{path}: {m}")
                    matches_rel = re.findall(r'/api/character-scenarios[^\s"\'`]*', content)
                    for m in set(matches_rel):
                        print(f"{path}: {m}")
            except Exception:
                pass
