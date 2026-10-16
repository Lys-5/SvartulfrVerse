import pathlib
import json
import re

root = pathlib.Path('.')
found_urls = []

for p in root.glob('**/*'):
    if p.is_file() and p.suffix in ['.json', '.md', '.txt'] and 'node_modules' not in p.parts:
        try:
            txt = p.read_text(encoding='utf-8', errors='ignore')
            if 'stanley davies' in txt.lower() or 'stan jr' in txt.lower() or 'stan_davies' in txt.lower():
                urls = re.findall(r'https?://[^\s"\'<>]+\.(?:png|webp|jpg|jpeg|public)', txt)
                if urls:
                    found_urls.append((p.name, urls))
        except:
            pass

for fname, urls in found_urls[:10]:
    print(f"{fname}: {urls}")
