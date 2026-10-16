import pathlib
import re

txt = pathlib.Path('scratch/inbox/wv_chunk.js').read_text(encoding='utf-8', errors='ignore')

# Search for any Select or Label mentioning "Type" or setting "type" on the entry
for m in re.finditer(r'["\']type["\']', txt):
    pos = m.start()
    s = max(0, pos - 200)
    e = min(len(txt), pos + 300)
    snippet = txt[s:e]
    if 'SelectItem' in snippet or 'eG("type"' in snippet or 'SelectTrigger' in snippet:
        print("=== MATCH SNIPPET ===")
        print(snippet)
        print("\n")
