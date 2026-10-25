import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f2 = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
c2 = f2.read_text(encoding='utf-8')

# Find NPC Information section
pos = c2.find("NPC Information")
if pos != -1:
    print("=== NPC Information UI in 66353-44918b7fd11ff8ae.js ===")
    print(c2[pos-200 : pos+4000])
