import requests
import re
import urllib.parse

r = requests.get('https://app.wyvern.chat', headers={'User-Agent': 'AuditorBot/1.0'})
scripts = re.findall(r'src=["\']([^"\']+\.js[^"\']*)["\']', r.text)
print(f"Found {len(scripts)} scripts on app.wyvern.chat")
for s in scripts:
    full_url = urllib.parse.urljoin('https://app.wyvern.chat', s)
    print("Script:", full_url)
