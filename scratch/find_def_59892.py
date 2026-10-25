import glob
import re

for f in glob.glob('e:/repository/SvartulfrVerse/scratch/*.js'):
    txt = open(f, encoding='utf-8').read()
    m = re.findall(r'[\{,](59892):', txt)
    if m:
        print(f"Defined in {f}")
        idx = txt.find('59892:')
        print(txt[max(0, idx-50):min(len(txt), idx+500)])
