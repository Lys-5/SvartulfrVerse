import glob
import re

for f in glob.glob('scratch/*.js'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
        if 'character-scenario' in c:
            for m in re.finditer(r'(/api/character-scenarios[^\s"\'`)]*)', c):
                print(f"{f}: {m.group(0)}")
            for m in re.finditer(r'method:\s*["\'](DELETE|POST|PUT|GET)["\'][^}]{0,100}character-scenario', c, re.IGNORECASE):
                print(f"Method match in {f}: {m.group(0)}")
