import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / 'page-385df219b0dca31a.js'
text = f.read_text(encoding='utf-8')

print("=== page-385df219b0dca31a.js: 65000 to 68000 ===")
print(text[65000:68000])
