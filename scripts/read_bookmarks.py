import os
import json

base = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data')
bookmarks_paths = []
for root, dirs, files in os.walk(base):
    if 'Bookmarks' in files:
        bookmarks_paths.append(os.path.join(root, 'Bookmarks'))

print(f"Found {len(bookmarks_paths)} Bookmarks files:")
for p in bookmarks_paths:
    print(" -", p)

found = []
for p in bookmarks_paths:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        def search(node):
            if isinstance(node, dict):
                if node.get('id') == '662':
                    found.append((p, node))
                    return
                for v in node.values():
                    search(v)
            elif isinstance(node, list):
                for item in node:
                    search(item)
                    
        search(data)
    except Exception as e:
        print(f"Error reading {p}: {e}")

if found:
    for path, node in found:
        print(f"\n=== MATCH IN {path} ===")
        print(json.dumps(node, indent=2))
else:
    print("\nNode 662 not found by id. Searching for AI/Provider bookmarks...")
    # Search for bookmarks with provider or ai names
    for p in bookmarks_paths:
        try:
            with open(p, 'r', encoding='utf-8') as f:
                data = json.load(f)
            hits = []
            def search_names(node):
                if isinstance(node, dict):
                    name = node.get('name', '')
                    url = node.get('url', '')
                    id_val = node.get('id')
                    if any(k in name.lower() or k in url.lower() for k in ['openrouter', 'groq', 'together', 'zhipu', 'bigmodel', 'deepinfra', 'fireworks', 'ai studio', 'gemini']):
                        hits.append({'id': id_val, 'name': name, 'url': url})
                    for v in node.values():
                        search_names(v)
                elif isinstance(node, list):
                    for item in node:
                        search_names(item)
            search_names(data)
            print(f"Found {len(hits)} AI bookmarks in {p}:")
            for h in hits[:20]:
                print(f"  [{h['id']}] {h['name']} -> {h['url']}")
        except Exception as e:
            pass
