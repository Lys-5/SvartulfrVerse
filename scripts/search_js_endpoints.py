import glob
import re

for f in glob.glob('scratch/*.js'):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        if 'providers' in content or 'connections' in content:
            matches = set(re.findall(r'["\'`](/api/[a-zA-Z0-9_\-/]+)["\'`]', content))
            relevant = [m for m in matches if 'provider' in m or 'connection' in m]
            if relevant:
                print(f"File {f}:")
                for r in relevant:
                    print("  ", r)
    except Exception as e:
        pass
