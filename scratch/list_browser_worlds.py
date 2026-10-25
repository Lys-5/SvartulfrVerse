import asyncio
import json
import os
from playwright.async_api import async_playwright

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')

with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
    TOKEN = f.read().strip()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # Intercept network calls to /api/
        api_calls = []
        page.on("request", lambda req: api_calls.append(f"{req.method} {req.url}") if "/api/" in req.url else None)

        # Set localStorage / token if needed, or navigate to login/app
        # First navigate to origin to set localStorage
        await page.goto("https://app.wyvern.chat")
        await page.evaluate(f"""() => {{
            localStorage.setItem('auth_token', '{TOKEN}');
            localStorage.setItem('token', '{TOKEN}');
        }}""")

        # Also set cookie if Firebase uses cookies or header
        # Let's navigate to https://app.wyvern.chat/worlds
        print("Navigating to https://app.wyvern.chat/worlds ...")
        response = await page.goto("https://app.wyvern.chat/worlds", wait_until="networkidle")
        print("Page loaded, status:", response.status)

        # Wait a bit for JS hydration
        await page.wait_for_timeout(3000)

        # Check API calls
        print("\nCaptured API calls:")
        for c in api_calls:
            print("  ", c)

        # Inspect cards/links on the page
        links = await page.eval_on_selector_all("a", "elements => elements.map(e => ({ href: e.href, text: e.innerText }))")
        world_links = [l for l in links if "/worlds/" in l['href']]
        print("\nFound World links on page:")
        for wl in world_links:
            print("  ", wl)

        # Also grab all text/headers
        cards = await page.eval_on_selector_all("div[class*='card'], div[class*='item'], div[class*='world'], tr, h2, h3", 
            "elements => elements.map(e => e.innerText.slice(0, 100))")
        print("\nPage elements snippet:")
        for card in cards[:20]:
            if card.strip():
                print("   Card snippet:", repr(card[:80]))

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
