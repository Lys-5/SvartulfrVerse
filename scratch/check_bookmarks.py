import json, os

path = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks')
if not os.path.exists(path):
    print("No bookmarks file at", path)
    exit()

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def search_items(node, path_str=''):
    if isinstance(node, dict):
        t = node.get('type')
        node_id = str(node.get('id', ''))
        name = node.get('name', '')
        url = node.get('url', '')
        if node_id == '662':
            print(f"FOUND ID 662 FOLDER [{node_id}] {path_str}/{name}")
            for child in node.get('children', []):
                print(f"  - [{child.get('id')}] {child.get('name')}: {child.get('url')}")
            return
        
        cur = path_str + '/' + name if name else path_str
        for k, v in node.items():
            if isinstance(v, (dict, list)):
                search_items(v, cur)
    elif isinstance(node, list):
        for item in node:
            search_items(item, path_str)

search_items(data)
