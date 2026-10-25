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
    
    # Inspect the form state
    form_state = page.evaluate("""() => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        let form = btn.closest('form') || document.querySelector('form');
        
        // Find React Hook Form control or context
        // Search fiber up tree
        let fiber = form[Object.keys(form).find(k => k.startsWith('__reactFiber$'))];
        let curr = fiber;
        let foundContext = null;
        while (curr) {
            if (curr.memoizedProps && curr.memoizedProps.control) {
                foundContext = curr.memoizedProps;
                break;
            }
            if (curr.memoizedState && curr.memoizedState.formState) {
                foundContext = curr.memoizedState;
                break;
            }
            curr = curr.return;
        }
        
        let errors = null;
        if (foundContext && foundContext.control) {
            errors = foundContext.control._formState.errors;
        }
        
        // Also check all inputs with invalid attribute
        let invalidInputs = Array.from(document.querySelectorAll('input:invalid, select:invalid, textarea:invalid')).map(el => ({
            name: el.name,
            placeholder: el.placeholder,
            validationMessage: el.validationMessage
        }));
        
        return {
            hasContext: !!foundContext,
            errors: errors,
            invalidInputs: invalidInputs
        };
    }""")
    print("Form state info:", json.dumps(form_state, indent=2))
    ctx.close()
