import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
text = (ROOT / 'scratch' / '53145-79a5e9c927da31b2.js').read_text(encoding='utf-8', errors='ignore')
idx = text.find('62924:function')
print(text[idx:idx + 3500])
