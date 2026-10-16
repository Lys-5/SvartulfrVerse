import pathlib, re

root = pathlib.Path('.')
found = []
for p in root.rglob('*.json'):
    if any(k in p.parts for k in ['.git', 'node_modules', '.gemini']):
        continue
    try:
        txt = p.read_text(encoding='utf-8')
        matches = re.findall(r'"avatar_activation_regex":\s*"([^"]+)"', txt)
        if matches:
            found.append((str(p), matches[:3]))
    except Exception:
        pass

print("Found files with non-empty avatar_activation_regex:", len(found))
for f, m in found[:10]:
    print(f, m)
