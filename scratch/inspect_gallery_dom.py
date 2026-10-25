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
    page.bring_to_front()
    
    # 1. Inspect "CHANGE AVATAR" button
    print("Finding 'CHANGE AVATAR' button...", flush=True)
    change_avatar_btn = page.locator("text='CHANGE AVATAR'").first
    print("Change avatar button visible:", change_avatar_btn.is_visible(), flush=True)
    
    # Click it to see dialog
    change_avatar_btn.click()
    time.sleep(2)
    
    # Inspect dialog / modal
    dialog_info = page.evaluate("""() => {
        const dialog = document.querySelector('[role="dialog"], div[class*="dialog"], div[class*="modal"]');
        if (!dialog) return { error: 'No dialog found' };
        
        const heading = dialog.querySelector('h1, h2, h3, h4, h5, div[class*="title"]') ? 
            dialog.querySelector('h1, h2, h3, h4, h5, div[class*="title"]').innerText : '';
        const buttons = Array.from(dialog.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
        const images = Array.from(dialog.querySelectorAll('img')).map(img => ({
            src: img.src,
            alt: img.alt,
            className: img.className
        }));
        const tabs = Array.from(dialog.querySelectorAll('[role="tab"]')).map(t => t.innerText.trim());
        
        return {
            heading,
            buttons,
            tabs,
            imagesCount: images.length,
            imagesSample: images.slice(0, 10),
            dialogHtmlSnippet: dialog.outerHTML.slice(0, 1000)
        };
    }""")
    
    page.screenshot(path="scratch/avatar_dialog.png")
    print("Avatar dialog info:", json.dumps(dialog_info, indent=2), flush=True)
    
    # Close dialog (press Escape or click cancel)
    page.keyboard.press("Escape")
    time.sleep(1)
    
    # 2. Inspect "Gallery" tab at top
    print("\nClicking top 'Gallery' tab...", flush=True)
    gallery_tab = page.locator("button:has-text('Gallery'), [role='tab']:has-text('Gallery')").first
    if gallery_tab.is_visible():
        gallery_tab.click()
        time.sleep(2)
        page.screenshot(path="scratch/gallery_tab.png")
        
        gallery_info = page.evaluate("""() => {
            const images = Array.from(document.querySelectorAll('img')).map(img => ({
                src: img.src,
                alt: img.alt,
                className: img.className
            }));
            const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
            return {
                imagesCount: images.length,
                imagesSample: images.slice(0, 10),
                buttonsSample: buttons.filter(b => ['Upload', 'Add', 'Delete', 'Select'].some(k => b.includes(k)))
            };
        }""")
        print("Gallery tab info:", json.dumps(gallery_info, indent=2), flush=True)
        
        # Switch back to 'Entries' tab
        page.locator("button:has-text('Entries'), [role='tab']:has-text('Entries')").first.click()
        time.sleep(1)
        
    browser.close()
