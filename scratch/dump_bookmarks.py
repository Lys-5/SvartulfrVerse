import os
import json

path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Bookmarks")
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

def dump_node(node, depth=0):
    indent = "  " * depth
    if isinstance(node, dict):
        name = node.get("name", "")
        ntype = node.get("type", "")
        url = node.get("url", "")
        if ntype == "folder":
            print(f"{indent}[FOLDER] {name} (children: {len(node.get('children', []))})")
            for c in node.get("children", []):
                dump_node(c, depth + 1)
        elif url:
            print(f"{indent}[URL] {name} -> {url}")

roots = data.get("roots", {})
for k, v in roots.items():
    print(f"=== ROOT: {k} ===")
    dump_node(v, 1)
