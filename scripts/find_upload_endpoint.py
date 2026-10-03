import urllib.request
import re
import json
import sys

def main():
    req = urllib.request.Request('https://app.wyvern.chat', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    scripts = re.findall(r'src=["\']([^"\']+\.js)["\']', html)
    print('Found scripts in index.html:', len(scripts))

    for s in scripts:
        s_url = s if s.startswith('http') else 'https://app.wyvern.chat' + s
        try:
            s_req = urllib.request.Request(s_url, headers={'User-Agent': 'Mozilla/5.0'})
            js_content = urllib.request.urlopen(s_req).read().decode('utf-8', errors='ignore')
            # Look for /gallery or /images or upload
            found = re.findall(r'/api/[a-zA-Z0-9_\-\/]+(?:upload|gallery|image)[a-zA-Z0-9_\-\/]*', js_content, re.IGNORECASE)
            if found:
                print(f"In {s}:")
                for u in set(found):
                    print("  API endpoint:", u)
            
            # Also search for cloudflare or direct upload url
            cf_found = re.findall(r'https?://[^\s"\'`]+cloudflare[^\s"\'`]*', js_content, re.IGNORECASE)
            if cf_found:
                print("  Cloudflare references:", set(cf_found[:5]))
        except Exception as e:
            print(f"Error reading {s}: {e}")

if __name__ == '__main__':
    main()
