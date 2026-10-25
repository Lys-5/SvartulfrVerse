import os
import time
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
    page.evaluate("""() => {
        let tabs = Array.from(document.querySelectorAll('button, [role="tab"]')).filter(b => (b.innerText || '').trim() === 'Gallery');
        if (tabs.length > 0) tabs[0].click();
    }""")
    time.sleep(2)
    
    text = page.evaluate("""() => {
        let main = document.querySelector('main') || document.querySelector('.flex-1.min-h-0') || document.body;
        return main.innerText;
    }""")
    print('=== GALLERY TAB TEXT ===')
    print(text[:1500])
    ctx.close()
