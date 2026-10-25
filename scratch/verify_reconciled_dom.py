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
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    test_chars = ['Scarlett Rose', 'Noah Loki', 'Logan', 'Malachia', 'Zefir']
    results = {}
    
    for cname in test_chars:
        page.evaluate("""(name) => {
            let items = Array.from(document.querySelectorAll('div[class*="cursor-pointer"]'));
            let item = items.find(it => (it.innerText || '').includes(name));
            if (item) {
                item.scrollIntoView({ block: 'nearest' });
                item.click();
            }
        }""", cname)
        time.sleep(1.5)
        
        info = page.evaluate("""() => {
            let text = document.body.innerText;
            return {
                hasUnknownSource: text.includes('Unknown source'),
                hasCustomImage: text.includes('Custom Image')
            };
        }""")
        results[cname] = info
        print(f"Check {cname:20s}: {info}")
        
    ctx.close()
