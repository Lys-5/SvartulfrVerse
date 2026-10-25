import urllib.request
import re

# We can search through the script chunks loaded by worlds/edit
url = "https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

scripts = re.findall(r'src="(/_next/static/chunks/[^"]+)"', html)
print(f"Checking {len(scripts)} scripts for module 77818...")

found_script = None
for s in scripts:
    s_url = f"https://app.wyvern.chat{s}"
    try:
        r = urllib.request.Request(s_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            if '77818:' in text or '77818 :' in text:
                print(f"Found 77818 in {s}")
                found_script = (s, text)
                break
    except Exception as e:
        pass

if found_script:
    s_name, text = found_script
    idx = text.find('77818:')
    print(text[idx:idx+2500])
