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
    
    erik_item = page.locator('div.group:has-text("Erik Ulfr Douglas")').first
    erik_item.click()
    time.sleep(2)
    
    type_select = page.locator('select:has(option[value="npc"])').first
    type_select.select_option('none')
    time.sleep(1)
    
    # Trigger onSubmit and capture what error handler receives!
    validation_res = page.evaluate("""async () => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        let form = btn.closest('form') || document.querySelector('form');
        let propsKey = Object.keys(form).find(k => k.startsWith('__reactProps$'));
        let props = form[propsKey] || {};
        
        let errorsCaptured = null;
        // Monkey-patch or call props.onSubmit with a mock event
        let mockEvent = {
            preventDefault: () => {},
            persist: () => {}
        };
        
        try {
            await props.onSubmit(mockEvent);
        } catch (e) {
            return { exception: e.toString() };
        }
        
        // Find any error text displayed in the DOM
        let errorTexts = Array.from(document.querySelectorAll('.text-destructive, p[class*="text-destructive"], span[class*="text-destructive"], [role="alert"]')).map(el => el.innerText).filter(Boolean);
        
        return {
            errorTexts: errorTexts
        };
    }""")
    print("Validation result:", json.dumps(validation_res, indent=2))
    ctx.close()
