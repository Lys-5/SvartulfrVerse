import win32gui

def enum_cb(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        cls = win32gui.GetClassName(hwnd)
        if title:
            results.append((hwnd, cls, title))

results = []
win32gui.EnumWindows(enum_cb, results)
for r in results:
    print(f"[{r[1]}] {r[2]}")
