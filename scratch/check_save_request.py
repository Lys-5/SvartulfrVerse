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
    requests = []
    page.on("request", lambda r: requests.append(f"{r.method} {r.url}") if 'lorebook' in r.url else None)
    
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    # Click first entry, change type to none
    page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div[class*="cursor-pointer"]'));
        items[0].click();
    }""")
    time.sleep(1)
    
    page.evaluate("""() => {
        let typeSelect = Array.from(document.querySelectorAll('select')).find(s => 
            Array.from(s.options).some(o => o.text.includes('No specific type'))
        );
        let setter = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
        setter.call(typeSelect, 'none');
        typeSelect.dispatchEvent(new Event('change', { bubbles: true }));
        typeSelect.dispatchEvent(new Event('input', { bubbles: true }));
    }""")
    time.sleep(1)
    
    # Click Save Changes
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Clicking save, text is:", save_btn.inner_text())
    save_btn.click()
    time.sleep(4)
    
    print("Requests during save:")
    for r in requests:
        print(" ", r)
        
    ctx.close()
