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
    
    page.locator('button:has-text("Gallery"), [role="tab"]:has-text("Gallery")').first.click()
    time.sleep(3)
    
    # Inspect gallery items
    gallery_items = page.evaluate("""() => {
        let imgs = Array.from(document.querySelectorAll('img')).filter(i => i.src.includes('imagedelivery.net'));
        return imgs.map(i => {
            let container = i.closest('div[class*="group"], div[class*="relative"]') || i.parentElement;
            return {
                src: i.src,
                alt: i.alt,
                title: container ? container.innerText.trim() : ''
            };
        });
    }""")
    
    print(f'Total gallery images rendered: {len(gallery_items)}')
    for item in gallery_items[:15]:
        print(f"  Title: {item['title']} | URL: {item['src']}")
        
    ctx.close()
