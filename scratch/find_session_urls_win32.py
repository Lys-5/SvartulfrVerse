import os
import re
import win32file
import win32con

session_dir = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sessions")
files = [os.path.join(session_dir, f) for f in os.listdir(session_dir) if os.path.getsize(os.path.join(session_dir, f)) > 0]
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

for path in files:
    print("Checking:", os.path.basename(path))
    try:
        handle = win32file.CreateFile(
            path,
            win32con.GENERIC_READ,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL,
            None
        )
        # Read file
        size = win32file.GetFileSize(handle)
        _, data = win32file.ReadFile(handle, size)
        win32file.CloseHandle(handle)

        print(f"Read {len(data)} bytes from {os.path.basename(path)}")

        # Check for RPG Source
        if b"RPG Source" in data:
            print("  >>> FOUND 'RPG Source' tab group!")
        
        # Find URLs
        urls = set()
        for m in re.finditer(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", data):
            u = m.group(0).decode("latin1", errors="ignore")
            # filter out static assets
            if not any(u.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".js", ".css", ".svg", ".ico", ".woff", ".woff2"]):
                urls.add(u)
        
        print(f"  Found {len(urls)} URLs. Sample:")
        for u in sorted(list(urls))[:15]:
            print("   *", u)

    except Exception as e:
        print("  Error:", e)
