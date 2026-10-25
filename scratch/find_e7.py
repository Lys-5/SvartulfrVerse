import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
text = f.read_text(encoding='utf-8')

pos = text.find('e7=')
if pos == -1:
    pos = text.find('e7 =')
print("Position of e7:", pos)
if pos != -1:
    print(text[pos-100:pos+500])
