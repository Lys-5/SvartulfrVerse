import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def scan_all():
    targets = [
        ROOT / 'FINAL',
        ROOT / 'ARCHIVIO' / 'cards_legacy',
        ROOT / 'lorebooks' / 'optimized'
    ]
    
    found = 0
    for t in targets:
        for f in t.rglob('*.json'):
            try:
                txt = f.read_text(encoding='utf-8')
                if '—' in txt:
                    found += 1
                    print(f"FOUND em-dash in {f.relative_to(ROOT)}:")
                    for idx, line in enumerate(txt.splitlines(), 1):
                        if '—' in line:
                            print(f"   L{idx}: {line[:100]}")
            except Exception as e:
                print(f"Error {f}: {e}")
    print(f"Total files with em-dash: {found}")

if __name__ == '__main__':
    scan_all()
