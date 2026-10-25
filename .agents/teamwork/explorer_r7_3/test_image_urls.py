import urllib.request

urls = [
    ('Official DCC Avatar Placeholder', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public'),
    ('Official House Svartúlfr Emblem (Cover)', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public'),
    ('Old Fallback Avatar (6f8b7c78)', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public'),
    ('Old Crest Avatar (98e2d06d)', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public')
]

for label, url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content_type = resp.headers.get('Content-Type')
            content_length = resp.headers.get('Content-Length')
            print(f"[{resp.status} OK] {label}:")
            print(f"  URL: {url}")
            print(f"  Content-Type: {content_type}, Content-Length: {content_length} bytes")
    except Exception as e:
        print(f"[FAIL] {label}: {url} -> {e}")
