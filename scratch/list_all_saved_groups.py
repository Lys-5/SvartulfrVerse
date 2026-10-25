import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")

all_data = b""
for fname in sorted(os.listdir(dir_path)):
    fpath = os.path.join(dir_path, fname)
    if os.path.isfile(fpath) and fname != "LOCK":
        try:
            with open(fpath, "rb") as f:
                all_data += f.read() + b"\n===FILE_SEP===\n"
        except Exception as e:
            # try to copy
            print(f"Skipping {fname}: {e}")

pattern = re.compile(rb"saved_tab_group-dt-([a-f0-9\-]+)")
records = []
for m in pattern.finditer(all_data):
    uuid = m.group(1).decode("latin1")
    start = max(0, m.start() - 20)
    end = min(len(all_data), m.start() + 1000)
    chunk = all_data[start:end]
    
    g_match = re.search(rb"\$([a-f0-9\-]{36})", chunk)
    guid = g_match.group(1).decode("latin1") if g_match else "unknown"
    
    url_match = re.search(rb"(https?://[^\x00-\x20\x7f-\xff\"\'<>]+)", chunk)
    url = url_match.group(1).decode("latin1") if url_match else None
    
    records.append((uuid, guid, url, chunk))

print(f"Total saved_tab_group-dt- records found: {len(records)}")
groups = {}
for u, g, url, chunk in records:
    if g not in groups:
        groups[g] = []
    groups[g].append((u, url, chunk))

for g, items in groups.items():
    print(f"\nGroup GUID: {g} (items: {len(items)})")
    seen_urls = set()
    for u, url, chunk in items:
        if url in seen_urls:
            continue
        seen_urls.add(url)
        title_match = re.search(rb'https?://[^\x00-\x20\x7f-\xff\"\'<>]+\"([^\x00-\x1f\x7f-\xff]+)', chunk)
        title = title_match.group(1).decode("latin1", errors="ignore") if title_match else ""
        print(f"   URL: {url}")
        print(f"   Title: {title}")
