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
    
    # 1. Click first entry (Hugh Rivers)
    page.locator('div.group.cursor-pointer').first.click()
    time.sleep(2)
    
    # 2. Change Entry Type using native setter
    change_res = page.evaluate("""() => {
        let typeSelect = Array.from(document.querySelectorAll('select')).find(s => 
            Array.from(s.options).some(o => o.text.includes('No specific type'))
        );
        if (!typeSelect) return { success: false, reason: 'Select not found' };
        
        let oldVal = typeSelect.value;
        let setter = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
        setter.call(typeSelect, 'none');
        typeSelect.dispatchEvent(new Event('change', { bubbles: true }));
        typeSelect.dispatchEvent(new Event('input', { bubbles: true }));
        
        return {
            success: true,
            oldVal: oldVal,
            newVal: typeSelect.value
        };
    }""")
    print('Native select change result:', change_res)
    time.sleep(1)
    
    # Check save button
    save_btn = page.locator('button:has-text("Save Changes")').first
    btn_text = save_btn.inner_text()
    print('Save button text:', btn_text)
    
    ctx.close()
