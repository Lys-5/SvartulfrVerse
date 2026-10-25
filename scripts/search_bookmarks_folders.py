import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

bak = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks.bak')
with open(bak, 'r', encoding='utf-8') as f:
    data = json.load(f)

def list_folders(n):
    if isinstance(n, dict):
        if n.get('type') == 'folder':
            print(f"[{n.get('id')}] {n.get('name')} (items: {len(n.get('children', []))})")
        for v in n.values():
            list_folders(v)
    elif isinstance(n, list):
        for i in n:
            list_folders(i)

list_folders(data)
