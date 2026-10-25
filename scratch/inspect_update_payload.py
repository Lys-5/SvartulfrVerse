import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
text = f.read_text(encoding='utf-8')

pos = text.find('o.hi.lorebooks.update')
print("Position:", pos)
if pos != -1:
    print(text[pos-1500:pos+1000])
