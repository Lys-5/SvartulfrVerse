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
    
    resolver_info = page.evaluate("""async () => {
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
        
        let values = control._formValues;
        let options = control._options;
        let resolver = options.resolver;
        
        let resolverResult = null;
        if (resolver) {
            try {
                resolverResult = await resolver(values, control._options.context, {
                    criteriaMode: options.criteriaMode,
                    fields: control._fields,
                    names: Object.keys(control._fields)
                });
            } catch (e) {
                resolverResult = { exception: e.toString() };
            }
        }
        
        return {
            hasResolver: !!resolver,
            errors: resolverResult ? resolverResult.errors : null,
            valuesKeys: Object.keys(values || {})
        };
    }""")
    print("Resolver info:", json.dumps(resolver_info, indent=2))
    ctx.close()
