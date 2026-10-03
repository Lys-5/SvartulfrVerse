import urllib.request
import re
import sys

def check_chunk(chunk_path):
    url = 'https://app.wyvern.chat' + chunk_path
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        data = urllib.request.urlopen(req, timeout=5).read().decode('utf-8', errors='ignore')
        if 'gallery' in data.lower() and ('upload' in data.lower() or 'post' in data.lower() or 'image' in data.lower()):
            matches = re.findall(r'[\'"`]/api[^\'"`]+[\'"`]', data)
            cf = re.findall(r'[\'"`]https?://[^\'"`]+cloudflare[^\'"`]+[\'"`]', data)
            direct_upload = re.findall(r'upload[a-zA-Z0-9_-]*', data, re.IGNORECASE)
            print(f"Match in {chunk_path}:")
            print("  API URLs:", set(matches[:15]))
            if cf:
                print("  CF:", set(cf[:5]))
    except Exception as e:
        pass

with open('scripts/fetch_wyvern_scripts.py') as f:
    pass

scripts = [
    "/_next/static/chunks/app/(content)/layout-2a3d55200e9320a8.js",
    "/_next/static/chunks/82451-b1de6fd77b2cd59a.js",
    "/_next/static/chunks/51112-51ceff4bccf391df.js",
    "/_next/static/chunks/87885-3eb12015d428467a.js",
    "/_next/static/chunks/76534-1d17eb3c0831afc1.js",
    "/_next/static/chunks/59364-07b37c24b9a03959.js",
    "/_next/static/chunks/46410-54aae8b6d6cff6b5.js",
    "/_next/static/chunks/69712-482ee41ed440d971.js",
    "/_next/static/chunks/19864-b58adaf58abcbf18.js",
    "/_next/static/chunks/86569-e159da44442ad134.js",
    "/_next/static/chunks/77862-4cd055377b26665f.js",
    "/_next/static/chunks/83403-d7abb1a90273e4b2.js",
    "/_next/static/chunks/11766-e39547adbe254368.js",
    "/_next/static/chunks/45658-788d764e582b8453.js",
    "/_next/static/chunks/36457-58e6c44e40c0435b.js",
    "/_next/static/chunks/99424-8a921029ff659f6a.js",
    "/_next/static/chunks/97141-0dae49e7cd83a9b7.js",
    "/_next/static/chunks/20358-442f45bdd4670295.js",
    "/_next/static/chunks/64702-41a3744acf1f6a86.js",
    "/_next/static/chunks/82388-d8cdc4b5df7e1b22.js",
    "/_next/static/chunks/91961-71cb4d3e937fcb05.js",
    "/_next/static/chunks/70055-c6a9377cbeddfedf.js",
    "/_next/static/chunks/62173-d65ec79081465ebe.js",
    "/_next/static/chunks/56861-a59d1f0dc067e51c.js",
    "/_next/static/chunks/54475-7451bfa619d51546.js",
    "/_next/static/chunks/29079-3bc29f46833c9a2b.js",
    "/_next/static/chunks/63444-825a6f36859259de.js",
    "/_next/static/chunks/73731-e83da07c134b2871.js",
    "/_next/static/chunks/15526-b5a4e1cc471206aa.js",
    "/_next/static/chunks/60147-7f0448b4a62ea4c1.js"
]

for s in scripts:
    check_chunk(s)
