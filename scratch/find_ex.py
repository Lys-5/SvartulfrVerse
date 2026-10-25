import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / '66353-44918b7fd11ff8ae.js'
text = f.read_text(encoding='utf-8')

# Search for function definition of eX in 66353-44918b7fd11ff8ae.js
# In React components eX is typically a callback: eX = useCallback(...) or function
pos = text.find('eX=')
if pos == -1:
    pos = text.find('eX =')
print("Position of eX:", pos)
if pos != -1:
    print(text[pos-100:pos+800])
