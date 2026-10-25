import re
import glob

files = glob.glob('scratch/*.js') + glob.glob('scratch/*.json')

for f in files:
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        if '=>' in content:
            matches = re.findall(r'(\b[a-zA-Z0-9_\$]+\s*=\s*\/[\^]?=>[^/]+\/)', content)
            if matches:
                print(f"File {f}: regexes found:", matches)
            str_matches = re.findall(r'([^\n]{0,40}=>[A-Z][a-zA-Z0-9_ ]+:[^\n]{0,40})', content)
            if str_matches:
                print(f"File {f}: speaker patterns found:", str_matches[:5])
    except Exception as e:
        pass
