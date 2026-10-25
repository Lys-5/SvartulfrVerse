import os
import json

path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Bookmarks")
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

items = []
def collect_items(node):
    if isinstance(node, dict):
        if "url" in node:
            items.append((node.get("date_added", "0"), node.get("name"), node.get("url")))
        for child in node.get("children", []):
            collect_items(child)
    elif isinstance(node, list):
        for item in node:
            collect_items(item)

for root_name, root_node in data.get("roots", {}).items():
    collect_items(root_node)

items.sort(key=lambda x: int(x[0]) if x[0].isdigit() else 0, reverse=True)
print(f"Total bookmarks: {len(items)}")
print("Latest 10 bookmarks:")
for d, name, url in items[:10]:
    print(f" - [{name}]({url})")
