import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
f = ROOT / 'scratch' / 'lorebook_chunks' / 'page-385df219b0dca31a.js'
text = f.read_text(encoding='utf-8')

pos = text.find('No gallery images')
print(text[pos+1000:pos+3000])
