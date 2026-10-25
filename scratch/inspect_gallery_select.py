import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
text = f.read_text(encoding='utf-8')

pos = text.find('Select avatar from gallery')
if pos == -1:
    pos = text.find('Select different avatar')
print("Position:", pos)
if pos != -1:
    print(text[pos-500 : pos+2500])
