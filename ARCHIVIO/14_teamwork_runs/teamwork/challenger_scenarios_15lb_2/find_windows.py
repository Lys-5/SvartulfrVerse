import ctypes

user32 = ctypes.windll.user32
titles = []

def enum_proc(hwnd, lParam):
    length = user32.GetWindowTextLengthW(hwnd)
    if length > 0:
        buf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buf, length + 1)
        titles.append(buf.value)
    return True

WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
user32.EnumWindows(WNDENUMPROC(enum_proc), 0)

for t in titles[:30]:
    print(f"Top window: {t}")
