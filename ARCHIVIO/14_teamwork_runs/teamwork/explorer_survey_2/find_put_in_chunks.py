import re
import glob

files = glob.glob('scratch/*-*.js')
print("Checking chunks:", len(files))

for f in files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    # Search for .put( or .patch(
    matches = re.findall(r'(\.put\([^)]+\)|\.patch\([^)]+\))', content)
    put_matches = [m for m in matches if 'chat' in m or 'message' in m or 'swipe' in m]
    if put_matches:
        print(f"File {f}: found {len(put_matches)} PUT/PATCH matches:")
        for m in put_matches[:10]:
            print("  ", m)
