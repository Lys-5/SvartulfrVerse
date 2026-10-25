import asyncio
import json
from playwright.async_api import async_playwright

async def find_display_settings():
    async with async_playwright() as p:
        with open(r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort') as f:
            port = f.readline().strip()
            ws_path = f.readline().strip()
        browser = await p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
        context = browser.contexts[0]
        page = None
        for pg in context.pages:
            if 'wyvern.chat' in pg.url:
                page = pg
                break
        
        if not page:
            print("No page found")
            return

        print("Page:", page.url)
        
        # Look for buttons with display or settings or sliders
        elements = await page.evaluate("""() => {
            const btns = Array.from(document.querySelectorAll('button, a, [role="button"]')).map(el => ({
                text: el.innerText.trim(),
                aria: el.getAttribute('aria-label') || '',
                title: el.getAttribute('title') || '',
                id: el.id,
                testId: el.getAttribute('data-testid') || ''
            }));
            return btns;
        }""")
        
        for el in elements:
            label = el['text'] or el['aria'] or el['title']
            if any(w in label.lower() for w in ['display', 'view', 'theme', 'font', 'size', 'mode', 'visual', 'setting', 'appearance', 'style', 'layout']):
                print("Match:", el)

asyncio.run(find_display_settings())
