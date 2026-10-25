import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")
guid = b"73c71ee0-b197-4a37-9dfd-11818d5b890e"

print("Scanning LevelDB files for GUID:", guid.decode())

found_tabs = {}

for fname in os.listdir(dir_path):
    fpath = os.path.join(dir_path, fname)
    if not os.path.isfile(fpath) or fname == "LOCK":
        continue
    with open(fpath, "rb") as f:
        data = f.read()
    
    # search for guid occurrences
    matches = [m.start() for m in re.finditer(re.escape(guid), data)]
    if matches:
        print(f"\n--- File: {fname} (occurrences: {len(matches)}) ---")
        for pos in matches:
            # Look backwards and forwards
            start = max(0, pos - 200)
            end = min(len(data), pos + 1000)
            block = data[start:end]
            
            # find tab UUID
            t_uuid = re.search(rb"saved_tab_group-dt-([a-f0-9\-]{36})", block)
            # find url
            u_match = re.search(rb"(https?://[^\x00-\x20\x7f-\xff\"\'<>]+)", block)
            
            if u_match:
                url = u_match.group(1).decode("latin1")
                # find title
                after_u = block[u_match.end():u_match.end()+200]
                # title is often after a quote or length byte
                title_match = re.search(rb'[\"\x12\x1a\x22]([A-Za-z0-9\s\-_:\'\.\|\(\)\!\?]{3,80})', after_u)
                title = title_match.group(1).decode("latin1") if title_match else ""
                
                tid = t_uuid.group(1).decode("latin1") if t_uuid else url
                found_tabs[url] = title
                print(f"  [Pos {pos}] URL: {url} | Title: {title}")

print("\n================ FINAL EXTRACTED TABS IN 'RPG Source' ================")
for url, title in found_tabs.items():
    print(f"* Title: {title}")
    print(f"  URL:   {url}")
print(f"Total tabs in 'RPG Source': {len(found_tabs)}")
