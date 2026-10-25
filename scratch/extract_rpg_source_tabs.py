import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")
group_id = b"73c71ee0-b197-4a37-9dfd-11818d5b890e"

all_data = b""
for fname in sorted(os.listdir(dir_path)):
    fpath = os.path.join(dir_path, fname)
    if not os.path.isfile(fpath):
        continue
    try:
        with open(fpath, "rb") as f:
            all_data += f.read() + b"\n---FILE_BOUNDARY---\n"
    except Exception:
        pass

print("Total LevelDB data read:", len(all_data))

# A tab in saved_tab_group has structure:
# key: saved_tab_group-dt-<tab_uuid>
# value: protobuf containing:
#   group_id: 73c71ee0-b197-4a37-9dfd-11818d5b890e
#   url: https://...
#   title: string

tabs = []
# Find all saved_tab_group-dt- entries
pattern = re.compile(rb"saved_tab_group-dt-([a-f0-9\-]+)")
for match in pattern.finditer(all_data):
    tab_uuid = match.group(1).decode("latin1")
    pos = match.start()
    snippet = all_data[pos:pos+2500]
    
    # Check if this tab belongs to RPG Source (group_id)
    if group_id in snippet:
        # Extract URL
        url_match = re.search(rb"(https?://[^\x00-\x20\x7f-\xff\"\'<>]+)", snippet)
        url = url_match.group(1).decode("latin1") if url_match else None
        
        # In protobuf, url is followed by title
        # Let's find readable strings
        strings = re.findall(rb"[\x20-\x7e]{3,}", snippet)
        str_list = [s.decode("latin1") for s in strings]
        
        tabs.append({
            "uuid": tab_uuid,
            "url": url,
            "raw_strings": str_list
        })

print(f"Found {len(tabs)} tab records for group 'RPG Source':")
seen_urls = {}
for t in tabs:
    u = t["url"]
    if u and u not in seen_urls:
        # Find title from raw strings
        title = ""
        for s in t["raw_strings"]:
            if s != u and not s.startswith("saved_tab_group") and not s.startswith("$") and not "==" in s and not "dt-" in s and len(s) > 2:
                if "Janitor" in s or "Wyvern" in s or "Modern" in s or "Character" in s or len(s) > title.__len__():
                    title = s
        seen_urls[u] = title
        print(f"  * URL: {u}")
        print(f"    TITLE: {title}")

print(f"\nTOTAL UNIQUE TABS IN RPG SOURCE: {len(seen_urls)}")
