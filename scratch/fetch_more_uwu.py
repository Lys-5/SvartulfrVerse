import sys
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

extra_urls = {
    'io_succc': 'https://io-succc.uwu.ai/',
    'iofan': 'https://iofan.uwu.ai/'
}

for name, url in extra_urls.items():
    print(f"Fetching {name}: {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            path = f'scratch/sites_raw/{name}.html'
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved {name} ({len(content)} chars)")
            soup = BeautifulSoup(content, 'html.parser')
            print(f"Title: {soup.title.string if soup.title else 'None'}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
