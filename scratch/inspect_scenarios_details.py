import json
import glob
import os

scenarios = sorted(glob.glob("FINAL/scenarios/*.json"))
print(f"Found {len(scenarios)} scenario files:")
for s in scenarios:
    print(" -", os.path.basename(s))

for s in scenarios:
    filename = os.path.basename(s)
    print(f"\n==================== {filename} ====================")
    with open(s, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Name: {data.get('name')}")
    print(f"Visibility: {data.get('visibility')}")
    print(f"Lorebook IDs count: {len(data.get('lorebook_ids', []))}")
    print(f"Lorebook IDs: {data.get('lorebook_ids')}")
    print(f"Slots count: {len(data.get('slots', []))}")
    for slot in data.get('slots', []):
        print(f"  Slot '{slot.get('key')}': label='{slot.get('label')}', pool_size={len(slot.get('pool', []))}")
        for p in slot.get('pool', []):
            print(f"    pool item: {p}")
    print(f"Greetings count: {len(data.get('greetings', []))}")
    for i, g in enumerate(data.get('greetings', [])):
        print(f"  Greeting {i}: title='{g.get('title')}', messages={len(g.get('messages', []))}")
        for j, m in enumerate(g.get('messages', [])):
            author = m.get('author_name', m.get('author', ''))
            content = m.get('content', '')
            first_line = content.split('\n')[0] if content else ''
            print(f"    msg {j}: author='{author}', content_len={len(content)}, start: {repr(first_line[:70])}")
