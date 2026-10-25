import os
import json
import asyncio
from playwright.async_api import async_playwright

async def main():
    devtools_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "DevToolsActivePort")
    with open(devtools_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    port = lines[0]
    ws_path = lines[1]
    cdp_url = f"http://127.0.0.1:{port}"
    print(f"Connecting to CDP: {cdp_url} (ws: {ws_path})")

    async with async_playwright() as p:
        try:
            browser = await p.chromium.connect_over_cdp(f"ws://127.0.0.1:{port}{ws_path}")
            print(f"Connected! Contexts: {len(browser.contexts)}")
            for ctx in browser.contexts:
                print(f"Pages in context: {len(ctx.pages)}")
                for page in ctx.pages:
                    print(f"- {page.url} | {await page.title()}")
            await browser.close()
        except Exception as e:
            print("Error connecting:", e)

if __name__ == "__main__":
    asyncio.run(main())
