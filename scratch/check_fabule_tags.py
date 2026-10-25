import sys
import urllib.request
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the tags or categories on fabuleurbane that explain lore
tags_to_check = [
    'https://fabuleurbane.wordpress.com/tag/cercatori-danime/',
    'https://fabuleurbane.wordpress.com/tag/exo/',
    'https://fabuleurbane.wordpress.com/tag/furie/',
    'https://fabuleurbane.wordpress.com/tag/operatore-spiritico/',
    'https://fabuleurbane.wordpress.com/tag/santuario/',
    'https://fabuleurbane.wordpress.com/tag/scuola-liberata/',
    'https://fabuleurbane.wordpress.com/tag/variaghi/',
    'https://fabuleurbane.wordpress.com/tag/cambiata/'
]

for url in tags_to_check:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(content, 'html.parser')
            # Extract post titles and snippets
            articles = soup.find_all('article')
            tag_name = url.strip('/').split('/')[-1]
            print(f"\n=== TAG: {tag_name} ({len(articles)} articles) ===")
            for a in articles[:3]:
                title = a.find('h1') or a.find('h2')
                t_str = title.get_text(strip=True) if title else 'No title'
                entry = a.find('div', class_='entry-summary') or a.find('div', class_='entry-content')
                snippet = entry.get_text(separator=' ', strip=True)[:150] if entry else ''
                print(f"  * {t_str}: {snippet}")
    except Exception as e:
        print(f"Error checking {url}: {e}")
