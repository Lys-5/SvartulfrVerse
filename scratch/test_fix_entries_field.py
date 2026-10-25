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
    
    # Test setting entries = lexicon and checking resolver
    res = page.evaluate("""async () => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        let form = btn.closest('form') || document.querySelector('form');
        let fiber = form[Object.keys(form).find(k => k.startsWith('__reactFiber$'))];
        
        let curr = fiber;
        let control = null;
        while (curr) {
            if (curr.memoizedProps && curr.memoizedProps.control) {
                control = curr.memoizedProps.control;
                break;
            }
            curr = curr.return;
        }
        
        if (!control) return { error: 'control not found' };
        
        // Populate entries from lexicon if undefined
        if (!control._formValues.entries && control._formValues.lexicon) {
            control._formValues.entries = control._formValues.lexicon;
        }
        
        let resolver = control._options.resolver;
        let result = await resolver(control._formValues, control._options.context, {
            criteriaMode: control._options.criteriaMode,
            fields: control._fields,
            names: Object.keys(control._fields)
        });
        
        return {
            errors: result.errors,
            hasEntriesNow: !!control._formValues.entries
        };
    }""")
    print("Resolver test with entries populated:", json.dumps(res, indent=2))
    ctx.close()
