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
    
    # Change type to none
    type_select = page.locator('select:has(option[value="npc"])').first
    type_select.select_option('none')
    time.sleep(1)
    
    # Submit form and check what fails
    submit_res = page.evaluate("""() => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        let form = btn.closest('form') || document.querySelector('form');
        if (!form) return { error: 'Form not found' };
        
        let invalidFields = [];
        let elements = Array.from(form.elements);
        for (let el of elements) {
            if (!el.checkValidity()) {
                invalidFields.push({ name: el.name, id: el.id, type: el.type, validationMessage: el.validationMessage });
            }
        }
        
        // Try requestSubmit
        let submitted = false;
        try {
            form.requestSubmit(btn);
            submitted = true;
        } catch (e) {
            submitted = e.toString();
        }
        
        return {
            formId: form.id,
            invalidFields: invalidFields,
            submitted: submitted
        };
    }""")
    print("Submit result:", json.dumps(submit_res, indent=2))
    time.sleep(3)
    
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Save button text after requestSubmit:", save_btn.inner_text())
    ctx.close()
