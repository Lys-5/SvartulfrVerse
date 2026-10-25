import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")

for fname in ["001219.log", "001220.ldb", "001218.ldb"]:
    fpath = os.path.join(dir_path, fname)
    if not os.path.exists(fpath):
        continue
    try:
        with open(fpath, "rb") as f:
            data = f.read()
    except Exception as e:
        print(f"Error reading {fname}: {e}")
        continue
    
    print(f"\n=================== {fname} ({len(data)} bytes) ===================")
    
    # Check if RPG Source is in this file
    if b"RPG Source" in data:
        print(">>> 'RPG Source' found in", fname)

    # Find all saved_tab_group-dt- entries
    pattern = re.compile(rb"saved_tab_group-dt-([a-f0-9\-]+)")
    for m in pattern.finditer(data):
        uuid = m.group(1).decode("latin1")
        snippet = data[m.start():m.start()+800]
        
        # URL
        url_match = re.search(rb"(https?://[^\x00-\x20\x7f-\xff\"\'<>]+)", snippet)
        url = url_match.group(1).decode("latin1") if url_match else None
        
        # Title: in protobuf, title follows url in a length-delimited string
        title = ""
        if url_match:
            after_url = snippet[url_match.end():url_match.end()+150]
            # search for readable title string
            t_match = re.search(rb'[\"\x12\x1a\x22]([A-Za-z0-9\s\-_:\'\.\|\(\)\!\?]{3,60})', after_url)
            if t_match:
                title = t_match.group(1).decode("latin1", errors="ignore")
        
        print(f"[{uuid}]")
        print(f"   URL:   {url}")
        print(f"   Title: {title}")
