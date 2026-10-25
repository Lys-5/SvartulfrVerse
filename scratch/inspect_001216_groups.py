import re

path = r"E:\repository\SvartulfrVerse\scratch\001216.log"
with open(path, "rb") as f:
    data = f.read()

# Let's search for any occurrences of "saved_tab_group"
pattern = re.compile(rb"saved_tab_group-dt-([a-f0-9\-]+)")
for m in pattern.finditer(data):
    uuid = m.group(1).decode("latin1")
    pos = m.start()
    chunk = data[pos:pos+1000]
    u_match = re.search(rb"(https?://[^\x00-\x20\x7f-\xff\"\'<>]+)", chunk)
    if u_match:
        url = u_match.group(1).decode("latin1")
        # search for group ID in chunk
        g_match = re.search(rb"\$([a-f0-9\-]{36})", chunk)
        gid = g_match.group(1).decode("latin1") if g_match else "none"
        print(f"Tab: {uuid} | Group: {gid} | URL: {url}")
