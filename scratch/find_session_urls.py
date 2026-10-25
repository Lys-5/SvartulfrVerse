import os
import re

session_dir = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sessions")
files = [os.path.join(session_dir, f) for f in os.listdir(session_dir) if os.path.getsize(os.path.join(session_dir, f)) > 0]
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

for path in files:
    print("Checking:", os.path.basename(path), "Size:", os.path.getsize(path))
    with open(path, "rb") as f:
        data = f.read()
    
    # Check UTF-8 and UTF-16 strings
    for m in re.finditer(rb"(?:https?://[^\x00-\x20\x7f-\xff]+)", data):
        url = m.group(0).decode("latin1", errors="ignore")
        if any(k in url.lower() for k in ["rpg", "dnd", "dice", "ttrpg", "special", "d20", "fallout", "wiki", "reddit", "sillytavern", "lore"]):
            print("  URL match:", url)

    # Search for group name "RPG Source"
    for name in [b"RPG Source", b"RPG", b"R P G   S o u r c e"]:
        if name in data:
            print("  Found Group Name pattern:", name)
