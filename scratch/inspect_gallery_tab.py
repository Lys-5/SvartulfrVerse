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
    
    # Click Gallery tab
    gal_click = page.evaluate("""() => {
        let tabs = Array.from(document.querySelectorAll('button, [role="tab"]')).filter(b => (b.innerText || '').trim() === 'Gallery');
        if (tabs.length > 0) {
            tabs[0].click();
            return true;
        }
        return false;
    }""")
    print('Clicked Gallery tab:', gal_click)
    time.sleep(3)
    
    # Inspect Gallery pane
    gal_info = page.evaluate("""() => {
        let imgs = Array.from(document.querySelectorAll('img')).map(i => ({ src: i.src, alt: i.alt }));
        let text = document.body.innerText;
        let buttons = Array.from(document.querySelectorAll('button')).map(b => (b.innerText || '').trim()).filter(Boolean);
        return {
            totalImages: imgs.length,
            sampleImages: imgs.slice(0, 10),
            buttons: buttons.filter(b => b.length < 30).slice(0, 30),
            hasUpload: text.includes('Upload') || text.includes('Add Image')
        };
    }""")
    
    print('Gallery info:')
    print(json.dumps(gal_info, indent=2))
    ctx.close()
