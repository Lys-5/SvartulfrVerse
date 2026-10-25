import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_endpoint = f'ws://127.0.0.1:{port}{ws_path}'

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint, timeout=5000)
    page = browser.contexts[0].pages[0]
    print(f"Inspecting active page: {page.url} | title: {page.title()}")

    # Evaluate DOM
    eval_script = """
    () => {
        const results = [];
        // Wyvern cards in /mine
        const links = Array.from(document.querySelectorAll('a[href*="/characters/"]'));
        for (const a of links) {
            const href = a.getAttribute('href');
            const img = a.querySelector('img');
            const imgSrc = img ? (img.getAttribute('src') || img.src) : null;
            const text = a.innerText.trim();
            results.push({ href, text, imgSrc });
        }
        
        // Also look for all img elements in main container
        const allImgs = Array.from(document.querySelectorAll('img')).map(img => ({
            src: img.getAttribute('src') || img.src,
            alt: img.getAttribute('alt') || ''
        }));
        
        return {
            totalLinks: links.length,
            cards: results,
            allImgs: allImgs,
            bodySnippet: document.body.innerText.slice(0, 800)
        };
    }
    """
    res = page.evaluate(eval_script)
    print(f"Total character links: {res['totalLinks']}")
    for c in res['cards']:
        print(f"  Link: {c['href']} | Img: {c['imgSrc']} | Text: {c['text'][:40]}")
    print(f"\nTotal images on page: {len(res['allImgs'])}")
    for img in res['allImgs']:
        print(f"  Img: {img['src']} | Alt: {img['alt']}")
    if res['totalLinks'] == 0:
        print("\nBody text snippet:")
        print(res['bodySnippet'])
