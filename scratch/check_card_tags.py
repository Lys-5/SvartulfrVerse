import json
import pathlib

root = pathlib.Path('FINAL')
for p in sorted(root.glob('*card.json')):
    card = json.loads(p.read_text(encoding='utf-8'))
    print(f"{p.name}:")
    print(f"  tags: {card.get('tags')}")
    print(f"  community_tags: {card.get('community_tags')}")
