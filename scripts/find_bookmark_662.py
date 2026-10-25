import os
import re

user_data = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data')
print("Searching in Chrome User Data for bookmarks referencing id 662...")

found_files = []
for root, dirs, files in os.walk(user_data):
    for f in files:
        if f in ['Bookmarks', 'Bookmarks.bak', 'Favicons', 'History'] or f.endswith('.ldb') or f.endswith('.log'):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, 'rb') as fp:
                    data = fp.read()
                    if b'"id": "662"' in data or b'"id":"662"' in data or b'id=662' in data:
                        found_files.append(fpath)
            except Exception:
                pass

print("Files containing id 662:", found_files)
for f in found_files:
    with open(f, 'rb') as fp:
        c = fp.read()
        idx = c.find(b'662')
        start = max(0, idx - 200)
        end = min(len(c), idx + 400)
        print(f"\n--- Context in {f} ---")
        print(c[start:end].decode('utf-8', errors='ignore'))
