import os
import sys
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

html_path = r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2830\content.md'
with open(html_path, 'r', encoding='utf-8') as f:
    raw = f.read()

soup = BeautifulSoup(raw, 'html.parser')

print("Title:", repr(soup.title.string if soup.title else 'No title'))

# Collect all sections
sections = soup.find_all('section')
print(f"Total sections: {len(sections)}")
for idx, sec in enumerate(sections):
    sec_id = sec.get('id', '')
    headings = [h.get_text(strip=True) for h in sec.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    print(f"Section {idx} [id='{sec_id}'] headings: {headings}")

# Collect all links
links = []
for a in soup.find_all('a'):
    href = a.get('href')
    text = a.get_text(strip=True)
    if href:
        links.append((text, href))
print(f"\nTotal links: {len(links)}")
internal_links = [l for l in links if l[1].startswith('#')]
external_links = [l for l in links if not l[1].startswith('#')]
print(f"Internal anchor links ({len(internal_links)}):")
for t, h in internal_links:
    print(f"  {t} -> {h}")

print(f"\nExternal links ({len(external_links)}):")
for t, h in external_links:
    print(f"  {t} -> {h}")

# Collect images
imgs = []
for img in soup.find_all('img'):
    src = img.get('src')
    alt = img.get('alt', '')
    imgs.append((alt, src))
print(f"\nTotal images: {len(imgs)}")
for a, s in imgs:
    print(f"  alt={a!r} -> src={s!r}")
