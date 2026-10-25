import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
text = f.read_text(encoding='utf-8')

# Search around 31500 to 34500
print("=== 66353-44918b7fd11ff8ae.js around custom_avatar_regex and auto-generation ===")
pos = text.find("auto-generate from NPC info")
print("Position of 'auto-generate':", pos)
if pos != -1:
    print(text[pos-1000 : pos+1500])
