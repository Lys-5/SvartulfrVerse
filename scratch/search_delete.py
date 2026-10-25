import os
import glob
import re

for root, dirs, files in os.walk('scratch'):
    for f in files:
        if f.endswith('.py') or f.endswith('.js'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    matches = re.findall(r'method\s*[:=]\s*["\']DELETE["\']', content, re.IGNORECASE)
                    if matches:
                        print(f"Found DELETE in {path}")
                        for line in content.splitlines():
                            if 'DELETE' in line:
                                print(f"  {line.strip()[:120]}")
            except Exception:
                pass
