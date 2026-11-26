import re
import glob

for f in glob.glob('scratch/*.js'):
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        if 'nameplate' in content.lower() or 'name plate' in content.lower() or 'speaker' in content.lower():
            matches = re.findall(r'.{0,60}(?:nameplate|speaker|=>\s*\[?[A-Za-z]+).{0,60}', content, flags=re.IGNORECASE)
            print(f"File {f}: found {len(matches)} matches")
            for m in matches[:5]:
                print("  ", m.strip())
    except Exception as e:
        pass
