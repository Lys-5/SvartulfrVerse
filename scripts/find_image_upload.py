import urllib.request
import re

req = urllib.request.Request('https://app.wyvern.chat', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)

for s in scripts:
    if not s.endswith('.js') or 'cloudflare' in s:
        continue
    url = 'https://app.wyvern.chat' + s
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        content = urllib.request.urlopen(req, timeout=5).read().decode('utf-8', errors='ignore')
        if 'imagedelivery' in content.lower() or 'upload' in content.lower():
            # Find URLs
            urls = re.findall(r'https?://[^\s"\'`<>]+', content)
            api_routes = re.findall(r'["\'](/api/[^"\'`<>]+)["\']', content)
            im_matches = [u for u in urls if 'imagedelivery' in u or 'upload' in u]
            api_matches = [a for a in api_routes if 'upload' in a.lower() or 'image' in a.lower() or 'media' in a.lower() or 'file' in a.lower()]
            if im_matches or api_matches:
                print(f"Match in {s}:")
                if im_matches:
                    print("  URLs:", set(im_matches[:5]))
                if api_matches:
                    print("  API Routes:", set(api_matches[:10]))
    except Exception as e:
        pass
