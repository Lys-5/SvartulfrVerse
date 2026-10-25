import urllib.request
import re
from bs4 import BeautifulSoup

url = 'https://wiki.wyvern.chat/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        print(f"{a.get_text(strip=True):35} -> {a['href']}")
except Exception as e:
    print("Error:", e)
