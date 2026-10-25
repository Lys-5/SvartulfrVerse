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
    saved_requests = []
    page.on("request", lambda r: saved_requests.append(f"{r.method} {r.url}") if 'lorebook' in r.url else None)
    page.on("response", lambda r: print(f"RESPONSE: {r.status} {r.url}") if 'lorebook' in r.url else None)
    
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    # Click first entry (Hugh Rivers)
    page.locator('div.group.cursor-pointer').first.click()
    time.sleep(1)
    
    # Change type to none
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
    
    save_btn = page.locator('button:has-text("Save Changes")').first
    btn_text = save_btn.inner_text()
    print("Button text before clicking:", btn_text)
    
    if '*' in btn_text:
        save_btn.click()
        print("Clicked save button!")
        time.sleep(5)
    else:
        print("Button was not dirty!")
        
    print("Logged requests during save:")
    for r in saved_requests:
        print(" ", r)
        
    ctx.close()
