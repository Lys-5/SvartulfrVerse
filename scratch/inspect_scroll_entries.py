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
    
    # Inspect the list of entries on the left
    entries_list = page.evaluate("""() => {
        // The list of entries in the scroll area
        let scrollArea = document.querySelector('[data-radix-scroll-area-viewport]') || document.querySelector('.min-h-0.flex-shrink-0');
        if (!scrollArea) return { error: 'scrollArea not found' };
        
        let items = Array.from(scrollArea.querySelectorAll('div[class*="cursor-pointer"], button[class*="cursor-pointer"], [role="button"]')).map((el, idx) => ({
            index: idx,
            text: el.innerText.split('\\n')[0],
            badge: el.innerText.split('\\n')[2] || ''
        }));
        return { count: items.length, sample: items.slice(0, 15) };
    }""")
    print('Entries list in UI:', json.dumps(entries_list, indent=2))
    ctx.close()
