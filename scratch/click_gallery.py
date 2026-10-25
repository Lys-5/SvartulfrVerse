import os
import time
import json
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe',
        headless=True
    )
    page = ctx.new_page()
    url = 'https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC'
    page.goto(url, wait_until='domcontentloaded', timeout=30000)
    time.sleep(4)
    
    # Check elements matching Gallery
    gal_elems = page.evaluate("""() => {
        let els = Array.from(document.querySelectorAll('*')).filter(el => {
            return (el.innerText || '').trim() === 'Gallery' && el.children.length === 0;
        });
        return els.map(el => ({
            tag: el.tagName,
            parentTag: el.parentElement.tagName,
            parentClass: el.parentElement.className,
            role: el.getAttribute('role') || el.parentElement.getAttribute('role')
        }));
    }""")
    print('Gallery elements:', json.dumps(gal_elems, indent=2))
    
    # Click each one
    page.locator('button:has-text("Gallery"), [role="tab"]:has-text("Gallery")').first.click()
    time.sleep(2)
    
    # Check what is now on screen
    url_now = page.url
    page_text = page.evaluate("() => document.body.innerText")
    print("Page URL:", url_now)
    print("Has 'Upload Image':", 'Upload Image' in page_text or 'Upload' in page_text)
    print("Has 'No images':", 'No images' in page_text or 'empty' in page_text)
    print("Snippet:", [line for line in page_text.split('\n') if any(w in line for w in ['Gallery', 'image', 'Image', 'Drop', 'Upload'])][:10])
    ctx.close()
