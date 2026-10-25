import asyncio
import json
from playwright.async_api import async_playwright

async def inspect():
    async with async_playwright() as p:
        with open(r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort') as f:
            port = f.readline().strip()
            ws_path = f.readline().strip()
        ws_url = f'ws://127.0.0.1:{port}{ws_path}'
        browser = await p.chromium.connect_over_cdp(ws_url)
        context = browser.contexts[0]
        wyvern_page = None
        for pg in context.pages:
            if 'wyvern.chat' in pg.url:
                wyvern_page = pg
                break
        
        if not wyvern_page:
            print("No Wyvern page found")
            return

        print("Connected to:", wyvern_page.url)

        # Inspect current display settings or tabs
        res = await wyvern_page.evaluate("""() => {
            // Find settings modals, display settings buttons, etc.
            const allButtons = Array.from(document.querySelectorAll('button')).map(b => ({
                text: b.innerText.trim(),
                title: b.getAttribute('title') || b.getAttribute('aria-label') || '',
                classes: b.className
            }));
            
            // Check localStorage for display settings
            const displayKeys = Object.keys(localStorage).filter(k => k.toLowerCase().includes('display') || k.toLowerCase().includes('setting') || k.toLowerCase().includes('theme') || k.toLowerCase().includes('chat') || k.toLowerCase().includes('sim'));
            const storage = {};
            displayKeys.forEach(k => {
                storage[k] = localStorage.getItem(k);
            });

            return {
                buttons: allButtons.filter(b => b.text || b.title).slice(0, 50),
                storage: storage
            };
        }""")
        
        print("Storage keys:", list(res['storage'].keys()))
        for k, v in res['storage'].items():
            print(f"  {k}: {v[:100] if v else ''}")

asyncio.run(inspect())
