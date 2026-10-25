import json
import time
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    page = next(pg for pg in context.pages if "lorebooks/edit" in pg.url)
    
    # Click the avatar combobox
    combo = page.locator("button[role='combobox']:has-text('Select different avatar...')").first
    print("Found combobox, clicking...", flush=True)
    combo.click()
    time.sleep(2)
    
    # Inspect popover/dialog content
    popover_info = page.evaluate("""() => {
        // Find radix popover or dialog
        const popovers = Array.from(document.querySelectorAll('[data-radix-popper-content-wrapper], [role="dialog"], [role="listbox"]'));
        const images = Array.from(document.querySelectorAll('[data-radix-popper-content-wrapper] img, [role="dialog"] img, [role="listbox"] img')).map(img => ({
            src: img.src,
            alt: img.alt,
            className: img.className
        }));
        const options = Array.from(document.querySelectorAll('[role="option"], [role="menuitem"], [cmdk-item]')).map(opt => ({
            text: opt.innerText.trim(),
            html: opt.outerHTML.slice(0, 300)
        }));
        
        return {
            popoversCount: popovers.length,
            imagesCount: images.length,
            imagesSample: images.slice(0, 10),
            optionsCount: options.length,
            optionsSample: options.slice(0, 10),
            popoverHtml: popovers.length ? popovers[0].outerHTML.slice(0, 1500) : ''
        };
    }""")
    
    page.screenshot(path="scratch/avatar_popover.png")
    print("Popover info:", json.dumps(popover_info, indent=2), flush=True)
    
    # Close popover by pressing Escape
    page.keyboard.press("Escape")
    browser.close()
