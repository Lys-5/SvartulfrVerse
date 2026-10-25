import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

bak = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks.bak')
with open(bak, 'r', encoding='utf-8') as f:
    data = json.load(f)

def find_node(node, target_id):
    if isinstance(node, dict):
        if str(node.get('id')) == str(target_id):
            return node
        for v in node.values():
            res = find_node(v, target_id)
            if res: return res
    elif isinstance(node, list):
        for item in node:
            res = find_node(item, target_id)
            if res: return res
    return None

ai_folder = find_node(data, '2566')
if ai_folder:
    print(f"Folder: {ai_folder.get('name')}")
    for item in ai_folder.get('children', []):
        if item.get('type') == 'url':
            print(f"- {item.get('name')} -> {item.get('url')}")
        else:
            print(f"+ [Folder] {item.get('name')} ({len(item.get('children', []))} items)")
            for sub in item.get('children', []):
                print(f"    * {sub.get('name')} -> {sub.get('url')}")
