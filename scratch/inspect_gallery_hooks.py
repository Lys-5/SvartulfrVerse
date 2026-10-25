import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / 'page-385df219b0dca31a.js'
text = f.read_text(encoding='utf-8')

print("=== page-385df219b0dca31a.js: API hooks for gallery ===")
print(text[60500:65000])
