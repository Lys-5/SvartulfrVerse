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
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    erik_item = page.locator('div.group:has-text("Erik Ulfr Douglas")').first
    erik_item.click()
    time.sleep(2)
    
    type_select = page.locator('select:has(option[value="npc"])').first
    type_select.select_option('none')
    time.sleep(1)
    
    # Call form.dispatchEvent with submit event
    print("Dispatching submit event on form...")
    save_res = page.evaluate("""() => {
        let form = document.querySelector('form');
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        
        // Dispatch click on the button directly
        btn.click();
        
        return {
            btnText: btn.innerText,
            btnDisabled: btn.disabled
        };
    }""")
    print("Save click result:", save_res)
    time.sleep(4)
    
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Save button text after click:", save_btn.inner_text())
    ctx.close()
