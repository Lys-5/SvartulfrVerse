import win32gui
import win32process

def enum_cb(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        cls = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        if "Chrome" in cls or "Chrome" in title:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            results.append((hwnd, pid, cls, title))

results = []
win32gui.EnumWindows(enum_cb, results)
print(f"Found {len(results)} Chrome windows:")
for r in results:
    print(f"HWND: {r[0]} | PID: {r[1]} | Class: {r[2]} | Title: {r[3]}")
