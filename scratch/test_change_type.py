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
    
    # Check type select for the open entry
    res = page.evaluate("""() => {
        // Find select that has options ['No specific type', 'NPCSpecial', ...]
        let typeSelect = Array.from(document.querySelectorAll('select')).find(s => 
            Array.from(s.options).some(o => o.text.includes('No specific type'))
        );
        if (!typeSelect) return { found: false };
        
        let oldVal = typeSelect.value;
        // Set to 'none'
        typeSelect.value = 'none';
        typeSelect.dispatchEvent(new Event('change', { bubbles: true }));
        typeSelect.dispatchEvent(new Event('input', { bubbles: true }));
        
        return {
            found: true,
            oldVal: oldVal,
            newVal: typeSelect.value
        };
    }""")
    print('Type select test:', res)
    time.sleep(1)
    
    # Check if "Save Changes" is now dirty / active
    save_status = page.evaluate("""() => {
        let saveBtn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        return {
            text: saveBtn ? saveBtn.innerText : null,
            disabled: saveBtn ? saveBtn.disabled : null
        };
    }""")
    print('Save button status after change:', save_status)
    ctx.close()
