import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for f in ROOT.glob('scratch/**/*.js'):
    txt = f.read_text(encoding='utf-8', errors='ignore')
    if 'addLorebookGalleryImage' in txt:
        print("Found addLorebookGalleryImage in", f.name)
        for m in re.finditer(r'addLorebookGalleryImage\s*[:=]', txt):
            print(" ", ' '.join(txt[max(0, m.start()-100):min(len(txt), m.end()+200)].split()))
    if 'getLorebookGalleryImages' in txt:
        print("Found getLorebookGalleryImages in", f.name)
        for m in re.finditer(r'getLorebookGalleryImages\s*[:=]', txt):
            print(" ", ' '.join(txt[max(0, m.start()-100):min(len(txt), m.end()+200)].split()))
