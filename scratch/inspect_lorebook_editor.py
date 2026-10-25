import json
import time
import sys
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

print("Connecting to ws_endpoint:", ws_endpoint, flush=True)

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    
    print("Existing pages:", flush=True)
    for pg in context.pages:
        print(" -", pg.title(), pg.url, flush=True)
        
    print("\nOpening new tab for Lorebook editor...", flush=True)
    page = context.new_page()
    page.goto("https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC", wait_until="domcontentloaded", timeout=30000)
    print("Navigated to:", page.url, "Title:", page.title(), flush=True)
    
    # Wait for the editor to render
    print("Waiting 5s for Next.js app to mount...", flush=True)
    time.sleep(5)
    
    html_title = page.title()
    print("Page Title:", html_title, flush=True)
    
    # Check current URL (in case of redirect)
    print("Current URL:", page.url, flush=True)
    
    # Evaluate and list interactive elements, headers, tabs
    eval_info = page.evaluate("""() => {
        const text = document.body.innerText;
        const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
        const inputs = Array.from(document.querySelectorAll('input')).map(i => ({
            id: i.id,
            name: i.name,
            placeholder: i.placeholder,
            type: i.type,
            value: i.value,
            className: i.className
        }));
        const headings = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(h => h.innerText.trim()).filter(Boolean);
        return {
            textSnippet: text.slice(0, 1000),
            headings,
            buttonsCount: buttons.length,
            buttonsSample: buttons.slice(0, 20),
            inputsSample: inputs.slice(0, 20)
        };
    }""")
    print("Eval info:", json.dumps(eval_info, indent=2), flush=True)
    
    page.screenshot(path="scratch/lorebook_editor_page.png")
    print("Screenshot saved to scratch/lorebook_editor_page.png", flush=True)
    
    page.close()
    browser.close()
